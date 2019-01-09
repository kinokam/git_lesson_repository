import pygame



pygame.init()
size = width, height = x, y
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
x_pos = 0

running = True
screen.fill((0, 0, 0))
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.circle(screen, (0, 0, 255), event.pos, 20)
    pygame.display.flip()

pygame.quit()
