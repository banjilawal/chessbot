# src/chess/square/service/service.py

"""
Module: chess.square.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from chess.board import Board, BoardService
from chess.coord import Coord, CoordService
from chess.system import BuildResult, IdentityService, LoggingLevelRouter, Service, id_emitter
from chess.square import Square, SquareBuilder, SquareServiceException, SquareValidator



class SquareService(Service[Square]):
    """
    # ROLE: Service, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single interface/entry point for Square, SquareValidator and SquareBuilder objects.
    2.  Masks implementation details and business logic making features easier to use.
    3.  Protects Square objects from direct, unprotected access.
    4.  Public facing API.

    # PROVIDES:
        *   SquareBuilder
        *   SquareValidator

    # ATTRIBUTES:
        *   builder (type[SquareBuilder]):
        *   validator (type[SquareValidator]):
    """
    SERVICE_NAME = "SquareService"

    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: SquareBuilder =  SquareBuilder(),
            validator: SquareValidator = SquareValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)