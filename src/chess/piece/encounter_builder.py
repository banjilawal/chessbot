from typing import cast
from enum import Enum

from assurance import ThrowHelper
from chess.common import BuildResult
from chess.piece import Piece, Encounter, PieceValidator, AutoEncounterException, EncounterBuilderException


class EncounterBuilder(Enum):
    """
    Builder class responsible for safely constructing `Encounter` instances.

    `EncounterBuilder` ensures that `Encounter` objects are always created successfully by performing comprehensive validation
     checks during construction. This separates the responsibility of building from validating - `EncounterBuilder` 
     focuses on creating while `EncounterValidator` is used for validating existing `Encounter` instances that are passed
     around the system.

    The builder runs through all validation checks individually to guarantee that any `Encounter` instance it produces 
    meets all required specifications before construction completes
    
    Usage:
        ```python
        # Safe encounter creation with validation
        build_outcome = EncounterBuilder.build(observer=bishop, discovery=pawn))
        if not build_outcome.is_success():
            raise build_outcome.exception
        encounter = build_outcome.payload
        ```
    
    See Also:
        `Encounter`: The data structure being constructed
        `EncounterValidator`: Used for validating existing `Encounter` instances
        `BuildResult`: Return type containing the built `Encounter` or error information
    """

    @staticmethod
    def build(observer: Piece, discovery: Piece) -> BuildResult[Encounter]:
        """
        Constructs a new `Encounter` instance with comprehensive checks on the parameters and states during the
        build process.

        Performs individual validation checks on each component to ensure the resulting `Encounter` meets all 
        specifications. If all checks are passed, a `Encounter` instance will be returned. It is not necessary to perform 
        any additional validation checks on the returned `Encounter` instance. This method guarantees if a `BuildResult` 
        with a successful status is returned, the contained `Encounter` is valid and ready for use.


        Args:
           `observer`(`Piece`): The piece that is doing a scan, or executing a move.
           `discovery`(`Piece`): The static piece the `observer` finds in a `square`.

        Returns:
            BuildResult[Encounter]: A `BuildResult` containing either:
                - On success: A valid `Encounter` instance in the payload
                - On failure: Error information and exception details

        Raises:
           `EncounterBuilderException`: Wraps any underlying validation failures that occur during the construction 
            process. This includes:
                * `PieceValidationException`: if `observer` or `discovery` fails validation checks
                * `AutoEncounterException`: if `observer` and `discovery` are the same.

        Note:
            The builder runs through all the checks on parameters and state to guarantee only a valid `Encounter` is 
            created, while `EncounterValidator` is used for validating `Encounter` instances that are passed around after 
            creation. This separation of concerns makes the validation and building independent of each other and 
            simplifies maintenance.

        Example:
            ```python
            # Valid encounter creation
            build_outcome = EncounterBuilder.build(value=1)
            if not build_outcome.is_success():
                return BuildResult(exception=build_outcome.exception)
            return BuildResult(payload=build_outcome.payload)
            ```
        """
        method = "EncounterBuilder.build"

        try:
            observer_validation = PieceValidator.validate(observer)
            if not observer_validation.is_success():
                ThrowHelper.throw_if_invalid(EncounterBuilder, observer_validation)
                
            discovery_validation = PieceValidator.validate(discovery)
            if not discovery_validation.is_success():
                ThrowHelper.throw_if_invalid(EncounterBuilder, observer_validation)
                
            if observer == discovery:
                ThrowHelper.throw_if_invalid(
                    EncounterBuilder,
                    AutoEncounterException(AutoEncounterException.DEFAULT_MESSAGE)
                )
                
            return BuildResult(payload=Encounter(discovery=cast(Piece, discovery)))

        except Exception as e:
            raise EncounterBuilderException(
                f"{method}: {EncounterBuilderException.DEFAULT_MESSAGE}"
            )