import pygame
import chess
import os

# Initialize pygame
pygame.init()

# Load chess piece images with custom names
piece_images = {}
piece_folder = "chess_pieces"

# Function to load chess piece images
def load_piece_images():
    # Map python-chess piece symbols to your custom file names
    piece_files = {
        'P': 'PW.png',  # White Pawn
        'R': 'RW.png',  # White Rook
        'N': 'KW.png',  # White Knight
        'B': 'BW.png',  # White Bishop
        'Q': 'QW.png',  # White Queen
        'K': 'KIW.png',  # White King
        'p': 'PB.png',  # Black Pawn
        'r': 'RB.png',  # Black Rook
        'n': 'KB.png',  # Black Knight
        'b': 'BB.png',  # Black Bishop
        'q': 'QB.png',  # Black Queen
        'k': 'KIB.png',  # Black King
    }
    
    # Load each image file based on the mapping
    for piece, file_name in piece_files.items():
        piece_images[piece] = pygame.image.load(os.path.join(piece_folder, file_name))

# Draw the board, pieces, and possible move circles
def draw_board(screen, board, square_size, legal_moves=[]):
    colors = [pygame.Color(240, 217, 181), pygame.Color(181, 136, 99)]  # Light and dark squares

    # Draw squares
    for row in range(8):
        for col in range(8):
            square = chess.square(col, 7 - row)
            color = colors[(row + col) % 2]

            pygame.draw.rect(screen, color, pygame.Rect(col * square_size, row * square_size, square_size, square_size))

            # Draw circles to indicate possible moves
            if square in legal_moves:
                # Draw a transparent circle at the center of the square
                circle_color = (0, 0, 0)  # Black circle for legal move
                circle_radius = square_size // 6
                center = (col * square_size + square_size // 2, row * square_size + square_size // 2)
                pygame.draw.circle(screen, circle_color, center, circle_radius, width=2)  # Width 2 for an elegant outline

    # Draw pieces centered on the square
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_image = piece_images[piece.symbol()]
            piece_rect = piece_image.get_rect()
            row, col = divmod(square, 8)
            piece_x = col * square_size + (square_size - piece_rect.width) // 2
            piece_y = (7 - row) * square_size + (square_size - piece_rect.height) // 2
            screen.blit(piece_image, (piece_x, piece_y))

# Get the square under the mouse pointer
def get_square_under_mouse(square_size):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    col = mouse_x // square_size
    row = 7 - (mouse_y // square_size)
    square = chess.square(col, row)
    return square

def main():
    # Game setup
    board = chess.Board()
    width, height = 640, 640  # Chess board is 8x8, so each square will be 80x80 pixels
    square_size = width // 8

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chess Game")
    clock = pygame.time.Clock()

    load_piece_images()

    selected_square = None
    move_from = None
    legal_moves = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                square = get_square_under_mouse(square_size)
                piece = board.piece_at(square)
                
                # Check if a piece is already selected
                if move_from is None:
                    # If selecting a piece
                    if piece and ((board.turn == chess.WHITE and piece.color == chess.WHITE) or (board.turn == chess.BLACK and piece.color == chess.BLACK)):
                        move_from = square
                        # Highlight possible moves
                        legal_moves = [move.to_square for move in board.legal_moves if move.from_square == square]
                else:
                    # If selecting another piece or empty square
                    if piece and ((board.turn == chess.WHITE and piece.color == chess.WHITE) or (board.turn == chess.BLACK and piece.color == chess.BLACK)):
                        # Reselect a different piece
                        move_from = square
                        legal_moves = [move.to_square for move in board.legal_moves if move.from_square == square]
                    else:
                        # Make the move if valid
                        move_to = square
                        move = chess.Move(move_from, move_to)

                        if move in board.legal_moves:
                            board.push(move)
                        # Reset selection
                        move_from = None
                        legal_moves = []

        # Draw everything (including highlighted legal moves)
        draw_board(screen, board, square_size, legal_moves)

        # Flip the screen buffer
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
