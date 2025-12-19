import pygame
from camera import Camera, camera_shake
from room_manager import RoomManager
from entities import Player

# ensure pygame subsystems are initialized before using fonts/display
pygame.init()

# constants
SCREEN_W, SCREEN_H = 960, 600
WORLD_W, WORLD_H = 3200, 2400
BG_COLOR = (25, 28, 35)


class Game:
    _entities: list = []
    def __init__(self):
        pygame.display.set_caption("Pygame Camera - Rooms + Entities")
        self.world = pygame.Rect(0, 0, WORLD_W, WORLD_H)
        self.screen = pygame.display.get_surface() or pygame.display.set_mode((SCREEN_W, SCREEN_H))
        self.clock = pygame.time.Clock()
        self.camera = Camera((SCREEN_W, SCREEN_H), self.world)
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 20)
        self.roomman = RoomManager()
        self.roomman.bfs_place("hall")
        self.roomman.compute_room_rects()

        # create player and append to self._entities
        hall_rect = self.roomman.room_rects.get("hall")
        if hall_rect:
            player_rect = pygame.Rect(hall_rect.centerx - 16, hall_rect.centery - 16, 32, 32)
        else:
            player_rect = pygame.Rect(WORLD_W // 2 - 16, WORLD_H // 2 - 16, 32, 32)

        self.player = Player(player_rect)
        self._entities.clear()
        self._entities.append(self.player)

        self.base_surf = pygame.Surface((SCREEN_W, SCREEN_H)).convert_alpha()
        self.zoom = 1.0
        self.running = True

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.zoom = max(0.5, round(self.zoom - 0.1, 2))
            elif event.key == pygame.K_e:
                self.zoom = min(2.0, round(self.zoom + 0.1, 2))

    def update(self, dt: float):
        for e in list(self._entities):
            e.update(dt)
            e.rect.clamp_ip(self.world)

        self.camera.update(self.player.rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            camera_shake(self.camera, intensity=20)

    def draw(self):
        self.base_surf.fill(BG_COLOR)
        self.roomman.draw(self.base_surf, self.camera, self.font)

        for e in self._entities:
            e.draw(self.base_surf, self.camera)

        if self.zoom != 1.0:
            zw = int(self.base_surf.get_width() * self.zoom)
            zh = int(self.base_surf.get_height() * self.zoom)
            scaled = pygame.transform.smoothscale(self.base_surf, (zw, zh))
            dst = scaled.get_rect(center=self.screen.get_rect().center)
            self.screen.fill((0, 0, 0))
            self.screen.blit(scaled, dst)
        else:
            self.screen.blit(self.base_surf, (0, 0))

        pygame.display.set_caption(f"Camera Demo | Zoom {self.zoom:.1f} | FPS {self.clock.get_fps():.1f}")
        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                self.handle_event(event)

            self.update(dt)
            self.draw()

        pygame.quit()


def main():
    Game().run()


if __name__ == "__main__":
    main()
