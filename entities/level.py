from typing import Dict

from chunk import Chunk


class Level:
    def __init__(self):
        self.chunks: Dict[int, Dict[int, Chunk]] = {}

    def add_chunk(self, chunk: Chunk):
        self.chunks[chunk.x][chunk.y] = chunk
