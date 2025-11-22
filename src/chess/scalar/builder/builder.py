# src/chess/scalar/builder/builder.py

"""
Module: chess.scalar.builder.builder
Author: Banji Lawal
Created: 2025-08-25
version: 1.0.0
"""
from wsgiref.validate import validator

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


    @LoggingLevelRouter.monitor
    def build(
            self,
            value: int,
            scalar_validator: ScalarValidator = ScalarValidator()
    ) -> BuildResult[Scalar]:
        """
        # Action:
        If the absolute value of the param is within BOARD_DIMENSION return a new Scalar instance.
        Otherwise, return an exception.
    
        # Parameters:
            *   value (int)
            *   scalar_validator (ScalarValidator)
    
        # Returns:
          BuildResult[Scalar] containing either:
                - On success: Scalar in the payload.
                - On failure: Exception.
    
        # Raises:
            * ScalarBuildFailedException
        """
        method = "ScalarBuilder.builder"
        
        try:
            validation = scalar_validator.validate_value(value)
            if validation.is_failure():
                return BuildResult.failure(validation.exception)
            
            return BuildResult.sucess(payload=Scalar(value=value))
        
        except Exception as ex:
            return BuildResult.failure(
                ScalarBuildFailedException(
                    ex=ex,
                    message=f"{method}: "
                            f"{ScalarBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
