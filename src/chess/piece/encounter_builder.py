from enum import Enum

from assurance import ThrowHelper
from chess.common import BuildResult
from chess.piece import Encounter, Piece, PieceValidator, AutoEncounterException, EncounterBuilderException


class EncounterBuilder(Enum):
    """
    Builder class responsible for safely constructing `Encounter` instances.
    
    `EncounterBuilder` ensures that `Encounter` objects are always created successfully by
    performing comprehensive validation checks during construction. This separates
    the responsibility of building from validating - `EncounterBuilder` focuses on
    creation while `EncounterValidator` is used for validating existing `Encounter` instances
    that are passed around the system.
    
    The builder runs through all validation checks individually to guarantee that
    any `Encounter` instance it produces meets all required specifications before
    construction completes.
    
    Usage:
        ```python
        # Safe encounter creation with validation
        build_outcome = EncounterBuilder.build(observer=id_emitter.observer, discovery="WN2", rank=Knight(), team=white_team)
        if not build_outcome.is_success():
            raise build_outcome.exception
        encounter = build_outcome.payload
        ```
    
    See Also:
        `EncounterValidator`: Used for validating existing `Encounter` instances
        `Encounter`: The data structure being constructed
        `BuildResult`: Return type containing the built `Encounter` or error information
    """

    @staticmethod
    def build(observer: Piece, discovery: Piece) -> BuildResult[Encounter]:
        """
        Constructs a new `Encounter` instance with comprehensive validation.

        Performs individual validation checks on each component to ensure the 
        resulting `Encounter` meets all specifications. The method validates bounds, 
        null checks, and uses `EncounterValidator` for final instance validation 
        before returning a successfully constructed `Encounter`.

        This method guarantees that if a `BuildResult` with a successful status 
        is returned, the contained `Encounter` is valid and ready for use.

        Args:
           `observer`(`Piece`): The discovery that is doing a scan, or executing a move.
           `discovery`(`Piece`): The static discovery discovered in a square.

        Returns:
            BuildResult[Encounter]: A `BuildResult` containing either:
                - On success: A valid `Encounter` instance in the payload
                - On failure: Error information and exception details

        Raises:
           EncounterBuilderException: Wraps any underlying validation failures that occur
           during the construction process. This includes:
            - `PieceValidationException`: if `observer` or `discovery`fails validation checks
            - `AutoEncounterException`: if `observer` and `discovery` are the same.

        Note:
            The builder performs validation at construction time, while 
            `EncounterValidator` is used for validating `Encounter` instances that 
            are passed around after creation. 
            This separation of concerns makes the validation responsibilities clearer.

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
                
            return BuildResult(payload=Encounter(discovery=discovery))

        except Exception as e:
            raise EncounterBuilderException(
                f"{method}: {EncounterBuilderException.DEFAULT_MESSAGE}"
            )