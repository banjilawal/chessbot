# src/randomize/account/machine/randomize/account.py

"""
Module: randomize.account.machine.randomize
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

import random
import string
from typing import List


class RandomMachineName:
    _letters: List[str]
    _numerics: List[str]
    
    def __init__(self):
        self._letters = [c for c in string.ascii_lowercase if c not in {'i', 'l', 'o'}]
        self._numerics = [str(n) for n in range(2, 10)]
        
    def execute(self) -> str:
        prefix = random.choices(self._letters, k=3)
        suffix = random.choices(self._numerics, k=3)
        
        return f"{''.join(prefix)}-{''.join(suffix)}".upper()