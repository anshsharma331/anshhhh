Marks = int(input('Marks you obtained:\n\t'))
if Marks <= 50:
    if Marks < 25:
        print('Your grade is F grade')
    else:
        if Marks < 45:
            print('You got E grade')
        else:
            print('You got D grade')
else:
    if Marks < 60:
        print('You got C grade')
    else:
        if Marks < 80:
            print('You got B grade')
        else:
            print('You got A grade!')








year = int(input('Enter year: \n\t'))
a = year % 4
b = year % 100
c = year % 400
if a == 0:
    if b == 0:
        if c == 0:
            print('The year is a leap year!')
        else:
            print('The year is not a leap year')
    else:
        print('The year is a leap year!')
else:
    print('The year is not a leap year')





import random



for count in range(11):
    q1 = random.randint(0, 10)
    q2 = random.randint(0, 10)
    a = int(input(f"{q1} X {q2}"))
    if a == round(q1*q2):
        print("right")
    else:
        print("Wrong, the ans is", round(q1*q2))






#We'll assign a variable in "for loop" to pieces of candy


"""We know pieces of candy in jar are less than 200,
so we can assign a range of 200 to our variable"""

#Then, we apply for "if statement" to give us output that we need

"""Since remainders on division by 5, 6, & 7 are given to us,
we use "%" operator with "and" to fulfil all 3 conditions and give us a number"""

for candy_in_jar in range(200):
    if candy_in_jar % 5 == 2 and candy_in_jar % 6 == 3 and candy_in_jar % 7 == 2:
        print(candy_in_jar)



