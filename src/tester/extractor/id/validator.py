# src/tester/extractor/id/extractor.py

"""
Module: tester.extractor.id.extractor
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations



class BlueprintIdExtractor(Tester):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Validate a Blueprint's id if one is present. Otherwise, generate a unique one for
            the Blueprint's class.

    Attributes:
        identity_service: IdetntiyService
        
    Provides:
        -   execute(candidate: Any, model_name: str) -> ValidationResult:

    Super Class:
        Tester
    """
    _identity_service: IdentityService
    
    def __init__(self, identity_service: IdentityService | None = IdentityService()):
        self._identity_service = identity_service
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any, model_name: str, ) -> ValidationResult[int]:
        """
        Verify the id if it already exists or create a new one.

        Action:
            1.  If the candidate is not null:
                    -   Send an exception chain in the ValidationResult when its not an int.
                    -   Otherwise, send the success result.
            2.  If the candidate is null:
                    -   Send an exception chain in the ValidationResult if the model_name is not a string.
                    -   Otherwise, generate a unique id for the next model instance.
        Args:
            candidate: Any
            model_name: str
        Returns:
            ValidationResult
        Raises:
            BlueprintIdValidatorException
        """
        method = f"{self.__clas__.__name__}.validate"
        
        # --- Process for candidates that are not null. ---#
        if candidate is not None:
            # Handle the case that, the candidate is not a number.
            id_validation = self._identity_service.validate_id(candidate)
            if id_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    BlueprintIdValidatorException(
                        cls_mthd=method,
                        cls_name=self.__clas__.__name__,
                        msg=BlueprintIdValidatorException.MSG,
                        err_code=BlueprintIdValidatorException.ERR_CODE,
                        ex=id_validation.exception,
                    )
                )
            # --- Return the work product. ---#
            return ValidationResult.success(cast(int, candidate))
        
        # --- If the candidate is null the id has to be generated using the model_name. ---#
        
        # Handle the case that, the model_name is not a valid string.
        model_name_validation_result = self._identity_service.validate_name(model_name)
        if model_name_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BlueprintIdValidatorException(
                    cls_mthd=method,
                    cls_name=self.__clas__.__name__,
                    msg=BlueprintIdValidatorException.MSG,
                    err_code=BlueprintIdValidatorException.ERR_CODE,
                    ex=model_name_validation_result.exception,
                )
            )
        # --- Return the work product. ---#
        return ValidationResult.success(IdFactory.next_id(class_name=model_name))
        

