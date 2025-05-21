import turtle

while True:
    try:
        side = int(input("Please input number of sides: "))
        break
    except:
        print(sides, " was input.")
        print("Input must be integer.")

for _ in range(side):
    turtle.forward(100)
    turtle.right(360/side)