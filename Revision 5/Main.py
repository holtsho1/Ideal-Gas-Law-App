from IGLF import *
#function that strips whitespace and lowercases letters, handles some user variances / edge cases for user input
def question_uniformity(question):
    question=question.strip()
    question=question.lower()
    question=question.strip('s')
    return question
#unused function, testing for way to use function to handle all user input testing
def input_test(the_input,correct_list):
    if not the_input in correct_list:
        print(the_input,'is not an expected input.')
        return False
    else:
        return True

IGLF_variables=['pressure','volume','temperature','moles'] #list of variables to pull from or loop over
#list of gas constant values as keys with units listed as values in order of: pressure, volume, temperature, moles
IGLF_constants={'0.08205':('atmosphere','liter','kelvin','mole'),'8.314':('pascal','meters cubed','kelvin','mole'),'.08205':('atmosphere','liter','kelvin','mole')}
#resets gas constant if run multiple times
R=0
print("Welcome to Ideal Gas Law App!")
print('Are you trying to find a graphical representation or a singular calcualted value of an Ideal Gas?')
question1=input('Please enter "Graph" or "Value":')

question1=question_uniformity(question1)
#handles program running in graph mode, loop continues until result is found, currently this mode is unavailable
while question1=='graph':
    print('This feature unavailable at this time')
    break
#handles program running in value mode, loop continues until result is found
while question1=='value':
    question2=input('Please type the variable you are trying to find: Pressure, Volume, Temperature, or Number of Moles. Variable you are trying to find:')

    question2=question_uniformity(question2)
    print("Let's figure out which gas constant you are using")
    question3=input('Do you know the value or the units of the gas constant you are using?')
    question3=question_uniformity(question3)
    #if user is entering the units they are using this code will find the value of gas constant for them
    if question3=='unit':
        test_list=[]
        m_list=[]
        for variable in IGLF_variables:
            test_list.append(input('What unit of '+variable+' are you using?'))
        for value_list in IGLF_constants.values():
            for value in value_list:
                for test in test_list:
                    if value==test:
                        m_list.append(test)
                        R=float(list(IGLF_constants.keys())[list(IGLF_constants.values()).index(value_list)])
                        #dict.keys()[dict.values().index(search_age)]
                        #(list(mydict.keys())[list(mydict.values()).index(16)])
            print(m_list)
            if not len(m_list)==4:
                m_list=[]
            else:
                break
        
        if not len(m_list)==4:
            print('Your 4 entered units do not match a gas constant. Please try again.')
            R=0
            continue
        else:
            print('Your gas constant has been selected!')
    #if user knows the value of gas constant, then this code will check that the value is for a gas constant, and find units for that value
    if question3=='value':
        gas_constant_input=input('What value for the gas constant are you using?')
        for key in IGLF_constants.keys():
            if key==gas_constant_input:
                R=float(key)
        if R==0:
            print('Your value did not match any of the gas constant values')
            print('Please try a different value')
            continue
#The next if statements calculate the value user is looking for based on variable they selected earlier
    if question2=='pressure':
        n=float(input('Number of Moles (in '+IGLF_constants[str(R)][3]+':)'))
        T=float(input('Temperature (in '+IGLF_constants[str(R)][2]+':)'))
        V=float(input('Volume(in '+IGLF_constants[str(R)][1]+':)'))
        units=IGLF_constants[str(R)][0]
        result=find_pressure(n,T,V,R)

    if question2=='temperature':
        n=float(input('Number of Moles(in '+IGLF_constants[str(R)][3]+':)'))
        P=float(input('Pressure(in '+IGLF_constants[str(R)][0]+':)'))
        V=float(input('Volume(in '+IGLF_constants[str(R)][1]+':)'))
        units=IGLF_constants[str(R)][2]
        result=find_temperature(n,V,P,R)

    if question2=='number of moles':
        T=float(input('Temperature(in '+IGLF_constants[str(R)][2]+':)'))
        P=float(input('Pressure(in '+IGLF_constants[str(R)][0]+':)'))
        V=float(input('Volume(in '+IGLF_constants[str(R)][1]+':)'))
        units=IGLF_constants[str(R)][3]
        result=find_moles(T,V,P,R)

    if question2=='volume':
        T=float(input('Temperature(in '+IGLF_constants[str(R)][2]+':)'))
        P=float(input('Pressure(in '+IGLF_constants[str(R)][0]+':)'))
        n=float(input('Number of Moles(in '+IGLF_constants[str(R)][3]+':)'))
        units=IGLF_constants[str(R)][1]
        result=find_volume(n,T,P,R)
    print('Your answer is',result,units) 
    question1='' #ends while loop to end program execution




