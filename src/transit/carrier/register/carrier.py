# src/transit/carrier/register/carrier.py

"""
Module: transit.carrier.register.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from carrier import EntityCarrier
from transit.structure.register import Register


class RegisterCarrier(EntityCarrier[Register], ABC):
    def __init__(self):
        super().__init__()





