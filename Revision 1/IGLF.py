def find_pressure(n,T,V):
    pressure=(.082057)*n*T/V
    return pressure

test_n = 10
test_T = 298
test_V = 5
print("Result:", find_pressure(test_n, test_T, test_V))
