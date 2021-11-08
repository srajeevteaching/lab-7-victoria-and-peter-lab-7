import random
# asks the user how many times they want to roll the dice
def get_number_of_rolls ():
    rolls = input("How many times would you like to roll the dice? ")
    if (rolls.isdigit()):
        rolls =int(rolls)
        return rolls
    # quits if a non-valid integer
    else:
        print ("Please input a valid integer")
        return 0
# simulates the two die rolling and sums them
def roll_dice ():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    sum = die1 + die2
    return sum
# inputs the dice sum into the next spot in the list
def create_histogram (x):
    count[x-2] += 1
    #print (count)
# prints out the histogram by printing the number rolled on the dice and how many times that sum resulted, represented by the number of *
def print_histogram():
    x=2
    # goes through the list and prints the sum number
    for item in count:
        print (x, ":", end = " ")
        y= item
        i=0
        # prints the correct number of * for that sum
        while (i<y):
            print("*", end =" ")
            i+=1
        print ("\t")
        x+=1
# main that calls all the functions
roll_number = get_number_of_rolls()
if (roll_number != 0):
    i=0
    count=[0,0,0,0,0,0,0,0,0,0,0]
    while (i < roll_number):
        dice_sum = roll_dice()
         #print (dice_sum)
        create_histogram(dice_sum)
        i+=1
# print out the final outputs
print (count)
print_histogram()
