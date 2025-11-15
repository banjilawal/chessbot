# src/chess/scalar/builder.py

"""
Module: chess.scalar.builder
Author: Banji Lawal
Created: 2025-08-25
version: 1.0.0
"""


from chess.system import (
    Builder, BuildResult, BOARD_DIMENSION, NullNumberException, LoggingLevelRouter
)
from chess.scalar import (
    Scalar, ScalarAboveBoundsException, ScalarBelowBoundsException, ScalarBuildFailedException
)


class ScalarBuilder(Builder[Scalar]):
    """
    # ROLE: Builder
  
    # RESPONSIBILITIES:
        1. Manage construction of Scalar instances that can be used safely by the client.
        2. Ensure params for Scalar creation have met the application's safety contract.

    # PROVIDES:
      ValidationResult[Scalar] containing either:
            - On success: Scalar in the payload.
            - On failure: Exception.
  
    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, value: int) -> BuildResult[Scalar]:
        """
        # Action:
        If the absolute value of the param is within BOARD_DIMENSION return a new Scalar instance.
        Otherwise, return an exception.
    
        # Parameters:
            * value (int): selected if search target is an id.
    
        # Returns:
          BuildResult[Scalar] containing either:
                - On success: Scalar in payload.
                - On failure: Exception.
    
        # Raises:
            * NullNumberException
            * ScalarBelowBoundsException
            * ScalarAboveBoundsException
            * ScalarBuildFailedException
        """
        method = "ScalarBuilder.build"
        
        try:
            if value is None:
                return BuildResult.failure(
                    NullNumberException(f"{method}: {NullNumberException.DEFAULT_MESSAGE}")
                )
            
            if value < -BOARD_DIMENSION:
                return BuildResult.failure(
                    ScalarBelowBoundsException(
                        f"{method}: {ScalarBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if value > BOARD_DIMENSION:
                return BuildResult.failure(
                    ScalarAboveBoundsException(
                        f"{method}: {ScalarAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return BuildResult.sucess(payload=Scalar(value=value))
        
        except Exception as ex:
            return BuildResult.failure(
                ScalarBuildFailedException(
                    f"{method}: {ScalarBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
