import pygame

pygame.init()
size = width, height = 800, 600
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
x_pos = 0

running = True
screen.fill((0, 0, 255))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 255))
    pygame.draw.circle(screen, (255, 255, 0), (200, 200), x_pos)
    x_pos += 1

    pygame.display.flip()

pygame.quit()