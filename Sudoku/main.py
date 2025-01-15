#imports necessary modules

import turtle as trtl
import time
import os
import random
from random import sample

#seq performs a mathematical formula that constructs the board
def seq(r, c):
    return (3 * (r % 3) + r // 3 + c) % 9
def change(s):
    return sample(s, len(s))
base = range(3)
#generates a valid board
rows = [i * 3 + r for i in change(base) for r in change(base)]
cols = [i * 3 + c for i in change(base) for c in change(base)]
nums = change(range(1, 3 * 3 + 1))
board = [[nums[seq(r, c)] for c in cols] for r in rows]
#contains the valid board generated
display = [[board[i][j] for j in range(0, 9)] for i in range(0, 9)]

#generates the number of missing values
missing = random.randint(35, 50)
cur = 0
while cur != missing:
    cur_x = random.randint(0, 8)
    cur_y = random.randint(0, 8)
    if display[cur_y][cur_x] != 0:
        display[cur_y][cur_x] = 0
        cur += 1
wn = trtl.Screen()
wn.setup(width=512, height=511)
#renders a blank board
sudoku_board = "sudoku.gif"
wn.bgpic(sudoku_board)

#stores the numbers that are drawn to the board
one = "one.gif"
two = "two.gif"
three = "three.gif"
four = "four.gif"
five = "five.gif"
six = "six.gif"
seven = "seven.gif"
eight = "eight.gif"
nine = "nine.gif"
zero = "zero.gif"

# keeps count of how many of the numbers have already been put on the board
rep_nine = 1
rep_zero = 1
rep_one = 1
rep_two = 1
rep_three = 1
rep_four = 1
rep_five = 1
rep_six = 1
rep_seven = 1
rep_eight = 1

#the location of each of the rows and colums so you can put the numbers into the right boxes
clocation = [-185, -135, -90, -40, 5, 55, 105, 150, 195]
rlocation = [170, 125, 75, 25, -20, -65, -115, -165, -210]


#puts all the numbers onto the intial board
for i in range(0, 9):
    for j in range(0, 9):
        if display[i][j] == 1:
            wn.addshape(str("one" + str(rep_one) + ".gif"))
            icon_one = trtl.Turtle(shape=str("one" + str(rep_one) + ".gif"))
            icon_one.hideturtle()
            icon_one.penup()
            icon_one.speed(10)
            icon_one.goto(clocation[j], rlocation[i])
            icon_one.showturtle()
            rep_one += 1
        if display[i][j] == 2:
            wn.addshape(str("two" + str(rep_two) + ".gif"))
            icon_two = trtl.Turtle(shape=str("two" + str(rep_two) + ".gif"))
            icon_two.hideturtle()
            icon_two.penup()
            icon_two.speed(10)
            icon_two.goto(clocation[j], rlocation[i])
            icon_two.showturtle()
            rep_two += 1
        if display[i][j] == 3:
            wn.addshape(str("three" + str(rep_three) + ".gif"))
            icon_three = trtl.Turtle(shape=str("three" + str(rep_three) + ".gif"))
            icon_three.hideturtle()
            icon_three.penup()
            icon_three.speed(10)
            icon_three.goto(clocation[j], rlocation[i])
            icon_three.showturtle()
            rep_three += 1
        if display[i][j] == 4:
            wn.addshape(str("four" + str(rep_four) + ".gif"))
            icon_four = trtl.Turtle(shape=str("four" + str(rep_four) + ".gif"))
            icon_four.hideturtle()
            icon_four.penup()
            icon_four.speed(10)
            icon_four.goto(clocation[j], rlocation[i])
            icon_four.showturtle()
            rep_four += 1
        if display[i][j] == 5:
            wn.addshape(str("five" + str(rep_five) + ".gif"))
            icon_five = trtl.Turtle(shape=str("five" + str(rep_five) + ".gif"))
            icon_five.hideturtle()
            icon_five.penup()
            icon_five.speed(10)
            icon_five.goto(clocation[j], rlocation[i])
            icon_five.showturtle()
            rep_five += 1
        if display[i][j] == 6:
            wn.addshape(str("six" + str(rep_six) + ".gif"))
            icon_six = trtl.Turtle(shape=str("six" + str(rep_six) + ".gif"))
            icon_six.hideturtle()
            icon_six.penup()
            icon_six.speed(10)
            icon_six.goto(clocation[j], rlocation[i])
            icon_six.showturtle()
            rep_six += 1
        if display[i][j] == 7:
            wn.addshape(str("seven" + str(rep_seven) + ".gif"))
            icon_seven = trtl.Turtle(shape=str("seven" + str(rep_seven) + ".gif"))
            icon_seven.hideturtle()
            icon_seven.penup()
            icon_seven.speed(10)
            icon_seven.goto(clocation[j], rlocation[i])
            icon_seven.showturtle()
            rep_seven += 1
        if display[i][j] == 8:
            wn.addshape(str("eight" + str(rep_eight) + ".gif"))
            icon_eight = trtl.Turtle(shape=str("eight" + str(rep_eight) + ".gif"))
            icon_eight.hideturtle()
            icon_eight.penup()
            icon_eight.speed(10)
            icon_eight.goto(clocation[j], rlocation[i])
            icon_eight.showturtle()
            rep_eight += 1
        if display[i][j] == 9:
            wn.addshape(str("nine" + str(rep_nine) + ".gif"))
            icon_nine = trtl.Turtle(shape=str("nine" + str(rep_nine) + ".gif"))
            icon_nine.hideturtle()
            icon_nine.penup()
            icon_nine.speed(10)
            icon_nine.goto(clocation[j], rlocation[i])
            icon_nine.showturtle()
            rep_nine += 1
#starts the timer
start = time.perf_counter()
correct = True
first = 0

#the actual game starts here by taking in user inputs
complete = False
while complete == False:
    if correct == True and first != 0: print("Correct!")
    elif first != 0: print("Nice try, guess again")
    first += 1
    row = int(input("row number: "))
    col = int(input("Column number: "))
    row -= 1
    col -= 1
    guess = int(input("What is your guess: "))
    if (guess == board[row][col]):
        display[row][col] = board[row][col]
        if display[row][col] == 1:
            wn.addshape(str("one" + str(rep_one) + ".gif"))
            icon_one = trtl.Turtle(shape=str("one" + str(rep_one) + ".gif"))
            icon_one.hideturtle()
            icon_one.penup()
            icon_one.speed(10)
            icon_one.goto(clocation[col], rlocation[row])
            icon_one.showturtle()
            rep_one += 1
        if display[row][col] == 2:
            wn.addshape(str("two" + str(rep_two) + ".gif"))
            icon_two = trtl.Turtle(shape=str("two" + str(rep_two) + ".gif"))
            icon_two.hideturtle()
            icon_two.penup()
            icon_two.speed(10)
            icon_two.goto(clocation[col], rlocation[row])
            icon_two.showturtle()
            rep_two += 1
        if display[row][col] == 3:
            wn.addshape(str("three" + str(rep_three) + ".gif"))
            icon_three = trtl.Turtle(shape=str("three" + str(rep_three) +
                                               ".gif"))
            icon_three.hideturtle()
            icon_three.penup()
            icon_three.speed(10)
            icon_three.goto(clocation[col], rlocation[row])
            icon_three.showturtle()
            rep_three += 1
        if display[row][col] == 4:
            wn.addshape(str("four" + str(rep_four) + ".gif"))
            icon_four = trtl.Turtle(shape=str("four" + str(rep_four) + ".gif"))
            icon_four.hideturtle()
            icon_four.penup()
            icon_four.speed(10)
            icon_four.goto(clocation[col], rlocation[row])
            icon_four.showturtle()
            rep_four += 1
        if display[row][col] == 5:
            wn.addshape(str("five" + str(rep_five) + ".gif"))
            icon_five = trtl.Turtle(shape=str("five" + str(rep_five) + ".gif"))
            icon_five.hideturtle()
            icon_five.penup()
            icon_five.speed(10)
            icon_five.goto(clocation[col], rlocation[row])
            icon_five.showturtle()
            rep_five += 1
        if display[row][col] == 6:
            wn.addshape(str("six" + str(rep_six) + ".gif"))
            icon_six = trtl.Turtle(shape=str("six" + str(rep_six) + ".gif"))
            icon_six.hideturtle()
            icon_six.penup()
            icon_six.speed(10)
            icon_six.goto(clocation[col], rlocation[row])
            icon_six.showturtle()
            rep_six += 1
        if display[row][col] == 7:
            wn.addshape(str("seven" + str(rep_seven) + ".gif"))
            icon_seven = trtl.Turtle(shape=str("seven" + str(rep_seven) +
                                               ".gif"))
            icon_seven.hideturtle()
            icon_seven.penup()
            icon_seven.speed(10)
            icon_seven.goto(clocation[col], rlocation[row])
            icon_seven.showturtle()
            rep_seven += 1
        if display[row][col] == 8:
            wn.addshape(str("eight" + str(rep_eight) + ".gif"))
            icon_eight = trtl.Turtle(shape=str("eight" + str(rep_eight) +
                                               ".gif"))
            icon_eight.hideturtle()
            icon_eight.penup()
            icon_eight.speed(10)
            icon_eight.goto(clocation[col], rlocation[row])
            icon_eight.showturtle()
            rep_eight += 1
        if display[row][col] == 9:
            wn.addshape(str("nine" + str(rep_nine) + ".gif"))
            icon_nine = trtl.Turtle(shape=str("nine" + str(rep_nine) + ".gif"))
            icon_nine.hideturtle()
            icon_nine.penup()
            icon_nine.speed(10)
            icon_nine.goto(clocation[col], rlocation[row])
            icon_nine.showturtle()
            rep_nine += 1
        missing -= 1
        os.system("clear")
        correct = True
    else:
        correct = False
        os.system("clear")
    if missing == 0: 
      complete = True
os.system("clear")
print("Congratulations you have completed the board!!!!!!!!")

# stops timer
end = time.perf_counter()

#performs calculations and prints time taken
minute = end-start
if(minute > 60):
  m = int(minute/60)
  s = minute % 60
  print("You took " + str(m) + " minutes " + str(round(s)) + " seconds")
else: print("You took " + str(round((end-start), 2)) + " seconds")

