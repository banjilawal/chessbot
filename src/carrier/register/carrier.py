# src/carrier/register/carrier.py

"""
Module: carrier.register.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC

from carrier import EntityCarrier
from register import Register


class RegisterCarrier(EntityCarrier[Register], ABC):
    def __init__(self):
        super().__init__()





