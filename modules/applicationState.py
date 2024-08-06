from entities.game import Game


class ApplicationState:
    def __init__(self, game):
        self.delta = 0
        self.fps = 0
        self.delay = 0

        self.collision_delta = 0
        self.collision_fps = 0
        self.collision_delay = 0

        self.last_key_pressed = 0

        self.game: Game = game
        self.view_offset_x = 0
        self.view_offset_y = 0
        self.is_ready = False
