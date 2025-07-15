import keyboard, random, os
os.system("")

#----------------------------------------------------------------------------
#Timer created for game refresh rate
def timer(t):
    while True:
        for n in range(t*1000000):
            if n == t*500000: return "A"

#----------------------------------------------------------------------------
#Creates playable area
board = []
height = 15
length = height*2
for a in ('\u2554'+'\u2550'*length+'\u2557'):
    board.append(a)
for line in range(height-2):
    for b in ('\u2551'+' '*length+'\u2551'):
        board.append(b)
for c in ('\u255A'+'\u2550'*length+'\u255D'):
    board.append(c)

#----------------------------------------------------------------------------
#Declaration of all variables needed
game = True
refresh_board = board.copy()
left = -1             # Goes Left
right = 1             # Goes Right
up = (length+2)*-1    # Goes Up
down = length+2       # Goes Down
path_left, path_right, path_up, path_down = True, False, False, False
snake = [113,114,115,116,117,118]
snack = random.randint(20,(height*length)-50)

#----------------------------------------------------------------------------
#Runs game in a forever loop
while game:

#----------------------------------------------------------------------------
#Gets user input (left,right,up,down), moves head of snake, saves inp in path
    if keyboard.is_pressed('left') :
        snake.insert(0,snake[0]+left)
        snake.pop(-1)
        path_left = True
        path_right = False
        path_up = False
        path_down = False
    if keyboard.is_pressed('right') :
        snake.insert(0,snake[0]+right)
        snake.pop(-1)
        path_left = False
        path_right = True
        path_up = False
        path_down = False
    if keyboard.is_pressed('up') :
        snake.insert(0,snake[0]+up)
        snake.pop(-1)
        path_left = False
        path_right = False
        path_up = True
        path_down = False
    if keyboard.is_pressed('down') :
        snake.insert(0,snake[0]+down)
        snake.pop(-1)
        path_left = False
        path_right = False
        path_up = False
        path_down = True

#----------------------------------------------------------------------------
#Continues snake movement from last user input saved in path
    if path_left:
        snake.insert(0,snake[0]+left)
        snake.pop(-1)
    elif path_right:
        snake.insert(0,snake[0]+right)
        snake.pop(-1)
    elif path_up:
        snake.insert(0,snake[0]+up)
        snake.pop(-1)
    elif path_down:
        snake.insert(0,snake[0]+down)
        snake.pop(-1)

#----------------------------------------------------------------------------
#Refresh rate
    if timer(20) == 'A':

#----------------------------------------------------------------------------
#Positions the snake on the board and checks for collisions with edges
        for pos in snake:
            if board[pos] in ('\u2550','\u2551','\u2554','\u2557','\u255A','\u255D'):
                board[pos] = "X"
                game = False
            else:
                board[pos] = "+"

#----------------------------------------------------------------------------
#Adds random snacks to board and to snake if eaten
    if snack not in snake and board[snack] not in ('\u2550','\u2551','\u2554','\u2557','\u255A','\u255D'):
        board[snack] = 'O'
    else:
        snack = random.randint(20,200)
        snake.append(snake[-1])

#----------------------------------------------------------------------------
#Prints the update board and clears board (ready for next update)
    print("\n"+" "*int(((length+2)/2)-3)+"SNAKE!"+" "*int(((length+2)/2)-3)+"\n")
    for t in range(0, len(board), length+2):
        print("".join(board[t:t+length+2]))
    print(end=f"\033[{height+3}A\r")
    board = refresh_board.copy()

#----------------------------------------------------------------------------
#Clears terminal if snake collides with edge
else:
    if timer(100) == 'A': 
        os.system('cls' if os.name == 'nt' else 'clear')
#----------------------------------------------------------------------------