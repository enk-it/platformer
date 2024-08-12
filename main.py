import curses
import asyncio

from entities.game import Game
from entities.level import Level
from modules.application import Application
from modules.applicationState import ApplicationState
from modules.connection import Connection
from modules.render import RenderEngine
from modules.updaterStats import UpdaterStats

from modules.data import settings
from modules.data import cached_level

import logging

logging.basicConfig(filename='myapp.log', level=logging.INFO)

event_loop = asyncio.get_event_loop()


stdscr = curses.initscr()
level = Level.model_validate(cached_level)
game = Game(level)
state = ApplicationState(game)
render_engine = RenderEngine(stdscr, curses, state)

render_updater = UpdaterStats(
    target_fps=settings["framerate"]
)

collision_updater = UpdaterStats(
    target_fps=250
)

position_broadcaster_updater = UpdaterStats(
    target_fps=20
)

connection = Connection(
    settings["host"],
    settings["port"]
)

app = Application(
    state,
    render_engine,
    render_updater,
    collision_updater,
    position_broadcaster_updater,
    connection,
)

if __name__ == '__main__':
    event_loop.run_until_complete(
        app.main()
    )

    # asyncio.run(
    #     app.main()
    # )
