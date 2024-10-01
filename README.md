# Chess Game UI with Pygame

A simple chess game UI created with **Pygame** and **python-chess** to visualize and interact with chess moves. This project focuses on creating a graphical interface and handling chessboard interactions, not the full AI logic.

## Features

- Graphical chessboard built with Pygame.
- Custom chess piece images loaded from local files.
- Displays legal moves and highlights selected pieces.
- Interact with the game using mouse clicks to make moves.

## Getting Started

### Prerequisites

To run this project, you need the following dependencies installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Pygame](https://www.pygame.org/wiki/GettingStarted) 
- [python-chess](https://pypi.org/project/python-chess/)

Install the required dependencies using pip:

```bash
pip install pygame python-chess```
Installation

    Clone the repository:

    bash

    git clone https://github.com/ahmedxsaad/Chess-game.git
    cd Chess-game

    Download or place your custom chess piece images in the chess_pieces/ folder:

    Ensure that the images are correctly named according to the chess pieces:
        PW.png, PB.png for pawns (White, Black)
        RW.png, RB.png for rooks
        KW.png, KB.png for knights
        BW.png, BB.png for bishops
        QW.png, QB.png for queens
        KIW.png, KIB.png for kings

    The naming convention is W for white pieces and B for black pieces.

Running the Game

To run the game, use the following command:

bash

python chess_game.py

How to Play

    Click on a piece to select it.
    Possible legal moves will be highlighted with circles on the board.
    Click on a legal move to move the selected piece.
    The game follows the basic chess rules without AI for now.

Project Structure

bash

.
├── chess_game.py       # Main game logic
├── chess_pieces/       # Folder with chess piece images
└── README.md           # This file

License

This project is licensed under the MIT License - see the LICENSE file for details.
Screenshots
![image](https://github.com/user-attachments/assets/960177c1-d610-4bec-a3c1-db1e8f046b46)
![image](https://github.com/user-attachments/assets/874503e4-3d02-415b-a4a6-710d6902f5c2)


Contributing

Feel free to submit issues, fork the repository, and make pull requests with improvements or new features.
Contact

For any questions or issues, feel free to reach out to me via GitHub.
