# src/chess/piece/service/service.py

"""
Module: chess.piece.service.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import Service
from chess.piece import Piece, PieceFactory, PieceValidator,

class PieceService(Service[Piece]):
    """
    # ROLE: Service, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single interface/entry point for Piece, PieceValidator and PieceBuilder.
    2.  Protects Piece objects from direct manipulation.
    3.  Extends behavior and functionality of Piece objects.
    4.  Public facing API for Piece modules.
  
    # PROVIDES:
        *   Piece building
        *   Piece validation

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   builder (PieceBuilder)
        *   validator (PieceValidator)
    """
    SERVICE_NAME = "PieceService"
    
    _id: int
    _name: str
    _builder: PieceFactory
    _validator: PieceValidator
    
    def __init__(
            self,
            id: int,
            name: str = SERVICE_NAME,
            builder: PieceFactory = PieceFactory(),
            validator: PieceValidator = PieceValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    
