#Write your code below this row 👇

for nr in range(0,100):
    nr += 1
    if nr % 3 == 0 and nr % 5 == 0:
        print("FizzBuzz")
    elif nr % 3 == 0:
        print("Fizz")
    elif nr % 5 == 0:
        print("Buzz")
    else:
        print(nr)