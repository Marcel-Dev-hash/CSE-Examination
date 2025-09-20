# CSE-Examination

Instructions:

Fork this repo and clone the fork onto your local computer.

Make sure to create a local branch name examination/midterm-python-exam and accomplish the task given in that branch.

Modify this README.md file to explain your code.

Push the activity back to your forked remote repo.


John Marcel Aleman Examination/Explanation

normalize_direction(cmd)

Takes user input, removes spaces, and converts it to lowercase.
Checks if the input matches any valid direction (n, north, etc.) or "stop".
Returns a single character ('N', 'S', 'E', 'W', or 'STOP') for valid inputs, or None for invalid ones.
main() function

Starts the player at position (0, 0).
Greets the user and enters a loop to accept commands.
For each input:
Converts it to a direction using normalize_direction.
If "STOP", breaks the loop and ends the session.
If a valid direction, updates the position accordingly:
'N': move north (increase y)
'S': move south (decrease y)
'E': move east (increase x)
'W': move west (decrease x)
Prints the current position after each valid move.
If invalid, asks again.
After stopping, prints the final position and whether the player returned to the origin (0, 0).
