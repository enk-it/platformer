class Player:
    def __init__(
            self,
            uid,
            name,
    ):
        self._uid = uid
        self._name = name
        self.pos_x = 5
        self.pos_y = 3

    def get_pos_y(self):
        return round(self.pos_y)

    def get_pos_x(self):
        return int(self.pos_x)


class PlayerMe(Player):
    def __init__(self, uid, name):
        super().__init__(uid, name)
        self.velocity_y = 0
        self.is_on_ground = False
        self.can_go_right = True
        self.can_go_left = True
        self.can_go_up = True

    def update(self, time_mult):

        self.pos_y += self.velocity_y * time_mult

        if (self.velocity_y < 0) or (not self.is_on_ground):
            self.velocity_y += 0.0025 * time_mult

    def move_left(self):
        if self.can_go_left:
            self.pos_x -= 1

    def move_right(self):
        if self.can_go_right:
            self.pos_x += 1

    def jump(self):
        if self.is_on_ground:
            self.velocity_y = -0.15
            # self.is_on_ground = False
