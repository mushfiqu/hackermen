# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 21:07:34 2022

@author: gibra
"""

aA + bB + I -> cC +dD

A -> C +2D
Ea = 237.05 #KJ/mol
a = 1
b = 0
c = 1
d = 2
A = 2.92*10**22
EA = 237.05
Hrxno = 150
CpA = 150
CpC = 150
CpD = 150


#adiabaticCSTR
 def adCSTR(CAo, V, vo, thetaB, thetaI, To):
     
    #Total heat capacity
    deltaCp = (d*CpD + c*CpC - a*CpA - b*CpB)/a    
    R = 8.314
    Tref = 298 #K
        
    def energy(T):
        X = -(CpA*(T - To) + thetaB*CpB*(T - To))/(Hrxno + deltaCp*(T - Tref))
        return X

    def moles(T):
        k = A*np.exp(-EA/(R*T))
        tau = V/vo
        X = (2*k*tau*CAo + 1 - np.sqrt(4*k*tau*CAo + 1))/2*k*tau*CAo
        return X

    def solution(T):
        XEB = energy(T)
        XMB = moles(T)
        sol = abs(XMB - XEB)
        return sol                                                                                                        

    #Solving the equations
    T = np.linspace(340, 400, 30) #K
    XEB = energy(T)
    XMB = moles(T)

    #Running the optimization
    Tsol = fmin(solution, 360, xtol=1e-8)
    Xfinal = energy(Tsol)
    
    #print('The operating temperature of the CSTR is',np.round(Tsol,2))
    #print('The exit conversion is',np.round(Xfinal,2))

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
    
    return (Tsol, Xfinal, XEM, XMB , T)

#Isothermal CSTR
def isoCSTR(CAo, V, vo, thetaB, thetaC, thetaD, thetaI, a, b, c, d, To, A, EA, Hrxno, CpA, CpB, CpC, CpD, Tc, U, SA):
    
    delta = d + c - b - a
    R = 8.314
    Tref = 298 #K
    
    def energy(T):
        X = (-U*SA*(T - Tc) - CAo*vo*CpA*(T - To))/(CAo*vo*Hrxno + CAo*vo*deltaCp*(T-Tref))
        return X

    def moles(T):
        k = A*np.exp(-EA/(R*T))
        tau = V/vo
        X = (k*tau)/(1 + k*tau)
        return X

    #Graphical approach
    T = np.linspace(280, 420, 100) #K
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
    #print('The exit temperature is',np.round(Tsol[0],1),'K')
    #print('The exit conversion is',np.round(Xsol[0],2))
    
    return (Tsol, Xsol, XEM, XMB, sol)


#Adiabtatic PFR

def adbPFR(CAo, V, vo, yAo, thetaB, thetaC, thetaD, thetaI, a, b, c, d, To, A, EA, Hrxno, CpA, CpB, CpC, CpD):
    
    delta = d + c - b - a
    eps = (yAo*delta)/a
    R = 8.314
    Tref = 298 #K    
    
    #Define the functions

    #S = [conversion, temperature]

    def pfr(S,V):
        k = A*np.exp(-EA/(R*S[1]))
        CA = CAo*To/S[1]*(1-S[0])/(1+eps*S[0])
        CB = CAo*To/S[1]*(thetaB-b/a*S[0])/(1+eps*S[0])
        rA = (k*CA)
        FAo = CAo*vo
        dXAdV = -rA/FAo  #from definition
        dTdV = ((deltaCp*(Tref - S[1])-Hrxno)*(k*(1-S[0])*To))/((CpA + S[0]*deltaCp)*(vo*S[1]))
        dSdV = [dXAdV, dTdV]
        return dSdV    

    #Solving the system of ODEs
    V = np.linspace(0, 20, 50)
    So = [0,To]
    S = odeint(pfr, So, V)
    XA = S[:,0]
    T = S[:,1]

    #Preparing the plots

    plt.subplot(2,1,1)
    plt.plot(V, XA, "k")
    plt.xlabel("Volume (L)")
    plt.ylabel("Conversion ($X_A$)")

    plt.subplot(2,1,2)
    plt.plot(V, T, "r")
    plt.xlabel("Volume (L)")
    plt.ylabel("Temperature (K)")
    plt.show()

    print('The exit temperature is',np.round(T[len(T)-1],2),'K')
    print('The exit conversion is',np.round(XA[len(XA)-1],2))


#isothermal PFR

def isoPFR(CAo, V, vo, yAo, thetaB, thetaC, thetaD, thetaI, a, b, c, d, To, A, EA, Hrxno, CpA, CpB, CpC, CpD):
    
    delta = d + c - b - a
    eps = (yAo*delta)/a
    R = 8.314
    Tref = 298 #K    
    
    #Define the functions

    #S = [conversion, temperature]

    def pfr(S,V):
        k = A*np.exp(-EA/(R*S[1]))
        CA = CAo*(1-S[0])/(1+eps*S[0])
        CA = CAo*(thetaB-b/a*S[0])/(1+eps*S[0])
        rA = (k*CA)
        FAo = CAo*vo
        dXAdV = -rA/FAo  #from definition
        dTcdW = (U*a*(To - S[1]))/(mc*CpCool)
        dSdV = [dXAdV, dTcdV]
        return dSdV    

    #Solving the system of ODEs
    V = np.linspace(0, 20, 50)
    So = [0,To]
    S = odeint(pfr, So, V)
    XA = S[:,0]
    T = S[:,1]

    #Preparing the plots

    plt.subplot(2,1,1)
    plt.plot(V, XA, "k")
    plt.xlabel("Volume (L)")
    plt.ylabel("Conversion ($X_A$)")

    plt.subplot(2,1,2)
    plt.plot(V, T, "r")
    plt.xlabel("Volume (L)")
    plt.ylabel("Temperature (K)")
    plt.show()

    print('The exit temperature is',np.round(T[len(T)-1],2),'K')
    print('The exit conversion is',np.round(XA[len(XA)-1],2))
    
    
    
    #Adiabatic PBR
    
    def adbPBR(CAo, V, vo, yAo, thetaB, thetaC, thetaD, thetaI, a, b, c, d, To, A, EA, Hrxno, CpA, CpB, CpC, CpD, alpha, rho):
    
    delta = d + c - b - a
    eps = (yAo*delta)/a
    FAo = CAo*vo #mol/min
    R = 8.314
    Tref = 298 #K  
    
    #Define the functions

    #S = [conversion, temperature]

    def pbr(S,V):
        k = A*np.exp(-EA/(R*S[1]))
        CA = CAo*S[1]*((1-S[0])/(1+eps*S[0]))   #(S[2]/To)
        CB = CAo*S[1]*((thetaB-(b/a*S[0]))/((1+eps*S[0])))  #(S[2]/To)
        rA = (k*CA)
        FAo = CAo*vo
        Hrxn = Hrxno + deltaCp*(S[1] - To)
        dXAdW = -rA/FAo  #from definition
        dTdW = -(U*(S[1]-Tcin) + (rA)*Hrxn)/(FAo*(1-S[0])*(CpA) + (FAo*(thetaB-b/a*S[0])*(CpA) + FAo*S[0]*CpC*c/a + FAo*S[0]*CpD*d/a))
        dydW = -(alpha*S[1]*(1 + eps*S[0]))/(2*S[2]*To)
        dSdW = [dXAdW, dTdW, dydW]
        return dSdW                                                                                                          
                                                                                                                   
    #Solving the system of ODEs
    W = np.linspace(0, 20, 40)
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
    
    #Isothermal PBR
    
    def isoPBR(CAo, V, vo, yAo, thetaB, thetaC, thetaD, thetaI, a, b, c, d, To, A, EA, Hrxno, CpA, CpB, CpC, CpD, alpha, rho):
    
    delta = d + c - b - a
    eps = (yAo*delta)/a
    FAo = CAo*vo #mol/min
    R = 8.314
    Tref = 298 #K  
    k = A*np.exp(-EA/(R*T))
    
    #Define the functions

    #S = [conversion, temperature]

    def pbr(S,V):
        CA = CAo*S[1]*((1-S[0])/(1+eps*S[0]))   #(S[2]/To)
        CB = CAo*S[1]*((thetaB-(b/a*S[0]))/((1+eps*S[0])))  #(S[2]/To)
        rA = (k*CA)
        FAo = CAo*vo
        dXAdW = -rA/FAo  #from definition
        dydW = -(alpha*(1 + eps*S[0]))/(2*S[1])
        dTcdW = (U*a*(To - S[2]))/(mc*CpCool)
        dSdV = [dXAdW, dydW, dTcdW]
        return dSdW    

    #The beg weight is 50 kg

    #Solving the system of ODEs
    W = np.linspace(0, 50, 200)
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

