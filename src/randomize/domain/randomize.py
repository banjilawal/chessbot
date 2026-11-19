# src/randomize/domain/randomize.py

"""
Module: randomize.domain.randomize
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

import random
from typing import List


class RandomDomain:
  _names: List[str] = []
  
  def __init__(self):
   self._names = [
     "gmail.com", "outlook.com", "yahoo.com", "yepmail.com", "math.org", "metrostate.edu", "ntp.org",
     "kerberos.org", "lopht.org", "kernel.org", "mail.tv", "lodoss.net",
   ]

  def execute(self) -> str:
    return random.choice(self._names)
