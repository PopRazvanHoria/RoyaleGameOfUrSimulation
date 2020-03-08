import matplotlib.pyplot as plt
import random

plt.ion()
def picks():
    a = []
    while len ( a )!=100000:
        w = random.randint(0,1)
        x = random.randint(0,1)
        y = random.randint(0,1)
        z = random.randint(0,1)
        sum=w+x+y+z
        a+=[sum]
    plt.xlabel('Value')
    plt.ylabel('Throws')
    plt.hist(a)
    plt.show()
    plt.savefig('plotUr.png')
picks()
