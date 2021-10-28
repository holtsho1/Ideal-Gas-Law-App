from IGLF import *

print("Welcome to Ideal Gas Law App! Please type the variable you are trying to find: Pressure, Volume, Temperature, or Number of Moles")

var=input('Variable you are trying to find:')

var=var.strip()
var=var.lower()

if var=='pressure':
    n=float(input('Number of Moles:'))
    T=float(input('Temperature (in Kelvin):'))
    V=float(input('Volume (in Liters):'))
    units='Atmospheres'
    result=find_pressure(n,T,V) #in atm

if var=='temperature':
    n=float(input('Number of Moles:'))
    P=float(input('Pressure (in atmospheres):'))
    V=float(input('Volume (in Liters):'))
    units='Kelvin'
    result=find_temperature(n,V,P)

if var=='number of moles':
    T=float(input('Temperature (in Kelvin):'))
    P=float(input('Pressure (in atmospheres):'))
    V=float(input('Volume (in Liters):'))
    units='Moles'
    result=find_moles(T,V,P)

if var=='volume':
    T=float(input('Temperature (in Kelvin):'))
    P=float(input('Pressure (in atmospheres):'))
    n=float(input('Number of Moles:'))
    units='Liters'
    result=find_volume(n,T,P)

print('Your answer is',result,units)
