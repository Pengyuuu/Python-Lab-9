'''

    Name: Eric Truong
    ID: 018149311
    Instructor: Minhthong Nguyen
    Date: October 17, 2018

'''
#import random
import random

#define the times ten function
def times_ten():
    num = int(input('Please enter a number: '))
    num = num * 10
    print(num)

#call it
times_ten()

#random function
rand = random.randint(1, 100)

#print the number
print(rand)

#define the get first name function
def get_first_name():
    name = input('What is your name?: ')
    return name

#call the function and assign the return value to x
x = get_first_name()

#print the return value
print('Your name is ',x)

