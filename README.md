Project Report: Number Guessing Game

1. Introduction
The Number Guessing Game is a simple Python-based console application that allows users to guess a randomly generated number within a limited number of attempts. The project is designed to enhance logical thinking and introduce key programming concepts such as random number generation, decision-making, loops, and exception handling. By integrating different difficulty levels, the game provides an engaging and interactive experience for users.
________________________________________
2. Objectives
•	To develop a simple, interactive Python game.
•	To implement random number generation using Python’s built-in libraries.
•	To apply loops and conditional statements for game flow control.
•	To introduce error handling for invalid user inputs.
•	To provide an enjoyable learning project suitable for beginners in Python programming.
________________________________________
3. Features
1.	Welcome Screen – Displays a friendly message before starting the game.
2.	Difficulty Levels – Users can choose from three levels:
o	Easy → 7 attempts
o	Medium → 5 attempts
o	Hard → 3 attempts
3.	Random Number Generation – A number between 1 and 20 is generated each round.
4.	User Input Validation – Handles invalid or non-numeric inputs gracefully.
5.	Feedback Mechanism – Tells the user if their guess is too high, too low, or correct.
6.	Win/Loss Conditions – Declares victory if guessed correctly or shows the correct number on failure.
7.	Replay Option – Allows players to restart or exit after completing one round.
________________________________________
4. System Requirements
•	Software: Python 3.x
•	Libraries Used: random (standard Python library)
•	Hardware: Any computer system capable of running Python
________________________________________
5. Methodology
The program is divided into four main functions:
1.	welcome()
Displays a greeting message to the player.
2.	choose_level()
Prompts the user to select difficulty. Returns the number of allowed attempts. If an invalid input is given, defaults to Easy.
3.	game()
o	Generates a random number between 1 and 20.
o	Accepts user guesses within allowed attempts.
o	Provides hints (too high/too low) until the user guesses correctly or exhausts attempts.
4.	main()
o	Executes the welcome screen.
o	Calls the game() function in a loop.
o	Provides an option for replaying.
________________________________________
6. Flow of Execution
1.	The program starts by calling the main() function.
2.	The welcome screen is displayed.
3.	The player selects a difficulty level.
4.	A random number is generated.
5.	The player repeatedly guesses the number until:
o	The correct number is guessed, OR
o	The maximum attempts are used up.
6.	The game announces the result.
7.	The user decides whether to replay or exit.
________________________________________
7. Advantages
•	Simple and beginner-friendly.
•	Enhances understanding of Python basics.
•	Includes user-friendly error handling.
•	Encourages logical thinking and decision-making.
________________________________________
8. Limitations
•	Only supports numbers between 1 and 20.
•	Limited to three difficulty levels.
•	No graphical interface (only console-based).
________________________________________
9. Future Enhancements
•	Adding score tracking across multiple rounds.
•	Allowing customizable number ranges.
•	Introducing hints or a help option.
•	Implementing a graphical user interface (GUI) using Tkinter or Pygame.
•	Adding multiplayer support.
________________________________________
10. Conclusion
The Number Guessing Game demonstrates the practical application of Python programming fundamentals in a fun and interactive way. By combining random number generation, loops, and conditionals, the program provides an engaging experience for users while strengthening programming knowledge. The project can be extended further with advanced features, making it a strong foundation for beginner-level game development.
________________________________________
