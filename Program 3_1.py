
"""
Problem Set 3_1: The purpose of this assignment is to
calculate quantities of chicken nuggets that fit within
available order quantities.
July 28, 2024
Sim
"""

def find_nuggets_combination(n):
    total_nuggets = [] #to store the possible combination
    for a in range(n//6 + 1): #Iterate over possible 6-piece boxes
        for b in range(n//9 +1): #Iterate over possible 9 pieces boxes
            for c in range(n//22 + 1): #Iterate over possible 22 pieces boxes
              #Checks if the current combination of boxes equals the desired quantity
                if 6 * a + 9*b + 22*c == n:
                    total_nuggets.append(f" Six_piece:  {a},  Nine piece: {b}  , Twenty-two piece : {c} " ) #if it does add the combination to list
    
    return total_nuggets

def main():

    #Ask user for the number of chicken nuggets they want to order
    try:
        n = int (input("How many chicken nuggets would you like to order ? : "))

    #Handles invalid input 
    except ValueError:
        print(" Error!!! Please enter a combination number.")
        return 
    
    #find all possible combination that add up to the desired quantity
    total_nuggets = find_nuggets_combination(n)
    
    #Check if there are any valid combinations
    if total_nuggets:
        print(f"For an order size of {n}, choose from the following {len(total_nuggets)} options:" )
        #Print each combination
        for combination in total_nuggets:
            print(combination)

    else:
        print(f"It is not possible to create a combination of {n} order")
    

if __name__ == "__main__":
    main()

