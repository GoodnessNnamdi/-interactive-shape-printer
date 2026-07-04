name = input("What's that your fine name?😏: ")

print("Ouuu, such a charming name🤭. Welcome, " + name + "!")

print("\nAvailable Shapes: ")
print("1. Left triangle")
print("2. right triangle")
print("3. Inverted Left triangle")
print("4. Inverted right triangle")
print("5. Pascal's left triangle")
print("6. Pascal's right triangle")
print("7. Diamond")
print("8. Pyramid")
print("9. Double pyramid")
print("10. Inverted pyramid")
print("11. Inverted double pyramid")
print("12. Hour glass")

choice = int(input("\nChoose a number corresponding to a shape (1-12): "))
rows = int(input("Enter the number of rows for the shape: "))
print("\nPrinting your shape:\n")


if choice == 1:
    for i in range(1, rows + 1):
        print("*" * i)

elif choice == 2:
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * i)
        
elif choice == 3:
    for i in range(rows, 0, -1):
        print("*" * i)

elif choice == 4:
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * i)

elif choice == 5:
    for i in range(1, rows + 1):
        print("*" * i)
    for i in range(rows - 1, 0, -1):
        print("*" * i)

elif choice == 6:
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * i)
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * i)

elif choice == 7:
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

elif choice == 8:
    for i in range(1, rows + 1):
        print(" " * (rows - i) + " *" * (2 * i - 1))


elif choice == 9:
    for i in range(1, rows + 1):
        left_side = " " * (rows - i) + "*" * (2 * i - 1)
        right_side = "  " * (rows - i) + "*" * (2 * i - 1)
        print(left_side + " " + right_side)

elif choice == 10:
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

elif choice == 11:
    for i in range(rows, 0, -1):
        left_side = " " * (rows - i) + "*" * (2 * i - 1)
        right_side = "  " * (rows - i) + "*" * (2 * i  - 1)
        print(left_side + " " + right_side)

elif choice == 12:
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    for i in range(2, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
        
else:
    print("😒 You no go like calm down? Please run the program again and select between 1 and 12. ")
