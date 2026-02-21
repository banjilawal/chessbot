# src/chess/scalar/builder/builder.py

"""
Module: chess.scalar.builder.builder
Author: Banji Lawal
Created: 2025-08-25
version: 1.0.0
"""
from wsgiref.validate import validator

from chess.system import Builder, BuildResult, LoggingLevelRouter
from chess.scalar import Scalar, ScalarBuildException, ScalarValidator


class ScalarBuilder(Builder[Scalar]):
    """
     # ROLE: Builder, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce Scalar instances whose integrity is guaranteed at creation.
     2.  Manage construction of Scalar instances that can be used safely by the client.
     3.  Ensure params for Scalar creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

     # PROVIDES:
         *   ScalarBuilder

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
     None
     """


    @LoggingLevelRouter.monitor
    def build(
            self,
            value: int,
            scalar_validator: ScalarValidator = ScalarValidator()
    ) -> BuildResult[Scalar]:
        """
        # ACTION:
        If the absolute value of the param is within BOARD_DIMENSION return a new Scalar instance.
        Otherwise, return an exception.
    
        # PARAMETERS:
            *   value (int)
            *   scalar_validator (ScalarValidator)
    
        # RETURNS:
          BuildResult[Scalar] containing either:
                - On success: Scalar in the payload.
                - On failure: Exception.
    
        # RAISES:
            * ScalarBuildException
        """
        method = "ScalarBuilder.builder"
        
        try:
            validation = scalar_validator.validate_value(value)
            if validation.is_failure():
                return BuildResult.failure(validation.exception)
            
            return BuildResult.sucess(payload=Scalar(value=value))
        
        except Exception as ex:
            return BuildResult.failure(
                ScalarBuildException(
                    ex=ex,
                    message=f"{method}: "
                            f"{ScalarBuildException.DEFAULT_MESSAGE}"
                )
            )
