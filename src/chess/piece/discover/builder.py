from typing import cast
from enum import Enum

from assurance import ThrowHelper
from chess.system import BuildResult
from chess.piece import Piece, Discovery, PieceValidator, AutoDiscoveryException, DiscoveryBuilderException, \
    AddDuplicateDiscoveryException
from chess.piece.discover import CircularDiscoveryException


class DiscoveryBuilder(Enum):
    """
    Builder class responsible for safely constructing `Discovery` instances.

    `DiscoveryBuilder` ensures that `Discovery` objects are always created successfully by performing comprehensive validation
    checks during construction. This separates the responsibility of building from validating - `DiscoveryBuilder`
    focuses on creating while `DiscoveryValidator` is used for validating existing `Discovery` instances that are passed
    around the system.

    The build runs through all validation checks individually to guarantee that any `Discovery` instance it produces
    meets all required specifications before construction completes
    
    Usage:
        ```python
        # Safe discover creation with validation
        build_outcome = DiscoveryBuilder.build(actor=bishop, discover=pawn))
        if not build_outcome.is_success():
            raise build_outcome.exception
        discover = build_outcome.payload
        ```
    
    See Also:
        `Discovery`: The data structure being constructed
        `DiscoveryValidator`: Used for validating existing `Discovery` instances
        `BuildResult`: Return type containing the built `Discovery` or exception information
    """

    @staticmethod
    def build(observer: Piece, subject: Piece) -> BuildResult[Discovery]:
        """
        Constructs a new `Discovery` instance with comprehensive checks on the parameters and states during the
        build process.

        Performs individual validation checks on each component to ensure the resulting `Discovery` meets all 
        specifications. If all checks are passed, a `Discovery` instance will be returned. It is not necessary to perform 
        any additional validation checks on the returned `Discovery` instance. This method guarantees if a `BuildResult` 
        with a successful status is returned, the contained `Discovery` is valid and ready for use.


        Args:
           `actor`(`Piece`): The piece that is doing a scan, or executing a move.
           `discover`(`Piece`): The static piece the `actor` finds in a `square`.

        Returns:
            BuildResult[Discovery]: A `BuildResult` containing either:
                - On success: A valid `Discovery` instance in the payload
                - On failure: Error information and exception details

        Raises:
           `DiscoveryBuilderException`: Wraps any underlying validation failures that occur during the construction 
            process. This includes:
                * `PieceValidationException`: if `actor` or `discover` fails validation checks
                * `AutoDiscoveryException`: if `actor` and `discover` are the same.

        Note:
            The build runs through all the checks on parameters and state to guarantee only a valid `Discovery` is
            created, while `DiscoveryValidator` is used for validating `Discovery` instances that are passed around after 
            creation. This separation of concerns makes the validation and building independent of each other and 
            simplifies maintenance.

        Example:
            ```python
            # Valid discover creation
            build_outcome = DiscoveryBuilder.build(value=1)
            if not build_outcome.is_success():
                return BuildResult(exception=build_outcome.exception)
            return BuildResult(payload=build_outcome.payload)
            ```
        """
        method = "DiscoveryBuilder.build"

        try:
            observer_validation = PieceValidator.validate(observer)
            if not observer_validation.is_success():
                ThrowHelper.throw_if_invalid(DiscoveryBuilder, observer_validation)
                
            subject_validation = PieceValidator.validate(subject)
            if not subject_validation.is_success():
                ThrowHelper.throw_if_invalid(DiscoveryBuilder, subject_validation)
                
            if observer == subject:
                ThrowHelper.throw_if_invalid(
                    DiscoveryBuilder,
                    CircularDiscoveryException(CircularDiscoveryException.DEFAULT_MESSAGE)
                )

            search_result = observer.discoveries.find_by_id(subject.id)
            if not search_result.is_empty():
                ThrowHelper.throw_if_invalid(
                    DiscoveryBuilder,
                    AddDuplicateDiscoveryException(AddDuplicateDiscoveryException.DEFAULT_MESSAGE)
                )
            return BuildResult(payload=Discovery(piece=cast(Piece, subject)))

        except Exception as e:
            raise DiscoveryBuilderException(
                f"{method}: {DiscoveryBuilderException.DEFAULT_MESSAGE}"
            )