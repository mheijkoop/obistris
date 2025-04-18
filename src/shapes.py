

class ObisTrisShape:
    width: int
    height: int
    shape: list[list[int]]
    x: int
    y: int

    def __init__(self):
        self.x = 0
        self.y = 0

    # this is not correct, that's okay for now TODO fix rotating when at edge of field
    def rotate(self):
        # absolutely stole this one-liner, not gonna lie
        self.shape = list(zip(*self.shape[::-1]))

        # clever variable swapping? no.. okay
        height = self.height
        self.height = self.width
        self.width = height


class ObisTrisHero(ObisTrisShape):

    def __init__(self):
        self.width = 1
        self.height = 4
        self.shape = [[1], [1], [1], [1]]
        ObisTrisShape.__init__(self)


class ObisTrisOrangeRicky(ObisTrisShape):

    def __init__(self):
        self.width = 2
        self.height = 3
        self.shape = [[1, 0], [1, 0], [1, 1]]
        ObisTrisShape.__init__(self)


class ObisTrisBlueRicky(ObisTrisShape):

    def __init__(self):
        self.width = 2
        self.height = 3
        self.shape = [[0, 1], [0, 1], [1, 1]]
        ObisTrisShape.__init__(self)

class ObisTrisSmashboy(ObisTrisShape):

    def __init__(self):
        self.width = 2
        self.height = 2
        self.shape = [[1, 1], [1, 1]]
        ObisTrisShape.__init__(self)

class ObisTrisCleveland(ObisTrisShape):

    def __init__(self):
        self.width = 2
        self.height = 3
        self.shape = [[0, 1], [1, 1], [1,0]]
        ObisTrisShape.__init__(self)

class ObisTrisRhodeIsland(ObisTrisShape):

    def __init__(self):
        self.width = 2
        self.height = 3
        self.shape = [[1, 0], [1, 1], [0,1]]
        ObisTrisShape.__init__(self)

class ObisTrisTeeWee(ObisTrisShape):

    def __init__(self):
        self.width = 3
        self.height = 2
        self.shape = [[0, 1, 0], [1, 1, 1]]
        ObisTrisShape.__init__(self)
