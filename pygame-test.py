import pygame
import random

pygame.init()
screen = pygame.display.set_mode((960, 600))
pygame.display.set_caption("Pygame Camera — Follow, Scroll, Zoom")
clock = pygame.time.Clock()

WORLD_W, WORLD_H = 3200, 2400
PLAYER_SPEED = 300  # px/s

class Camera:
    def __init__(self, screen_size: tuple[int,int], world_rect: pygame.Rect):
        self.screen_w, self.screen_h = screen_size
        self.world_rect = world_rect
        self.offset = pygame.Vector2(0, 0)
        self.shake_offset = pygame.Vector2(0, 0)

    def update(self, target_rect: pygame.Rect):
        cx = target_rect.centerx - self.screen_w // 2
        cy = target_rect.centery - self.screen_h // 2
        cx = max(self.world_rect.left, min(cx, self.world_rect.right - self.screen_w))
        cy = max(self.world_rect.top,  min(cy, self.world_rect.bottom - self.screen_h))
        self.offset.update(cx, cy)
        self.offset += self.shake_offset

    def apply_rect(self, rect: pygame.Rect) -> pygame.Rect:
        return rect.move(-int(self.offset.x), -int(self.offset.y))

    def apply_pos(self, pos: tuple[int,int]) -> tuple[int,int]:
        return (int(pos[0] - self.offset.x), int(pos[1] - self.offset.y))

    @property
    def view_rect(self) -> pygame.Rect:
        return pygame.Rect(int(self.offset.x), int(self.offset.y), self.screen_w, self.screen_h)


def camera_shake(camera, intensity=6):
    camera.shake_offset.update(
        random.randint(-intensity, intensity),
        random.randint(-intensity, intensity)
    )

def main():
    world = pygame.Rect(0, 0, WORLD_W, WORLD_H)
    camera = Camera(screen.get_size(), world)

    # player in the middle of world
    player = pygame.Rect(WORLD_W//2 - 16, WORLD_H//2 - 16, 32, 32)
    player_color = (240, 110, 80)

    # decorative world rectangles/grid
    rects = []
    for x in range(0, WORLD_W, 200):
        rects.append(pygame.Rect(x, 0, 4, WORLD_H))
    for y in range(0, WORLD_H, 200):
        rects.append(pygame.Rect(0, y, WORLD_W, 4))

    zoom = 1.0
    base_surf = pygame.Surface(screen.get_size()).convert_alpha()

    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    zoom = max(0.5, round(zoom - 0.1, 2))
                elif event.key == pygame.K_e:
                    zoom = min(2.0, round(zoom + 0.1, 2))

        keys = pygame.key.get_pressed()
        move = pygame.Vector2(0, 0)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            move.x -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            move.x += 1
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            move.y -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            move.y += 1
        if move.length_squared() > 0:
            move = move.normalize() * PLAYER_SPEED * dt
            player.x += int(move.x)
            player.y += int(move.y)
            player.clamp_ip(world)

        camera.update(player)
        
        if keys[pygame.K_SPACE]: camera_shake(camera, intensity=20)

        # draw world to base_surf
        base_surf.fill((25, 28, 35))
        # draw only objects visible in camera view
        view = camera.view_rect
        grid_color = (70, 120, 200)
        for r in rects:
            if r.colliderect(view):
                pygame.draw.rect(base_surf, grid_color, camera.apply_rect(r))

        pygame.draw.rect(base_surf, player_color, camera.apply_rect(player))

        # zoomed blit to screen
        if zoom != 1.0:
            zw = int(base_surf.get_width() * zoom)
            zh = int(base_surf.get_height() * zoom)
            scaled = pygame.transform.smoothscale(base_surf, (zw, zh))
            dst = scaled.get_rect(center=screen.get_rect().center)
            screen.fill((0, 0, 0))
            screen.blit(scaled, dst)
        else:
            screen.blit(base_surf, (0, 0))
        # simple HUD
        pygame.display.set_caption(f"Camera Demo | Zoom {zoom:.1f} | FPS {clock.get_fps():.1f}")
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()