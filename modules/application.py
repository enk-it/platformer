import asyncio
import curses

from modules.ApplicationState import ApplicationState
from modules.Connection import Connection
from modules.Render import render_one_frame
from modules.RenderStats import RenderStats
from modules.Utils import setup, read_message, get_event_model


class Application:
    def __init__(
            self,
            state: ApplicationState,
            render_stats: RenderStats,
            connection: Connection | None = None
    ):
        self.state = state
        self.render_stats = render_stats
        self.connection = connection

    def startup(self):
        # достать из кеша и настроек всё что можно, если не получается создать новое и запросить
        pass

    async def main(self, stdscr):
        await setup(curses, stdscr)

        await asyncio.gather(
            self.renderer(stdscr),
            self.keyboard_listener(stdscr),
            # self.event_polling()
        )

    async def on_key_pressed(self, key):
        self.state.last_key_pressed = key

    async def renderer(self, stdscr):
        while True:
            self.state.delta = self.render_stats.delta()
            self.state.fps = self.render_stats.fps()
            self.state.delay = self.render_stats.delay()

            render_one_frame(stdscr, self.state)
            await asyncio.sleep(self.render_stats.delay())

    async def keyboard_listener(self, stdscr):
        while True:
            key = stdscr.getch()

            if key != -1:
                await self.on_key_pressed(key)

            await asyncio.sleep(self.render_stats.delay())

    async def event_polling(self):
        while True:
            message = await read_message(self.connection)
            event = get_event_model(message)

            pass
