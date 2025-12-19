import pygame

ENTITIES = []


class Entity:
    def __init__(self, rect: pygame.Rect, color=(255, 255, 255)):
        self.rect = rect
        self.color = color
        self.visible = True

    def update(self, dt: float):
        pass

    def draw(self, surface: pygame.Surface, camera):
        if not self.visible:
            return
        surface_rect = camera.apply_rect(self.rect)
        pygame.draw.rect(surface, self.color, surface_rect)


class Player(Entity):
    def __init__(self, rect: pygame.Rect, color=(240, 110, 80), speed=300):
        super().__init__(rect, color)
        self.speed = speed

    def update(self, dt: float):
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
            move = move.normalize() * self.speed * dt
            self.rect.x += int(move.x)
            self.rect.y += int(move.y)
