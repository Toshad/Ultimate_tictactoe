'''

This is the engine for the Ultimate TicTacToe Tournament. The code in this file is not for reproduction.
@author: Devansh Shah

The structure of the code is as below:
1. Header Files
2. Sample implementations of your class (Player and ManualPlayer)
3. Game Logic
4. Game simulator

In case of any queries, please post on moodle.iiit.ac.in

'''

import sys
import random
import signal
import copy

class TimedOutExc(Exception):
        pass

m = {}

def temp(s,c):
            return s+c

def check(s,a):
        if isinstance(s,type("")):
                s = list(s)
        h = 0
        for i in range(9):
                if s[i] == a:
                        h += (1<<i)
        if (h&7) == 7:
                return 1
        if (h&56) == 56:
                return 1
        if (h&448) == 448:
                return 1
        if (h&292) == 292:
                return 1
        if (h&146) == 146:
                return 1
        if (h&73) == 73:
                return 1
        if (h&273) == 273:
                return 1
        if (h&84) == 84:
                return 1
        return 0


def dfs(s,c):
        global m
        if check(s,'x')==1:
                m[temp(s,c)] =  1.0
                return 1.0
        elif check(s,'o')==1:
                m[temp(s,c)]= -1.0
                return -1.0

        if temp(s,c) in m.keys():
                    return m[temp(s,c)]

        if isinstance(s,type("")):
                    s = list(s)
        x = float('-inf')
        y = float('inf')
        fl = 0
        for i in range(9):
                if s[i] == '-':
                        s[i] = c;
                        r = ''.join(s)
                        if c == 'x':
                                x += dfs(r,'o')
                        else:
                                y += dfs(r,'x')
                        s[i]='-'
                        fl += 1

        if(fl==0):
                fl=1
#        if fl>2:
#                fl=2
        r = ''.join(s)
        if c == 'x':
                m[temp(r,c)] = x/fl
                return x/fl
        else:
                m[temp(r,c)] = y/fl
                return y/fl

def start():
        global m
        s = "---------"
        m = {}
        dfs(s,'x')
        dfs(s,'o')
        i = 0;
        #print check("x-o-ooxxx",'x')
        #print m["x-o-oox-xx"]
        i=0
        rrr = m.keys()
        #rrr.sort()

        for k in rrr:
                #x='o'
                if k[9] == 'o':
                        m[k]= -m[k]
                if check(k,k[9]):
                        m[k]=200+m[k]
                else:
                        m[k]*=100
                #x='x'
                #print k,":",m[k]
                #print k,",",heuristic(k,k[9],x)
                #print i

def handler(signum, frame):
        #print 'Signal handler called with signal', signum
        raise TimedOutExc()


class ManualPlayer:
	def __init__(self):
		pass
	def move(self, temp_board, temp_block, old_move, flag):
		print 'Enter your move: <format:row column> (you\'re playing with', flag + ")"
		mvp = raw_input()
		mvp = mvp.split()
		return (int(mvp[0]), int(mvp[1]))



class Player48:

	def __init__(self):
		# You may initialize your object here and use any variables for storing throughout the game
		pass

	def move(self,temp_board,temp_block,old_move,flag):
                print temp_board
                if(old_move==(-1,-1)):
                    return (4,4)
		#List of permitted blocks, based on old move.
		blocks_allowed  = determine_blocks_allowed(old_move, temp_block)
		#Get list of empty valid cells
		cells = get_empty_out_of(temp_board, blocks_allowed,temp_block)
                if flag=='x':
                    other_flag='o'
                else:
                    other_flag='x'
		#Choose a move based on some algorithm, here it is a random move.


                tmp_board=copy.deepcopy(temp_board)
                optimal_move = init_minimax(tmp_board, temp_block, old_move, flag, other_flag, float("-inf"), float("inf"), 4)  #Levels to go
                #print 'OPTIMAL:',optimal_move[0], optimal_move[1]
		return (optimal_move)

class Player2:

	def __init__(self):
		# You may initialize your object here and use any variables for storing throughout the game
		pass

	def move(self,temp_board,temp_block,old_move,flag):
                if(old_move==(-1,-1)):
                    return (4,4)
		#List of permitted blocks, based on old move.
		blocks_allowed  = determine_blocks_allowed(old_move, temp_block)
		#Get list of empty valid cells
		cells = get_empty_out_of(temp_board, blocks_allowed,temp_block)
                #if flag=='x':
                #    other_flag='o'
                #else:
                #    other_flag='x'
		#Choose a move based on some algorithm, here it is a random move.
                #optimal_move = init_minimax(temp_board, temp_block, old_move, flag, other_flag, float("-inf"), float("inf"), 4)  #Levels to go
		#return optimal_move
                return cells[random.randrange(len(cells))]



def init_minimax(temp_board, temp_block, old_move, flag, other_flag, ALPHA, BETA, init_depth):
        # Init the recursive procedure for minimax

        # Its our turn,
        blocks_allowed  = determine_blocks_allowed(old_move, temp_block)
    	cells = get_empty_out_of(temp_board, blocks_allowed,temp_block)
        #print cells
        max_hvalue,maxX,maxY = float('-inf'),-1,-1
        for i,j in cells:
                temp_board[i][j] = flag
                local_hvalue = minimax(temp_board, temp_block, (i,j), other_flag, flag, ALPHA, BETA, 1,init_depth)
                if local_hvalue > max_hvalue:
                        max_hvalue = local_hvalue
                        maxX = i
                        maxY = j
                ALPHA = max(ALPHA, max_hvalue)
                temp_board[i][j] = '-'

                if BETA <= ALPHA:   # Beta cut-off
                        break;

        print 'Expected Max Hvalue:', max_hvalue, 'at', maxX, maxY
        return maxX,maxY


def heuristic_9x9(board, pos, neg, blal):
        global m
        big_boy = range(9)
        Hbig_boy = range(9)
#        l=determine_blocks_allowed(old_move,board)
        for i in big_boy:
                R = (i/3)*3
                C = (i%3)*3
                if i in blal:
                        Hbig_boy[i] = heuristic_3x3(board[R][C:C+3], board[R+1][C:C+3], board[R+2][C:C+3], pos, neg)
                else:
                        Hbig_boy[i] = (heuristic_3x3(board[R][C:C+3], board[R+1][C:C+3], board[R+2][C:C+3], pos, neg) - heuristic_3x3(board[R][C:C+3], board[R+1][C:C+3], board[R+2][C:C+3], neg, pos))/2.0
#        s=[]
#        pass
        x=0.0
        for i in big_boy:
#                s.append('-')
#                if Hbig_boy[i] == 1.0:
#                        s[i]=pos
#                elif Hbig_boy[i] == -1.0:
#                        s[i]=neg
                x+=Hbig_boy[i]

        state = range(9)
        for i in big_boy:
                if Hbig_boy>=100:
                        state[i] = pos
                elif Hbig_boy <=-100:
                        state[i] = neg
                else:
                        state[i] = '-'
        bigH = 100*heuristic_3x3(state[0:3],state[3:6],state[6:9],pos,neg)

#    for i in range(3):
#
#               if state[i+0] and state[i+1] and state[i+2]:
#                        return

#        s.append(pos)
#        s=''.join(s)
#        x+=2.5*heuristic(s,pos,neg)


        return bigH+x



def hsh(a,b,c,pos,m):
        h=(100*(a==pos))+(10*(b==pos))+(c==pos)
        #if h==0:
        #        return 0.0
        if h==111:
                return 100*m
        elif h==101 or h==11 or h==110:
                if a=='-' or b=='-' or c=='-':
                        return 5.3*m
        return 0.0


def heuristic(s,pos,neg):
#        try:
#                return m[s];
#        except KeyError:
#                pass

#        if check(s,pos) == 1:
#                print s
#                return 5000.0
#        elif check(s,neg) == 1:
#                print '-jghg',s
#                return -5000.0
#        else:
        x=0
        y=0
        x+=hsh(s[0],s[1],s[2],pos,2.5)
        x+=hsh(s[0],s[4],s[8],pos,2.5)
        x+=hsh(s[2],s[4],s[6],pos,2.5)
        x+=hsh(s[0],s[3],s[6],pos,2.5)
        x+=hsh(s[2],s[5],s[8],pos,2.5)
        x+=hsh(s[3],s[4],s[5],pos,2.5)
        x+=hsh(s[1],s[4],s[7],pos,2.5)
        x+=hsh(s[6],s[7],s[8],pos,2.5)

        y+=hsh(s[3],s[4],s[5],neg,1)
        y+=hsh(s[6],s[7],s[8],neg,1)
        y+=hsh(s[0],s[3],s[6],neg,1)
        y+=hsh(s[1],s[4],s[7],neg,1)
        y+=hsh(s[0],s[4],s[8],neg,1)
        y+=hsh(s[2],s[5],s[8],neg,1)
        y+=hsh(s[0],s[1],s[2],neg,1)
        y+=hsh(s[2],s[4],s[6],neg,1)
        return x-y


def heuristic_3x3(row1, row2, row3, pos, neg):
        # Skip cells which are already won
        #print row1,row2,row3
        #print pos
        global m
        s=[]
        s+=row1
        s+=row2
        s+=row3         # currently assumed that we will call heuristic only at pos
        r=0.0
        for i in s:
                if i == pos:
                        r+=0.1
                elif i == neg:
                        r-=0.1
        s=''.join(s)
        s+=pos
        return r+heuristic(s,pos,neg)
        #pass



# Alpha-beta also added
def minimax(temp_board, temp_block, old_move, flag, other_flag, ALPHA, BETA, depth, max_depth):
        # Just return hvalue.
        # print heuristic_9x9(temp_board,flag,other_flag)
        if(check(temp_block,flag)):
                return float('inf')/2

        if depth >= max_depth:
                # Return the Hvalue of this state.
                blocks_allowed  = determine_blocks_allowed(old_move, temp_block)
                return heuristic_9x9(temp_board, flag, other_flag, blocks_allowed)
        elif depth%2 == 1:
                # Find min
                blocks_allowed  = determine_blocks_allowed(old_move, temp_block)
	        cells = get_empty_out_of(temp_board, blocks_allowed,temp_block)

                min_hvalue = float('inf')
                for i,j in cells:
                        temp_board[i][j] = flag
                        min_hvalue = min(min_hvalue, minimax(temp_board, temp_block, (i,j), flag, other_flag, ALPHA, BETA, depth+1,max_depth))
                        BETA = min(BETA, min_hvalue)
                        temp_board[i][j] = '-'

                        if BETA <= ALPHA:   # Alpha cut-off
                                break;
        #        print "here",heuristic_9x9(temp_board,flag,other_flag)
                if min_hvalue == float('inf'):
                        min_hvalue = 0.0
                return min_hvalue

        elif depth%2 == 0:
                # Find max
                blocks_allowed  = determine_blocks_allowed(old_move, temp_block)
	        cells = get_empty_out_of(temp_board, blocks_allowed,temp_block)

                max_hvalue = float('-inf')
                for i,j in cells:
                        temp_board[i][j] = flag
                        max_hvalue = max(max_hvalue, minimax(temp_board, temp_block, (i,j), flag, other_flag, ALPHA, BETA, depth+1,max_depth))
                        ALPHA = max(ALPHA, max_hvalue)
                        temp_board[i][j] = '-'

                        if BETA <= ALPHA:   # Beta cut-off
                                break
                #print "here",heuristic_9x9(temp_board,flag,other_flag)
                #print len(temp_board)
                #print_lists(temp_board,temp_block)
                if max_hvalue == float('-inf'):
                        max_hvalue = 0.0
                return max_hvalue


def determine_blocks_allowed(old_move, block_stat):
	blocks_allowed = []
	if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
		blocks_allowed = [1,3]
	elif old_move[0] % 3 == 0 and old_move[1] % 3 == 2:
		blocks_allowed = [1,5]
	elif old_move[0] % 3 == 2 and old_move[1] % 3 == 0:
		blocks_allowed = [3,7]
	elif old_move[0] % 3 == 2 and old_move[1] % 3 == 2:
		blocks_allowed = [5,7]
	elif old_move[0] % 3 == 0 and old_move[1] % 3 == 1:
		blocks_allowed = [0,2]
	elif old_move[0] % 3 == 1 and old_move[1] % 3 == 0:
		blocks_allowed = [0,6]
	elif old_move[0] % 3 == 2 and old_move[1] % 3 == 1:
		blocks_allowed = [6,8]
	elif old_move[0] % 3 == 1 and old_move[1] % 3 == 2:
		blocks_allowed = [2,8]
	elif old_move[0] % 3 == 1 and old_move[1] % 3 == 1:
		blocks_allowed = [4]
	else:
		sys.exit(1)
	final_blocks_allowed = []
	for i in blocks_allowed:
		if block_stat[i] == '-':
			final_blocks_allowed.append(i)
	return final_blocks_allowed

#Initializes the game
def get_init_board_and_blockstatus():
	board = []
	for i in range(9):
		row = ['-']*9
		board.append(row)

	block_stat = ['-']*9
	return board, block_stat

# Checks if player has messed with the board. Don't mess with the board that is passed to your move function.
def verification_fails_board(board_game, temp_board_state):
	return board_game == temp_board_state

# Checks if player has messed with the block. Don't mess with the block array that is passed to your move function.
def verification_fails_block(block_stat, temp_block_stat):
	return block_stat == temp_block_stat

#Gets empty cells from the list of possible blocks. Hence gets valid moves.
def get_empty_out_of(gameb, blal,block_stat):
	cells = []  # it will be list of tuples
	#Iterate over possible blocks and get empty cells
	for idb in blal:
		id1 = idb/3
		id2 = idb%3
		for i in range(id1*3,id1*3+3):
			for j in range(id2*3,id2*3+3):
				if gameb[i][j] == '-':
					cells.append((i,j))
 #       if blal==[6,8]:
  #          print cells
	# If all the possible blocks are full, you can move anywhere
	if cells == []:
		new_blal = []
		all_blal = [0,1,2,3,4,5,6,7,8]
		for i in all_blal:
			if block_stat[i]=='-':
				new_blal.append(i)

		for idb in new_blal:
			id1 = idb/3
			id2 = idb%3
			for i in range(id1*3,id1*3+3):
				for j in range(id2*3,id2*3+3):
					if gameb[i][j] == '-':
						cells.append((i,j))
	return cells

# Returns True if move is valid
def check_valid_move(game_board, block_stat, current_move, old_move):

	# first we need to check whether current_move is tuple of not
	# old_move is guaranteed to be correct
	if type(current_move) is not tuple:
		return False

	if len(current_move) != 2:
		return False

	a = current_move[0]
	b = current_move[1]

	if type(a) is not int or type(b) is not int:
		return False
	if a < 0 or a > 8 or b < 0 or b > 8:
		return False

	#Special case at start of game, any move is okay!
	if old_move[0] == -1 and old_move[1] == -1:
		return True

	#List of permitted blocks, based on old move.
	blocks_allowed  = determine_blocks_allowed(old_move, block_stat)
	# We get all the empty cells in allowed blocks. If they're all full, we get all the empty cells in the entire board.
#        print "bl",blocks_allowed
	cells = get_empty_out_of(game_board, blocks_allowed, block_stat)
#        print "cinv",cells
	#Checks if you made a valid move.
	if current_move in cells:
		return True
	else:
		return False

def update_lists(game_board, block_stat, move_ret, fl):

	game_board[move_ret[0]][move_ret[1]] = fl

	block_no = (move_ret[0]/3)*3 + move_ret[1]/3
	id1 = block_no/3
	id2 = block_no%3
	mflg = 0

	flag = 0
	for i in range(id1*3,id1*3+3):
		for j in range(id2*3,id2*3+3):
			if game_board[i][j] == '-':
				flag = 1


	if block_stat[block_no] == '-':
		if game_board[id1*3][id2*3] == game_board[id1*3+1][id2*3+1] and game_board[id1*3+1][id2*3+1] == game_board[id1*3+2][id2*3+2] and game_board[id1*3+1][id2*3+1] != '-' and game_board[id1*3+1][id2*3+1] != 'D':
			mflg=1
		if game_board[id1*3+2][id2*3] == game_board[id1*3+1][id2*3+1] and game_board[id1*3+1][id2*3+1] == game_board[id1*3][id2*3 + 2] and game_board[id1*3+1][id2*3+1] != '-' and game_board[id1*3+1][id2*3+1] != 'D':
			mflg=1
		if mflg != 1:
                    for i in range(id2*3,id2*3+3):
                        if game_board[id1*3][i]==game_board[id1*3+1][i] and game_board[id1*3+1][i] == game_board[id1*3+2][i] and game_board[id1*3][i] != '-' and game_board[id1*3][i] != 'D':
                                mflg = 1
                                break
		if mflg != 1:
                    for i in range(id1*3,id1*3+3):
                        if game_board[i][id2*3]==game_board[i][id2*3+1] and game_board[i][id2*3+1] == game_board[i][id2*3+2] and game_board[i][id2*3] != '-' and game_board[i][id2*3] != 'D':
                                mflg = 1
                                break
	if flag == 0:
		block_stat[block_no] = 'D'
	if mflg == 1:
		block_stat[block_no] = fl

	return mflg

#Check win
def terminal_state_reached(game_board, block_stat,point1,point2):
	### we are now concerned only with block_stat
	bs = block_stat
	## Row win
	if (bs[0] == bs[1] and bs[1] == bs[2] and bs[1]!='-' and bs[1]!='D') or (bs[3]!='-' and bs[3]!='D' and bs[3] == bs[4] and bs[4] == bs[5]) or (bs[6]!='D' and bs[6]!='-' and bs[6] == bs[7] and bs[7] == bs[8]):
		return True, 'W'
	## Col win
	elif (bs[0] == bs[3] and bs[3] == bs[6] and bs[0]!='-' and bs[0]!='D') or (bs[1] == bs[4] and bs[4] == bs[7] and bs[4]!='-' and bs[4]!='D') or (bs[2] == bs[5] and bs[5] == bs[8] and bs[5]!='-' and bs[5]!='D'):
		return True, 'W'
	## Diag win
	elif (bs[0] == bs[4] and bs[4] == bs[8] and bs[0]!='-' and bs[0]!='D') or (bs[2] == bs[4] and bs[4] == bs[6] and bs[2]!='-' and bs[2]!='D'):
		return True, 'W'
	else:
		smfl = 0
		for i in range(9):
			if block_stat[i] == '-':
				smfl = 1
				break
		if smfl == 1:
			return False, 'Continue'

		else:
			if point1>point2:
				return True, 'P1'
			elif point2>point1:
				return True, 'P2'
			else:
				return True, 'D'


def decide_winner_and_get_message(player,status, message):
	if status == 'P1':
		return ('P1', 'MORE BLOCKS')
	elif status == 'P2':
		return ('P2', 'MORE BLOCKS')
	elif player == 'P1' and status == 'L':
		return ('P2',message)
	elif player == 'P1' and status == 'W':
		return ('P1',message)
	elif player == 'P2' and status == 'L':
		return ('P1',message)
	elif player == 'P2' and status == 'W':
		return ('P2',message)
	else:
		return ('NONE','DRAW')
	return


def print_lists(gb, bs):
	print '=========== Game Board ==========='
	for i in range(9):
		if i > 0 and i % 3 == 0:
			print
		for j in range(9):
			if j > 0 and j % 3 == 0:
				print " " + gb[i][j],
			else:
				print gb[i][j],

		print
	print "=================================="

	print "=========== Block Status ========="
	for i in range(0, 9, 3):
		print bs[i] + " " + bs[i+1] + " " + bs[i+2]
	print "=================================="
	print


def simulate(obj1,obj2):

	# Game board is a 9x9 list of lists & block_stat is a list of 9 elements indicating if a block has been won.
	game_board, block_stat = get_init_board_and_blockstatus()

	pl1 = obj1
	pl2 = obj2

	# Player with flag 'x' will start the game
	pl1_fl = 'x'
	pl2_fl = 'o'

	old_move = (-1, -1) # For the first move

	WINNER = ''
	MESSAGE = ''
	TIMEALLOWED = 15
	p1_pts=0
	p2_pts=0

	print_lists(game_board, block_stat)

#        print heuristic_9x9(game_board,'x','o')

	while(1): # Main game loop

		temp_board_state = game_board[:]
		temp_block_stat = block_stat[:]

		signal.signal(signal.SIGALRM, handler)
		signal.alarm(TIMEALLOWED)
#		ret_move_pl1 = pl1.move(temp_board_state, temp_block_stat, old_move, pl1_fl)

		#try:
		ret_move_pl1 = pl1.move(temp_board_state, temp_block_stat, old_move, pl1_fl)
		#except:
                if False:
                        print sys.exc_info()[0]
			WINNER, MESSAGE = decide_winner_and_get_message('P1', 'L',   'TIMED OUT')
		#	print MESSAGE
			break
		signal.alarm(0)

		# Check if list is tampered.
		if not (verification_fails_board(game_board, temp_board_state) and verification_fails_block(block_stat, temp_block_stat)):
			WINNER, MESSAGE = decide_winner_and_get_message('P1', 'L',   'MODIFIED CONTENTS OF LISTS')
			break

		# Check if the returned move is valid
		if not check_valid_move(game_board, block_stat, ret_move_pl1, old_move):
			WINNER, MESSAGE = decide_winner_and_get_message('P1', 'L',   'MADE AN INVALID MOVE')
			break


		print "Player 1 made the move:", ret_move_pl1, 'with', pl1_fl
		# Update the 'game_board' and 'block_stat' move
		p1_pts += update_lists(game_board, block_stat, ret_move_pl1, pl1_fl)

		gamestatus, mesg =  terminal_state_reached(game_board, block_stat,p1_pts,p2_pts)
		if gamestatus == True:
			print_lists(game_board, block_stat)
			WINNER, MESSAGE = decide_winner_and_get_message('P1', mesg,  'COMPLETE')
			break


		old_move = ret_move_pl1
		print_lists(game_board, block_stat)

        	temp_board_state = game_board[:]
        	temp_block_stat = block_stat[:]

        	signal.signal(signal.SIGALRM, handler)
        	signal.alarm(TIMEALLOWED)

#        	try:
      		ret_move_pl2 = pl2.move(temp_board_state, temp_block_stat, old_move, pl2_fl)
#        	except:
                if False:
                        print sys.exc_info()[0]
			WINNER, MESSAGE = decide_winner_and_get_message('P2', 'L',   'TIMED OUT')
			break
        	signal.alarm(0)

        	if not (verification_fails_board(game_board, temp_board_state) and verification_fails_block(block_stat, temp_block_stat)):
			WINNER, MESSAGE = decide_winner_and_get_message('P2', 'L',   'MODIFIED CONTENTS OF LISTS')
			break

        	if not check_valid_move(game_board, block_stat, ret_move_pl2, old_move):
			WINNER, MESSAGE = decide_winner_and_get_message('P2', 'L',   'MADE AN INVALID MOVE')
			break

        	print "Player 2 made the move:", ret_move_pl2, 'with', pl2_fl

        	p2_pts += update_lists(game_board, block_stat, ret_move_pl2, pl2_fl)

        	# Now check if the last move resulted in a terminal state
        	gamestatus, mesg =  terminal_state_reached(game_board, block_stat,p1_pts,p2_pts)
        	if gamestatus == True:
			print_lists(game_board, block_stat)
			WINNER, MESSAGE = decide_winner_and_get_message('P2', mesg,  'COMPLETE' )
			break
        	else:
			old_move = ret_move_pl2
			print_lists(game_board, block_stat)

	print WINNER
	print MESSAGE

if __name__ == '__main__':
	## get game playing objects
#        print heuristic("x--oo---xx",'x','o')
 #       print heuristic("oxo---ox-x",'x','o')
  #      raw_input()
        start()
        print heuristic("oo-------x",'x','o')
        print heuristic("oox------o",'o','x')
	if len(sys.argv) != 2:
		print 'Usage: python simulator.py <option>'
		print '<option> can be 1 => Random player vs. Random player'
		print '                2 => Human vs. Random Player'
		print '                3 => Human vs. Human'
		sys.exit(1)

	obj1 = ''
	obj2 = ''
	option = sys.argv[1]
	if option == '1':
		obj1 = Player48()
		obj2 = Player2()

	elif option == '2':
		obj1 = Player48()
		obj2 = ManualPlayer()
	elif option == '3':
		obj1 = ManualPlayer()
		obj2 = ManualPlayer()
	else:
		print 'Invalid option'
		sys.exit(1)

	num = 0.7
        #random.uniform(0,1)
	if num > 0.5:
		simulate(obj2, obj1)
	else:
		simulate(obj1, obj2)
