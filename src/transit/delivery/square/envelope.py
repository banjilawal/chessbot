# src/transit/delivery/square/envelope.py

"""
Module: transit.delivery.square.envelope
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import Board, Coord, SquareState, Square, SquarePrimeExtract
from transit import HomeSquareCarrier, ProductEnvelope


class RootSquareEnvelope(ProductEnvelope[Square]):
    """
    Role
        -   Data Transfer

    Responsibilities:
        1.  Data from a RootSquareValidator forwarded to client validators.

    Attributes:
        id: int
        name: str
        board: Board
        coord: Coord
        state: SquareState
        prime_extract: SquarePrimeExtract

    Provides:

    Super Class:
        ProductEnvelopeTable
    """
    _id: int
    _name: str
    _board: Board
    _coord: Coord
    _state: SquareState

    def __init__(
            self,
            id: int,
            name: str,
            board: Board,
            coord: Coord,
            state: SquareState,
            prime_extract: SquarePrimeExtract,
    ):
        """
        Args:
            id: int
            name: str
            board: Board
            coord: Coord
            state: SquareState
            prime_extract: SquarePrimeExtract
        """
        super().__init__(prime_extract=prime_extract)
        self._id = id
        self._name = name
        self._board = board
        self._coord = coord
        self._state = state
    
    @property
    def prime_extract(self) -> SquarePrimeExtract:
        return cast(SquarePrimeExtract, super().prime_extract)
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def coord(self) -> Coord:
        return self._coord
    
    @property
    def state(self) -> SquareState:
        return self._state
    
    @property
    def for_home_square_consumer(self) -> bool:
        return isinstance(self._prime_extract.reference, HomeSquareCarrier)
    
    @property
    def for_public_square_consumer(self) -> bool:
        return self.for_home_square_consumer
    

