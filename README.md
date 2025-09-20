# CSE-Examination

Instructions:

Fork this repo and clone the fork onto your local computer.

Make sure to create a local branch name examination/midterm-python-exam and accomplish the task given in that branch.

Modify this README.md file to explain your code.

Push the activity back to your forked remote repo.


John Marcel Aleman Examination:

This program simulates a basic GPS tracker where the player starts at position (0, 0) and can move North, South, East, or West by entering commands. The program accepts various forms of input for directions (e.g., n, N, north, etc.) and handles invalid inputs gracefully.

How it works:

The player starts at (0, 0).
Each valid command moves the player in the specified direction:
North (N): y increases by 1
South (S): y decreases by 1
East (E): x increases by 1
West (W): x decreases by 1
After each move, the current position is displayed.
The user can enter STOP (case-insensitive) to end the session.
When the session ends, the program shows the final position and tells whether the user returned to the origin (0, 0).