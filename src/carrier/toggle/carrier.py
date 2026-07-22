# src/toggle/toggle.py

"""
Module: toggle.toggle
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC

from carrier import EntityCarrierToggle
from toggle import Toggle


class ToggleCarrier(EntityCarrierToggle[Toggle], ABC):
    pass
        
        
