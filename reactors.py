# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 21:07:34 2022

@author: gibra
"""
import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fmin
import matplotlib.pyplot as plt

#aA + bB + I -> cC +dD
#A + B -> C

a = 1
b = 1
c = 1 
d = 0
delta = d + c - b - a
eps = (yAo*delta)/a
A = 500000 #L/mol.s
EA = 45000 #J/mol.K
Hrxno = -65000 #J/mol
CpA = 130 #J/mol.K
CpB = 150 #J/mol.K
CpC = 125 #J/mol.K
CpD = 0 #J/mol.K
deltaCp = (d*CpD + c*CpC - a*CpA - b*CpB)/a    
Tref = 298 #K
R = 8.314


def adbCSTR(CAo, Vr, vo, thetaB, thetaI, To, T1, T2):
     
    a = 1
    b = 1
    c = 1 
    d = 0
    delta = d + c - b - a
    eps = (yAo*delta)/a
    A = 500000 #L/mol.s
    EA = 45000 #J/mol.K
    Hrxno = -65000 #J/mol
    CpA = 130 #J/mol.K
    CpB = 150 #J/mol.K
    CpC = 125 #J/mol.K
    CpD = 0 #J/mol.K
    deltaCp = (d*CpD + c*CpC - a*CpA - b*CpB)/a    
    Tref = 298
    R = 8.314
        
    def energy(T):
        X = -(CpA*(T - To) + thetaB*CpB*(T - To))/(Hrxno + deltaCp*(T - Tref))
        return X
    
    def moles(T):
        k = A*np.exp(-EA/(R*T))
        tau = Vr/vo
        X = (2*k*tau*CAo + 1 - np.sqrt(4*k*tau*CAo + 1))/2*k*tau*CAo
        return X
    
    def solution(T):
        XEB = energy(T)
        XMB = moles(T)
        sol = abs(XMB - XEB)
        return sol                                                                                                        
    
    #Solving the equations
    T = np.linspace(T1, T2, 100) #K
    XEB = energy(T)
    XMB = moles(T)
    
    #Running the optimization
    Tsol = fmin(solution, 360, xtol=1e-8)
    Xfinal = energy(Tsol)
    
    print('The operating temperature of the CSTR is',np.round(Tsol,2))
    print('The exit conversion is',np.round(Xfinal,2))
    
    #Preparing the plots
    plt.plot(T, XEB, "b", label = '$X_{EB}$')
    plt.plot(T, XMB, "r", label = '$X_{MB}$')
    plt.plot(Tsol, Xfinal, "ko")
    plt.axhline(y=Xfinal, color='k', linestyle='--')
    plt.axvline(x=Tsol, color='k',linestyle='--')
    plt.xlabel("Temperature (K)")
    plt.ylabel("Conversion ($X_{EB}$ & $X_{MB}$)")
    plt.legend()
    plt.show()
    
    return (Tsol, Xfinal)


def isoCSTR(CAo, Vr, vo, thetaB, thetaI, To, T1, T2, Tc, U, SA):
    
    a = 1
    b = 1
    c = 1 
    d = 0
    delta = d + c - b - a
    eps = (yAo*delta)/a
    A = 500000 #L/mol.s
    EA = 45000 #J/mol.K
    Hrxno = -65000 #J/mol
    CpA = 130 #J/mol.K
    CpB = 150 #J/mol.K
    CpC = 125 #J/mol.K
    CpD = 0 #J/mol.K
    deltaCp = (d*CpD + c*CpC - a*CpA - b*CpB)/a    
    Tref = 298
    R = 8.314
    
    def energy(T):
        X = (-U*SA*(T - Tc) - CAo*vo*CpA*(T - To))/(CAo*vo*Hrxno + CAo*vo*deltaCp*(T-Tref))
        return X

    def moles(T):
        k = A*np.exp(-EA/(R*T))
        tau = Vr/vo
        X = (k*tau)/(1 + k*tau)
        return X

    #Graphical approach
    T = np.linspace(T1, T2, 100) #K
    XEB = energy(T)
    XMB = moles(T)

    #Preparing the plots
    plt.plot(T, XEB, "k", label ='$X_{EB}$')
    plt.plot(T, XMB, "r",label ='$X_{MB}$')
    plt.xlabel("Temperature (K)")
    plt.ylabel("Conversion")
    plt.legend()
    plt.show()

    #Solving the problem using optimization

    def solution(T):
        XEB = energy(T)
        XMB = moles(T)
        sol = abs(XMB - XEB)
        return sol

    #Running the optimization
    Tsol = fmin(solution, 360, xtol=1e-8)
    Xsol = moles(Tsol)
    print('The exit temperature is',np.round(Tsol[0],1),'K')
    print('The exit conversion is',np.round(Xsol[0],2))
    
    return (Tsol, Xsol)


def adbPFR(CAo, Vr, vo, yAo, thetaB, thetaI, To):
    
    a = 1
    b = 1
    c = 1 
    d = 0
    delta = d + c - b - a
    eps = (yAo*delta)/a
    A = 500000 #L/mol.s
    EA = 45000 #J/mol.K
    Hrxno = -65000 #J/mol
    CpA = 130 #J/mol.K
    CpB = 150 #J/mol.K
    CpC = 125 #J/mol.K
    CpD = 0 #J/mol.K
    deltaCp = (d*CpD + c*CpC - a*CpA - b*CpB)/a    
    Tref = 298
    R = 8.314  
    
    #Define the functions

    #S = [conversion, temperature]

    def pfr(S,V):
        k = A*np.exp(-EA/(R*S[1]))
        CA = CAo*To/S[1]*(1-S[0])/(1+eps*S[0])
        CB = CAo*To/S[1]*(thetaB-b/a*S[0])/(1+eps*S[0])
        rA = (k*CA*CB)
        FAo = CAo*vo
        dXAdV = -rA/FAo  #from definition
        dTdV = ((deltaCp*(Tref - S[1])-Hrxno)*(k*(1-S[0])*To))/((CpA + S[0]*deltaCp)*(vo*S[1]))
        dSdV = [dXAdV, dTdV]
        return dSdV    

    #Solving the system of ODEs
    V = np.linspace(0, Vr, 50)
    So = [0,To]
    S = odeint(pfr, So, V)
    XA = S[:,0]
    T = S[:,1]

    #Preparing the plots
    plt.plot(V, XA, "k", label = '$X_{A}$' )
    plt.plot(V, T, "r", label = 'Temp')
    plt.xlabel("Volume (L)")
    plt.ylabel("Conversion or Temperature")
    plt.legend()
    plt.show()

    print('The exit temperature is',np.round(T[len(T)-1],2),'K')
    print('The exit conversion is',np.round(XA[len(XA)-1],2))

    return(T[len(T)-1],XA[len(XA)-1])
    
    
def isoPFR(CAo, Vr, vo, yAo, thetaB, thetaI, To):
    
    a = 1
    b = 1
    c = 1 
    d = 0
    delta = d + c - b - a
    eps = (yAo*delta)/a
    A = 500000 #L/mol.s
    EA = 45000 #J/mol.K
    Hrxno = -65000 #J/mol
    CpA = 130 #J/mol.K
    CpB = 150 #J/mol.K
    CpC = 125 #J/mol.K
    CpD = 0 #J/mol.K
    deltaCp = (d*CpD + c*CpC - a*CpA - b*CpB)/a    
    Tref = 298
    R = 8.314
     
    #Define the functions

    #S = [conversion]

    def pfr(S,V):
    k = A*np.exp(-EA/(R*To))
    CA = CAo*(1-S[0])/(1+eps*S[0])
    CB = CAo*(thetaB-b/a*S[0])/(1+eps*S[0])
    rA = (k*CA*CB)
    FAo = CAo*vo
    dXAdV = -rA/FAo  #from definition
    return dXAdV    

    #Solving the system of ODEs
    Xo = 0
    V = np.linspace(0, Vr, 50)
    XA = odeint(pfr, Xo, V)
    index = np.size(XA) - 1
    XAexit = XA[index]

    #Preparing the plots
    plt.plot(V, XA, "k")
    plt.xlabel("Volume (L)")
    plt.ylabel("Conversion ($X_A$)")

    print('The exit conversion is',XAexit)
    
    return(XAexit)
    
    
def adbPBR(CAo, Vr, vo, yAo, thetaB, thetaI, To, alpha, rho, BW):
    
    a = 1
    b = 1
    c = 1 
    d = 0
    delta = d + c - b - a
    eps = (yAo*delta)/a
    A = 500000 #L/mol.s
    EA = 45000 #J/mol.K
    Hrxno = -65000 #J/mol
    CpA = 130 #J/mol.K
    CpB = 150 #J/mol.K
    CpC = 125 #J/mol.K
    CpD = 0 #J/mol.K
    deltaCp = (d*CpD + c*CpC - a*CpA - b*CpB)/a    
    Tref = 298
    R = 8.314 
    
    #Define the functions

    #S = [conversion, temperature, pressure drop]

    def pbr(S,V):
        k = A*np.exp(-EA/(R*S[1]))
        CA = (CAo*S[2]*To*(1 - S[0]))/(S[1]*(1 + eps*S[0]))
        CB = (CAo*S[2]*To*(thetaB - b/a*S[0]))/(S[1]*(1 + eps*S[0]))
        rA = (k*CA*CB)
        FAo = CAo*vo
        Hrxn = Hrxno + deltaCp*(S[1] - To)
        dXAdW = -rA/FAo  #from definition
        dTdW = -(U*(S[1]-To) + (-rA)*Hrxn)/(FAo*(1-S[0])*(CpA) + (FAo*(thetaB-b/a*S[0])*(CpA) + FAo*S[0]*CpC*c/a + FAo*S[0]*CpD*d/a))
        dydW = -(alpha*S[1]*(1 + eps*S[0]))/(2*S[2]*To)
        dSdW = [dXAdW, dTdW, dydW]
        return dSdW                                                                                                          
                                                                                                                   
    #Solving the system of ODEs
    W = np.linspace(0, BW, 40)
    S0 = [0,To,1]
    S = odeint(pbr, S0, W)

    #Extracting the solutions
    XA = S[:,0]
    T = S[:,1]
    y = S[:,2]

    #Preparing the plots

    plt.plot(W, XA, "k", label = '$X_{A}$')
    plt.plot(W, y, "g", label = 'y')
    plt.xlabel("Bed weight (kg)")
    plt.ylabel("Conversion or dimensionless pressure")
    plt.legend()
    plt.show()

    plt.plot(W, T, "r--", label = "Reactor")
    plt.xlabel("Bed weight (kg)")
    plt.ylabel("Temperature (K)")
    plt.legend()
    plt.show()

    print('The exit temperature of the reacting stream is',np.round(T[len(T)-1],2),'K')
    print('The exit conversion is',np.round(XA[len(XA)-1],2))
    print('The pressure drop is',np.round((1-y[len(y)-1])*100,2),'%')
    
    return(T[len(T)-1], XA[len(XA)-1], (1-y[len(y)-1])*100)
    
    
def isoPBR(CAo, V, vo, yAo, thetaB, thetaI, To, Tc, alpha, rho, U, mc, CpCool, sav):
    
    a = 1
    b = 1
    c = 1 
    d = 0
    delta = d + c - b - a
    eps = (yAo*delta)/a
    A = 500000 #L/mol.s
    EA = 45000 #J/mol.K
    Hrxno = -65000 #J/mol
    CpA = 130 #J/mol.K
    CpB = 150 #J/mol.K
    CpC = 125 #J/mol.K
    CpD = 0 #J/mol.K
    deltaCp = (d*CpD + c*CpC - a*CpA - b*CpB)/a    
    Tref = 298
    R = 8.314 
    
    #Define the functions

    #S = [conversion, pressure drop, coolant temperature]

    def pbr(S,V):
        k = A*np.exp(-EA/(R*S[1]))
        CA = CAo*S[1]*((1-S[0])/(1+eps*S[0])) 
        CB = CAo*S[1]*((thetaB-(b/a*S[0]))/((1+eps*S[0])))
        rA = (k*CA*CB)
        FAo = CAo*vo
        dXAdW = -rA/FAo  #from definition
        dydW = -(alpha*(1 + eps*S[0]))/(2*S[1])
        dTcdW = (U*a*(To - S[2]))/(mc*CpCool)
        dSdV = [dXAdW, dydW, dTcdW]
        return dSdW    

    #The beg weight is 50 kg

    #Solving the system of ODEs
    W = np.linspace(0, BW, 200)
    S0 = [0,1,Tcin] #Initial conditions
    S = odeint(pbr, S0, W)

    #Extracting solutions
    XA = S[:,0]
    y = S[:,1]
    Tc = S[:,2]

    #Plotting the solution
    plt.plot(W, XA, "k", label = 'Conversion')
    plt.plot(W, y, "b", label = 'Dimensionless pressure')
    plt.xlabel("Bed weight (kg)")
    plt.ylabel("Conversion & dimensionless pressure")
    plt.legend()
    plt.show()

    plt.plot(W, Tc, "r--", label = "Coolant")
    plt.xlabel("Bed weight (kg)")
    plt.ylabel("Temperature (K)")
    plt.legend()
    plt.show()

    print('The exit temperature of the cooling stream is',np.round(Tc[len(Tc)-1],2),'K')
    print('The exit conversion is',np.round(XA[len(XA)-1],2))
    print('The pressure drop is',np.round((1-y[len(y)-1])*100,2),'%')

    return(T[len(T)-1], XA[len(XA)-1], (1-y[len(y)-1])*100)    
    