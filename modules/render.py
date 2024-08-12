BASE_OFFSET_X = 10
BASE_OFFSET_Y = 10


class RenderEngine:
    def __init__(
            self,
            stdscr,
            curses,
            state
    ):
        self.stdscr = stdscr
        self.curses = curses
        self.state = state

    def setup(self):
        self.curses.curs_set(0)
        self.stdscr.keypad(True)
        self.stdscr.timeout(1)
        self.curses.noecho()

        self.curses.start_color() # при желании отключить

    def render_char(self, x, y, char):
        height, width = self.stdscr.getmaxyx()

        if x < 0 or y < 0 or x > width - 1 or y > height - 1:
            return

        self.stdscr.addch(y, x, char)

    def render_top_bar(self, *args, **kwargs):
        result = []

        for keyword in kwargs:
            value = kwargs[keyword]
            if isinstance(value, str):
                result.append(f"{keyword}: {value}")
            elif isinstance(value, int):
                result.append(f"{keyword}: {value}")
            elif isinstance(value, float):
                result.append(f"{keyword}: {round(value, 4)}")

        for y, line in enumerate(result):
            for x, char in enumerate(line):
                # stdscr.addch(y, x, ord(char))
                self.render_char(x, y, ord(char))

    def render_terrain(self):
        rendered_level = self.state.game.level.render()

        for y, row in enumerate(rendered_level):
            for x, char in enumerate(row):
                # stdscr.addch(y + BASE_OFFSET_Y, x + BASE_OFFSET_X, ord(char))
                self.render_char(x + BASE_OFFSET_X, y + BASE_OFFSET_Y,
                                 ord(char))

    def render_players(self):
        x = self.state.game.me.get_pos_x()
        y = self.state.game.me.get_pos_y()
        self.render_char(x + BASE_OFFSET_X, y + BASE_OFFSET_Y,
                         ord('i'))

        for player in self.state.game.players:
            x = player.get_pos_x()
            y = player.get_pos_y()
            self.render_char(x + BASE_OFFSET_X, y + BASE_OFFSET_Y,
                             ord('j'))
        # stdscr.addch(y + BASE_OFFSET_Y, x + BASE_OFFSET_X, ord('K'))

    def render_frame(self):
        self.stdscr.clear()

        x = self.state.game.me.get_pos_x()
        y = self.state.game.me.get_pos_y()

        self.render_top_bar(
            # delta_time=state.delta,
            fps=self.state.fps,
            collision_fps=self.state.collision_fps,
            last_key_pressed=self.state.last_key_pressed,
            player_pos_y=y,
            player_pos_raw_y=self.state.game.me.pos_y,
            player_pos_x=x,
            on_ground=self.state.game.me.is_on_ground,
            materail_under_me=self.state.game.level.blocks[y + 1][x].material
            # current_time=str(time.time()),
        )

        self.render_terrain()

        self.render_players()

        self.stdscr.refresh()
