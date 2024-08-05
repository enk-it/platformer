class Player:
    def __init__(
            self,
            uid,
            name,
    ):
        self._uid = uid
        self._name = name
        self.pos_x = 0
        self.pos_y = -3

    def get_pos_y(self):
        return round(self.pos_y)

    def get_pos_x(self):
        return int(self.pos_x)


class PlayerMe(Player):
    def __init__(self, uid, name):
        super().__init__(uid, name)
        self.velocity_y = 0
        self.is_on_ground = False

    def update(self):
        self.pos_y += self.velocity_y

        if (self.velocity_y < 0) or (not self.is_on_ground):
            self.velocity_y += 0.005

    def move_up(self):
        pass
        # self.pos_y -= 1

    def move_down(self):
        pass
        # self.pos_y += 1

    def move_left(self):
        self.pos_x -= 1

    def move_right(self):
        self.pos_x += 1

    def jump(self):
        if self.is_on_ground:
            self.velocity_y = -0.15
            # self.is_on_ground = False
