# snake_game.py
import random
import pygame
from collections import deque

# --- Конфиг ---
CELL_SIZE = 20
GRID_W, GRID_H = 32, 24  # дэлгэц: 640x480 (if CELL_SIZE=20 -> 640x480)
SCREEN_W, SCREEN_H = GRID_W * CELL_SIZE, GRID_H * CELL_SIZE
FPS = 12

# Өнгө
BG = (18, 18, 18)
SNAKE_COLOR = (0, 200, 0)
FOOD_COLOR = (200, 50, 50)
GRID_COLOR = (30, 30, 30)

# --- Тоглоомын объектууд ---


class Snake:
    def __init__(self, x, y):
        self.body = deque()  # head at left
        self.body.append((x, y))
        self.dir = (1, 0)  # right
        self.grow_pending = 0

    def set_dir(self, dx, dy):
        # Хажуу тийш буцаж орохгүй байх шалгалт
        if (dx, dy) == (-self.dir[0], -self.dir[1]) and len(self.body) > 1:
            return
        self.dir = (dx, dy)

    def step(self):
        headx, heady = self.body[0]
        nx, ny = headx + self.dir[0], heady + self.dir[1]
        self.body.appendleft((nx, ny))
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

    def grow(self, amount=1):
        self.grow_pending += amount

    def collides_with_self(self):
        head = self.body[0]
        return head in list(self.body)[1:]

    def collides_with_bounds(self):
        x, y = self.body[0]
        return not (0 <= x < GRID_W and 0 <= y < GRID_H)


class Food:
    def __init__(self, occupied):
        self.pos = self.random_pos(occupied)

    def random_pos(self, occupied):
        while True:
            p = (random.randrange(GRID_W), random.randrange(GRID_H))
            if p not in occupied:
                return p

    def respawn(self, occupied):
        self.pos = self.random_pos(occupied)

# --- Тоглоомын логик ---


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Snake.io - single player (Python)")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    snake = Snake(GRID_W // 2, GRID_H // 2)
    # Улс төрийн эхэнд жаахан өсгөе
    for _ in range(3):
        snake.grow()

    food = Food(set(snake.body))
    score = 0
    running = True
    paused = False

    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            elif ev.type == pygame.KEYDOWN:
                # WASD / arrows
                if ev.key in (pygame.K_w, pygame.K_UP):
                    snake.set_dir(0, -1)
                elif ev.key in (pygame.K_s, pygame.K_DOWN):
                    snake.set_dir(0, 1)
                elif ev.key in (pygame.K_a, pygame.K_LEFT):
                    snake.set_dir(-1, 0)
                elif ev.key in (pygame.K_d, pygame.K_RIGHT):
                    snake.set_dir(1, 0)
                elif ev.key == pygame.K_SPACE:
                    paused = not paused
                elif ev.key == pygame.K_r:  # reset
                    return main()

        if not paused:
            snake.step()

            # Хоол идэвэл
            if snake.body[0] == food.pos:
                snake.grow(3)  # өсөлт
                score += 1
                food.respawn(set(snake.body))

            # Мөргөлдөөнүүд
            if snake.collides_with_bounds() or snake.collides_with_self():
                # Тоглоом дуусна
                msg = font.render(
                    f"Game Over! Score: {score}  (R to restart)", True, (220, 220, 220))
                screen.blit(msg, (20, SCREEN_H//2 - 10))
                pygame.display.flip()
                # Хэсэг хугацаанд хүлээгээд restart эсвэл quit
                waiting = True
                while waiting:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            pygame.quit()
                            return
                        elif e.type == pygame.KEYDOWN:
                            if e.key == pygame.K_r:
                                waiting = False
                                return main()
                            elif e.key == pygame.K_ESCAPE:
                                pygame.quit()
                                return
                    clock.tick(10)

        # Draw
        screen.fill(BG)
        # жижиг grid (сонголтоор)
        for x in range(0, SCREEN_W, CELL_SIZE):
            pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_H))
        for y in range(0, SCREEN_H, CELL_SIZE):
            pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_W, y))

        # food
        fx, fy = food.pos
        pygame.draw.rect(screen, FOOD_COLOR, (fx*CELL_SIZE,
                         fy*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # snake
        for i, (sx, sy) in enumerate(snake.body):
            rect = pygame.Rect(sx*CELL_SIZE, sy*CELL_SIZE,
                               CELL_SIZE, CELL_SIZE)
            # head илүү тод харагдуулна
            if i == 0:
                pygame.draw.rect(
                    screen, (SNAKE_COLOR[0], SNAKE_COLOR[1], 255), rect)
            else:
                pygame.draw.rect(screen, SNAKE_COLOR, rect)

        # score
        sc = font.render(f"Score: {score}", True, (200, 200, 200))
        screen.blit(sc, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
