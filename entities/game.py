from entities.player import Player


class Game:
    def __init__(self):
        self.level = None
        self.me: Player | None = None
        self.players: list[Player] = []

    def add_player(self, player: Player):
        pass

    def remove_player(self, player_id):
        pass

    def set_me(self, me: Player):
        pass

    def set_level(self, chunks):
        pass

