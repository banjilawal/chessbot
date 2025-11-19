# src/chess/system/identity/service.py

"""
Module: chess.system.identity.service
Author: Banji Lawal
Created: 2025-11-13
version: 1.0.0
"""

from typing import Any, cast

from chess.system import (
    IdValidator, InvalidIdentityParamException, NameValidator, ValidationResult, id_emitter,
    IdEmitter
)


class IdentityService:
    """
    # ROLE: Service, Validation, Data Integrity, ID Generation

    # RESPONSIBILITIES:
    1.  Issue IDs to new objects.
    2.  Manage integrity checks on IDs and names of existing objects.
    3.  Assure names are:
        *   Not null.
        *   Not white space only (" ", tab, newline).
        *   Not empty. (".", ".\n", ".\t", ".\r").
        *   Meet minimum length requirement specified in chess.syst.
        *   Meet maximum length requirement specified in class.

    # PROVIDES:
        *   IdEmitter
        *   IdValidator
        *   NameValidator


    # ATTRIBUTES:
        *   id_validator (type[IdValidator]):
        *   name_validator (type[NameValidator]):
        *   id_emitter (type[IdEmitter]):
    """
    _id_validator: type[IdValidator]
    _name_validator: type[NameValidator]
    
    
    def __init__(
            self,
            id_validator: type[IdValidator]=IdValidator,
            name_validator: type[NameValidator]=NameValidator
    ):
        """
        ACTION:
        Construct an IdentityService object.
        
        PARAMETERS:
            *   id_validator (type[IdValidator]):
            *   name_validator (type[NameValidator]):

        # Returns:
        None

        RAISES:
        None
        """
        method = "IdentityService.__init__"
        
        self._id_validator=id_validator
        self._name_validator=name_validator
        self._emit_id=id_emitter
        
    @property
    def id_emitter(self) -> IdEmitter:
        """
        # ACTION:
        Issue a unique ID to a new class instance. The ID is unique within the class.

        # PARAMETERS:
        None

        # Returns:
        int

        # Raises:
        None
        """
        method = "IdentityService.id_emitter"
        
        return IdEmitter
        
    def validate_id(self, candidate: Any) -> ValidationResult[int]:
        """
        # Action:
        IdentityService directs id_validator to run the ID verification process on the candidate.

        # Parameters:
            *   candidate(Any): object to validate as an ID

        # Returns:
        ValidationResult[int] containing either:
            - On success: int in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   id_validator sends any validation exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "IdentityService.validate_id"
        return self._id_validator.validate(candidate)
    
    def validate_name(self, candidate: Any) -> ValidationResult[str]:
        """
        # Action:
        IdentityService directs name_validator to run the name verification process on the candidate.

        # Parameters:
            *   candidate(Any): object to validate as name

        # Returns:
        ValidationResult[str] containing either:
            - On success: int in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   name_validator sends any validation exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "IdentityService.validate_name"
        return self._name_validator.validate(candidate)
    
    def validate_identity(
            self,
            id_candidate: Any,
            name_candidate: Any
    ) -> ValidationResult[(int, str)]:
        """
        # ACTION:
        1.  IdentityService directs id_validator verify the id_candidate.
        2.  name_validator verifies the name_candidate.
        3.  If any checks fail their exception is sent to the caller inside a ValidationResult.
        4.  On success
                *   cast name_candidate to a STRING.
                *   cast id_candidate to an INT.
                *   send the (id, name) tuple to the caller in a ValidationResult.

        # PARAMETERS:
            * id_candidate (Any): object to certify is a legal ID.
            * name_candidate (Any): object to certify is a legal name.

        # Returns:
        ValidationResult[Tuple(int, str)] containing either:
            - On success: Tuple(int, str) in the payload.
            - On failure: Exception.

        # Raises:
            *   InvalidIdentityParamException
        """
        method = "IdentityService.validate_identity"
        
        try:
            id_validation = self._id_validator.validate(id_candidate)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            id = cast(int, id_candidate)
            
            name_validation = self._name_validator.validate(name_candidate)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            
            name = cast(str, name_candidate)
            return ValidationResult.success(payload=(id, name))
        except Exception as ex:
            return ValidationResult.failure(
                InvalidIdentityParamException(
                    f"{method}: {InvalidIdentityParamException.DEFAULT_MESSAGE}"
                )
            )


"""
Module: chess.target.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from typing import Any

from chess.scalar import Scalar, ScalarService
from chess.vector import Vector, VectorService
from chess.system import BuildResult, ValidationResult
from chess.coord import Coord, CoordBuilder, CoordValidator


class CoordService:
    def validate_as_coord(self, candidate: Any) -> ValidationResult[Coord]:

        return self._coord_validator.validate(candidate=candidate)
    
    def build_coord(self, row: int, column: int) -> BuildResult[Coord]:
        """
        # Action:
        CoordService directs builder to run the build process with the inputs.

        # Parameters:
            *   row (int):
            *   column (int):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here
            *   builder sends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        return self._coord_builder.build(row=row, column=column)
    
    def add_vector_to_coord(self, coord: Coord, vector: Vector) -> BuildResult[Coord]:
        """
        # Action:
        1.  validator runs integrity checks on the target param.
        2.  vector_service runs integrity checks on the vector param.
        3.  If any checks raise an exception return it in the BuildResult.
        4.  If target and vector params are valid:
                new_row, new_colum = target.row + vector.y, target.column + vector.x
        5.  Run build_coord(new_row, new_column) to ensure the computed values produce a safe Coord instance.

        # Parameters:
            *   target(Coord):
            *   vector (Vector):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   Any validation exceptions that occur are sent to the caller by either
                    validator
                    vector_service
            *   builder sends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "CoordService.add_vector_to_coord"
        
        try:
            coord_validation = self._coord_validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            vector_validation = self._vector_service.validate_as_vector(candidate=vector)
            if vector_validation.is_failure():
                return BuildResult.failure(vector_validation.exception)
            
            column = coord.column + vector.x
            row = coord.row + vector.y
            
            return self._coord_builder.build(row=row, column=column)
        except Exception as ex:
            return BuildResult.failure(ex)
    
    def dot_product(self, coord: Coord, vector: Vector) -> BuildResult[Coord]:
        """
        # Action:
        1.  validator runs integrity checks on the target param.
        2.  vector_service runs integrity checks on the vector param.
        3.  If any checks raise an exception return it in the BuildResult.
        4.  If target and vector params are valid:
                new_row, new_colum = target.row + vector.y, target.column + vector.x
        5.  Run build_coord(new_row, new_column) to ensure the computed values produce a safe Coord instance.

        # Parameters:
            *   target(Coord):
            *   vector (Vector):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   Any validation exceptions that occur are sent to the caller by either
                    validator
                    vector_service
            *   builder sends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "CoordService.dot_product"
        
        try:
            coord_validation = self._coord_validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            vector_validation = self._vector_service.validate_as_vector(candidate=vector)
            if vector_validation.is_failure():
                return BuildResult.failure(vector_validation.exception)
            
            column = coord.column * vector.y
            row = coord.row * vector.x
            
            return self._coord_builder.build(row=row, column=column)
        except Exception as ex:
            return BuildResult.failure(ex)
    
    def multiply_coord_by_scalar(self, coord: Coord, scalar: Scalar) -> BuildResult[Coord]:
        """
        # Action:
        1.  validator runs integrity checks on the target param.
        2.  scalar_service runs integrity checks on the scalar param.
        3.  If any checks raise an exception return it in the BuildResult.
        4.  If target and scalar params are valid:
                new_row, new_colum = target.row * scalar.value, target.column * scalar.value
        5.  Run build_coord(new_row, new_column) to ensure the computed values produce a safe Coord instance.

        # Parameters:
            *   target (Coord):
            *   scalar (Scalar):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   Any validation exceptions that occur are sent to the caller by either
                    validator
                    scalar_service
            *   builder sends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "CoordService.multiply_coord_by_scalar"
        
        try:
            coord_validation = self._coord_validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            scalar_validation = self._scalar_service.validate_as_scalar(candidate=scalar)
            if scalar_validation.is_failure():
                return BuildResult.failure(scalar_validation.exception)
            
            row = coord.y * scalar.value
            column = coord.x * scalar.value
            
            return self._coord_builder.build(row=row, column=column)
        except Exception as ex:
            return BuildResult.failure(ex)
    
    def convert_vector_to_coord(self, vector: Vector) -> BuildResult[Coord]:
        """
        # Action:
        1.  vector_service runs integrity checks on param.
        2.  If any checks raise an exception return it in the BuildResult.
        3.  Run build_coord(row=y, column=y) to ensure the computed values produce a
            safe Coord instance.

        # Parameters:
            *   vector (Vector):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   vector_service sends any validation exceptions back to the caller.
            *   builder sends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "CoordService.convert_vector_to_coord"
        
        try:
            vector_validation = self._vector_service.validate_as_vector(candidate=vector)
            if vector_validation.is_failure():
                return BuildResult.failure(vector_validation.exception)
            
            return self._coord_builder.build(row=vector.y, column=vector.x)
        except Exception as ex:
            return BuildResult.failure(ex)