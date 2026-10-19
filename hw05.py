"""
Name: Frida Li
Peers: 
References: 
"""

def get_letter():
     """Ask the user for a single uppercase letter (A, B, or C)."""
     while True:
         letter1 = input("Give an single uppercase letter: ")
         if len(letter1) != 1:
             print("Error: it needs to be a single character.")
             continue
         if letter1 != "A" and letter1 and "B" and letter1 != "C":
             print("Error: You provided the wrong character.")
             continue
         return letter1
        
    # remove the default return and add your code

def get_digit():
    """Get a single digit (1, 2, or 3) from the user."""
    while True:
        number = input("Give an single number character: ")
        if number.isdigit() is False:
            print("Error: your input should be only digits.")
            continue
        
        if number not in ("1", "2", "3"):
            print("Error: a single digit needs to be in [1,3].")
            continue
        
        return number
    # remove the default return and add your code


def check_pattern(letter, digit, lst):
    """Print strings where the given letter appears before the digit."""
    print("Strings with the pattern:")
    for i in range(len(lst)):
        string = lst[i]
        # Track whether a matching pattern is found in the current string
        found = False
        
        for k in range(len(string)):
            if string[k] == letter:
                for j in range(k+1, len(string)):
                    if string[j] == digit:
                        found = True
                        
        if found:
            print(string, end = " ")

            
    print()       

    # remove the default pass and add your code
    pass


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    
    # Get the letter and digit, then search for matches
    letter = get_letter()
    
    digit = get_digit()
    
    lst = st_list
    
    check_pattern(letter, digit, lst)
    
    answer = input("Try Again? (y/n):")
    if answer == "y":
        main()
        
    elif answer == "n":
        print("The End")

        
        
    # Your code Here

    # -------------------------------------------------
    # No need to modify anything Below this line
    

# Do not modify these two lines
if __name__ == "__main__":
    main()