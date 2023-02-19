import pygame
from ast import literal_eval


def draw(coeff):
    points_draw = [(elem[0] * coeff + 250, (0 - elem[1]) * coeff + 250) for elem in points]
    pygame.draw.polygon(screen, "white", points_draw, 1)


if __name__ == '__main__':
    pygame.init()
    running = True
    size = 501, 501
    color = "black"
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Zoom")
    coeff = 1

    with open("points.txt") as file:
        data = file.read().split(", ")
        for i in range(len(data)):
            data[i] = data[i].replace(",", ".")
            data[i] = data[i].replace(";", ",")

    points = list(map(literal_eval, data))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    coeff += 1
                if event.button == 5:
                    coeff -= 1

        screen.fill(color)
        draw(coeff)
        pygame.display.flip()

    pygame.quit()

