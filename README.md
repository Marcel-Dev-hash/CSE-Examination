# CSE-Examination

Instructions:

Fork this repo and clone the fork onto your local computer.

Make sure to create a local branch name examination/midterm-python-exam and accomplish the task given in that branch.

Modify this README.md file to explain your code.

Push the activity back to your forked remote repo.


Inocente, Ashley John Examination

Explanation
This program simulates a simple GPS tracker where the player starts at coordinates (0, 0) and can move in four directions: North, South, East, or West by entering corresponding commands. It recognizes multiple forms of input for directions (such as "n", "N", "north", etc.) and responds to invalid commands appropriately.

How it works:

The player begins at the starting point (0, 0).

Each valid command moves the player in the specified direction:

North (N): Increases the y-coordinate by 1

South (S): Decreases the y-coordinate by 1

East (E): Increases the x-coordinate by 1

West (W): Decreases the x-coordinate by 1

After each move, the player's current position is displayed.

The user can type STOP (case-insensitive) to end the session.

Upon session completion, the program shows the final position and checks if the player has returned to the origin (0, 0).

Input Handling:

The program accepts both uppercase and lowercase commands, as well as full words (e.g., "north").

Invalid inputs will prompt the user to enter a valid direction.