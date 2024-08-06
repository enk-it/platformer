import curses
import asyncio

from entities.game import Game
from entities.level import Level
from modules.application import Application
from modules.applicationState import ApplicationState
from modules.render import RenderEngine
from modules.updaterStats import UpdaterStats

from modules.data import settings
from modules.data import cached_level

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

# connection = Connection(
#     settings["host"],
#     settings["port"]
# )

app = Application(
    state,
    render_engine,
    render_updater,
    collision_updater
    # connection,
)

if __name__ == '__main__':
    asyncio.run(
        app.main()
    )
