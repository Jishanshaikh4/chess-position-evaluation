from common.transformations import FenTranformation

# https://lichess.org/editor/8/1P4B1/8/1q3k2/2Q5/8/4r1Np/K7_b_-_-
def test_reverse_fen_end_game_pawns_to_be_promoted():
    input_fen = "8/1P4B1/8/1q3k2/2Q5/8/4r1Np/K7 b - -"
    output_fen = "7k/Pn1R4/8/5q2/2K3Q1/8/1b4p1/8 w - -"
    reverse_and_compare(input_fen, output_fen)

# https://lichess.org/editor/8/4qk2/5q2/1r1R4/3Q4/2QK4/8/8_b_-_-
def test_reverse_fen_end_game_with_queens_and_rooks():
    input_fen = "8/4qk2/5q2/1r1R4/3Q4/2QK4/8/8 b - -"
    output_fen = "8/8/4kq2/4q3/4r1R1/2Q5/2KQ4/8 w - -"
    reverse_and_compare(input_fen, output_fen)

# https://lichess.org/editor/3qk3/8/8/8/8/8/8/3KQ3_b_-_-
def test_reverse_fen_end_game_with_queens():
    input_fen = "3qk3/8/8/8/8/8/8/3KQ3 b - -"
    output_fen = "3qk3/8/8/8/8/8/8/3KQ3 w - -"
    reverse_and_compare(input_fen, output_fen)

# https://lichess.org/editor/8/8/8/8/5k2/8/2P5/3K4_b_-_-
def test_reverse_fen_end_game():
    input_fen = "8/8/8/8/5k2/8/2P5/3K4 b - -"
    output_fen = "4k3/5p2/8/2K5/8/8/8/8 w - -"
    reverse_and_compare(input_fen, output_fen)

# https://lichess.org/editor/rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR_w_KQkq_-
def test_reverse_fen_initial_position():
    input_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -"
    output_fen = "rnbkqbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBKQBNR b KQkq -"
    reverse_and_compare(input_fen, output_fen)

def reverse_and_compare(input_fen, output_fen):
    f = FenTranformation(input_fen)
    f.flip()
    assert f.fen == output_fen