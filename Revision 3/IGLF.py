def find_pressure(n,T,V,R=.082057):
    try:
        Pressure=n*R*T/V
        return Pressure
    except ZeroDivisionError:
        return "Volume must be greater than 0."
   


#test code/parameters
test_n = 10
test_T = 298
test_V = 0
test_R = 62.364 #Torr!
print("Result:", find_pressure(test_n, test_T, test_V, R = test_R))
