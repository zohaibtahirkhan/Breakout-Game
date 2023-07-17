from blocks import Block


class TopBlock(Block):
    def __init__(self):
        super().__init__()
        self.color('gold')
        self.points_given = 10
