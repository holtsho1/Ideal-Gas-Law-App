from IGLF import *
def question_uniformity(question):
    question=question.strip()
    question=question.lower()
    return question

def input_test(the_input,correct_list):
    
print("Welcome to Ideal Gas Law App!")
print('Are you trying to find a graphical representation or a singular calcualted value of an Ideal Gas?')
question1=input('Please enter "Graph" or "Value":')

question1=question_uniformity(question1)
while question1=='graph':
    print('This feature unavailable at this time')
    break
while question1=='value':
    question2=input('Please type the variable you are trying to find: Pressure, Volume, Temperature, or Number of Moles. Variable you are trying to find:')

    question2=question_uniformity(question2)
    print("Let's figure out which gas constant you are using")
    question3=input('Do you know the number value or the units of the gas constant you are using?')
    question3=question_uniformity(question3)

    if question2=='pressure':
        n=float(input('Number of Moles:'))
        T=float(input('Temperature (in Kelvin):'))
        V=float(input('Volume (in Liters):'))
        units='Atmospheres'
        result=find_pressure(n,T,V) #in atm

    if question2=='temperature':
        n=float(input('Number of Moles:'))
        P=float(input('Pressure (in atmospheres):'))
        V=float(input('Volume (in Liters):'))
        units='Kelvin'
        result=find_temperature(n,V,P)

    if question2=='number of moles':
        T=float(input('Temperature (in Kelvin):'))
        P=float(input('Pressure (in atmospheres):'))
        V=float(input('Volume (in Liters):'))
        units='Moles'
        result=find_moles(T,V,P)

    if question2=='volume':
        T=float(input('Temperature (in Kelvin):'))
        P=float(input('Pressure (in atmospheres):'))
        n=float(input('Number of Moles:'))
    units='Liters'
    result=find_volume(n,T,P)
    print('Your answer is',result,units)


question1=''

