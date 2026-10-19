# src/transit/route/validation/rank.py

"""
Module: transit.route.validation.rank
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Rank
from err import (
    RankValidationRouteMissingException, RankValidationRouterException, RootRankEnvelopeNullException
)
from transit import RootRankEnvelope, RankCarrier, ValidationRouter
from util import LoggingLevelRouter


class RankValidationRouter(ValidationRouter[Rank]):
    """
    Role
        - Router

    Responsibilities:
        1.  Route a RootRankEnvelope to its appropriate Consumer
            by Carrier type.

    Attributes:
        bishop_consumer: BishopEnvelopeConsumer
        king_consumer: KingEnvelopeConsumer
        knight_consumer: KnightEnvelopeConsumer
        pawn_consumer: PawnEnvelopeConsumer
        queen_consumer: QueenEnvelopeConsumer
        rook_consumer: RookEnvelopeConsumer

    Provides:
        -   def execute(envelope: RootRankEnvelope) -> ValidationResult[RankCarrier]

    Super Class:
        ValidationRouter
    """
    
    _bishop_consumer: BishopEnvelopeConsumer
    _king_consumer: KingEnvelopeConsumer
    _knight_consumer: KnightEnvelopeConsumer
    _pawn_consumer: PawnEnvelopeConsumer
    _queen_consumer: QueenEnvelopeConsumer
    _rook_consumer: RookEnvelopeConsumer
    
    def __init__(
            self,
            bishop_consumer: Optional[BishopEnvelopeConsumer] | None = None,
            king_consumer: Optional[KingEnvelopeConsumer] | None = None,
            knight_consumer: Optional[KnightEnvelopeConsumer] | None = None,
            pawn_consumer: Optional[PawnEnvelopeConsumer] | None = None,
            queen_consumer: Optional[QueenEnvelopeConsumer] | None = None,
            rook_consumer: Optional[RookEnvelopeConsumer] | None = None,
    ):
        """
        Args:
            bishop_consumer: Optional[BishopEnvelopeConsumer]
            king_consumer: Optional[KingEnvelopeConsumer]
            knight_consumer: Optional[KnightEnvelopeConsumer]
            pawn_consumer: Optional[PawnEnvelopeConsumer]
            queen_consumer: Optional[QueenEnvelopeConsumer]
            rook_consumer: Optional[RookEnvelopeConsumer]
        """
        super().__init__()
        self._bishop_consumer = king_consumer or BishopEnvelopeConsumer()
        self._king_consumer = king_consumer or KingEnvelopeConsumer()
        self._knight_consumer = knight_consumer or KnightEnvelopeConsumer()
        self._pawn_consumer = pawn_consumer or PawnEnvelopeConsumer()
        self._queen_consumer = king_consumer or QueenEnvelopeConsumer()
        self._rook_consumer = pawn_consumer or RookEnvelopeConsumer()
    
    @LoggingLevelRouter.monitor
    def execute(self, envelope: RootRankEnvelope) -> ValidationResult[RankCarrier]:
        """
        Assure a candidate is a safe RankCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of
                the following occur:
                    -   The router cannot be primed.
                    -   The endpoint cannot consume the envelope.
                    -   No consumption route exists
            2.  Otherwise, cast the payload and send in the success result.
        Args:
            envelope: RootRankEnvelope
        Returns:
            ValidationResult[RankCarrier]
        Raises:
           RankValidationRouterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the router cannot be primed.
        priming = self.toolkit.priming_validator.execute(
            candidate=envelope,
            target_model=RootRankEnvelope,
            null_exception=RootRankEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidationRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidationRouterException.MSG,
                    err_code=RankValidationRouterException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # Otherwise get the payload.
        safe = cast(RootRankEnvelope, priming.payload)
        
        # --- Route to the appropriate consumer. ---#
        result = ValidationResult.failure(
            RankValidationRouteMissingException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
            )
        )
        
        # Route to bishop_validation consumers.
        if safe.for_bishop_consumer:
            result = self._bishop_consumer.execute(envelope=safe)
        # Route to the king_rank_validation consumers
        if safe.for_king_consumer:
            result = self._king_consumer.execute(envelope=safe)
        # Route to the king_rank_validation consumers
        if safe.for_knight_consumer:
            result = self._knight_consumer.execute(envelope=safe)
        # Route to pawn_rank_validation consumers.
        if safe.for_pawn_consumer:
            result = self._pawn_consumer.execute(envelope=safe)
        # Route to the king_rank_validation consumers
        if safe.for_queen_consumer:
            result = self._queen_consumer.execute(envelope=safe)
        # Route to pawn_rank_validation consumers.
        if safe.for_rook_consumer:
            result = self._rook_consumer.execute(envelope=safe)

            
        # Handle the case that the envelope is not consumed.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidationRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidationRouterException.MSG,
                    err_code=RankValidationRouterException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Send the work product to client. ---#
        carrier = cast(RankCarrier, result.payload)
        return ValidationResult.success(carrier)
        




    