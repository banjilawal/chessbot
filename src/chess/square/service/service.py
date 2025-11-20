# src/chess/square/service.py

"""
Module: chess.square.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""


from chess.coord import Coord, CoordService
from chess.system import BuildResult, IdentityService, Service
from chess.square import Square, SquareBuilder, SquareValidator


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
        *   coord_service (CoordService)
        *   identity_service (IdentityService)
    """
    SERVICE_NAME = "SquareService"
    
    _builder: type[SquareBuilder]
    _validator: type[SquareValidator]
    
    _coord_service: CoordService
    _identity_service: IdentityService

    
    def __init__(
            self,
            id: int,
            name: str = SERVICE_NAME,
            builder: type[SquareBuilder] = SquareBuilder,
            validator: type[SquareValidator] = SquareValidator,
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
    ):
        super().__init__(id=id, name=name)
        self._builder= builder
        self._validator = validator
        
        self._coord_service = coord_service
        self._identity_service = identity_service

    
    def validator(self) -> type[SquareValidator]:
        """
        # Action:
        CoordService directs validator to run the verification process on the candidate.

        # Parameters:
            *   row (int):
            *   column (int):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
        None
        """
        return self._validator
    
    def build_square(self, id: int, name: str, coord: Coord) -> BuildResult[Square]:
        """
        # Action:
        Use builder, coord_service and identity_service to build a new Square object.

        # Parameters:
            *   id (int):
            *   name (str):
            *   coord (Coord):

        # Returns:
        BuildResult[Square] containing either:
            - On success: Square in the payload.
            - On failure: Exception.

        Raises:
        None
        """
        return self._builder.build(
            id=id,
            name=name,
            coord=coord,
            identity_service=self._identity_service,
            coord_service=self._coord_service
        )
            