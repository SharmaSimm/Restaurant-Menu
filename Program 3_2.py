"""
Problem Set 3_2: The purpose of this program is to
determine the closest feasible value of the quantity ordered 
by the user.
July 28, 2024
Sim Sharma
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

def find_closest_feasible_n(n):
    #Initialize variable to store the closest feasible value and its combinations
    closest_n = None
    closest_combinations = []

    #Search for the closest feasible value by increasing and decreasing n
    for offset in range(1, n + 22): #Add a margin to ensure we find the closet

        #Check the next feasible value above the requested quantit
        upper_n = n + offset
        upper_combinations = find_nuggets_combination(upper_n)
        if upper_combinations:
            closest_n = upper_n
            closest_combinations = upper_combinations
            break

        #Check the next feasible value below the requested quantity
        lower_n = n - offset
        if lower_n > 0 : # Ensure we donot go negative or zero
            lower_combinations = find_nuggets_combination(lower_n)
            if lower_combinations:
                closest_n = lower_n
                closest_combinations = lower_combinations
                break

    return closest_n, closest_combinations

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
        #Find the closest feasible value and its combinations
        closest_n, closest_combinations = find_closest_feasible_n(n)
        if closest_combinations:
            print(f"It is not possible to create a combination of {n} nuggets.")
            print(f"The closest feasible quantity is {closest_n}. Choose from the following {len(closest_combinations)} options:")
            for combination in closest_combinations:
                print(combination)
        else:
            print(f"No feasible combination found close to {n} nugget")
    

if __name__ == "__main__":
    main()