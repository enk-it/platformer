import curses
import asyncio

from entities.game import Game
from entities.level import Level
from modules.application import Application
from modules.applicationState import ApplicationState
from modules.connection import Connection
from modules.renderStats import RenderStats

from modules.data import settings
from modules.data import cached_level


state = ApplicationState()
state.game = Game()
state.game.level = Level.model_validate(cached_level)

render_stats = RenderStats(
    target_fps=settings["framerate"]
)

# connection = Connection(
#     settings["host"],
#     settings["port"]
# )

app = Application(
    state,
    render_stats,
    # connection,
)

if __name__ == '__main__':
    asyncio.run(curses.wrapper(app.main))
