# src/randomize/firstname/randomize.py

"""
Module: randomize.firstname.randomize
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

import random
from typing import List


class RandomFirstname:
    _names: List[str] = []
    
    def __init__(self):
        self._names = [
            "Amani", "Kwame", "Zahara", "Tumelo", "Nala", "Wei", "Priya", "Haruto", "Mei", "Ravi",
            "Emma", "Luca", "Sophie", "Mateo", "Freya", "Santiago", "Olivia", "Ximena", "Elijah",
            "Camila", "Tane", "Hine", "Manaia", "Aroha", "Kauri", "Leila", "Amir", "Yara", "Omar",
            "Layla", "Arjun", "Aanya", "Kabir", "Diya", "Rohan", "Hao", "Yuki", "Min", "Jin", "Hana",
            "Aylen", "Dakota", "Kai", "Tala", "Mato", "Sofia", "Idris", "Zuri", "Kofi", "Anaya"
        ]
    
    def execute(self) -> str:
        return random.choice(self._names)