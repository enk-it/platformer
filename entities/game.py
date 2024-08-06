from entities.player import Player

from entities.player import PlayerMe


class Game:
    def __init__(self, level):
        self.level = level
        self.me: PlayerMe | None = None
        self.players: list[Player] = []

    def check_me_ways(self):
        x = self.me.get_pos_x()
        y = self.me.get_pos_y()

        self.check_me_on_ground(x, y)
        self.check_can_go_right(x, y)
        self.check_can_go_left(x, y)

    def check_me_on_ground(self, x, y):
        if len(self.level.blocks) <= y or y < 0:
            self.me.is_on_ground = False
            return
        if len(self.level.blocks[y]) <= x or x < 0:
            self.me.is_on_ground = False
            return

        if self.level.blocks[y + 1][x].material != "air":
            self.me.is_on_ground = True
            self.me.velocity_y = 0
        else:
            self.me.is_on_ground = False

    def check_can_go_right(self, x, y):
        if self.level.blocks[y][x + 1].material == "air":
            self.me.can_go_right = True
        else:
            self.me.can_go_right = False

    def check_can_go_left(self, x, y):
        if self.level.blocks[y][x - 1].material == "air":
            self.me.can_go_left = True
        else:
            self.me.can_go_left = False

    def add_player(self, player: Player):
        pass

    def remove_player(self, player_id):
        pass

    def set_me(self, me: Player):
        pass

    def set_level(self, chunks):
        pass
