import time
from typing import Optional


class UpdaterStats:
    def __init__(self, target_fps: float):
        self._lastTime: Optional[float] = time.time()
        self._fps: float = 0
        self._delay_offset = 0

        self._target_fps = target_fps
        self._target_delay = 1 / target_fps

    def delta(self) -> float:
        current_time = time.time()
        delta = current_time - self._lastTime
        self._lastTime = current_time
        self._fps = 1 / delta

        if self._fps < self._target_fps:
            self._delay_offset -= 0.00005
        elif self._fps > self._target_fps:
            self._delay_offset += 0.00005

        return delta

    def get_target_fps(self) -> float:
        return self._target_fps

    def fps(self) -> float:
        return self._fps

    def delay(self) -> float:
        return self._target_delay + self._delay_offset

