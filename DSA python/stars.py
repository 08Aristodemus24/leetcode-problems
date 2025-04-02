from argparse import ArgumentParser

# print the ff. diagram
#    *   
#   ***
#  *****
#   ***
#    *

#    *
#   ***
#    *


# for corner cases like
# 2, and 1 level
# we just print *

def print_star(levels: int=10):

    # pattern is 1, 2, 3, 4, 5 then 4, 3, 2, 1 if 5 levels
    # 1, 2, 3, then 2, 1 if 3 levels
    # we have to somehow find the median of a level
    # e.g. for 10 its 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1
    n = levels
    median = n // 2
    print(median)

    # this prints a triangle
    # |\
    # | \
    # |__\
    for i in range(n):

        for j in range(i + 1):
            print("*", end="")
        
        # print nextline
        print()

    # this prints a triangle not leaning
    #   /|
    #  / |
    # /__|
    print('\n')
    for i in range(1, n + 1):
        # we print the spaces going from
        # n - 1 = 9
        # n - 2
        # n - 3
        # n - 4
        # ...
        # n - 9 = 1
        # 10 - 1
        for j in range(n - i):
            print(" ", end="")
        
        # then we print the stars for this level
        # which will be 1, 2, 3, 4, ..., 10
        for j in range(i):
            print("*", end="")
        
        # print a newline for every new line of stars
        print()

    # prints a this triangle
    # ____
    # \   |
    #  \  |
    #   \ |
    #    \|
    # 5 stars, 0 spaces
    # 4 stars, 1 spaces
    # 3, stars, 2 spaces
    # 2 stars, 3 spaces
    # 1 star, 4 spaces

    print('\n')
    for i in range(n, 0, -1):
        # print spaces first
        # 5 - 5 = 0 spaces
        # 5 - 4 = 1 spaces
        # 5 - 3 = 2 spaces
        # 5 - 2 = 3 spaces
        # 5 - 1 = 4 spaces
        # for j in range(n - i):
        print(" " * (n - i), end="")

        # print the stars second
        # 5 - 0
        # 4
        for j in range(i):
            print("*", end="")
        
        # print a newline for every new line of stars
        print()

    # this can be the first method of doing a hill and an inverted hill
    # 0000* 00000 
    # 000** *0000
    # 00*** **000
    # 0**** ***00
    # ***** ****0

    # ***** ****0
    # 0**** ***00
    # 00*** **000
    # 000** *0000
    # 0000* 00000

    # for first outer loop
    # 4 spaces 1 star 0 star 5 spaces
    # 3 spaces 2 stars 1 star 4 spaces
    # 2 spaces 3 stars 2 stars 3 spaces
    # 1 spaces 4 stars 3 stars 2 spaces
    # 0 spaces 5 stars 4 stars 1 spaces

    # for second outer loop
    # 0 spaces 5 stars 4 stars 1 space
    # 1 spaces 4 stars 3 stars 2 space
    # 2 spaces 3 stars 2 stars 3 space
    # 3 spaces 2 stars 1 stars 4 space
    # 4 spaces 1 stars 0 stars 5 space

    print('\n')
    for i in range(n):
        # pattern for first set of spaces
        # 5 - (0 + 1) = 4
        # 5 - (1 + 1) = 3
        # ...
        # 5 - (4 + 1) = 0
        print(" " * (n - (i + 1)), end="")

        # pattern for stars
        print("*" * (i + 1), end="")
        print("*" * i, end="")
        # print("*" * (i + (i + 1)), end="")

        # pattern for second set of spaces
        print(" " * (n - i), end="")

        # for newline
        print()

    # for second outeer loop
    for i in range(1, n):
        # pattern for first set of spaces
        # 0, 1, ..., 4
        print(" " * i, end="")

        # pattern for stars
        # 5 - 0 = 5
        # 5 - 1 = 4
        # ...
        # 5 - 4 = 1
        print("*" * (n - i), end="")

        # 5 - (0 + 1) = 4
        # 5 - (1 + 1) = 3
        # ...
        # 5 - (4 + 1) = 0
        print("*" * (n - (i + 1)), end="")

        # pattern for second set of spaces
        print(" " * (i + 1), end="")

        # for newline
        print()

    # this can be the first method of doing a an hourglass
    # ***** ****0
    # 0**** ***00
    # 00*** **000
    # 000** *0000
    # 0000* 00000

    # 0000* 00000 
    # 000** *0000
    # 00*** **000
    # 0**** ***00
    # ***** ****0

    # for first outer loop
    # 0 spaces 5 stars 4 stars 1 space
    # 1 spaces 4 stars 3 stars 2 space
    # 2 spaces 3 stars 2 stars 3 space
    # 3 spaces 2 stars 1 stars 4 space
    # 4 spaces 1 stars 0 stars 5 space

    # for second outer loop
    # 4 spaces 1 star 0 star 5 spaces
    # 3 spaces 2 stars 1 star 4 spaces
    # 2 spaces 3 stars 2 stars 3 spaces
    # 1 spaces 4 stars 3 stars 2 spaces
    # 0 spaces 5 stars 4 stars 1 spaces

    print('\n')
    for i in range(n):
        # pattern for first set of spaces
        # 0, 1, ..., 4
        print(" " * i, end="")

        # pattern for stars
        # 5 - 0 = 5
        # 5 - 1 = 4
        # ...
        # 5 - 4 = 1
        print("*" * (n - i), end="")

        # 5 - (0 + 1) = 4
        # 5 - (1 + 1) = 3
        # ...
        # 5 - (4 + 1) = 0
        print("*" * (n - (i + 1)), end="")

        # pattern for second set of spaces
        print(" " * (i + 1), end="")

        # for newline
        print()

    for i in range(1, n):
        # pattern for first set of spaces
        # 5 - (0 + 1) = 4
        # 5 - (1 + 1) = 3
        # ...
        # 5 - (4 + 1) = 0
        print(" " * (n - (i + 1)), end="")

        # pattern for stars
        print("*" * (i + 1), end="")
        print("*" * i, end="")
        # print("*" * (i + (i + 1)), end="")

        # pattern for second set of spaces
        print(" " * (n - i), end="")

        # for newline
        print()


    # this can be the second or more efficient method of doing a hill and an inverted hill
    # 0000*
    # 000*0*
    # 00*0*0*
    # 0*0*0*0*
    # *0*0*0*0*

    # *0*0*0*0*
    # 0*0*0*0*
    # 00*0*0*
    # 000*0*
    # 0000*
    # for the first outer loop
    # given level of 5 we need to print for the first line 
    # 4 spaces 1 star and space as end char
    # 3 spaces 2 
    # 2 spaces 3 stars
    # 1 space 4 stars
    # 0 spaces 5 stars
    # for second outer loop
    # 0 spaces 5 stars
    # 1 spaces 4 stars
    # 2 spaces 3 stars
    # 3 spaces 2 stars
    # 4 spaces 1 star 

    print('\n')
    for i in range(1, n + 1):
        # 1, 2, 3, 4, 5
        # 5 - (1) = 4
        # 5 - (2) = 3
        # 5 - (3) = 2
        # 5 - (4) = 1
        # 5 - (5) = 0
        print(" " * (n - i), end="")
        for j in range(i):
            # 0 < 1
            # 01 < 2
            # ...
            # 01234 < 5
            print("*", end=" ")
        print()
    
    for i in range(1, n):
        # 0, 1, 2, 3, 4 
        print(" " * i, end="")
        for j in range(n - i, 0, -1):
            # 5 - 0 = 5 stars
            # 5 - 1 = 4 stars
            # ...
            # 5 - 4 = 1 star
            print("*", end=" ")
        
        print()


    # prints an hour glass
    # *0*0*0*0*
    # 0*0*0*0*
    # 00*0*0*
    # 000*0*
    # 0000*

    # 0000*
    # 000*0*
    # 00*0*0*
    # 0*0*0*0*
    # *0*0*0*0*

    # first outer loop has 
    # 0 spaces 5 stars
    # 1 spaces 4 stars
    # 2 spaces 3 stars
    # 3 spaces 2 stars
    # 4 spaces 1 star 

    # second outer loop has
    # 4 spaces 1 star and space as end char
    # 3 spaces 2 
    # 2 spaces 3 stars
    # 1 space 4 stars
    # 0 spaces 5 stars
    
    print('\n')
    for i in range(n):
        # 0, 1, 2, 3, 4 spaces 
        print(" " * i, end="")
        for j in range(n - i, 0, -1):
            # 5 - 0 = 5 stars
            # 5 - 1 = 4 stars
            # ...
            # 5 - 4 = 1 star
            print("*", end=" ")
        
        print()

    # second outerloop of hour glass
    for i in range(2, n + 1):
        # 1, 2, 3, 4, 5
        # 5 - (1) = 4
        # 5 - (2) = 3
        # 5 - (3) = 2
        # 5 - (4) = 1
        # 5 - (5) = 0
        print(" " * (n - i), end="")
        for j in range(i):
            # 0 < 1
            # 01 < 2
            # ...
            # 01234 < 5
            print("*", end=" ")
        print()




    


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--level", type=int, help="number of levels")
    args = parser.parse_args()

    print_star(levels=args.level)

