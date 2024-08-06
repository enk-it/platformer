import asyncio
import curses

from entities.player import PlayerMe
from modules.applicationState import ApplicationState
from modules.connection import Connection
from modules.render import render_one_frame
from modules.updaterStats import UpdaterStats
from modules.utils import setup, read_message, get_event_model


class Application:
    def __init__(
            self,
            state: ApplicationState,
            render_stats: UpdaterStats,
            collision_stats: UpdaterStats,
            connection: Connection | None = None
    ):
        self.state: ApplicationState = state
        self.render_stats: UpdaterStats = render_stats
        self.collision_stats: UpdaterStats = collision_stats
        self.connection: Connection | None = connection

        self.startup()

    def startup(self):
        self.state.game.me = PlayerMe("asd", "Vovan")
        # достать из кеша и настроек всё что можно, если не получается создать новое и запросить
        pass

    async def main(self, stdscr):
        await setup(curses, stdscr)

        await asyncio.gather(
            self._collision(),
            self._update(stdscr),
            self._keyboard_listener(stdscr),
            # self.event_polling()
        )

    async def on_key_pressed(self, key):
        self.state.last_key_pressed = key

        if key == ord('d'):
            self.state.game.me.move_right()
        if key == ord('a'):
            self.state.game.me.move_left()
        if key == ord(' '):
            self.state.game.me.jump()

    async def _collision(self):
        while True:
            self.state.collision_delta = self.collision_stats.delta()
            self.state.collision_fps = self.collision_stats.fps()
            self.state.collision_delay = self.collision_stats.delay()

            target_fps = self.collision_stats.get_target_fps()

            mult = target_fps / self.state.collision_fps

            self.state.game.me.update(mult)
            self.state.game.check_me_ways()

            await asyncio.sleep(self.collision_stats.delay())

    async def _update(self, stdscr):
        while True:
            self.state.delta = self.render_stats.delta()
            self.state.fps = self.render_stats.fps()
            self.state.delay = self.render_stats.delay()

            render_one_frame(stdscr, self.state)
            await asyncio.sleep(self.render_stats.delay())

    async def _keyboard_listener(self, stdscr):
        while True:
            key = stdscr.getch()

            if key != -1:
                await self.on_key_pressed(key)

            await asyncio.sleep(self.collision_stats.delay())

    async def event_polling(self):
        while True:
            message = await read_message(self.connection)
            event = get_event_model(message)

            pass
