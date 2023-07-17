from blocks import Block


class EasyBlock(Block):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.points_given = 1
