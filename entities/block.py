from pydantic import BaseModel
from typing import Literal


class Block(BaseModel):
    x: int
    y: int
    material: Literal['stone', 'air', 'wood']
