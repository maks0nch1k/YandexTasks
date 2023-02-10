import pygame
import math


def draw():
    pygame.draw.circle(screen, color, (x0, y0), 10)
    pygame.draw.polygon(screen, color, [a1, b1, c1])
    pygame.draw.polygon(screen, color, [a2, b2, c2])
    pygame.draw.polygon(screen, color, [a3, b3, c3])


if __name__ == "__main__":
    pygame.init()
    size = width, height = 201, 201
    screen = pygame.display.set_mode(size)
    running = True
    color_bg = "black"
    color = "white"
    screen.fill(color_bg)
    pygame.display.set_caption("Вентилятор")
    fps = 240
    v = 0
    pos = 270
    clock = pygame.time.Clock()

    x0, y0 = 100, 100
    r = 70

    a1 = (x0 + r * math.cos((pos + 15) / 180 * math.pi), y0 + r * math.sin((pos + 15) / 180 * math.pi))
    b1 = (x0 + r * math.cos((pos - 15) / 180 * math.pi), y0 + r * math.sin((pos - 15) / 180 * math.pi))
    c1 = (100, 100)

    a2 = (x0 + r * math.cos((pos + 15 + 120) / 180 * math.pi), y0 + r * math.sin((pos + 15 + 120) / 180 * math.pi))
    b2 = (x0 + r * math.cos((pos - 15 + 120) / 180 * math.pi), y0 + r * math.sin((pos - 15 + 120) / 180 * math.pi))
    c2 = (100, 100)

    a3 = (x0 + r * math.cos((pos + 15 + 240) / 180 * math.pi), y0 + r * math.sin((pos + 15 + 240) / 180 * math.pi))
    b3 = (x0 + r * math.cos((pos - 15 + 240) / 180 * math.pi), y0 + r * math.sin((pos - 15 + 240) / 180 * math.pi))
    c3 = (100, 100)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    v -= 50
                elif event.button == 3:
                    v += 50

        pos += v/fps

        a1 = (x0 + r * math.cos((pos + 15) / 180 * math.pi), y0 + r * math.sin((pos + 15) / 180 * math.pi))
        b1 = (x0 + r * math.cos((pos - 15) / 180 * math.pi), y0 + r * math.sin((pos - 15) / 180 * math.pi))
        c1 = (100, 100)

        a2 = (x0 + r * math.cos((pos + 15 + 120) / 180 * math.pi), y0 + r * math.sin((pos + 15 + 120) / 180 * math.pi))
        b2 = (x0 + r * math.cos((pos - 15 + 120) / 180 * math.pi), y0 + r * math.sin((pos - 15 + 120) / 180 * math.pi))
        c2 = (100, 100)

        a3 = (x0 + r * math.cos((pos + 15 + 240) / 180 * math.pi), y0 + r * math.sin((pos + 15 + 240) / 180 * math.pi))
        b3 = (x0 + r * math.cos((pos - 15 + 240) / 180 * math.pi), y0 + r * math.sin((pos - 15 + 240) / 180 * math.pi))
        c3 = (100, 100)

        screen.fill(color_bg)
        clock.tick(fps)
        draw()
        pygame.display.flip()

    pygame.quit()