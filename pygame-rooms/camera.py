import random
import pygame


class Camera:
    def __init__(self, screen_size: tuple[int, int], world_rect: pygame.Rect):
        self.screen_w, self.screen_h = screen_size
        self.world_rect = world_rect
        self.offset = pygame.Vector2(0, 0)
        self.shake_offset = pygame.Vector2(0, 0)

    def update(self, target_rect: pygame.Rect):
        cx = target_rect.centerx - self.screen_w // 2
        cy = target_rect.centery - self.screen_h // 2
        cx = max(self.world_rect.left, min(cx, self.world_rect.right - self.screen_w))
        cy = max(self.world_rect.top, min(cy, self.world_rect.bottom - self.screen_h))
        self.offset.update(cx, cy)
        self.offset += self.shake_offset

    def apply_rect(self, rect: pygame.Rect) -> pygame.Rect:
        return rect.move(-int(self.offset.x), -int(self.offset.y))

    def apply_pos(self, pos: tuple[int, int]) -> tuple[int, int]:
        return (int(pos[0] - self.offset.x), int(pos[1] - self.offset.y))

    @property
    def view_rect(self) -> pygame.Rect:
        return pygame.Rect(int(self.offset.x), int(self.offset.y), self.screen_w, self.screen_h)


def camera_shake(camera: Camera, intensity=6):
    camera.shake_offset.update(
        random.randint(-intensity, intensity),
        random.randint(-intensity, intensity),
    )
