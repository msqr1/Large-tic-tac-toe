def reset():
    import pygame,sys,time 
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0,0,255)    
    XO = 'x' #Who goes first?
    FPS = 120
    WIDTH = 28
    HEIGHT = 28
    MARGIN = 2
    rownum = 33
    colnum = 64
    grid = []
    for row in range(rownum):
        grid.append([])
        for column in range(colnum):
            grid[row].append(0)
    pygame.init()
    WINDOW_SIZE = [1920,990]
    screen = pygame.display.set_mode(WINDOW_SIZE,pygame.RESIZABLE)
    x_img = pygame.transform.smoothscale(pygame.image.load("X_modified-100x100.png").convert(),(28,28))
    o_img = pygame.transform.smoothscale(pygame.image.load("o_modified-100x100.png").convert(),(28,28))
    pygame.display.set_caption("Caro")
    def checkwin(board):
        indices = [i for i,x in enumerate(board) if 'x' in x]
        for index in indices:
            xrowindices = [i for i, x in enumerate(board[index]) if x == "x"]
            for xs in xrowindices:
                if xs<=len(board[0])-5:
                    if board[index][xs] == board[index][xs+1] == board[index][xs+2] == board[index][xs+3] == board[index][xs+4]:
                        return 1
                if index<=len(board)-5:
                    if board[index][xs] == board[index+1][xs] == board[index+2][xs] == board[index+3][xs] == board[index+4][xs]:
                        return 1
                    if xs<=len(board[0])-5:
                        if board[index][xs] == board[index+1][xs+1] == board[index+2][xs+2] == board[index+3][xs+3] == board[index+4][xs+4]:
                            return 1
                        if board[index][xs] == board[index+1][xs-1] == board[index+2][xs-2] == board[index+3][xs-3] == board[index+4][xs-4]:
                            return 1
        indices1 = [i for i,x in enumerate(board) if 'o' in x]
        for index1 in indices1:
            orowindices = [i for i, x in enumerate(board[index1]) if x == "o"]
            for os in orowindices:
                if os<=len(board[0])-5:
                    if board[index1][os] == board[index1][os+1] == board[index1][os+2] == board[index1][os+3] == board[index1][os+4]:
                        return 2
                if index1<=len(board)-5:
                    if board[index1][os] == board[index1+1][os] == board[index1+2][os] == board[index1+3][os] == board[index1+4][os]:
                        return 2
                    if os<=len(board[0])-5:
                        if board[index1][os] == board[index1+1][os+1] == board[index1+2][os+2] == board[index1+3][os+3] == board[index1+4][os+4]:
                            return 2
                        if board[index1][os] == board[index1+1][os-1] == board[index1+2][os-2] == board[index1+3][os-3] == board[index1+4][os-4]:
                            return 2
        for rows in board:
            for cells in rows:
                count = 0
                if cells == 'x' or cells == 'o':
                    count+=1
                if count == rownum*colnum:
                    return 3
    done = False
    status = None
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                done = True 
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = pos[0] // (WIDTH + MARGIN)
                row=  pos[1] // (HEIGHT + MARGIN)
                if grid[row][col] == 0:
                    if XO == 'x':
                        grid[row][col] = XO
                        XO = 'o'
                    else:
                        grid[row][col] = XO
                        XO = 'x'
                    if checkwin(grid) == 1:
                        status = 1
                    if checkwin(grid) == 2:
                        status = 2
                    if checkwin(grid) == 3:
                        status = 3
        screen.fill(BLACK)
        for row in range(rownum):
            for column in range(colnum):
                color = WHITE
                pygame.draw.rect(screen,
                                 color,
                                  [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
                if grid[row][column] == 'x': 
                    screen.blit(x_img,((WIDTH + MARGIN)*column+2,(HEIGHT + MARGIN)*row+2))
                if grid[row][column] == 'o':
                    screen.blit(o_img,((WIDTH + MARGIN)*column+2,(HEIGHT + MARGIN)*row+2))
        if status == 0:
            font = pygame.font.Font('freesansbold.ttf', 100)
            text = font.render('Draw', True, GREEN, BLUE)
            textRect = text.get_rect()
            textRect.center = (WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2)
            screen.blit(text,textRect)
            pygame.display.update()
            time.sleep(2)
            reset()
        if status == 1:
            font = pygame.font.Font('freesansbold.ttf', 100)
            text = font.render('X wins', True, GREEN, BLUE)
            textRect = text.get_rect()
            textRect.center = (WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2)
            screen.blit(text,textRect)
            pygame.display.update()
            time.sleep(2)
            reset()
        if status == 2:
            font = pygame.font.Font('freesansbold.ttf', 100)
            text = font.render('O wins', True, GREEN, BLUE)
            textRect = text.get_rect()
            textRect.center = (WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2)
            screen.blit(text,textRect)
            pygame.display.update()
            time.sleep(2)
            reset()
        #Limit to 99999999 FPS
        clock.tick(FPS)
        pygame.display.update()
    quit()
    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    reset()