import asyncio
import curses
import logging
from uuid import uuid4
from entities.player import PlayerMe, Player
from modules.applicationState import ApplicationState
from modules.connection import Connection
from modules.render import RenderEngine
from modules.updaterStats import UpdaterStats
from modules.utils import setup, read_message, get_response_model
from schemas.requests import ConnectRequest, PositionUpdateRequest
from schemas.responses import UserPositionUpdated, CurrentUsers, UserConnected, UserDisconnected


class Application:
    def __init__(
            self,
            state: ApplicationState,
            render_engine: RenderEngine,
            render_stats: UpdaterStats,
            collision_stats: UpdaterStats,
            position_broadcaster_updater: UpdaterStats,
            connection: Connection | None = None
    ):
        self.state: ApplicationState = state
        self.render_engine: RenderEngine = render_engine
        self.render_stats: UpdaterStats = render_stats
        self.collision_stats: UpdaterStats = collision_stats
        self.position_broadcaster_updater: UpdaterStats = position_broadcaster_updater
        self.connection: Connection | None = connection

        self.startup()

    def startup(self):
        self.state.game.me = PlayerMe(str(uuid4()))
        self.render_engine.setup()

    async def main(self):
        await self.connection.send_request(
            ConnectRequest(
                uid=self.state.game.me.get_uid(),
                x=self.state.game.me.get_pos_x(),
                y=self.state.game.me.get_pos_y(),
            )
        )

        await asyncio.gather(
            self._collision(),
            self._update(),
            self._keyboard_listener(),
            self.position_broadcasting(),
            self.event_polling()
        )

    async def on_key_pressed(self, key):
        self.state.last_key_pressed = key

        if key == ord('d'):
            self.state.game.me.move_right()
        if key == ord('a'):
            self.state.game.me.move_left()
        if key == ord('w'):
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

    async def _update(self):
        while True:
            self.state.delta = self.render_stats.delta()
            self.state.fps = self.render_stats.fps()
            self.state.delay = self.render_stats.delay()

            self.render_engine.render_frame()
            await asyncio.sleep(self.render_stats.delay())

    async def _keyboard_listener(self):
        while True:
            key = self.render_engine.stdscr.getch()

            if key != -1:
                await self.on_key_pressed(key)

            await asyncio.sleep(self.collision_stats.delay())

    async def event_polling(self):
        while True:
            message = await read_message(self.connection)
            event = get_response_model(message)
            if isinstance(event, UserPositionUpdated):
                self.state.game.update_player_position(
                    event.uid,
                    event.x,
                    event.y,
                )
            elif isinstance(event, CurrentUsers):
                temp_players = []
                for user in event.users:
                    temp_players.append(
                        Player(
                            user.uid
                        )
                    )
                self.state.game.set_players(temp_players)
            elif isinstance(event, UserConnected):
                temp_player = Player(
                    event.uid
                )
                temp_player.pos_x = event.x
                temp_player.pos_y = event.y
                self.state.game.add_player(
                    Player(
                        event.uid
                    )
                )
            elif isinstance(event, UserDisconnected):
                logging.info(event)
                self.state.game.remove_player(
                    event.uid
                )

    async def position_broadcasting(self):
        while True:
            pass
            await self.connection.send_request(
                PositionUpdateRequest(
                    x=self.state.game.me.get_pos_x(),
                    y=self.state.game.me.get_pos_y(),
                )
            )

            # logging.info(self.state.game.me.broadcast_position())

            await asyncio.sleep(self.position_broadcaster_updater.delay())
