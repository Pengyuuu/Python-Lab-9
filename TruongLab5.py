'''
    Name: Eric Truong
    ID: 018149311
    Instructor: Minhthong Nguyen
    Date: September 28, 2019

'''
choice = 'Y'
while(choice == 'Y' or choice == 'y'):
    usrinput = int(input('Enter a number between 1 and 100: '))
    while usrinput > 100 or usrinput < 1:
        usrinput = int(input('Not valid, please try again'))
    print('This number is valid')
    choice = input('Would you like to continue? Y/N: ')
        
'''
#identify num
num = 0

#loop it to get to 1000
for i in range(0, 1010, 10):
    print(num)
    num = num + 10
'''

'''

#prompt user about what's going to happen
print('When prompted, please enter a series of numbers')
print('To stop, please enter a negative number')

#loop it
sum = 0
counter = 0
flag = True
while flag:
    num = int(input('Please enter a number: '))
    if num < 0:
        flag = False
        #break
    else:
        sum = sum + num
        #counter = counter + 1
print('Your total is ',sum)

'''

    
    

    
