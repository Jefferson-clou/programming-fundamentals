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

#print (opt==1)

if opt==1:
    add=num1+num2
    print(f"Addition is: {add}")

if opt==2:
    subs=num1-num2
    print(f"Substraction is: {subs}")

if opt==3:
    mult=num1*num2
    print(f"Multiplication is: {mult}")

if opt==4:
    div=num1/num2
    print(f"Division is: {div}")

if opt==5:
    add=num1+num2
    subs=num1-num2
    mult=num1*num2
    div=num1/num2
    print(f"\nAddition is: {add}")
    print(f"Substraction is: {subs}")
    print(f"Multiplication is: {mult}")
    print(f"Division is: {div}\n")
if opt <1 or opt >5:
    print ("Invalid option. Try again")


