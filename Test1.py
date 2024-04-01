import pygame
import sys
pygame.init()

X = 560
Y = 1080

WHITE = (255, 255, 255)
GREY = (200, 200, 200)
DARK_GREY = (50, 50, 50)
BLACK = (0, 0, 0)
ORANGE = (255, 100, 15)
DARK_ORANGE = (200, 100, 0)
LIGHT_ORANGE = (255, 187, 87)
YELLOW = (255, 255, 0)
DARK_YELLOW = (189, 186, 0)
LIGHT_YELLOW = (255, 255, 100)
DARK_PURPLE = (62, 0, 112)
BROWN = (75, 35, 15)

#pygame.draw.rect(DISPLAY, , [, , , ])
#pygame.draw.polygon(DISPLAY, , [[, ], [, ], [, ]])
#pygame.draw.line(DISPLAY, , [, ], [, ], )
#pygame.draw.arc(DISPLAY, , [, , , ], pi, 2*pi, )
#pygame.draw.cirlce(DISPLAY, , (, ), )
#pygame.draw.ellipse(DISPLAY, , oval_rect)
#pygame.draw.ellipse(DISPLAY, , (, , , ))
#oval_rect = pygame.Rect(, , , )
# hw_image = pygame.image.load("/Favorites/halloween-spooky.otf").convert_alpha()
# size = (X,Y)
# hw_scale =  pygame.transform.scale(hw_image, size)
# DISPLAY.blit(hw_scale, (25, 25))



DISPLAY = pygame.display.set_mode([X,Y])
pygame.display.set_caption('Halloween Poster')
font = pygame.font.Font(None, 45)
pi = 3.14

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    DISPLAY.fill(BLACK)

    pygame.draw.polygon(DISPLAY, DARK_PURPLE, [[-10, -10], [-10, 70], [400, -10]])
    pygame.draw.polygon(DISPLAY, DARK_PURPLE, [[100, -10], [150, 70], [500, -10]])

    #pygame.draw.polygon(DISPLAY, PURPLE, [[, ], [, ], [, ]])
    text = font.render("Happy Halloween!", True, WHITE)
    DISPLAY.blit(text, [0, 0])
    text2 = font.render("Happy Halloween!", True, BLACK)
    DISPLAY.blit(text2, [2, 2])

    #STEM
    #pygame.draw.polygon(DISPLAY, BROWN, [[320, 140], [320, 165], [365, 140], [365, 165]])
    pygame.draw.rect(DISPLAY, BROWN, [325, 140, 35, 80])
    pygame.draw.rect(DISPLAY, BROWN, [325, 110, 80, 35])

    # PUMPKIN
    pygame.draw.ellipse(DISPLAY, ORANGE, (400, 200, 300, 1000))
    pygame.draw.ellipse(DISPLAY, ORANGE, (0, 200, 300, 1000))
    pygame.draw.arc(DISPLAY, LIGHT_ORANGE, [-50, 200, 400, 2000], 0, pi, 12)
    pygame.draw.ellipse(DISPLAY, ORANGE, (125, 150, 450, 1000))

    #SOCKETS
    pygame.draw.polygon(DISPLAY, DARK_ORANGE, [[185, 310], [135, 435], [235, 475]])
    pygame.draw.polygon(DISPLAY, DARK_ORANGE, [[510, 310], [560, 425], [460, 475]])
    pygame.draw.polygon(DISPLAY, BLACK, [[175, 300], [125, 425], [225, 465]])
    pygame.draw.polygon(DISPLAY, BLACK, [[500, 300], [550, 425], [450, 465]])

    #EYES
    pygame.draw.circle(DISPLAY, DARK_GREY, (190, 400), 12)
    pygame.draw.circle(DISPLAY, GREY, (190, 400), 7)
    pygame.draw.circle(DISPLAY, WHITE, (190, 400), 5)
    pygame.draw.circle(DISPLAY, DARK_GREY, (485, 400), 12)
    pygame.draw.circle(DISPLAY, GREY, (485, 400), 7)
    pygame.draw.circle(DISPLAY, WHITE, (485, 400), 5)

    #MOUTH
    pygame.draw.polygon(DISPLAY, DARK_ORANGE, [[110, 470], [130, 1090], [310, 1090]])
    pygame.draw.polygon(DISPLAY, DARK_ORANGE, [[210, 510], [10, 1090], [410, 1090]])
    pygame.draw.polygon(DISPLAY, DARK_ORANGE, [[285, 530], [85, 1090], [485, 1090]])
    pygame.draw.polygon(DISPLAY, DARK_ORANGE, [[410, 530], [210, 1090], [610, 1090]])
    pygame.draw.polygon(DISPLAY, DARK_ORANGE, [[485, 510], [285, 1090], [685, 1090]])
    pygame.draw.polygon(DISPLAY, DARK_ORANGE, [[575, 470], [555, 1090], [435, 1090]])

    pygame.draw.polygon(DISPLAY, BLACK, [[100, 460], [120, 1080], [300, 1080]])
    pygame.draw.polygon(DISPLAY, BLACK, [[200, 500], [0, 1080], [400, 1080]])
    pygame.draw.polygon(DISPLAY, BLACK, [[275, 520], [75, 1080], [475, 1080]])
    pygame.draw.polygon(DISPLAY, BLACK, [[400, 520], [200, 1080], [600, 1080]])
    pygame.draw.polygon(DISPLAY, BLACK, [[475, 500], [275, 1080], [675, 1080]])
    pygame.draw.polygon(DISPLAY, BLACK, [[565, 460], [545, 1080], [425, 1080]])


    # pygame.draw.polygon(DISPLAY, BLACK, [[, ], [, ], [, ]])
    pygame.display.flip()