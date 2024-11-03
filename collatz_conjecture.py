#if odd multiply by 3 then add 1
#if even divide by 2
import matplotlib.pyplot as plt
#variables
steps = 0
sec = []
#define the initial number
num = int(input("Enter your initial number: "))

#the algorithm
def collatz(num):
    global steps, sec
    while num!=1: 
        if num%2==0:
            sec.append(num)
            num=num//2
            print(num)
        else:
            sec.append(num)
            num=3*num+1
            print(num)
        steps+=1

collatz(num)
print("Results:")
print(f"{sec}\n{steps}")

#Plotting the numbers in a grahp
plt.suptitle(f'Collazt Conjecture of {num}')
plt.text(0, 0, f'Steps:{steps}')
plt.plot(sec, 'g--')
plt.show()