import random
random_number=random.randrange(1,100,1)
print("guess the number. range is 1-100")
print(random_number)
def check(random_number):
    try:
        vysledek=input("type it:")
        if vysledek < random_number:
            raise ValueError("too low")
        elif vysledek == random_number:
            print("you did it")
    except:
check(random_number)