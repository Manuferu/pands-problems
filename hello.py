# This program calculates how many tiles you will need
# when tiling a wall of flor (in m2)

length = float(input("Enter room length:"))
width = float(input("Enter room width:"))


area =length *width

needed = area *1.05
print("you need ",needed, "tiles in metres squared.")


