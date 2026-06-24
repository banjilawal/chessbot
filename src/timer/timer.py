# src/timer/timer.py

"""
Module: timer.timer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


class CountdownTimer:
    _count_down_start: int
    _elapsed_time: int
    
    def __init__(self, count_down_start: int | None = 1000):
        self._count_down_start = count_down_start
        self._elapsed_time = 0
    
    @property
    def count_down_start(self) -> int:
        return self._count_down_start
    
    @property
    def elapsed_time(self) -> int:
        return self._elapsed_time
    
    @elapsed_time.setter
    def elapsed_time(self, elapsed_time: int):
        self._elapsed_time = elapsed_time