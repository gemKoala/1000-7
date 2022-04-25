# program 1000-7
import time

# variables
num = 1000
print("Program 1000-7")
while num >= 0:
    num = num - 7
    print(num, "-7 =", num)
    time.sleep(0.05)
    if num <= 0:
        print("Number less than 0,program end")
        input("Press enter to exit")
