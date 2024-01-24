# Draw a spiral
import turtle

t = turtle.Turtle()

length = 10
degrees = 90

while True:
    t.forward(length)
    t.right(degrees)

    t.forward(length)
    t.right(degrees)

    length += 10
    degrees += 5

# Grocery List
item_list = []

choice = ""

while choice != "quit" and choice != "q":
    choice = input("What would you like to do: add (a), remove (r), replace (p), view (v)? ")

    if choice == "add" or choice == "a":
        item = input("Enter the item to add: ")
        item_list.append(item)

    elif choice == "remove" or choice == "r":
        index = int(input("Enter the item's index to remove that item: "))
        item_list.pop(index-1)

    elif choice == "replace" or choice == "p":
        item = input("Enter the item to add: ")
        index = int(input("Enter the item's index to replace that item: "))
        item_list[index-1] = item

    elif choice == "view" or choice == "v":
        print(item_list)
