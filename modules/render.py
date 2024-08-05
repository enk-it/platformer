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
            stdscr.addch(y, x, ord(char))


def render_one_frame(stdscr, state):
    stdscr.clear()

    render_top_bar(
        stdscr,
        # delta_time=state.delta,
        fps=state.fps,
        last_key_pressed=state.last_key_pressed,
        # current_time=str(time.time()),
    )

    stdscr.refresh()
