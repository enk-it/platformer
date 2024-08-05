from modules.Connection import Connection
from modules.RenderStats import RenderStats
from pydantic import BaseModel
import asyncio


async def setup(curses, stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)
    stdscr.timeout(1)
    curses.noecho()


async def send_request(connection: Connection, raw_request: BaseModel):
    writer = connection.get_writer()
    request = (raw_request.model_dump_json() + "\n").encode()
    writer.write(request)
    await writer.drain()


async def read_message(connection: Connection) -> str:

    reader = connection.get_reader()
    data = await reader.readline()
    message = data.decode().strip()
    return message


def get_event_model(data: str):
    return adaptor.validate_json(data)
