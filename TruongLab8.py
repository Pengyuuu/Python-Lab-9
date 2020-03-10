'''
    Name: Eric Truong
    ID: 018149311
    Instructor: Minhthong Nguyen
    Date: October 26, 2018

'''

#import turtle
import turtle

#prompt user for the vertices of the triangle
x1 = float(input('What is the x coordinate for your first vertex?: '))
y1 = float(input('What is the y coordinate for your first vertex?: '))

x2 = float(input('What is the x coordinate for your second vertex?: '))
y2 = float(input('What is the y coordinate for your second vertex?: '))

x3 = float(input('What is the x coordinate for your third vertex?: '))
y3 = float(input('What is the y coordinate for your third vertex?: '))

#ask for the color of the triangle
tricolor = input('What color should the triangle be?:')

#define drawing the triangle
def drawTriangle():
    turtle.speed(0)
    turtle.penup()
    turtle.fillcolor(tricolor)
    turtle.begin_fill()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    turtle.end_fill()
    
#call the function
drawTriangle()

#define compound monthly interest formula
def formula():
    total = 1
    total += interest
    total = total ** months
    total = total * present

    return total

#prompt user for information
present = float(input('What is your current amount of money?: '))

interest = float(input('What is your interest rate?: '))
interest = interest / 100

months = int(input('How many months will pass?: '))

#set total to the return value in function
total = formula()

#print it
print('You will have', \
      format(total, '.2f'))
      

