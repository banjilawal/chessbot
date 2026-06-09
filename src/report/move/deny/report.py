# src/report/move/occupation/report.py

"""
Module: report.move.occupation.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass


from report import MoveOrder
from model import Square, Token


@dataclass
class MoveDenialReport(ABC, MoveOrder):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Details about why a token was denied permission to occupy a square.
        
    Attributes:
        origin: Square
        recipient: Token
        
    Provides:

    Super Class:
        MoveOrder
    """
