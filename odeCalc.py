# -*- coding: utf-8 -*-
"""

Semester oppgave FE-MAT1000 - 2014
• Oppgave 1
• Oppgave 2

@author: Jens

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

"--------Verdier som kan endres--------"

Valg = 3 # skriv 1 for oppgave 1. Skriv 2 for opg 2, del 1. Skriv 3 for opg 2, del 2.

A0 = 0.25 # A0 kan ta verdiene: {0.0, 0.01, 0.25} 
B0 = 2.0 # B0 kan ta verdiene: {0.1, 1.5, 2.0, 7.0, 10.0}

delintervall = 400 # antall intervaller til integranden
iterasjon = 100 # antall iterasjoner til newtons metode

"--------------------------------------"

if Valg == 2 or Valg == 3:
    y0velger = 0.0001 # Her velger vi y0 for valg 2 og 3

if Valg == 1:
    y0velger = 1.0 # Her velger vi y0 for valg 1

"   Lille 'f' er høyre siden av diff-likningen sett slik: y'= f  " 
# Her velger vi mellom de forskjellige likningene.

if Valg == 1:
    def f(xx,yy):
        return -xx*yy # Likning 1 fra oppgave 1

if Valg == 2: 
    def f(xx,yy):
        return 1 - A0 * abs(yy) * yy # Likning 1 fra oppgave 2

if Valg == 3:
    def f(xx,yy):
        return 1 - A0 * abs(yy) * yy - B0 * np.sin(xx)**2 # Likning 2 fra oppgave 2
        
# Nedre og øvre x verdi for de forskjellige valgene

if Valg == 2 or Valg == 3:
    upper = 25.0 # Øvre del av intervallet integrasjonsintervallet
    lower = 0.0 # Nedre del av integrasjonsintervallet

if Valg == 1:
    upper = 3.0 # Øvre del av intervallet integrasjonsintervallet
    lower = 0.0 # Nedre del av integrasjonsintervallet
    
# Hvilke grafer som skal vises

if Valg == 2 or Valg == 3:
    viseuler = 1 # Euler
    vismodeuler = 1 # Modifisert Euler
    visheun = 1 # Heuns
    visnewton = 1 # Newtons
    visexact = 1 # Exact
    
if Valg == 1:
    viseuler = 0 # Euler
    vismodeuler = 0 # Modifisert Euler
    visheun = 0 # Heuns
    visnewton = 1 # Newtons
    visexact = 1 # Exact

"--------Forskjellige konstanter for programmet--------"

h = (upper - lower) / delintervall

teller = 1.0

x0 = 0.0
y0 = y0velger # v(t0) = 0.0001 , v(0) = 0.0001
x1 = 0.0
y1 = 0.0

"--------Deklarer listene og array som skal brukes--------"

x = np.linspace(lower, upper, delintervall+1) # Skaper en liste med (delintervall+1) elementer der det første =lower og det siste =upper
y = np.linspace(0.0, 0.0, delintervall+1) # Tallmengden produsert av Euler-metoden
w = np.linspace(0.0, 0.0, delintervall+1) # Tallmengden produsert av den modifiserte Euler-metoden
v = np.linspace(0.0, 0.0, delintervall+1) # Tallmengden produsert av den Huens metode

listX11 = [] # liste for x-verdiene
listY11 = [] # liste for y-verdiene

o0 = np.array([y0velger]) # Oppretter y0 som en array
br = np.linspace(lower, upper, delintervall) # Oppretter en liste med elementene lower, upper og delintervall

"--------Definerer funksjonene--------"
# Definerer alle nødvendige funksjoner

def deriv(o,t): # Her definerer vi den deriverte som en array
    yprime = np.array([f(t,o[0])]) # Funksjonen som en array
    return yprime # Returnerer funksjonen som yprime slik at integrate.odeint kan forstå den
       
def f1(xx,yy): 
    return (f(xx,yy)*(-1)) # Funksjonen *(-1) for bruk i newtons metode

o = integrate.odeint(deriv, o0, br) # Den tilnærmet eksakte løsningen til funksjonen
    
def F(y1):
	return y1 - y0 + ( (h / 2.0) * ( f1(x0, y0) + f1(x1, y1) ) ) # Her definerer vi funksjonen f(x) for trapes metoden
	
def Fd(x1):
	return 1.0 + ( (h * x1) / 2.0) # Her definerer vi den deriverte av f(x) for trapes metoden
 
def g(n):
    return y[n-1] + h * f(x[n-1], y[n-1]) # EULER: y_n=y_(n-1)+hf(x_(n-1),y_(n-1))

def p(m):
    return w[m-1] + h * f(x[m-1] + h * 0.5, w[m-1] + h * 0.5 * f(x[m-1], w[m-1])) #  MOD.-EULER: w_m=w_(n-1)+hf(x_(m-1),w_(m-1)+h/2f(x[m-1],w[m-1]))

def q(r):
    return v[r-1] + h * 0.5 * (f(x[r-1], y[r-1]) + f(x[r], y[r-1] + h * f(x[r-1], y[r-1]))) # HEUNS metode

"--------Euler, Mod. Euler og Heun--------"

y[0] = y0velger # Initialverdien ved x=0 for Euler
w[0] = y0velger # Initialverdien ved x=0 for mod.-Euler
v[0] = y0velger # Initialveriden ved x=0 for Huens metode

print 'Euler nummer',teller-1,':', y[teller-1] # Skriver ut de approx.-verdiene generert av Euler
print 'Mod.-Euler nummer', teller-1,':',w[teller-1] # Skriver ut de approx.-verdiene generert av mod.-Euler
print 'Huen nummer', teller-1,':',v[teller-1] # Skriver ut de approx.-verdiene generert av Huen

while teller <= delintervall:
    y[teller] = g(teller) # Fyller inn Euler approx. verdier til løsningen
    w[teller] = p(teller) # Fyller inn Mod. Euler approx. verdier for løsningen
    v[teller] = q(teller) # Fyller inn Huen approx. verdier for løsningen
    
    print 'Euler nummer',teller,':', y[teller] # Skriver ut de approx.-verdiene generert av Euler
    print 'Mod.-Euler nummer', teller,':',w[teller] # Skriver ut de approx.-verdiene generert av mod.-Euler
    print 'Huen nummer', teller,':',v[teller] # Skriver ut de approx.-verdiene generert av Huen
    
    teller = teller + 1 # øker teller med 1

"--------Newtons metode--------"

Ny1 = 1.0 # En gjetting for y(1) / v(1)

listY11.append(y0) # Legger y0 i listen listY
listX11.append(x0) # Legger x0 i listen listX11

while x1 < upper - h: # ytre løkke som går til neste trapes
    
    Ny0 = y0 # Ny0 settes lik y0
    teller = 0.0 # setter teller til 0
    x1 = x0 + h # x1 er lik x0 pluss bredden på trapeset
     
    while teller < iterasjon: # antall iterasjoner for newtons metode
        Ny1 = Ny0 - (F(Ny0) / Fd(Ny0)) # newtons metode
        Ny0 = Ny1 # Ny0 settes lik Ny1
        teller += 1 # øker teller med 1
       
    y1 = Ny0 # y1 settes lik den nye verdien fra newtons
    x0 = x1 # x0 settes lik x1
    y0 = y1 # y0 settes lik y1 som er verdien fra Ny0
    
    listY11.append(y0) # Legger den nye verdien av y0 i listY
    listX11.append(x0) # Legger den nye verdien av x0 i listX

"--------Plotting--------"

plt.clf() # Visker ut leretet

if viseuler == 1:
    plt.plot(x, y, 'bo', label = r'$Euler$') # Plotter Euler approx.

if vismodeuler == 1:
    plt.plot(x, w, 'ro', label = r'$Mod.-Euler$') # Plotter Modifisert Euler approx.

if visheun == 1:
    plt.plot(x, v, 'go', label = r'$Heun$') # Plotter Heun approx.

if visnewton == 1:
    plt.plot(listX11, listY11, 'yo', label = r'$Newton$') # Plotter Newton approx.

if visexact == 1:
    plt.plot(br, o[:], label = r'$Exact$')  # Plotter Exact

plt.title(r'FE-MAT1000 - Semester oppgave 2014')

if Valg == 1:
    plt.xlabel('x - akse')
    plt.ylabel('y - akse')

if Valg == 2 or Valg == 3:
    plt.xlabel('Tid (s)')
    plt.ylabel('Fart (m/s)')
    
plt.legend(loc='lower right') # Plotter legend
plt.show() # Viser frem leretet (canvas)
