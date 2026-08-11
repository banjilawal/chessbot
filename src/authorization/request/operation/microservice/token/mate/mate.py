# src/logic/token/service/operation/mate/mate.py

"""
Module: logic.token.service.operation.mate.mate
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations

from typing import List

from model.state.token import CheckSquare, KingToken


class Checkmate:
    
    _king: KingToken
    _mates: List[CheckSquare]