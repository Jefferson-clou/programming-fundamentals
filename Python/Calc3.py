#Import packages
import os
from random import randint
#Initialize
num1=0
num2=0
add=0
subs=0
mult=0
div=0
apt=0

os.system("Clear")
print("Loading Basic Calc v.2.0...\n")

#Getr data (Imputs)

num1= randint(-100,100)
num2= randint(-100,100)

#Dsiplay generated numbers

print (f"Number 1: {num1}")
print (f"Number 2: {num2}\n")

#Display MainMenu

print("MAINMENU\n")
print("[1].Addition\n[2].Substraction\n[3].Multiplication\n[4].Division\n[5].All operations\n")

opt= int(input("Please, press any option[1-5]: ")) 

if opt==1:
    print(f"\nAddition is: {num1+num2}")
else:
    if opt==2:
        print(f"Substraction is: {num1-num2}")
    else:
            if opt==3:
                print(f"Multiplication is: {num1*num2}")
            else:
                    if opt==4:
                        print(f"Divison is: {num1/num2}")
                    else:
                            if opt==5:
                                print("Addition is:",num1+num2,"\nSubstraction is:", num1-num2,"\nMultiplication is:", num1*num2,"\nDivison is: ",num1/num2)
                            else:
                                print("Invalid option. Try aagin")
                

