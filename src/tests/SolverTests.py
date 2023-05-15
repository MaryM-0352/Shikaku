import unittest
from ..models import Anchor,AnchorVariantsResolver,Rectangle,SolvingGrid


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ancs = [
            Anchor(0, 0, 2),
            Anchor(1, 0, 4),
            Anchor(1, 1, 3),
            Anchor(4, 1, 4),
            Anchor(0, 2, 4),
            Anchor(1, 3, 2),
            Anchor(2, 3, 2),
            Anchor(3, 3, 2),
            Anchor(1, 4, 2)
        ]
        grid = SolvingGrid(5, ancs)
        singles = []
        for i in ancs:
            solver = AnchorVariantsResolver(i, grid)
            solver.variants = solver.get_rectangle_variants()
            if len(solver.variants) == 1:
                singles.append(solver.anchor)


        self.assertEqual(singles, [ancs[0],ancs[1]])  # add assertion here


if __name__ == '__main__':
    unittest.main()
