import matplotlib.pyplot as plt
import time
import math

log_time = []
linearithmic_time = []
linear_time = []
quadratic_time = []
polynomial_time = []
exponential_time = []

inputs = []
n = 5

def logarithmic(n):
    return math.log(n)

def linearithmic(n):
    return n*math.log(n)
    
def linear(n):
    return n

def quadratic(n):
    return n*n

def polynomial(n):
    return n**3
    
def exponential(n):
    return 2**n
    

while n < 100000:
    n += 5
    inputs.append(n)

    start = time.time()
    (logarithmic(n))
    log_time.append(time.time()-start)

    start_1 = time.time()
    (linearithmic(n))
    linearithmic_time.append(time.time()-start_1)

    start_2 = time.time()
    (linear(n))
    linear_time.append(time.time()-start_2)

    start_3 = time.time()
    (quadratic(n))
    quadratic_time.append(time.time()-start_3)

    start_4 = time.time()
    (polynomial(n))
    polynomial_time.append(time.time()-start_4)

    start_5 = time.time()
    (exponential(n))
    exponential_time.append(time.time()-start_5)
    

plt.plot(inputs,log_time)
plt.plot(inputs,linearithmic_time)
plt.plot(inputs,linear_time)
plt.plot(inputs,quadratic_time)
plt.plot(inputs,polynomial_time)
plt.plot(inputs,exponential_time)
plt.title('Asymptotic Analysis of\n' + 'Common Functions')
plt.xlabel('Input Size')
plt.ylabel('Execution Time')
plt.legend(["logarithm", "linearithmic", "linear", "quadratic", "polynomial", "exponential"])

plt.show()





    