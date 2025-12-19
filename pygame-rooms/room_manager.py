import pygame
from collections import deque
import game_map

# defaults kept consistent with previous layout
TILE = 280
ROOM_SIZE = 280


class RoomManager:
    DIRS = (("north", (0, -1)), ("south", (0, 1)), ("east", (1, 0)), ("west", (-1, 0)))

    def __init__(self, tile=TILE, room_size=ROOM_SIZE, world_w=3200, world_h=2400):
        self.tile = tile
        self.room_size = room_size
        self.world_w = world_w
        self.world_h = world_h
        self.room_rects: dict[str, pygame.Rect] = {}
        self.rects_for_grid = []
        self.positions = {}
        self.min_x = self.max_x = self.min_y = self.max_y = 0

    def bfs_place(self, start="hall"):
        pos = {}
        occupied = {}
        q = deque([start])
        pos[start] = (0, 0)
        occupied[(0, 0)] = start
        while q:
            room = q.popleft()
            rpos = pos[room]
            for d, vec in self.DIRS:
                nbr = game_map.ROOM_MAP.get(room, {}).get(d)
                if not nbr:
                    continue
                if nbr in pos:
                    continue
                dx, dy = vec
                candidate = (rpos[0] + dx, rpos[1] + dy)
                while candidate in occupied:
                    candidate = (candidate[0] + dx, candidate[1] + dy)
                pos[nbr] = candidate
                occupied[candidate] = nbr
                q.append(nbr)
        self.positions = pos
        xs = [p[0] for p in pos.values()]
        ys = [p[1] for p in pos.values()]
        self.min_x, self.max_x = min(xs), max(xs)
        self.min_y, self.max_y = min(ys), max(ys)
        return pos

    def compute_room_rects(self):
        if not self.positions:
            self.bfs_place("hall")
        cols = self.max_x - self.min_x + 1
        rows = self.max_y - self.min_y + 1
        map_w = cols * self.tile
        map_h = rows * self.tile
        offset_x = max(0, (self.world_w - map_w) // 2)
        offset_x -= offset_x % self.tile
        offset_y = max(0, (self.world_h - map_h) // 2)
        offset_y -= offset_y % self.tile

        self.room_rects.clear()
        for name, (gx, gy) in self.positions.items():
            rx = offset_x + (gx - self.min_x) * self.tile + (self.tile - self.room_size) // 2
            ry = offset_y + (gy - self.min_y) * self.tile + (self.tile - self.room_size) // 2
            self.room_rects[name] = pygame.Rect(rx, ry, self.room_size, self.room_size)

        self.rects_for_grid = []
        for x in range(0, self.world_w, self.tile):
            self.rects_for_grid.append(pygame.Rect(x, 0, 4, self.world_h))
        for y in range(0, self.world_h, self.tile):
            self.rects_for_grid.append(pygame.Rect(0, y, self.world_w, 4))

    def draw(self, base_surf: pygame.Surface, camera, font: pygame.font.Font):
        view = camera.view_rect
        GRID_COLOR = (70, 120, 200)
        ROOM_COLOR = (200, 200, 200)
        ROOM_BORDER = (100, 100, 100)
        ROOM_LABEL = (20, 20, 20)

        for r in self.rects_for_grid:
            if r.colliderect(view):
                pygame.draw.rect(base_surf, GRID_COLOR, camera.apply_rect(r))

        for name, r in self.room_rects.items():
            if r.colliderect(view):
                draw_r = camera.apply_rect(r)
                pygame.draw.rect(base_surf, ROOM_COLOR, draw_r, border_radius=6)
                pygame.draw.rect(base_surf, ROOM_BORDER, draw_r, 2, border_radius=6)
                label = game_map.ROOM_MAP.get(name, {}).get("name", name)
                txt = font.render(label, True, ROOM_LABEL)
                base_surf.blit(txt, (draw_r.x + 6, draw_r.y + 6))

    def room_center(self, name: str):
        r = self.room_rects.get(name)
        return (r.centerx, r.centery) if r else None

    def room_under_point(self, point: tuple[int, int]):
        for name, r in self.room_rects.items():
            if r.collidepoint(point):
                return name
        return None
