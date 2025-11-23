# src/chess/square/service/service.py

"""
Module: chess.square.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from chess.board import Board, BoardService
from chess.coord import Coord, CoordService
from chess.system import BuildResult, IdentityService, Service
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
        *   coord_service (CoordService)
        *   identity_service (IdentityService)
    """
    SERVICE_NAME = "SquareService"
    
    _id: int
    _name: str
    _builder: SquareBuilder
    _validator: SquareValidator
    _coord_service: CoordService
    _identity_service: IdentityService


    def __init__(
            self,
            id: int,
            name: str = SERVICE_NAME,
            builder: SquareBuilder =  SquareBuilder(),
            validator: SquareValidator = SquareValidator(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
    ):
        super().__init__(id=id, name=name)
        self._builder= builder
        self._validator = validator
        self._coord_service = coord_service
        self._identity_service = identity_service
    
    @property
    def validator(self) -> SquareValidator:
        """
        SquareValidator is the single-source-of truth for
            1.  Certifying the safety of Square instances.
            2.  Verifying Piece-Square bindings.
        With those two responsibilities, it makes sense to directly expose SquareValidator.
        """
        return self._validator
    
    def build(
            self,
            id: int,
            name: str,
            coord: Coord,
            board: Board,
            coord_service: CoordService = CoordService(),
            board_service: BoardService = BoardService(),
            identity_service: IdentityService = IdentityService()
    ) -> BuildResult[Square]:
        """
        Builders have
            1.  A single responsibility.
            2.  Require external resources to create products.
        Those facts make Builders strong encapsulation targets.
        
        # Action:
        Delegate fabrication responsibility to builder. Pass coord_service and identity_service to
        builder.

        # Parameters:
            *   id (int):
            *   name (str):
            *   square (Coord):

        # Returns:
        BuildResult[Square] containing either:
            - On success: Square in the payload.
            - On failure: Exception.
        #
        Raises:
        None
        """
        method = "SquareService"
        try:
            build_result = self._builder.build(
                id=id,
                name=name,
                coord=coord,
                board=board,
                coord_service=coord_service,
                board_service=board_service,
                identity_service=identity_service
            )
            if build_result.is_failure():
                return BuildResult.failure(build_result.exception)
            
            return build_result
        except Exception as ex:
            return BuildResult.failure(
                SquareServiceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{SquareServiceException.DEFAULT_MESSAGE}"
                    )
                )
            )