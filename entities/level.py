from typing import List

from entities.block import Block
from pydantic import BaseModel
from modules.data import settings


class Level(BaseModel):
    blocks: list[list[Block]]

    def render(self) -> list[str]:
        result = []
        for block_row in self.blocks:
            row = ""
            for block in block_row:
                row += settings["skin"][block.material]
            result.append(row)
        return result
