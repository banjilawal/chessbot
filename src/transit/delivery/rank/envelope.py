# src/transit/delivery/rank/envelope.py

"""
Module: transit.delivery.rank.envelope
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import Persona, Rank, RankPrimeExtract
from transit import ProductEnvelope


class RootRankEnvelope(ProductEnvelope[Rank]):
    """
    Role
        -   Data Transfer

    Responsibilities:
        1.  Data from a RootRankValidator forwarded to client validators.

    Attributes:
        personaL Persona
        prime_extract: RankPrimeExtract

    Provides:
        for_kill_rank_consumer: bool
        for_checkmate_rank_consumer: bool
        for_rank_warning_consumer: bool
        for_stalemate_rank_consumer: bool

    Super Class:
        ProductEnvelope
    """
    
    _persona: Persona
    
    def __init__(
            self,
            persona: Persona,
            prime_extract: RankPrimeExtract,
    ):
        """
            persona: Persona
            prime_extract: RankPrimeExtract
        """
        super().__init__(prime_extract=prime_extract)
        self._persona = persona

    @property
    def persona(self) -> Persona:
        return self._persona
        
    @property
    def prime_extract(self) -> RankPrimeExtract:
        return cast(RankPrimeExtract, super().prime_extract)
    
    @property
    def for_bishop_consumer(self) -> bool:
        return isinstance(self._prime_extract.reference, BishopCarrier)
    
    @property
    def for_king_consumer(self) -> bool:
        return isinstance(self._prime_extract.reference, KingCarrier)
    
    @property
    def for_knight_consumer(self) -> bool:
        return isinstance(self._prime_extract.reference, KnightCarrier)
    
    @property
    def for_pawn_consumer(self) -> bool:
        return isinstance(self._prime_extract.reference, PawnCarrier)
    
    @property
    def for_queen_consumer(self) -> bool:
        return isinstance(self._prime_extract.reference, QueenCarrier)
    
    @property
    def for_rook_consumer(self) -> bool:
        return isinstance(self._prime_extract.reference, RootCarrier)
    

    