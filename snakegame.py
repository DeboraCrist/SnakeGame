import pygame, sys, random, time

verificar_erros = pygame.init()

if verificar_erros[1] > 0:
    print("(!) Teve {0} erros de iniciação, saindo... ".format(verificar_erros[1]))
    sys.exit()
else:
    print("(+) Pygame inicialização com sucesso!")

playSurface = pygame.display.set_mode((720, 460))  # (720 , 460) é uma lista
pygame.display.set_caption("Snake Game")

# colores
red = pygame.Color(255, 0, 0)  # game over
green = pygame.Color(0, 255, 0)  # snake
black  = pygame.Color(255,255,255)  # fundo
white = pygame.Color(0,0,0)  # score
purple = pygame.Color(125,0, 120)  # uva

fpsController = pygame.time.Clock()

score = 0

snakePos = [100, 50]
snakeCorpo= [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
foodSpawn = True

direction = 'RIGHT'
mudar = direction


def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render("Game Over!", True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf, GOrect)
    updateScore()
    pygame.display.flip()  # atualização do quadro
    time.sleep(1)
    pygame.quit()  # pygame exit
    sys.exit()  # console exit


def updateScore():
    myFont = pygame.font.SysFont('monaco', 20)
    setScore = "{}{}".format("Score:", score)
    Ssurf = myFont.render(setScore, True, black)
    Srect = Ssurf.get_rect()
    Srect.topleft = (20, 15)
    playSurface.blit(Ssurf, Srect)
    pygame.display.flip()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                mudar = 'RIGHT'

            if event.key == pygame.K_LEFT or event.key == ord('a'):
                mudar = 'LEFT'

            if event.key == pygame.K_UP or event.key == ord('w'):
                mudar = 'UP'

            if event.key == pygame.K_DOWN or event.key == ord('s'):
                mudar = 'DOWN'

            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # variação da direção
    if mudar == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if mudar == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if mudar == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if mudar == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    # mecanismo do corpo da cobra
    snakeCorpo.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        foodSpawn = False
        score += 1
    else:
        snakeCorpo.pop()  # remove o ultimo retangulo da cobra para dar senseção de movimento

    #uva
    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

    playSurface.fill(white)
    for pos in snakeCorpo:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(playSurface, purple, pygame.Rect(foodPos[0], foodPos[1], 10, 10))
    if snakePos[0] > 710 or snakePos[0] < 10:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 10:
        gameOver()

    for i in snakeCorpo[1:]:
        if i == snakePos:
            gameOver()

    pygame.display.update()
    updateScore()
    fpsController.tick(10)