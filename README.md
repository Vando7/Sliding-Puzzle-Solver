___________________________________________
Board implementation:
The board is an array of numbers.
It is assumed that the target board is

[1, 2, 3, 4, 5, 6, 7, 8, 0]

Which can be presented as
1 2 3
4 5 6
7 8 0

It is possible to change the place of zero
up, down, left and right. Zero cannot come out of the board.

If we look at the top board, zero can only move up and to the left.

1 2 3    1 2 3
4 5 6 -> 4 5 0
7 8 0    7 8 6

1 2 3    1 2 3
4 5 6 -> 4 5 6
7 8 0    7 0 8

___________________________________________
Heuristic function

The game is implemented in the format of states. A state contains a board, an h-value, and a g-value of the board. The initial state has a g-value of 0. In the process of solving children are generated: a set of states that are the result of every possible move of the current.

Let's look at the following board:
8 1 3
4 0 2
7 6 5

===================
h-value is obtained from the sum of the displaced tiles and how many strokes they are from their place.

The distance of each tile from its target:
8 7 6 5 4 3 2 1
3 + 0 + 2 + 2 + 0 + 0 + 2 + 1 = 10 <- h-value

g-value is obtained by adding 1 to the g-value of the parent. This value indicates how far we are from the initial state.

===================

If we have the top board as the initial state, it will represent:

state = [[8,1,3,4,0,2,7,6,5], 10, 0]

This is the well-known Manhattan distance, which is obtained by adding h and g = 10 + 0


___________________________________________
Implementation of A *

The solve function takes the initial state.

We initialize an empty open list and add the initial state to it. We also initialize an empty parent dictionary.

We are entering a cycle:

1. Initialize tmp = open [0]
2. Check if this element is the target -> End
  2.1 On the standard output we make the way from the initial state to the goal.
3. We generate the children of tmp
  3.1 If a generated child already has a parent, it is ignored.
  3.2 If there is no parent. We create a key in the dictionary parent: parent [child] = tmp
  3.3 Add the child to open
4. Remove the first element of open
5. Sort the list by Manhattan distance.
6. We return to 1.

___________________________________________
Check for a solution

To check if a board can be solved, we calculate how many inversions there are in the array. If the number of inversions is even - there is a solution, if not - there is no solution.

I have written a validation function, but since there is no requirement to accept a state from the standard input - I generate a board by making 10,000 random shifts of the target board. So I make sure there is a solution.

For specific boards:
The main function has a variable "start", which by default is the target board:
[1,2,3,4,5,6,7,8,0]

Enter the desired board and change the value of the "doShuffle" variable to False.

In this case, the validation and the entered board will be used.

___________________________________________
Execution of the code.
Python 3.8.5 is used for the implementation:
https://www.python.org/downloads/

Open a command terminal in the folder where hw1.py is located and run with
> python hw1.py

___________________________________________
Given boards:

Solvable:
[1,8,2,0,4,3,7,6,5]

Not solvable:
[8,1,2,0,4,3,7,6,5]
