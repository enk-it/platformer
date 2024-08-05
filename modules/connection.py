from asyncio import StreamReader, StreamWriter
from asyncio import get_event_loop
import asyncio


class Connection:
    def __init__(
            self,
            host,
            port
    ):
        loop = get_event_loop()
        reader, writer = loop.run_until_complete(
            asyncio.open_connection(host, port))

        self._reader = reader
        self._writer = writer

    def get_reader(self) -> StreamReader:
        return self._reader

    def get_writer(self) -> StreamWriter:
        return self._writer

