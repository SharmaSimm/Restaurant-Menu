# MCDonalds - Menu

Program One:
The first program, solved is the whether or not the quantity requested by the
user is a viable option when ordering chicken nuggets at McDonalds. We can
purchase chicken nuggets in quantities of 6, 9, and 22. That means that there is no combination
of options that will allow you to purchase 23 chicken nuggets. Regarding the Diophantine
equation, you can think of it as 6a + 9b + 22c = n. There are four
specific requirements to achieve this objective. This program starts by asking the user how many chicken nuggets they would like to
order. For each possible order quantity by box size identify which combinations are equivalent to n
(in other words, look for what values of a, b, and c in the Diophantine equation work). If the
order is possible, print a statement to the console that states how many options are available and
what these options are.

Program Two:
The second program is built on the foundation of the first program. For this program, it
has been determined that it is simply not enough to tell the user their requested size is not
feasible. The program also determines the closest feasible value of n given the quantity ordered by the
user. Then, it lets the user know that their requested quantity is not feasible but lets them know they have
options, by providing the quantity by box size options for this alternative feasible quantity. 

Program Three:
For the third program, we built on our previous work.
The cost per nugget by quantity varies. In this program, I gave the user the lowest
cost option. Assuming that the 6-piece option costs $3, the 9-piece costs $4, and the 22-piece costs
$9. Instead of presenting all possible options, provide the least expensive option and the total
cost, instead. When the user requests a quantity that is not feasible, I let them know that their order
quantity isn’t feasible and present the least expensive option and total cost for the suggested
alternative quantity. This is more like a second Diophantine equation. While we still need
to identify the values that satisfy the quantity requirements of 6a + 9b + 22c = n, there is an
additional constraint 3a + 4b + 9c = cost (where 3, 4, and 9 represent the costs associated
with the 6, 9, and 22-piece options, respectively). 
