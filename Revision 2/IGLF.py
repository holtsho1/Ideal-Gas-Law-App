def find_pressure(n,T,V,R=.082057):
    pressure=(R)*n*T/V
    return pressure

#test code
test_n = 10
test_T = 298
test_V = 5
test_R = 62.364 #Torr!
print("Result:", find_pressure(test_n, test_T, test_V, R = test_R))
