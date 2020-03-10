'''
    Name: Eric Truong
    ID: 018149311
    Instructor: Minhthong Nguyen
    Date: November 2nd, 2018
'''


def reading():

    name = open('my_name', 'w')

    name.write('Eric Truong')

    name.close()
    
    file = open('my_name', 'r')

    file_contents = file.read()

    file.close()

    print(file_contents)

def writing():

    numbers = open('testing', 'w')

    x = 0

    while x < 100:
        x += 1
        numbers.write(str(x))
        numbers.write('\n')

    numbers.close()

reading()

writing()
