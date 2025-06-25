
def get_starting_number():
    number = input("How many bottles of beer on the wall? ")
    while not number.isdigit() or int(number) < 1:
        number = input("How many bottles of beer on the wall? ")
    return int(number)

def sing(starting_number):
    bottles = starting_number
    keep_singing = True
    while keep_singing:
        if bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            keep_singing = False
        else:
            next_bottles = bottles - 1
            bottle_word = "bottle" if next_bottles == 1 else "bottles"
            print(str(bottles) + " bottles of beer on the wall, " + str(bottles) + " bottles of beer.")
            print("Take one down, pass it around, " + str(next_bottles) + " " + bottle_word + " of beer on the wall.\n")
            bottles = next_bottles
