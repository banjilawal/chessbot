# src/chess/piece/service/service.py

"""
Module: chess.piece.service.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""
from typing import cast

from chess.system import EntityService, id_emitter
from chess.piece import Piece, PieceFactory, PieceValidator


class PieceService(EntityService[Piece]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Piece microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Piece state by providing single entry and exit points to Piece
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
        *   builder:    -> PieceFactory
        *   validator:  -> PieceValidator

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    DEFAULT_NAME = "PieceService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: PieceFactory = PieceFactory(),
            validator: PieceValidator = PieceValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (PieceFactory)
            *   validator (PieceValidator)

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> PieceFactory:
        """get PieceFactory"""
        return cast(PieceFactory, self.entity_builder)
    
    @property
    def validator(self) -> PieceValidator:
        """get PieceValidator"""
        return cast(PieceValidator, self.entity_validator)
    
