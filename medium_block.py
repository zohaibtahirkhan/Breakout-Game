from blocks import Block


class MediumBlock(Block):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.points_given = 2
