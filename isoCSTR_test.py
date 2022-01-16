# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 04:40:59 2022

@author: gibra
"""

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
        tau = V/vo
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
    
    return (Tsol, Xsol, XEB, XMB, sol)
