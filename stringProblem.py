# Given String with letters and numbers
# Eliminate space and number bigger than 5
# Print out in list of string

def origin(str):
    print("Origin = ", str)

def niceFilter(str):

    afterFilter = []

    for letter in str:
        if letter == " " or letter == "7" or letter == "6" or letter == "9" or letter == "8":
            continue
        afterFilter.append(letter)

    print("After = ",afterFilter)

# Here the sample 1

word1 = "classic laptops at RM2758.91"
origin(word1)
niceFilter(word1)
