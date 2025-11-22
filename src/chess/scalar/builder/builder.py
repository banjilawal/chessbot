# src/chess/scalar/builder/builder.py

"""
Module: chess.scalar.builder.builder
Author: Banji Lawal
Created: 2025-08-25
version: 1.0.0
"""


from chess.system import Builder, BuildResult, LoggingLevelRouter
from chess.scalar import Scalar, ScalarBuildFailedException, ScalarValidator


class ScalarBuilder(Builder[Scalar]):
    """
    # ROLE: Builder, Data Integrity Guarantor
  
    # RESPONSIBILITIES:
        1. Manage construction of Scalar instances that can be used safely by the client.
        2. Ensure params for Scalar creation have met the application's safety contract.

    # PROVIDES:
      ValidationResult[Scalar] containing either:
            - On success: Scalar in the payload.
            - On failure: Exception.
  
    # ATTRIBUTES:
        *   _value (int)
        *   _scalar_validator (ScalarValidator)
    """
    _value: int
    
    def __init__(self, value: int, scalar_validator: ScalarValidator = ScalarValidator()):
        super().__init__()
        self._value = value
        self._scalar_validator = scalar_validator
        
    @property
    def value(self) -> int:
        return self._value
    

    @LoggingLevelRouter.monitor
    def build(self) -> BuildResult[Scalar]:
        """
        # Action:
        If the absolute value of the param is within BOARD_DIMENSION return a new Scalar instance.
        Otherwise, return an exception.
    
        # Parameters:
            * value (int): selected if search target is an id.
    
        # Returns:
          BuildResult[Scalar] containing either:
                - On success: Scalar in the payload.
                - On failure: Exception.
    
        # Raises:
            * NullNumberException
            * ScalarBelowBoundsException
            * ScalarAboveBoundsException
            * ScalarBuildFailedException
        """
        method = "ScalarBuilder.builder"
        
        try:
            validation = self._scalar_validator.validate_value(self._value)
            if validation.is_failure():
                return BuildResult.failure(validation.exception)
            # if value is None:
            #     return BuildResult.failure(
            #         NullNumberException(f"{method}: {NullNumberException.DEFAULT_MESSAGE}")
            #     )
            #
            # if value < -BOARD_DIMENSION:
            #     return BuildResult.failure(
            #         ScalarBelowBoundsException(
            #             f"{method}: {ScalarBelowBoundsException.DEFAULT_MESSAGE}"
            #         )
            #     )
            #
            # if value > BOARD_DIMENSION:
            #     return BuildResult.failure(
            #         ScalarAboveBoundsException(
            #             f"{method}: {ScalarAboveBoundsException.DEFAULT_MESSAGE}"
            #         )
            #     )
            
            return BuildResult.sucess(payload=Scalar(value=self._value))
        
        except Exception as ex:
            return BuildResult.failure(
                ScalarBuildFailedException(
                    f"{method}: {ScalarBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
