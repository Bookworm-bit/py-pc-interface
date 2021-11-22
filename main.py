import sys
import os 
import decimal
print("Pick a category to start with!")
print("[1] Calculator")
print("[2] Games")
print("[3] UNDER CONTRUCTION")
print("[4] UNDER CONTRUCTION")
print("[5] UNDER CONTRUCTION")
while True:
    catPick = input("\n")
    try:
        int(catPick)
    except ValueError:
        print("Oops there was an error")
        if (catPick == "home"):
            print("Pick a category to start with!")
            print("[1] Calculator")
            print("[2] Games")
            print("[3] UNDER CONTRUCTION")
            print("[4] UNDER CONTRUCTION")
            print("[5] UNDER CONTRUCTION")
    while (int(catPick) != ValueError):
        if (int(catPick) == 1):
            o = input("Select your operator! (add = 1, subtract = 2, multiply = 3, divide = 4, power of = 5) \n")
            g = input("Enter your first number! \n")
            h = input("Enter your second number! \n")
            try:
                int(o)
                int(g)
                int(h)
            except ValueError:
                if (str(o) == "home"):
                    print("Pick a category to start with!")
                    print("[1] Calculator")
                    print("[2] Games")
                    print("[3] UNDER CONTRUCTION")
                    print("[4] UNDER CONTRUCTION")
                    print("[5] UNDER CONTRUCTION")
                if (str(o) == "home"):
                    print("Pick a category to start with!")
                    print("[1] Calculator")
                    print("[2] Games")
                    print("[3] UNDER CONTRUCTION")
                    print("[4] UNDER CONTRUCTION")
                if (str(h) == "home"):
                    print("Pick a category to start with!")
                    print("[1] Calculator")
                    print("[2] Games")
                    print("[3] UNDER CONTRUCTION")
                    print("[4] UNDER CONTRUCTION")
                    print("[5] UNDER CONTRUCTION")
            ans = ""
            if (int(o) == 1):
                ans = float(g) + float(h)
            if (int(o) == 2):
                ans = float(g) - float(h)
            if (int(o) == 3):
                ans = float(g) * float(h)
            if (int(o) == 4):
                ans = float(g) / float(h)
            if (int(o) == 5):
                ans = pow(float(g), float(h))
            print("The answer is", float(ans))




    

