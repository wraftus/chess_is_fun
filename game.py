#!/usr/bin/env python3
import os
from board import BoardWrapper

class HumanPlayer(object):
    def __init__(self, colour):
        self.colour = colour

    def get_next_move(self):
        while(True):
            raw_move = input("Please enter your next move " + ("White: " if self.colour else "Black: "))
            raw_move = raw_move.split(' ')
            if len(raw_move) != 2:
                print("Moves should be in the form 'A3 A4'")
                continue

            from_col = ord(raw_move[0][0]) - ord('A')
            from_row = ord(raw_move[0][1]) - ord('1')
            to_col = ord(raw_move[1][0]) - ord('A')
            to_row = ord(raw_move[1][1]) - ord('1')

            if (not 0 <= from_col < 8) or (not 0 <= from_row < 8):
                print("First coordinate is not valid")
                continue
            if (not 0 <= to_col < 8) or (not 0 <= to_row < 8):
                print("Second coordinate is not valid")
                continue

            from_coord = from_col + 8 * from_row
            to_coord = to_col + 8 * to_row
            return from_coord, to_coord

if __name__ == '__main__':
    board = BoardWrapper()
    white_player = HumanPlayer(True)
    black_player = HumanPlayer(False)
    cur_player = white_player

    while(board.playing):
        os.system('clear')
        board.draw()
        while(True):
            from_coord, to_coord = cur_player.get_next_move()
            if board.move(from_coord, to_coord, cur_player.colour):
                break
            print("Not a valid move")
        cur_player = black_player if cur_player.colour else white_player
        
        
