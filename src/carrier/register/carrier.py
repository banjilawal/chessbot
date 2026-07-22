# src/carrier/register/operand.py

"""
Module: carrier.register.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC

from carrier import EntityCarrierToggle
from register import Register


class RegisterCarrier(EntityCarrierToggle[Register], ABC):
    def __init__(self):
        super().__init__()





