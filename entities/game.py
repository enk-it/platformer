from entities.player import Player

from entities.player import PlayerMe
from schemas.responses import UserResponse


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
        self.check_can_go_up(x, y)

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
            self.me.pos_y = self.me.get_pos_y()
        else:
            self.me.is_on_ground = False

    def check_can_go_right(self, x, y):
        if len(self.level.blocks[y]) > x + 1 and self.level.blocks[y][x + 1].material == "air":
            self.me.can_go_right = True
        else:
            self.me.can_go_right = False

    def check_can_go_left(self, x, y):
        if x - 1 >= 0 and self.level.blocks[y][x - 1].material == "air":
            self.me.can_go_left = True
        else:
            self.me.can_go_left = False

    def check_can_go_up(self, x, y):
        if y < 0 or self.level.blocks[y - 1][x].material != "air":
            if self.me.velocity_y < 0:
                self.me.velocity_y = 0

    def set_players(self, players: list[Player]):
        self.players = players
        pass

    def add_player(self, player: Player):
        self.players.append(player)
        pass

    def remove_player(self, player_id):
        temp_player = None
        for player in self.players:
            if player.get_uid() == player_id:
                temp_player = player
                break
        if temp_player is not None:
            self.players.remove(temp_player)

    def update_player_position(self, uid: str, x: int, y: int):
        for player in self.players:
            if player.get_uid() == uid:
                player.pos_x = x
                player.pos_y = y
                break
