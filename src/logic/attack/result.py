# src/logic/attack/result.py

"""
Module: logic.attack.result
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

from logic.hostage import Hostage
from logic.occupation.result import OccupationResult
from logic.system.result import Result


class AttackResult(Result[Hostage, OccupationResult]):
    pass