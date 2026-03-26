import random
import sys
import pygame

# -------------------------
# Configuration
# -------------------------
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 60

PLAYER_WIDTH = 60
PLAYER_HEIGHT = 24
PLAYER_SPEED = 7

OBSTACLE_WIDTH = 55
OBSTACLE_HEIGHT = 55
OBSTACLE_START_SPEED = 4
OBSTACLE_SPEED_GROWTH = 0.002  # speed gain per frame based on score timer

SPAWN_INTERVAL_MS = 700


# -------------------------
# Game Objects
# -------------------------
class Player:
    def __init__(self, x: int, y: int):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.color = (80, 220, 255)

    def update(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += PLAYER_SPEED

        # Keep player on screen
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=8)


class Obstacle:
    def __init__(self, speed: float):
        self.rect = pygame.Rect(
            random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH),
            -OBSTACLE_HEIGHT,
            OBSTACLE_WIDTH,
            OBSTACLE_HEIGHT,
        )
        self.base_speed = speed
        self.color = (255, 110, 110)

    def update(self, bonus_speed: float):
        self.rect.y += self.base_speed + bonus_speed

    def off_screen(self) -> bool:
        return self.rect.top > SCREEN_HEIGHT

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=6)


# -------------------------
# Main Game Controller
# -------------------------
class DodgeGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("OOP Dodge Game")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 28)
        self.big_font = pygame.font.SysFont("arial", 48, bold=True)

        self.spawn_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.spawn_event, SPAWN_INTERVAL_MS)

        self.reset()

    def reset(self):
        self.player = Player(SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2, SCREEN_HEIGHT - 70)
        self.obstacles = []
        self.running = True
        self.game_over = False
        self.score = 0
        self.start_ticks = pygame.time.get_ticks()

    def spawn_obstacle(self):
        self.obstacles.append(Obstacle(OBSTACLE_START_SPEED))

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)

        elapsed_ms = pygame.time.get_ticks() - self.start_ticks
        self.score = elapsed_ms // 100
        bonus_speed = self.score * OBSTACLE_SPEED_GROWTH

        for obs in self.obstacles:
            obs.update(bonus_speed)

        # Remove obstacles that passed the screen
        self.obstacles = [obs for obs in self.obstacles if not obs.off_screen()]

        # Collision check
        for obs in self.obstacles:
            if self.player.rect.colliderect(obs.rect):
                self.game_over = True
                break

    def draw_background(self):
        self.screen.fill((20, 24, 30))
        # subtle lane lines for style
        for x in range(100, SCREEN_WIDTH, 100):
            pygame.draw.line(self.screen, (35, 40, 50), (x, 0), (x, SCREEN_HEIGHT), 1)

    def draw_hud(self):
        score_text = self.font.render(f"Score: {self.score}", True, (235, 235, 235))
        self.screen.blit(score_text, (15, 12))

    def draw_game_over(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))

        title = self.big_font.render("Game Over", True, (255, 90, 90))
        sub = self.font.render(f"Final Score: {self.score}", True, (240, 240, 240))
        hint = self.font.render("Press R to restart or Q to quit", True, (220, 220, 220))

        self.screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 70)))
        self.screen.blit(sub, sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
        self.screen.blit(hint, hint.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)))

    def draw(self):
        self.draw_background()
        self.player.draw(self.screen)
        for obs in self.obstacles:
            obs.draw(self.screen)
        self.draw_hud()

        if self.game_over:
            self.draw_game_over()

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == self.spawn_event and not self.game_over:
                self.spawn_obstacle()

            if self.game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.reset()
                elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                    self.running = False

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()

            if not self.game_over:
                self.update()

            self.draw()

        pygame.quit()
        sys.exit()

print('hey from', __name__)

if __name__ == "__main__":
    print('running the game')
    DodgeGame().run()
