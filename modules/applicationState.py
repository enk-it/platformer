class ApplicationState:
    def __init__(self):
        self.delta = 0
        self.fps = 0
        self.delay = 0
        self.last_key_pressed = 0

        self.game = None
        self.is_ready = False
