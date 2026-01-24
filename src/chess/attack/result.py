# src/chess/attack/result.py

"""
Module: chess.attack.result
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

from chess.hostage import HostageManifest
from chess.occupation.result import OccupationResult
from chess.system.result import Result


class AttackResult(Result[HostageManifest, OccupationResult]):
    pass