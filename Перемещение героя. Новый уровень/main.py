import pygame
import sys
import os


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)


def generate_level(level):
    new_player = None
    for y_pos in range(-len(level), 2 * len(level)):
        y_now = y_pos
        if y_now >= len(level):
            y_now %= len(level)
        for x_pos in range(-len(level[y_now]), 2 * len(level[y_now])):
            x_now = x_pos
            if x_now >= len(level[y_now]):
                x_now %= len(level[y_now])
            if level[y_now][x_now] == '.':
                Tile('empty', x_pos, y_pos)
            elif level[y_now][x_now] == '#':
                Tile('wall', x_pos, y_pos)
            elif level[y_now][x_now] == '@':
                Tile('empty', x_now, y_now)
                new_player = Player(x_now, y_now)
    return new_player # , x_pos, y_pos


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


if __name__ == "__main__":
    pygame.init()
    size = WIDTH, HEIGHT = 500, 500
    screen = pygame.display.set_mode(size)
    running = True
    color = "black"
    screen.fill(color)

    pygame.display.set_caption("игра")
    FPS = 240
    clock = pygame.time.Clock()
    start_screen()
    # name_file = input("Название файла: ")
    name_file = "file_path.txt"
    camera = Camera()
    try:
        level = load_level(name_file)

        for i in range(len(level)):
            if "@" in level[i]:
                y, x = i, level[i].find("@")

        tile_images = {
            'wall': load_image('box.png'),
            'empty': load_image('grass.png')
        }
        player_image = load_image('mario.png')
        tile_width = tile_height = 50
        player = None
        all_sprites = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()
        player_group = pygame.sprite.Group()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # print(x, y)
                    # pprint.pprint(level)
                    if event.key == pygame.K_DOWN:
                        if y < 10 and level[y + 1][x] == ".":
                            level[y] = level[y][:x] + "." + level[y][x + 1:]
                            level[y + 1] = level[y + 1][:x] + "@" + level[y + 1][x + 1:]
                            y += 1
                        elif y >= 10 and level[y - 10][x] == ".":
                            level[y] = level[y][:x] + "." + level[y][x + 1:]
                            level[0] = level[0][:x] + "@" + level[0][x + 1:]
                            y = 0
                    if event.key == pygame.K_LEFT:
                        if x > 0 and level[y][x - 1] == ".":
                            level[y] = level[y][:x - 1] + "@." + level[y][x + 1:]
                            x -= 1
                        elif x <= 0 and level[y][-1] == ".":
                            level[y] = "." + level[y][1:-1] + "@"
                            x = 12
                    if event.key == pygame.K_RIGHT:
                        if x < 12 and level[y][x + 1] == ".":
                            level[y] = level[y][:x] + ".@" + level[y][x + 2:]
                            x += 1
                        elif x >= 12 and level[y][0] == ".":
                            level[y] = "@" + level[y][:-2] + "."
                            x = 0
                    if event.key == pygame.K_UP:
                        if y > 0 and level[y - 1][x] == ".":
                            level[y] = level[y][:x] + "." + level[y][x + 1:]
                            level[y - 1] = level[y - 1][:x] + "@" + level[y - 1][x + 1:]
                            y -= 1
                        elif y <= 0 and level[-1][x] == ".":
                            level[0] = level[0][:x] + "." + level[0][x + 1:]
                            level[-1] = level[-1][:x] + "@" + level[-1][x + 1:]
                            y = 10

            screen.fill(color)
            clock.tick(FPS)
            player = generate_level(level)
            camera.update(player)
            for sprite in all_sprites:
                camera.apply(sprite)
            all_sprites.update(screen)
            all_sprites.draw(screen)
            pygame.display.flip()
    except Exception as e:
        print(e)
    pygame.quit()



"""
####.....####
#...........#
#.......#...#
#...........#
......@......
.............
.....#.......
#...........#
#.......#...#
#...........#
####.....####
"""