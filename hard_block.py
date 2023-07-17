from blocks import Block


class HardBlock(Block):
    def __init__(self):
        super().__init__()
        self.color('cyan')
        self.points_given = 5
