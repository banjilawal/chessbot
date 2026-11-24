# src/randomize/account/separator/randomize/account.py

"""
Module: randomize.account.separator.randomize
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

import random
from typing import List


class RandomSeparator:
    _names: List[str] = []
    
    def __init__(self):
        self._names = ["", "-", "_", ".", ]
    
    def execute(self) -> str:
        return random.choice(self._names)