# Menu class that stores all methods of the Menu
import os

newProduct = "N"
showProduct = "P"
showUsers = "U"


def menuchoice(choice):
    if newProduct.lower() == choice.lower():
        newproduct()

    elif showProduct.lower() == choice.lower():
        showproducts()

    elif showUsers.lower() == choice.lower():
        showusers()

    else:
        print("false choice")



def menudisplay():
    clear()
    print("MENU")
    print("\n")
    print("\n")
    print("New Product ["+newProduct+"] | Show Products ["+showProduct+"] | Show Users ["+showUsers+"]")
    return input()


def newproduct():
    print("hello world")


def showproducts():
    print("hello world")


def showusers():
    print("hello world")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')