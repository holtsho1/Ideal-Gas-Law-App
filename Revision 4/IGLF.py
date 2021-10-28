
def find_pressure(n,T,V,R=.082057):
    
    try:
        Pressure=(n*R*T/V)
        return Pressure
    except ZeroDivisionError:
        return "Volume must be greater than 0."
   
def find_volume(n,T,P,R=.082057):
    try:
        Volume=(n*R*T/P)
        return Volume
    except ZeroDivisionError:
        return "Pressure must be greater than 0."

def find_temperature(n,V,P,R=.082057):
    try:
        Temperature=(V*P/(n*R))
        return Temperature
    except ZeroDivisionError:
        return "Temperature must be greater than 0."

def find_moles(T,V,P,R=.082057):
    try:
        NumberMoles=(V*P/(R*T))
        return NumberMoles
    except ZeroDivisionError:
        return "Temperature must be greater than 0."




#test code/parameters
#test_n = 10
#test_T = 298
#test_V = 0
#test_P = 40 #Torr!
#test_R = 62.364 #Torr!
#print("Result:", find_pressure(test_n, test_T, test_V, R = test_R))
#print("Result:", find_volume(test_n, test_T, test_P, R = test_R))
#print("Result:", find_temperature(test_n, test_V, test_P, R = test_R))
#print("Result:", find_temperature(test_T, test_V, test_P, R = test_R))

