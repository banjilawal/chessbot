# src/chess/rank/spec/validator.py

"""
Module: chess.rank.spec.validator
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from typing import Any, cast

from chess.rank import (
    InvalidRankDesignationException, InvalidRankIdException, InvalidRankNameException, InvalidRankRansomException,
    InvalidRankSpecException, InvalidTeamQuotaException, NullRankSpecException, RankSpec, TeamQuotaBoundsException,
    RankDesignationBoundsException, RankIdBoundsException, RankNameBoundsException, RankRansomBoundsException
)
from chess.system import (
    IdentityService, LoggingLevelRouter, NumberValidator, TextValidator, ValidationResult, Validator
)


class RankSpecValidator(Validator[RankSpec]):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    1.  Verifies a candidate is not null and is an actual RankSpec Enum.
    2.  Only have to write the two verification checks for a RankSpec once. This gives cleaner code.
    3.  Verifies names and colors used in filtering and branching logic gets arguments in bounds.

    # PROVIDES:
    ValidationResult[RankSpec] containing either:
        - On success: RankSpec in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
    No attributes

    # CONSTRUCTOR:
    Default Constructor

    # CLASS METHODS:
        *   validate(candidate: Any) -> ValidationResult[RankSpec]:
        
        *   verify_id_in_spec(candidate: Any, identity_service: IdentityService) -> ValidationResult[int]:
        
        *   verify_name_in_spec(candidate: Any, identity_service: IdentityService) -> ValidationResult[str]:
        
        *   verify_designation_in_spec(candidate: Any, text_validator: TextValidator) -> ValidationResult[str]:
        
        *   verify_ransom_in_spec(candidate: Any, number_validator: NumberValidator) -> ValidationResult[int]:
        
        *   verify_quota_in_spec(candidate: Any, number_validator: NumberValidator) -> ValidationResult[int]:
        
    # INSTANCE METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[RankSpec]:
        """
        # ACTION:
        1.  Check candidate is not null.
        2.  Check the candidate is a RankSpec enum
        3.  If both checks pass cast the candidate to a RankSpec and return in a
            ValidationResult.

        # PARAMETERS:
            *   candidate (Any)

        # Returns:
        ValidationResult[RankSpec] containing either:
            - On success:   RankSpec in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullRankSpecException
            *   InvalidRankSpecException
        """
        method = "RankSpecValidator.validate"
        
        try:
            # Start the error detection process.
            if candidate is None:
                return ValidationResult.failure(
                    NullRankSpecException(f"{method} {NullRankSpecException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, RankSpec):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected RankSpec, got {type(candidate).__name__} instead.")
                )
            # If no errors are detected cast the candidate to a RankSpec object then return in
            # a ValidationResult.
            return ValidationResult.success(cast(RankSpec, candidate))
        
        # Finally, if there is an unhandled exception Wrap an InvalidPieceException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidRankSpecException(ex=ex, message=f"{method} {InvalidRankSpecException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_in_ransom_spec(
            cls,
            candidate: Any,
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Verify candidate is a safe id using identity_service. If safe get the id. Else return failure.
        2.  If number not in RankSpec.allowed_ransoms return a failed validation result.
        3.  If all checks pass the number in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[int] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   RankIdBoundsException
            *   InvalidRankIdException
        """
        method = "RankSpecValidator.verify_in_id_spec"
        try:
            # Start the error detection process.
            id_validation = identity_service.validate_id(candidate)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
                # Next check if id is allowed.
            id = id_validation.payload
            if id not in RankSpec.allowed_ids():
                return ValidationResult.failure(
                    RankIdBoundsException(f"{method}: {RankIdBoundsException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified ransom inside a ValidationResult.
            return ValidationResult.success(payload=id)
            
            # Finally, if there is an unhandled exception Wrap a InvalidRankIdException around it
            # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidRankIdException(ex=ex, message=f"{method}: {InvalidRankIdException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def verify_name_in_spec(
            cls,
            candidate: Any,
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[str]:
        """
        # ACTION:
        1.  Verify candidate is a safe id using identity_service. If so convert to id. Else return failure.
        2.  If id not in RankSpec.allowed_ids return a failed validation result.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[str] containing either:
            - On success:   str in the payload.
            - On failure:   Exception.

        # RAISES:
            *   RankNameBoundsException
            *   InvalidRankNameException
        """
        method = "RankSpecValidator.verify_name_in_spec"
        try:
            # Test if the candidate is safe text.
            validation = identity_service.validate_name(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if designation is allowed.
            name = validation.payload
            if name.upper() not in RankSpec.allowed_upper_case_names():
                return ValidationResult.failure(
                    RankNameBoundsException(f"{method} {RankNameBoundsException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the name inside a ValidationResult.
            return ValidationResult.success(payload=name)
            
            # Finally, if there is an unhandled exception Wrap a InvalidRankNameException around it
            # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidRankNameException(ex=ex, message=f"{method} {InvalidRankNameException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_in_ransom_spec(
            cls,
            candidate: Any,
            number_validator: NumberValidator = NumberValidator(),
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Verify candidate is a safe number using number_validator. If safe get the number. Else return failure.
        2.  If number not in RankSpec.allowed_ransoms return a failed validation result.
        3.  If all checks pass the number in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   number_validator (NumberValidator)

        # Returns:
        ValidationResult[int] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   RankRansomBoundsException
            *   InvalidRankRansomException
        """
        method = "RankSpecValidator.verify_in_ransom_spec"
        try:
            # Start the error detection process.
            number_validation = number_validator.validate(candidate)
            if number_validation.is_failure():
                return ValidationResult.failure(number_validation.exception)
                # Next check if ransom is allowed.
            ransom = number_validation.payload
            if ransom not in RankSpec.allowed_ransoms():
                return ValidationResult.failure(
                    RankRansomBoundsException(f"{method}: {RankRansomBoundsException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified ransom inside a ValidationResult.
            return ValidationResult.success(payload=ransom)
            
            # Finally, if there is an unhandled exception Wrap a InvalidRankRansomException around it
            # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidRankRansomException(ex=ex, message=f"{method}: {InvalidRankRansomException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def verify_in_designation_spec(
            cls,
            candidate: Any,
            text_validator: TextValidator = TextValidator(),
    ) -> ValidationResult[str]:
        """
        # ACTION:
        1.  Verify candidate is a safe string using text_validator. If safe convert to text. Else return failure.
        2.  If text not in RankSpec.allowed_designations return a failed validation result.
        3.  If all checks pass the text in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   text_validator (TextValidator)

        # Returns:
        ValidationResult[str] containing either:
            - On success:   str in the payload.
            - On failure:   Exception.

        # RAISES:
            *   RankDesignationBoundsException
            *   InvalidRankDesignationException
        """
        method = "RankSpecValidator.verify_designation_in_spec"
        try:
            # Test if the candidate is safe text.
            validation = text_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if designation is allowed.
            designation = validation.payload
            if designation.upper() not in RankSpec.allowed_upper_case_designations():
                return ValidationResult.failure(
                    RankDesignationBoundsException(f"{method} {RankDesignationBoundsException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the designation inside a ValidationResult.
            return ValidationResult.success(payload=designation)
            
            # Finally, if there is an unhandled exception Wrap an InvalidRankDesignationException around it
            # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidRankDesignationException(
                    ex=ex, message=f"{method} {InvalidRankDesignationException.DEFAULT_MESSAGE}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_in_team_quota_spec(
            cls,
            candidate: Any,
            number_validator: NumberValidator = NumberValidator(),
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Verify candidate is a safe number using number_validator. If safe get the number. Else return failure.
        2.  If number not in RankSpec.allowed_quotas return a failed validation result.
        3.  If all checks pass the number in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   number_validator (NumberValidator)

        # Returns:
        ValidationResult[int] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TeamQuotaBoundsException
            *   InvalidTeamQuotaException
        """
        method = "RankSpecValidator.verify_in_team_quota_spec"
        try:
            # Tes if the candidate is a safe number.
            number_validation = number_validator.validate(candidate)
            if number_validation.is_failure():
                return ValidationResult.failure(number_validation.exception)
            # Next check if team_quota is allowed.
            team_quota = number_validation.payload
            if team_quota not in RankSpec.allowed_team_quotas():
                return ValidationResult.failure(
                    TeamQuotaBoundsException(f"{method}: {TeamQuotaBoundsException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified team_quota inside a ValidationResult.
            return ValidationResult.success(payload=team_quota)
            
            # Finally, if there is an unhandled exception Wrap an InvalidTeamQuotaException around it
            # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamQuotaException(ex=ex, message=f"{method}: {InvalidTeamQuotaException.DEFAULT_MESSAGE}")
            )