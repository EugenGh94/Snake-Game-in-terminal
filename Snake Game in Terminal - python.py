import keyboard, random, os
os.system("")

#----------------------------------------------------------------------------
#Timer created for game refresh rate
def timer(t):
    while True:
        for n in range(t*150000):
            if n == t*125000: return "A"

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
lf_rt_speed = 30                    # Left/right moving speed
up_dn_speed = int(lf_rt_speed*1.6)  # Up or down moving speed (slower)
score = 0
level = 1

#----------------------------------------------------------------------------
#Gets user input (left,right,up,down), moves head of snake, saves inp in path
def get_user_input():
    global snake,path_left,path_right,path_up,path_down
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
#Runs game in a forever loop
while game:
    get_user_input()

#----------------------------------------------------------------------------
#Continues snake movement from last user input saved in path
    if path_left:
        snake.insert(0,snake[0]+left)
        snake.pop(-1)
        mvmt = lf_rt_speed
    elif path_right:
        snake.insert(0,snake[0]+right)
        snake.pop(-1)
        mvmt = lf_rt_speed
    elif path_up:
        snake.insert(0,snake[0]+up)
        snake.pop(-1)
        mvmt = up_dn_speed
    elif path_down:
        snake.insert(0,snake[0]+down)
        snake.pop(-1)
        mvmt = up_dn_speed

#----------------------------------------------------------------------------
#Refresh rate
    if timer(mvmt) == 'A':

#----------------------------------------------------------------------------
#Gets input again to reduce lag caused by slow refresh rate (~0.5sec)
        get_user_input()

#----------------------------------------------------------------------------
#Refresh rate again to slow down snake speed in order to be playable
        if timer(mvmt) == 'A':

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
        score += 1

#----------------------------------------------------------------------------
#Prints the update board and clears board (ready for next update)
    print(f"\n{' '*36}▒█▀▀▀█ █▀▀▄ █▀▀█ █░█ █▀▀ ")
    print(f"{' '*36}░▀▀▀▄▄ █░░█ █▄▄█ █▀▄ █▀▀ ")
    print(f"{' '*36}▒█▄▄▄█ ▀░░▀ ▀░░▀ ▀░▀ ▀▀▀\n")                                                   
    print(f"{' '*24}Use ↑ ↓ ← → on your keyboard to control the Snake")
    print(f"{' '*22}Don't touch the edges, be carefull with your movement")
    print(f"{' '*23}Try to eat as many random snacks ('O') as possible")
    print(f"{' '*24}As the Snake gets bigger the speed will increase")
    print(f"{' '*44}Have fun!")
    print(f"{' '*24}Level: {level}{' '*32}Score: {score}")
    for t in range(0, len(board), length+2):
        print(f"{' '*32}{"".join(board[t:t+length+2])}")
    print(end=f"\033[{height+11}A\r")
    board = refresh_board.copy()

#----------------------------------------------------------------------------
#Increases speed (level) if snake gets bigger 
    if len(snake) >= 10:
        lf_rt_speed = 20
        up_dn_speed = int(lf_rt_speed*1.6)
        level = 2
    if len(snake) >= 15:
        lf_rt_speed = 10
        up_dn_speed = int(lf_rt_speed*1.6)
        level = 3
    if len(snake) >= 20:
        lf_rt_speed = 8
        up_dn_speed = int(lf_rt_speed*1.6)
        level = 4

#----------------------------------------------------------------------------
#Prints GAME OVER and clears terminal if snake collides with edge
else:
    print(f"{'\n'*(height+11)}")
    print(f"{' '*30}█▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█")
    print(f"{' '*30}█▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄")
    if timer(800) == 'A': 
        os.system('cls' if os.name == 'nt' else 'clear')
