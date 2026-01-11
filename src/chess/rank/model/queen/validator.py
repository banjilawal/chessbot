# src/chess/rank/model/queen/validator_.py

"""
Module: chess.rank.model.queen.validator
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Any, cast

from chess.rank import (
    Queen, NotQueenIdException, NotQueenRansomException, RankSpec, NullQueenException,
    InvalidQueenException, NotQueenDesignationException, NotQueenNameException, NotQueenQuotaException,
)
from chess.system import (
    IdentityService, LoggingLevelRouter, NumberValidator, StringValidator, ValidationResult, Validator
)


class QueenValidator(Validator[Queen]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    Verifies a candidate is an instance of Queen, that meets integrity requirements, before the candidate is used.

    # PROVIDES:
    ValidationResult[Queen] containing either:
        - On success: Queen in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
    No attributes
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            text_validator: StringValidator = StringValidator(),
            number_validator: NumberValidator = NumberValidator(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[Queen]:
        """
        # ACTION:
        1.  Check candidate is not validation.
        2.  Check if candidate is a Rank.
        3.  Cast to candidate to its subclass.
        4.  Validate
                *   id      ->  with id_validator
                *   designation    ->  with name_validator
                *   designation  ->  with designation_validator
                *   team_quota   ->  with quota_validator
                *   ransom  ->  with ransom_validator
        5.  If any check fails, return the exception inside a ValidationResult.
        6.  When all checks pass return the Rank instance inside a ValidationResult.

        # PARAMETERS:
            *   candidate (Any): Object to validate.
            *   id_validator (type[RankIdValidator]=RankIdValidator)
            *   name_validator (type[RankNameValidator]=RankNameValidator)
            *   designation_validator (type[RankLetterValidator]=RankLetterValidator)
            *   quota_validator (type[RankQuotaValidator]=RankQuotaValidator)
            *   ransom_validator (type[RankRansomValidator]=RankRansomValidator)

        # RETURNS:
        ValidationResult[Rank] containing either:
            - On success: Rank in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NullRankException
            *   RankValidationFailedException
        """
        method = "RankValidatorFactory.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullQueenException(f"{method}: {NullQueenException.DEFAULT_MESSAGE}")
                )
            if not isinstance(candidate, Queen):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a Queen, got {type(candidate).__name__} instead.")
                )
            queen = cast(Queen, candidate)
            
            # Verify the id
            id_validation = cls.verify_id(queen.id)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            # Verify the designation
            name_validation = cls.verify_name(queen.name)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            # Verify designation
            designation_validation = cls.verify_designation(queen.designation)
            if designation_validation.is_failure():
                return ValidationResult.failure(designation_validation.exception)
            # Verify the quota
            quota_validation = cls.verify_team_quota(queen.team_quota)
            if quota_validation.is_failure():
                return ValidationResult.failure(quota_validation.exception)
            # Verify the ransom
            ransom_validation = cls.verify_ransom(queen.ransom)
            if ransom_validation.is_failure():
                return ValidationResult.failure(ransom_validation.exception)
            
            # If all the checks pass return the certified Queen.
            return ValidationResult.success(queen)
        # Finally, if there is an unhandled exception wap an InvalidQueenException around it
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidQueenException(ex=ex, message=f"{method}: {InvalidQueenException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_id(
            cls,
            candidate: Any,
            rank_spec: RankSpec = RankSpec(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Verify candidate is a safe id using identity_service. If so convert to id. Else return failure.
        2.  Check if id != Persona.QUEEN.id. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   persona (Persona)
            *   identity_service (IdentityService)

        # RETURNS:
        ValidationResult[int] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotQueenIdException
            *   InvalidQueenException
        """
        method = "QueenValidator.verify_id"
        try:
            # Test if the candidate is a safe id.
            validation = identity_service.validate_id(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if id is correct for a queen.
            id = validation.payload
            if id != rank_spec.QUEEN.id:
                return ValidationResult.failure(
                    NotQueenIdException(f"{method}: {NotQueenIdException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified queen.id inside a ValidationResult.
            return ValidationResult.success(id)
        
        # Finally, if there is an unhandled exception wap an InvalidQueenException around it
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidQueenException(ex=ex, message=f"{method}: {InvalidQueenException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_name(
            cls,
            candidate: Any,
            rank_spec: RankSpec = RankSpec(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Verify candidate is a safe designation using identity_service. If so convert to designation. Else return failure.
        2.  Check if designation != Persona.QUEEN.designation. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   persona (Persona)
            *   identity_service (IdentityService)

        # RETURNS:
        ValidationResult[str] containing either:
            - On success:   str in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotQueenNameException
            *   InvalidQueenException
        """
        method = "QueenValidator.verify_name"
        try:
            # Test if the candidate is a safe designation.
            validation = identity_service.validate_name(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if designation is correct for a queen.
            name = validation.payload
            if name.upper() != rank_spec.QUEEN.name.upper():
                return ValidationResult.failure(
                    NotQueenNameException(f"{method}: {NotQueenNameException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified queen.designation inside a ValidationResult.
            return ValidationResult.success(name)
        # Finally, catch any missed exception, wrap an InvalidQueenException around it
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidQueenException(ex=ex, message=f"{method}: {InvalidQueenException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_ransom(
            cls,
            candidate: Any,
            rank_spec: RankSpec = RankSpec(),
            number_validator: NumberValidator = NumberValidator(),
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Verify candidate is a safe number using not_negative_validator. If so convert to number. Else return failure.
        2.  Check if ransom != Persona.QUEEN.ransom. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   persona (Persona)
            *   not_negative_validator (NumberValidator)

        # RETURNS:
        ValidationResult[int] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotQueenRansomException
            *   InvalidQueenException
        """
        method = "QueenValidator.verify_ransom"
        try:
            # Test if the candidate is a safe id.
            validation = number_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if id is correct for a queen.
            ransom = validation.payload
            if ransom != rank_spec.QUEEN.ransom:
                return ValidationResult.failure(
                    NotQueenRansomException(f"{method}: {NotQueenRansomException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified queen.ransom inside a ValidationResult.
            return ValidationResult.success(ransom)
        
        # Finally, catch any missed exception, wrap an InvalidQueenException around it
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidQueenException(ex=ex, message=f"{method}: {InvalidQueenException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_designation(
            cls,
            candidate: Any,
            rank_spec: RankSpec = RankSpec(),
            text_validator: StringValidator = StringValidator(),
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Verify candidate is a safe string using text_validator. If so convert to string. Else return failure.
        2.  Check if string != Persona.QUEEN.designation. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   persona (Persona)
            *   text_validator (StringValidator)

        # RETURNS:
        ValidationResult[str] containing either:
            - On success:   str in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotQueenDesignationException
            *   InvalidQueenException
        """
        method = "QueenValidator.verify_designation"
        try:
            # Test if the candidate is a safe designation.
            validation = text_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if designation is correct for a queen.
            designation = validation.payload
            if designation.upper() != rank_spec.QUEEN.designation.upper():
                return ValidationResult.failure(
                    NotQueenDesignationException(f"{method}: {NotQueenDesignationException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified queen.designation inside a ValidationResult.
            return ValidationResult.success(designation)
        
        # Finally, catch any missed exception, wrap an InvalidQueenException around it
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidQueenException(ex=ex, message=f"{method}: {InvalidQueenException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_team_quota(
            cls,
            candidate: Any,
            rank_spec: RankSpec = RankSpec(),
            number_validator: NumberValidator = NumberValidator(),
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Verify candidate is a safe number using not_negative_validator. If so convert to number. Else return failure.
        2.  Check if ransom != Persona.QUEEN.team_quota. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   persona (Persona)
            *   not_negative_validator (NumberValidator)

        # RETURNS:
        ValidationResult[int] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotQueenQuotaException
            *   InvalidQueenException
        """
        method = "QueenValidator.verify_team_quota"
        try:
            # Test if the candidate is a safe number.
            validation = number_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if team_quota is correct for a queen.
            team_quota = validation.payload
            if team_quota != rank_spec.QUEEN.quota:
                return ValidationResult.failure(
                    NotQueenQuotaException(f"{method}: {NotQueenQuotaException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified queen.team_quota inside a ValidationResult.
            return ValidationResult.success(team_quota)
        
        # Finally, catch any missed exception, wrap an InvalidQueenException around it
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidQueenException(ex=ex, message=f"{method}: {InvalidQueenException.DEFAULT_MESSAGE}")
            )