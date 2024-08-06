from entities.level import Level

BASE_OFFSET_X = 10
BASE_OFFSET_Y = 10


def add_char_wrapper(stdscr, x, y, char):
    height, width = stdscr.getmaxyx()

    if x < 0 or y < 0 or x > width - 1 or y > height - 1:
        return

    stdscr.addch(y, x, char)


def render_top_bar(stdscr, *args, **kwargs):
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
            add_char_wrapper(stdscr, x, y, ord(char))


def render_terrain(stdscr, state):
    rendered_level = state.game.level.render()

    for y, row in enumerate(rendered_level):
        for x, char in enumerate(row):
            # stdscr.addch(y + BASE_OFFSET_Y, x + BASE_OFFSET_X, ord(char))
            add_char_wrapper(stdscr, x + BASE_OFFSET_X, y + BASE_OFFSET_Y,
                             ord(char))


def render_players(stdscr, state):
    x = state.game.me.get_pos_x()
    y = state.game.me.get_pos_y()
    add_char_wrapper(stdscr, x + BASE_OFFSET_X, y + BASE_OFFSET_Y, ord('i'))
    # stdscr.addch(y + BASE_OFFSET_Y, x + BASE_OFFSET_X, ord('K'))


def render_one_frame(stdscr, state):
    stdscr.clear()

    x = state.game.me.get_pos_x()
    y = state.game.me.get_pos_y()

    render_top_bar(
        stdscr,
        # delta_time=state.delta,
        fps=state.fps,
        collision_fps=state.collision_fps,
        last_key_pressed=state.last_key_pressed,
        player_pos_y=state.game.me.get_pos_y(),
        player_pos_raw_y=state.game.me.pos_y,
        player_pos_x=state.game.me.get_pos_x(),
        on_ground=state.game.me.is_on_ground,
        materail_under_me=state.game.level.blocks[y + 1][x].material
        # current_time=str(time.time()),
    )

    render_terrain(
        stdscr,
        state
    )

    render_players(
        stdscr,
        state
    )

    stdscr.refresh()
