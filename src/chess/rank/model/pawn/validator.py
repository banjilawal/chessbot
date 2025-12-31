# src/chess/rank/model/pawn/validator_.py

"""
Module: chess.rank.model.pawn.validator
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Any, cast

from chess.rank import (
    Pawn, NotPawnIdException, NotPawnRansomException, RankSpec, NullPawnException,
    InvalidPawnException, NotPawnDesignationException, NotPawnNameException, NotPawnQuotaException,
)
from chess.system import (
    IdentityService, LoggingLevelRouter, NumberValidator, StringValidator, ValidationResult, Validator
)


class PawnValidator(Validator[Pawn]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    Verifies a candidate is an instance of Pawn, that meets integrity requirements, before the candidate is used.

    # PROVIDES:
    ValidationResult[Pawn] containing either:
        - On success: Pawn in the payload.
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
    ) -> ValidationResult[Pawn]:
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
            *   InvalidRankException
        """
        method = "RankValidatorFactory.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullPawnException(f"{method}: {NullPawnException.DEFAULT_MESSAGE}")
                )
            if not isinstance(candidate, Pawn):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a Pawn, got {type(candidate).__name__} instead.")
                )
            pawn = cast(Pawn, candidate)
            
            # Verify the id
            id_validation = cls.verify_id(pawn.id)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            # Verify the designation
            name_validation = cls.verify_name(pawn.name)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            # Verify designation
            designation_validation = cls.verify_designation(pawn.designation)
            if designation_validation.is_failure():
                return ValidationResult.failure(designation_validation.exception)
            # Verify the quota
            quota_validation = cls.verify_team_quota(pawn.team_quota)
            if quota_validation.is_failure():
                return ValidationResult.failure(quota_validation.exception)
            # Verify the ransom
            ransom_validation = cls.verify_ransom(pawn.ransom)
            if ransom_validation.is_failure():
                return ValidationResult.failure(ransom_validation.exception)
            
            # If all the checks pass return the certified Pawn.
            return ValidationResult.success(pawn)
        # Finally, if there is an unhandled exception wap an InvalidPawnException around it
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidPawnException(ex=ex, message=f"{method}: {InvalidPawnException.DEFAULT_MESSAGE}")
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
        2.  Check if id != Persona.PAWN.id. If not, return failure.
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
            *   NotPawnIdException
            *   InvalidPawnException
        """
        method = "PawnValidator.verify_id"
        try:
            # Test if the candidate is a safe id.
            validation = identity_service.validate_id(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if id is correct for a pawn.
            id = validation.payload
            if id != rank_spec.PAWN.id:
                return ValidationResult.failure(
                    NotPawnIdException(f"{method}: {NotPawnIdException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified pawn.id inside a ValidationResult.
            return ValidationResult.success(id)
        
        # Finally, if there is an unhandled exception wap an InvalidPawnException around it
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidPawnException(ex=ex, message=f"{method}: {InvalidPawnException.DEFAULT_MESSAGE}")
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
        2.  Check if designation != Persona.PAWN.designation. If not, return failure.
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
            *   NotPawnNameException
            *   InvalidPawnException
        """
        method = "PawnValidator.verify_name"
        try:
            # Test if the candidate is a safe designation.
            validation = identity_service.validate_name(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if designation is correct for a pawn.
            name = validation.payload
            if name.upper() != rank_spec.PAWN.name.upper():
                return ValidationResult.failure(
                    NotPawnNameException(f"{method}: {NotPawnNameException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified pawn.designation inside a ValidationResult.
            return ValidationResult.success(name)
        # Finally, catch any missed exception, wrap an InvalidPawnException around it
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidPawnException(ex=ex, message=f"{method}: {InvalidPawnException.DEFAULT_MESSAGE}")
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
        2.  Check if ransom != Persona.PAWN.ransom. If not, return failure.
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
            *   NotPawnRansomException
            *   InvalidPawnException
        """
        method = "PawnValidator.verify_ransom"
        try:
            # Test if the candidate is a safe id.
            validation = number_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if id is correct for a pawn.
            ransom = validation.payload
            if ransom != rank_spec.PAWN.ransom:
                return ValidationResult.failure(
                    NotPawnRansomException(f"{method}: {NotPawnRansomException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified pawn.ransom inside a ValidationResult.
            return ValidationResult.success(ransom)
        
        # Finally, catch any missed exception, wrap an InvalidPawnException around it
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidPawnException(ex=ex, message=f"{method}: {InvalidPawnException.DEFAULT_MESSAGE}")
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
        2.  Check if string != Persona.PAWN.designation. If not, return failure.
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
            *   NotPawnDesignationException
            *   InvalidPawnException
        """
        method = "PawnValidator.verify_designation"
        try:
            # Test if the candidate is a safe designation.
            validation = text_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if designation is correct for a pawn.
            designation = validation.payload
            if designation.upper() != rank_spec.PAWN.designation.upper():
                return ValidationResult.failure(
                    NotPawnDesignationException(f"{method}: {NotPawnDesignationException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified pawn.designation inside a ValidationResult.
            return ValidationResult.success(designation)
        
        # Finally, catch any missed exception, wrap an InvalidPawnException around it
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidPawnException(ex=ex, message=f"{method}: {InvalidPawnException.DEFAULT_MESSAGE}")
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
        2.  Check if ransom != Persona.PAWN.team_quota. If not, return failure.
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
            *   NotPawnQuotaException
            *   InvalidPawnException
        """
        method = "PawnValidator.verify_team_quota"
        try:
            # Test if the candidate is a safe number.
            validation = number_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if team_quota is correct for a pawn.
            team_quota = validation.payload
            if team_quota != rank_spec.PAWN.quota:
                return ValidationResult.failure(
                    NotPawnQuotaException(f"{method}: {NotPawnQuotaException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified pawn.team_quota inside a ValidationResult.
            return ValidationResult.success(team_quota)
        
        # Finally, catch any missed exception, wrap an InvalidPawnException around it
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidPawnException(ex=ex, message=f"{method}: {InvalidPawnException.DEFAULT_MESSAGE}")
            )