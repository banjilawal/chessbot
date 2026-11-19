# src/randomize/email/randomize.py

"""
Module: randomize.email.randomize
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

import random
from typing import Optional

from randomize import RandomDomain, RandomSeparator


class RandomEmail:
    _random_domain: RandomDomain
    _random_separator: RandomSeparator
    
    def __init__(
            self,
            random_domain: Optional[RandomDomain] | None = None,
            random_separator: Optional[RandomSeparator] | None = None,
    ):
        self._random_domain = random_domain or RandomDomain()
        self._random_separator = random_separator or RandomSeparator()
    
    def execute(self, firstname: str, lastname: str) -> str:
        domain = "@" + self._random_domain.execute()
        separator = self._random_separator.execute()
        
        number = random.random() * 100
        if number < 70:
            return firstname + separator + lastname + domain
        return lastname + separator + firstname + domain