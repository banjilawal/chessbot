from enum import Enum

from assurance import ThrowHelper
from chess.exception import NullNumberException
from chess.common import BuildResult, BOARD_DIMENSION

from chess.scalar import (
    Scalar, ScalarAboveBoundsException,
    ScalarBelowBoundsException, ScalarBuilderException
)



class ScalarBuilder(Enum):
    """
    Builder class responsible for safely constructing `Scalar` instances.

    `ScalarBuilder` ensures that `Scalar` objects are always created successfully by performing comprehensive validation
     checks during construction. This separates the responsibility of building from validating - `ScalarBuilder` 
     focuses on creating while `ScalarValidator` is used for validating existing `Scalar` instances that are passed
     around the system.

    The builder runs through all validation checks individually to guarantee that any `Scalar` instance it produces 
    meets all required specifications before construction completes

    Usage:
        ```python
        # Safe scalar creation
        build_result = ScalarBuilder.build(value=1))
        
        if not build_result.is_success():
            raise build_result.exception
        scalar = build_result.payload
        ```

    See Also:
        `Scalar`: The data structure being constructed
        `ScalarValidator`: Used for validating existing `Scalar` instances
        `BuildResult`: Return type containing the built `Scalar` or error information
    """
    
    @staticmethod
    def build(value: int) -> BuildResult[Scalar]:
        """
        Constructs a new `Scalar` instance with comprehensive checks on the parameters and states during the
        build process.

        Performs individual validation checks on each component to ensure the resulting `Scalar` meets all 
        specifications. If all checks are passed, a `Scalar` instance will be returned. It is not necessary to perform 
        any additional validation checks on the returned `Scalar` instance. This method guarantees if a `BuildResult` 
        with a successful status is returned, the contained `Scalar` is valid and ready for use.

        Args:
           `scalar_id`(`int`): The unique id for the scalar. Must pass `IdValidator` checks.
            `name`(`Name`): The human or cybernetic moving pieces in `Scalar.roster`. The name
                must not be None and must pass `NameValidator` checks.must pass `NameValidator` checks.
            `profile`(`ScalarProfile`): The profile defining scalar attributes and behaviors. Must not be None and be
                an instance of `ScalarProfile`.

        Returns:
            BuildResult[Scalar]: A `BuildResult` containing either:
                - On success: A valid `Scalar` instance in the payload
                - On failure: Error information and exception details

        Raises:
            `ScalarBuilderException`: Wraps any underlying validation failures that occur during the construction
            process. This includes:
                * `NullScalarException`: if `t` is null
                * `TypeError`: if `t` is not Scalar
                * `NullNumberException`: If `scalar.value` is null
                * `ScalarBelowLowerBoundException`: If `scalar.value` < 0
                * `ScalarAboveBoundsException`: If `scalar.value` >= `BOARD_DIMENSION`
                * `ScalarValidationException`: Wraps any preceding exceptions

        Note:
            The builder runs through all the checks on parameters and state to guarantee only a valid `Scalar` is 
            created, while `ScalarValidator` is used for validating `Scalar` instances that are passed around after 
            creation. This separation of concerns makes the validation and building independent of each other and 
            simplifies maintenance.

        Example:
            ```python
            # Valid scalar creation
            build_outcome = ScalarBuilder.build(value=1)
            if not build_outcome.is_success():
                return BuildResult(exception=build_outcome.exception)
            return BuildResult(payload=build_outcome.payload)
            ```
        """    
        method = "ScalarBuilder.build"

        try:
            if value is None:
                ThrowHelper.throw_if_invalid(
                    ScalarBuilder, 
                    NullNumberException(NullNumberException.DEFAULT_MESSAGE)
                )
            if value < -BOARD_DIMENSION:
                ThrowHelper.throw_if_invalid(
                    ScalarBuilder, 
                    ScalarBelowBoundsException(ScalarBelowBoundsException.DEFAULT_MESSAGE)
                )
            if value > BOARD_DIMENSION:
                ThrowHelper.throw_if_invalid(
                    ScalarBuilder, 
                    ScalarAboveBoundsException(ScalarAboveBoundsException.DEFAULT_MESSAGE)
            )
                
            return BuildResult(payload=Scalar(value=value))
        except Exception as e:
            raise ScalarBuilderException(f"{method}: {ScalarBuilderException.DEFAULT_MESSAGE}") from e
