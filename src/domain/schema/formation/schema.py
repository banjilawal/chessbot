# src/domain/schema/formation/schema.py

"""
Module: domain.schema.formation.schema
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations
from enum import Enum

from domain.model import Bishop, King, Knight, Pawn, Rank, Rook
from domain.schema import Persona
from config.setting import GameColor


class Formation(Enum):
    """
    Role:
        -   Configuration Table
        -   Metadata Set

    Responsibilities:
        1.  Supply parameters to Token builders and factories.
    
    Attributes:
        square_name: str
        color: GameColor
        designation: str
        roster_number: int
        rank: rank
        persona: Persona

    Super Class:
        Enum
    """
    def __new__(
            cls,
            square_name: str,
            color: GameColor,
            designation: str,
            roster_number: int,
            rank: Rank,
            persona: Persona,
    ):
        """
        Args:
            square_name: str
            color: GameColor
            designation: str
            roster_number: int
            persona: Persona
        """
        obj = object.__new__(cls)
        obj._square_name = square_name
        obj._color = color
        obj._designation = designation
        obj._roster_number = roster_number
        obj._rank = rank
        obj._persona = persona
        return obj
    
    BLACK_KING_CASTLE = ("A1", GameColor.BLACK, "BC1", 1, Rook, Persona.ROOK)
    BLACK_KING_KNIGHT = ("B1", GameColor.BLACK, "BN1", 2, Knight, Persona.KNIGHT)
    BLACK_KING_BISHOP = ("BB1", GameColor.BLACK, "C1", 3, Bishop, Persona.BISHOP)
    BLACK_KING = ("D1", GameColor.BLACK, "BK", 4, King, Persona.KING)
    BLACK_QUEEN = ("E1", GameColor.BLACK, "BQ", 5, Persona.QUEEN)
    BLACK_QUEEN_BISHOP = ("F1", GameColor.BLACK, "BB2", 6, Bishop, Persona.BISHOP)
    BLACK_QUEEN_KNIGHT = ("G1", GameColor.BLACK, "BN2", 7, Knight, Persona.KNIGHT)
    BLACK_QUEEN_CASTLE = ("H1", GameColor.BLACK, "BC2", 8, Rook, Persona.ROOK)
    
    BLACK_PAWN_1 = ("A2", GameColor.BLACK, "BP1", 9, Pawn, Persona.PAWN)
    BLACK_PAWN_2 = ("B2", GameColor.BLACK, "BP2", 10, Pawn, Persona.PAWN)
    BLACK_PAWN_3 = ("C2", GameColor.BLACK, "BP3", 11, Pawn, Persona.PAWN)
    BLACK_PAWN_4 = ("D2", GameColor.BLACK, "BP4", 12, Pawn, Persona.PAWN)
    BLACK_PAWN_5 = ("E2",  GameColor.BLACK, "BP5", 13, Pawn, Persona.PAWN)
    BLACK_PAWN_6 = ("F2", GameColor.BLACK, "BP6", 14, Pawn, Persona.PAWN)
    BLACK_PAWN_7 = ("G2", GameColor.BLACK, "BP8", 15, Pawn, Persona.PAWN)
    BLACK_PAWN_8 = ("H2", GameColor.BLACK, "BP8", 16, Pawn, Persona.PAWN)
    
    WHITE_KING_CASTLE = ("A8", GameColor.WHITE, "WC1", 1, Rook, Persona.ROOK)
    WHITE_KING_KNIGHT = ("B8", GameColor.WHITE, "WN1", 2, Knight, Persona.KNIGHT)
    WHITE_KING_BISHOP = ("C8", GameColor.WHITE, "WB1", 3, Bishop, Persona.BISHOP)
    WHITE_KING = ("D8", GameColor.WHITE, "WK", 4, King, Persona.KING)
    WHITE_QUEEN = ("E8", GameColor.WHITE, "WQ", 5, Persona.QUEEN)
    WHITE_QUEEN_BISHOP = ("F8", GameColor.WHITE, "WB2", 6, Bishop, Persona.BISHOP)
    WHITE_QUEEN_KNIGHT = ("G8", GameColor.WHITE, "WN2", 7, Knight, Persona.KNIGHT)
    WHITE_QUEEN_CASTLE = ("H8", GameColor.WHITE, "WC2", 8, Rook, Persona.ROOK)
    
    WHITE_PAWN_1 = ("A7", GameColor.WHITE, "WP1", 9, Pawn, Persona.PAWN)
    WHITE_PAWN_2 = ("B7", GameColor.WHITE, "WP2", 10, Pawn, Persona.PAWN)
    WHITE_PAWN_3 = ("C7", GameColor.WHITE, "WP3", 11, Pawn, Persona.PAWN)
    WHITE_PAWN_4 = ("D7", GameColor.WHITE, "WP4", 12, Pawn, Persona.PAWN)
    WHITE_PAWN_5 = ("E7", GameColor.WHITE, "WP5", 13, Pawn, Persona.PAWN)
    WHITE_PAWN_6 = ("F7", GameColor.WHITE, "WP6", 14, Pawn, Persona.PAWN)
    WHITE_PAWN_7 = ("G7", GameColor.WHITE, "WP7", 15, Pawn, Persona.PAWN)
    WHITE_PAWN_8 = ("H7", GameColor.WHITE, "WP8", 16, Pawn, Persona.PAWN)
    
    @property
    def designation(self) -> str:
        """Common chess archetype of the Token."""
        return self._designation
    
    @property
    def color(self) -> GameColor:
        """Matches the Team's color"""
        return self._color
    
    @property
    def home_square_name(self) -> str:
        """Name of the Square a piece makes its opening move from."""
        return self._square_name
    
    @property
    def persona(self) -> Persona:
        """Configuration entry for the Token's rank."""
        return self._persona
    
    @property
    def rank(self) -> Rank:
        return self._rank
    
    @property
    def roster_number(self) -> int:
        """Number assigned to the Token by its Team"""
        return self._roster_number