# src/chess/piece/context/service/service.py

"""
Module: chess.piece.context.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import Service, id_emitter
from chess.piece import PieceContext, PieceContextBuilder, PieceContextValidator

class PieceContextService(Service[PieceContext]):
    """
    # ROLE: Service, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single entry point for PieceContextBuilder and PieceContextValidator objects.
    2.  Passing its self._validator to the self._builder simplifies the Context lifecycle.
    3.  Protects Context from direct, unprotected access.
    4.  Public facing API.

    # PROVIDES:
        *   PieceContextValidator
        *   PieceContextBuilder

    # ATTRIBUTES:
        *   builder (PieceContextBuilder):
        *   validator (PieceContextValidator):
    """
    DEFAULT_NAME = "PieceContextService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: PieceContextBuilder = PieceContextBuilder(),
            validator: PieceContextValidator = PieceContextValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)