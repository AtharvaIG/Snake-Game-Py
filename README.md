

# Snake Game

A simple Snake game built using Python's Turtle Graphics module. This game allows you to control the snake using the arrow keys and grow longer by eating food while avoiding collisions with walls and its own tail.

## Features

- **Classic Snake Gameplay**: Navigate the snake with arrow keys.
- **Score System**: Track your score as you eat food, which causes the snake to grow.
- **Game Over**: The game ends when the snake collides with the wall or its own tail.
- **Responsive Interface**: Built using the turtle module, with real-time updates.

## Requirements

- Python 3.x
- `turtle` module (built-in with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/snake-game.git
   ```

2. Navigate into the project directory:
   ```bash
   cd snake-game
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## Gameplay Instructions

- Use the **Up** arrow to move the snake upwards.
- Use the **Down** arrow to move the snake downwards.
- Use the **Left** arrow to move the snake to the left.
- Use the **Right** arrow to move the snake to the right.
- Eat the blue food to grow the snake and increase your score.
- Avoid hitting the walls or the snake's tail to prevent losing the game.

## Game Over

When the snake collides with the walls or its own tail, the game will end, and the final score will be displayed.

## File Structure

```plaintext
snake-game/
├── main.py             # The main game file that runs the game
├── snake.py            # Contains the Snake class
├── food.py             # Contains the Food class
├── scoreboard.py       # Contains the Scoreboard class
├── README.md           # This README file
└── LICENSE             # Project license
```

## Credits

- The game was built using the `turtle` module in Python.
- The initial structure and logic of the game were inspired by various Snake game tutorials.

