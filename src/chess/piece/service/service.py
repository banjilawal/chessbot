# src/chess/piece/service/service.py

"""
Module: chess.piece.service.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import IntegrityService, id_emitter
from chess.piece import Piece, PieceFactory, PieceValidator

class PieceIntegrityService(IntegrityService[Piece]):
    """
    # ROLE: IntegrityService, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Protects Piece instance's internal state.
    3.  Masks implementation details and business logic making features easier to use.
    4.  Single entry point for managing Piece lifecycles with PieceBuilder and PieceValidator.

    # PROVIDES:
        *   PieceBuilder
        *   PieceValidator
        *   PieceSchema

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   builder (PieceBuilder)
        *   validator (PieceValidator)
    """
    SERVICE_NAME = "PieceIntegrityService"
    
    _id: int
    _name: str
    _item_builder: PieceFactory
    _item_validator: PieceValidator
    
    def __init__(
            self,
            id: int = id_emitter.service_id,
            name: str = SERVICE_NAME,
            builder: PieceFactory = PieceFactory(),
            validator: PieceValidator = PieceValidator(),
    ):
        """
        # Action
        1.  Use id_emitter to automatically generate a unique id for each PieceIntegrityService instance.
        2.  Automatic dependency injection by providing working default instances of each attribute.
        """
        method = "PieceIntegrityService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    
