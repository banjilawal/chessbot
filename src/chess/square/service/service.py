# src/chess/square/service/service.py

"""
Module: chess.square.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""


from chess.coord import Coord, CoordService
from chess.system import BuildResult, IdentityService, Result, SearchResult, Service
from chess.square import (
    AddingDuplicateSquareException, RemovingNonExistentSquareException, Square, SquareBuilder,
    SquareServiceException, SquareValidator
)


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
    
    _squarest: []
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
        
        self._squares = []
    
    @property
    def validator(self) -> type[SquareValidator]:
        """
        SquareValidator is the single-source-of truth for
            1.  Certifying the safety of Square instances.
            2.  Verifying Piece-Square bindings.
        With those two responsibilities, it makes sense to directly expose SquareValidator.
        """
        return self._validator
    
    def build_square(self, id: int, name: str, coord: Coord) -> BuildResult[Square]:
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
    
    def add_square(self, square: Square) -> Result[Square]:
        method = "SquaredService.add_square"
        try:
            square_validation = self._validator.validate(candidate=square)
            if square_validation.is_failure():
               return Result.failure(square_validation.exception)
            
            if square in self._squares:
                return Result.failure(
                    AddingDuplicateSquareException(
                        f"{method}: {AddingDuplicateSquareException.DEFAULT_MESSAGE}"
                    )
                )
            
            self._squares.append(square)
            return Result.success(square)
        except Exception as ex:
            return Result.failure(
                SquareServiceException(
                    f"{method}: ex=ex, message={SquareServiceException.DEFAULT_MESSAGE}"
                )
            )
    
    def remove_square(self, square: Square) -> Result[Square]:
        method = "SquaredService.remove_square"
        try:
            square_validation = self._validator.validate(candidate=square)
            if square_validation.is_failure():
                return Result.failure(square_validation.exception)
            
            if square not in self._squares:
                return Result.failure(
                    RemovingNonExistentSquareException(
                        f"{method}: {RemovingNonExistentSquareException.DEFAULT_MESSAGE}"
                    )
                )
            
            self._squares.remove(square)
            return Result.success(square)
        except Exception as ex:
            return Result.failure(
                SquareServiceException(
                    f"{method}: ex=ex, message={SquareServiceException.DEFAULT_MESSAGE}"
                )
            )
        
    def find_by_square_by_coord(self, coord: Coord) -> SearchResult[[Square]]:
        method = "SquareService.find_square_by_coord"
        try:
            coord_validation = self._validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return SearchResult.failure(coord_validation.exception)
            
            matches = [square for square in self._squares if square.coord == coord]
            if len(matches) == 0:
            
                return SearchResult.empty()
            return SearchResult.success(payload=matches)
        except Exception as ex:
            return SearchResult.failure(
                SquareServiceException(
                    f"{method}: ex=ex, message={SquareServiceException.DEFAULT_MESSAGE}"
                )
            )
    
    def find_by_square_by_name(self, name: str) -> SearchResult[[Square]]:
        method = "SquareService.find_square_by_name"
        try:
            name_validation = self._identity_service.validate_name(candidate=name)
            if name_validation.is_failure():
                return SearchResult.failure(name_validation.exception)
            
            matches = [square for square in self._squares if square.name.upper() == name.upper()]
            if len(matches) == 0:
                return SearchResult.empty()
            return SearchResult.success(payload=matches)
        except Exception as ex:
            return SearchResult.failure(
                SquareServiceException(
                    f"{method}: ex=ex, message={SquareServiceException.DEFAULT_MESSAGE}"
                )
            )
    
    def find_by_square_by_id(self, id: int) -> SearchResult[[Square]]:
        method = "SquareService.find_square_by_id"
        try:
            id_validation = self._identity_service.validate_id(candidate=id)
            if id_validation.is_failure():
                return SearchResult.failure(id_validation.exception)
            
            matches = [square for square in self._squares if square.id == id]
            if len(matches) == 0:
                return SearchResult.empty()
            return SearchResult.success(payload=matches)
        except Exception as ex:
            return SearchResult.failure(
                SquareServiceException(
                    f"{method}: ex=ex, message={SquareServiceException.DEFAULT_MESSAGE}"
                )
            )