from IPython.display import clear_output

import random

def display_board(board):
	"""
	print board game
	"""
	#clear_output()
	print(board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('---------')
	print(board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('---------')
	print(board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('\n\n')

def player_input():
	"""
	Write a function that can take in a player input and assign their marker as 'X' or 'O'
	"""
	markerset = ''
	marker = ''
	while not (marker == 'X' or marker == 'O'):
		marker = input('Player 1: Do you want to be X or O?').upper()
		if(marker == 'X'):
			markerset = ('X','O')
		else:
			markerset = ('O','X')
	clear_output()
	print(f'Player 1: Do you want to be X or O? {markerset[0]}')
	print(f'Player 2: Do you want to be X or O? {markerset[1]}')
	return markerset

def place_marker(board, marker, position):
	"""
	function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
	"""
	board[position] = marker

def win_check(board, mark):
	"""
	function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
	"""
	return ((board[1] == mark and board[2] == mark and board[3] == mark) or
	(board[4] == mark and board[5] == mark and board[6] == mark) or
	(board[7] == mark and board[8] == mark and  board[9] == mark) or
	(board[1] == mark and board[5] == mark and board[9] == mark) or
	(board[7] == mark and board[5] == mark and board[3] == mark))

def choose_first():
	"""
	randomly decide which player goes first
	"""
	first = random.randint(1,2)
	print(f'Player {first} will go first')
	return first

def space_check(board, position):
	"""
	function that returns a boolean indicating whether a space on the board is freely available.
	"""
	return (board[position] == ' ')

def full_board_check(board):
	"""
	 function that checks if the board is full and returns a boolean value
	"""
	for x in range(1,10):
		if(space_check(board,x) == True):
			return False
	return True

def player_choice(board):
	"""
	 function that asks for a player's next position and see if the position is available
	"""
	while(True):
		pos = int(input('Choose your next position (1-9)'))
		if(space_check(board,pos)==True):
			return pos
		else:
			continue

def replay():
	"""
	function that asks the player if they want to play again
	"""
	while(True):
		replay = input('Do you want to play again? Y/N')
		if(replay.lower() == 'y'):
			clear_output()
			return True
		elif(replay.lower() == 'n'):
			clear_output()
			return False
		else:
			continue


#GAME

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board = [' '] * 10
    markset = player_input()
    first = choose_first()
    
    play = input(print('Are you ready to Play? Y/N'))
    if(play.lower() == 'y'):
            game_on = True
    else:
        game_on = False
    
    #pass
    while game_on:
        if(first == 1):
            #Player 1 Turn
            display_board(board)
            pos = player_choice(board)
            place_marker(board,markset[0],pos)
            if(win_check(board,markset[0])==True):
                display_board(board)
                print('Yayyy Player1!! You\'ve won the game!')
                game_on = False
            else:
                if(full_board_check(board) == True):
                    display_board(board)
                    print('It\'s a draw!!')
                    game_on = False
                else:
                    first = 2
        else:
            
            # Player2's turn.
            display_board(board)
            pos = player_choice(board)
            place_marker(board,markset[1],pos)
            if(win_check(board,markset[1])==True):
                display_board(board)
                print('Yayyy Player2!! You\'ve won the game!')
                game_on = False
            else:
                if(full_board_check(board)==True):
                    display_board(board)
                    print('It\'s a draw!!')
                    game_on = False
                else:
                    first = 1
            #pass
    #print('Yayyy Player{first}!! You\'ve won the game!')
    if (replay()==False):
        break