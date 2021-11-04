import random
def get_number_of_rolls ():
    rolls = input("How many times would you like to roll the dice? ")
    if (rolls.isdigit()==True):
        rolls =int(rolls)
        return rolls
    else:
        print ("Please input a valid integer")
        return 0

def roll_dice ():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    sum = die1 + die2
    return sum

def create_histogram (x):
    count[x-2] += 1
    print (count)

def print_histogram(a):
    #print (count[1], end =" ")
    for item in a:
        print ("\t", item, ":")
        for i in range (count[item]):
            print("*", end =" ")


    #for i in range (count[1]):
       # print ("*", end=" ")
roll_number = get_number_of_rolls()
if (roll_number != 0):
    i=0
    count=[0,0,0,0,0,0,0,0,0,0,0]
    while (i < roll_number):
        dice_sum = roll_dice()
        print (dice_sum)
        create_histogram(dice_sum)
        i+=1
print_histogram(count)