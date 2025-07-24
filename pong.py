import pygame
import random

GAME_WIDTH = 800
GAME_HEIGHT = 800
BALL_DIAMETER = 10
PADDLE_PADDING = 10
PADDLE_THICKNESS = 10
PADDLE_LENGTH = 100
PADDLE_VELOCITY = 200

WINDOW_WIDTH = GAME_WIDTH + 100
WINDOW_HEIGHT = GAME_HEIGHT
BALL_BOX_X1 = BALL_DIAMETER/2
BALL_BOX_X2 = GAME_WIDTH-BALL_DIAMETER/2
BALL_BOX_Y1 = BALL_DIAMETER/2 + PADDLE_PADDING + PADDLE_THICKNESS
BALL_BOX_Y2 = GAME_HEIGHT-PADDLE_PADDING-PADDLE_THICKNESS-BALL_DIAMETER/2

game_over = 0

pygame.init()
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0


class Ball:
    def __init__(self):
        self.x = GAME_WIDTH/2
        self.y = GAME_HEIGHT/2
        self.draw_ball()
        self.vx = random.randint(150, 200) * (random.randint(0, 1)*2-1)
        self.vy = random.randint(150, 200) * (random.randint(0, 1)*2-1)
    def draw_ball(self):
        pygame.draw.circle(screen, "white", (self.x, self.y), BALL_DIAMETER/2)
    def move(self):
        if not (BALL_BOX_X1 < self.x < BALL_BOX_X2):
            self.vx *= -1
        if not (BALL_BOX_Y1 < self.y < BALL_BOX_Y2):
            if self.y >= BALL_BOX_Y2 and not (paddle1.x <= self.x <= paddle1.x + PADDLE_LENGTH):
                heart1.lives -= 1
                self.x = GAME_WIDTH/2
                self.y = GAME_HEIGHT/2
                self.vx = random.randint(100, 150) * (random.randint(0, 1)*2-1)
                self.vy = random.randint(100, 150) * (random.randint(0, 1)*2-1)
            elif self.y <= BALL_BOX_Y1 and not (paddle2.x <= self.x <= paddle2.x + PADDLE_LENGTH):
                heart2.lives -= 1
                self.x = GAME_WIDTH/2
                self.y = GAME_HEIGHT/2
                self.vx = random.randint(100, 150) * (random.randint(0, 1)*2-1)
                self.vy = random.randint(100, 150) * (random.randint(0, 1)*2-1)
            else:
                self.vy *= -1
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.draw_ball()

class Paddle:
    def __init__(self, player):
        self.player = player
        self.x = GAME_WIDTH/2 - PADDLE_LENGTH/2
        if self.player == 1:
            self.y = GAME_HEIGHT-PADDLE_PADDING-PADDLE_THICKNESS
        elif self.player == 2:
            self.y = PADDLE_PADDING
        self.draw_paddle()
    def draw_paddle(self):
        pygame.draw.rect(screen, "white", (self.x, self.y, PADDLE_LENGTH, PADDLE_THICKNESS), border_radius=int(PADDLE_THICKNESS/2))
    def move(self):
        keys = pygame.key.get_pressed()
        if self.player == 1:
            if keys[pygame.K_RIGHT] and self.x < GAME_WIDTH - PADDLE_LENGTH:
                self.x += PADDLE_VELOCITY * dt
            if keys[pygame.K_LEFT] and self.x > 0:
                self.x -= PADDLE_VELOCITY * dt
        elif self.player == 2:
            if keys[pygame.K_d]  and self.x < GAME_WIDTH - PADDLE_LENGTH:
                self.x += PADDLE_VELOCITY * dt
            if keys[pygame.K_a] and self.x > 0:
                self.x -= PADDLE_VELOCITY * dt
        self.draw_paddle()

class Heart:
    def __init__(self, player):
        self.player = player
        self.lives = 3
        self.draw_hearts()
    def draw_hearts(self):
        global game_over
        heart = pygame.image.load('heart.svg')
        initial_padding = GAME_WIDTH + 10
        # TODO: this can be cleaned up
        if self.player == 1:
            for i in range(self.lives):
                screen.blit(heart, (initial_padding + i*30, GAME_HEIGHT - 2.5*PADDLE_PADDING))
        elif self.player == 2:
            for i in range(self.lives):
                screen.blit(heart, (initial_padding + i*30, 2.5*PADDLE_PADDING))
        if self.lives == 0:
            game_over = 3 - self.player # Assuming it's 2 player pong, this returns the winner

ball = Ball()
paddle1 = Paddle(1)
paddle2 = Paddle(2)
heart1 = Heart(1)
heart2 = Heart(2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#121212")

    if not game_over:
        pygame.draw.rect(screen, "white", (0, 0, GAME_WIDTH, GAME_HEIGHT), width=1)
        ball.move()
        paddle1.move()
        paddle2.move()
        heart1.draw_hearts()
        heart2.draw_hearts()
    else:
        font = pygame.font.SysFont(None, 40)
        text_surface = font.render(f"Player {game_over} wins!", True, "white")
        text_rect = text_surface.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()