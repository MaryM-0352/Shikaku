import dataclasses
from utils.mathUtils import get_divider_pairs


@dataclasses.dataclass
class Anchor:
    x: int
    y: int
    size: int


@dataclasses.dataclass
class Cell:
    is_occupied: bool


@dataclasses.dataclass
class Rectangle:
    x: int
    y: int
    width: int
    height: int


class SolvingGrid:
    def __init__(self, size: int, anchors: list[Anchor]):
        self.size: int = size
        self.matrix: list[Cell] = [Cell(False) for i in range(self.size * self.size)]
        for i in anchors:
            self.mark_occupied(i.x, i.y)

    def is_cell_occupied(self, x, y) -> bool:
        return self.matrix[y * self.size + x].is_occupied

    def mark_occupied(self, x, y) -> None:
        self.matrix[y * self.size + x].is_occupied = True

    def collide(self, rect: Rectangle) -> [tuple[int, int]]:
        ans = []
        for y in range(rect.height):
            for x in range(rect.width):
                if self.is_cell_occupied(rect.x + x, rect.y + y):
                    ans.append((rect.x + x, rect.y + y))
        return ans

    def is_rect_valid(self, rect: Rectangle) -> bool:

        return 0 <= rect.x < self.size and \
            0 <= rect.y < self.size and \
            0 <= rect.x + rect.width - 1 < self.size \
            and 0 <= rect.y + rect.height - 1 < self.size

    def print(self):
        ans = ""
        for i in range(len(self.matrix)):
            if i % self.size == 0:
                ans += f"\n"

            ans += f"{int(self.matrix[i].is_occupied)} "
        print(ans)


class AnchorVariantsResolver:
    def __init__(self, anchor: Anchor, grid: SolvingGrid):
        self.anchor = anchor
        self.grid = grid
        self.variants: list[Rectangle] = self.get_rectangle_variants()

    def get_rectangle_variants(self) -> [Rectangle]:
        size: int = self.anchor.size
        ans = []
        for width, height in get_divider_pairs(size):
            for start_x in range(self.anchor.x - width + 1, self.anchor.x + 1):
                for start_y in range(self.anchor.y - height + 1, self.anchor.y + 1):
                    r = Rectangle(start_x, start_y, width, height)
                    if not self.grid.is_rect_valid(r):
                        continue
                    collide_entries: tuple[int, int] = self.grid.collide(r)
                    if len(collide_entries) == 1:
                        ans.append(r)
        return ans



