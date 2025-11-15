# chess/square/service.py

"""
Module: chess.square.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""
from typing import Any

from chess.coord import Coord, CoordService
from chess.piece import Piece
from chess.system import BuildResult, IdentityService, ValidationResult
from chess.square import Square, SquareBuilder, SquareValidator


class SquareService:
    """
    # ROLE: Service, Data Protraction

    # RESPONSIBILITIES:
    1.  Manages integrity lifecycle of Square objects.
    2.  Validate Piece-Square bindings.

    # PROVIDES:
        *   SquareBuilder
        *   SquareValidator
        *   CoordService
        *   PieceService
        *   IdentityService

    # ATTRIBUTES:
        *   square_builder (type[SquareBuilder]): produces safe Coord objects.
        *   square_validator (type[SquareValidator]): ensures existing Coord objects are safe.

        *   coord_service (type[CoordService): Manages integrity of the Square's coord attributes
        *   identity_service (type[IdentityService]): Manages integrity of Square's id and name attributes.
        *   piece_service (type[PieceService]): Tests Piece is actionable for in Piece-Square binding checks.
    """
    
    _square_validator: type[SquareBuilder]
    _square_validator: type[SquareValidator]
    _coord_service: type[CoordService]
    _identity_service: type[IdentityService]
    _piece_service: type[PieceService]
    
    def __init__(
            self,
            coord_builder: type[SquareBuilder]=SquareBuilder,
            square_validator: type[SquareValidator]=SquareValidator,
            coord_service: type[CoordService]=CoordService,
            piece_service: type[PieceService]=PieceService,
            identity_service: type[IdentityService]=IdentityService
    ):
        self._square_builder= coord_builder
        self._square_validator = square_validator
        self._coord_service = coord_service
        self._identity_service = identity_service
        self._piece_service = piece_service
    
    def validate_as_square(self, candidate: Any) -> ValidationResult[Square]:
        """
        # Action:
        CoordService directs square_validator to run the verification process on the candidate.

        # Parameters:
            *   row (int):
            *   column (int):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   square_validator sends any validation exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        return self._square_validator.validate(
            candidate=candidate,
            coord_service=self._coord_service,
            identity_service=self._identity_service
        )
    
    def build_square(self, id: int, name: str, coord: Coord) -> BuildResult[Square]:
        """
        # Action:
        CoordService directs square_builderto run the build process with the inputs.

        # Parameters:
            *   row (int):
            *   column (int):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in payload.
            - On failure: Exception.

        Raises:
            *   None are raised here
            *   square_buildersends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        return self._square_builder.build(
            id=id,
            name=name,
            coord=coord,
            identity_service=self._identity_service,
            coord_service=self._coord_service
        )
    
    def validate_piece_square_binding(self, coord: Coord, vector: Vector) -> BuildResult[(Square, Piece)]:
        """
        # Action:
        1.  square_validator runs integrity checks on the coord param.
        2.  identity_service runs integrity checks on the vector param.
        3.  If any checks raise an exception return it in the BuildResult.
        4.  If coord and vector params are valid:
                new_row, new_colum = coord.row + vector.y, coord.column + vector.x
        5.  Run build_square(new_row, new_column) to ensure the computed values produce a safe Coord instance.

        # Parameters:
            *   coord(Coord):
            *   vector (Vector):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   Any validation exceptions that occur are sent to the caller by either
                    square_validator
                    identity_service
            *   square_buildersends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "CoordService.add_vector_to_coord"
        
        try:
            coord_validation = self._square_validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            vector_validation = self._identity_service.validate_as_vector(candidate=vector)
            if vector_validation.is_failure():
                return BuildResult.failure(vector_validation.exception)
            
            column = coord.column + vector.x
            row = coord.row + vector.y
            
            return self._square_validator.build(row=row, column=column)
        except Exception as ex:
            return BuildResult.failure(ex)
    
    def dot_product(self, coord: Coord, vector: Vector) -> BuildResult[Square]:
        """
        # Action:
        1.  square_validator runs integrity checks on the coord param.
        2.  identity_service runs integrity checks on the vector param.
        3.  If any checks raise an exception return it in the BuildResult.
        4.  If coord and vector params are valid:
                new_row, new_colum = coord.row + vector.y, coord.column + vector.x
        5.  Run build_square(new_row, new_column) to ensure the computed values produce a safe Coord instance.

        # Parameters:
            *   coord(Coord):
            *   vector (Vector):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   Any validation exceptions that occur are sent to the caller by either
                    square_validator
                    identity_service
            *   square_buildersends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "CoordService.dot_product"
        
        try:
            coord_validation = self._square_validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            vector_validation = self._identity_service.validate_as_vector(candidate=vector)
            if vector_validation.is_failure():
                return BuildResult.failure(vector_validation.exception)
            
            column = coord.column * vector.y
            row = coord.row * vector.x
            
            return self._square_validator.build(row=row, column=column)
        except Exception as ex:
            return BuildResult.failure(ex)
    
    def multiply_coord_by_scalar(self, coord: Coord, scalar: Scalar) -> BuildResult[Square]:
        """
        # Action:
        1.  square_validator runs integrity checks on the coord param.
        2.  coord_service runs integrity checks on the scalar param.
        3.  If any checks raise an exception return it in the BuildResult.
        4.  If coord and scalar params are valid:
                new_row, new_colum = coord.row * scalar.value, coord.column * scalar.value
        5.  Run build_square(new_row, new_column) to ensure the computed values produce a safe Coord instance.

        # Parameters:
            *   coord (Coord):
            *   scalar (Scalar):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   Any validation exceptions that occur are sent to the caller by either
                    square_validator
                    coord_service
            *   square_buildersends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "CoordService.multiply_coord_by_scalar"
        
        try:
            coord_validation = self._square_validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            scalar_validation = self._coord_service.validate_as_scalar(candidate=scalar)
            if scalar_validation.is_failure():
                return BuildResult.failure(scalar_validation.exception)
            
            row = coord.y * scalar.value
            column = coord.x * scalar.value
            
            return self._square_validator.build(row=row, column=column)
        except Exception as ex:
            return BuildResult.failure(ex)
    
    def convert_vector_to_coord(self, vector: Vector) -> BuildResult[Square]:
        """
        # Action:
        1.  identity_service runs integrity checks on param.
        2.  If any checks raise an exception return it in the BuildResult.
        3.  Run build_square(row=y, column=y) to ensure the computed values produce a
            safe Coord instance.

        # Parameters:
            *   vector (Vector):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   identity_service sends any validation exceptions back to the caller.
            *   square_buildersends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "CoordService.convert_vector_to_coord"
        
        try:
            vector_validation = self._identity_service.validate_as_vector(candidate=vector)
            if vector_validation.is_failure():
                return BuildResult.failure(vector_validation.exception)
            
            return self._square_validator.build(row=vector.y, column=vector.x)
        except Exception as ex:
            return BuildResult.failure(ex)