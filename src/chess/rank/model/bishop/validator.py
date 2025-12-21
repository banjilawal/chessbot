# src/chess/rank/model/bishop/validator_.py

"""
Module: chess.rank.model.bishop.validator
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Any, cast

from chess.rank import (
    Bishop, NotBishopIdException, NotBishopRansomException, RankSpec, NullBishopException,
    InvalidBishopException, NotBishopDesignationException, NotBishopNameException, NotBishopQuotaException,
)
from chess.system import (
    IdentityService, LoggingLevelRouter, NumberValidator, StringValidator, ValidationResult, Validator
)


class BishopValidator(Validator[Bishop]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    Verifies a candidate is an instance of Bishop, that meets integrity requirements, before the candidate is used.

    # PROVIDES:
    ValidationResult[Bishop] containing either:
        - On success: Bishop in the payload.
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
    ) -> ValidationResult[Bishop]:
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

        # Returns:
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
                    NullBishopException(f"{method}: {NullBishopException.DEFAULT_MESSAGE}")
                )
            if not isinstance(candidate, Bishop):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a Bishop got {type(candidate).__name__} instead.")
                )
            bishop = cast(Bishop, candidate)
            
            # Verify the id
            id_validation = cls.verify_id(bishop.id)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            # Verify the designation
            name_validation = cls.verify_name(bishop.name)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            # Verify designation
            designation_validation = cls.verify_designation(bishop.designation)
            if designation_validation.is_failure():
                return ValidationResult.failure(designation_validation.exception)
            # Verify the quota
            quota_validation = cls.verify_team_quota(bishop.team_quota)
            if quota_validation.is_failure():
                return ValidationResult.failure(quota_validation.exception)
            # Verify the ransom
            ransom_validation = cls.verify_ransom(bishop.ransom)
            if ransom_validation.is_failure():
                return ValidationResult.failure(ransom_validation.exception)
            
            # If all the checks pass return the certified Bishop.
            return ValidationResult.success(bishop)
        # Finally, if there is an unhandled exception wap an InvalidBishopException around it
        # then return the exception inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidBishopException(ex=ex, message=f"{method}: {InvalidBishopException.DEFAULT_MESSAGE}")
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
        2.  Check if id != Catalog.BISHOP.id. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   rank_spec (Catalog)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[int] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotBishopIdException
            *   InvalidBishopException
        """
        method = "BishopValidator.verify_id"
        try:
            # Test if the candidate is a safe id.
            validation = identity_service.validate_id(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if id is correct for a bishop.
            id = validation.payload
            if id != rank_spec.BISHOP.id:
                return ValidationResult.failure(
                    NotBishopIdException(f"{method}: {NotBishopIdException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified bishop.id inside a ValidationResult.
            return ValidationResult.success(id)
        
        # Finally, if there is an unhandled exception wap an InvalidBishopException around it
        # then return the exception inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidBishopException(ex=ex, message=f"{method}: {InvalidBishopException.DEFAULT_MESSAGE}")
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
        2.  Check if designation != Catalog.BISHOP.designation. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   rank_spec (Catalog)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[str] containing either:
            - On success:   str in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotBishopNameException
            *   InvalidBishopException
        """
        method = "BishopValidator.verify_name"
        try:
            # Test if the candidate is a safe designation.
            validation = identity_service.validate_name(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if designation is correct for a bishop.
            name = validation.payload
            if name.upper() != rank_spec.BISHOP.name.upper():
                return ValidationResult.failure(
                    NotBishopNameException(f"{method}: {NotBishopNameException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified bishop.designation inside a ValidationResult.
            return ValidationResult.success(name)
        # Finally, if there is an unhandled exception Wrap an InvalidBishopException around it
        # then return the exception inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidBishopException(ex=ex, message=f"{method}: {InvalidBishopException.DEFAULT_MESSAGE}")
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
        2.  Check if ransom != Catalog.BISHOP.ransom. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   rank_spec (Catalog)
            *   not_negative_validator (NumberValidator)

        # Returns:
        ValidationResult[int] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotBishopRansomException
            *   InvalidBishopException
        """
        method = "BishopValidator.verify_ransom"
        try:
            # Test if the candidate is a safe id.
            validation = number_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if id is correct for a bishop.
            ransom = validation.payload
            if ransom != rank_spec.BISHOP.ransom:
                return ValidationResult.failure(
                    NotBishopRansomException(f"{method}: {NotBishopRansomException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified bishop.ransom inside a ValidationResult.
            return ValidationResult.success(ransom)
        
        # Finally, if there is an unhandled exception wrap an InvalidBishopException around it
        # then return the exception inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidBishopException(ex=ex, message=f"{method}: {InvalidBishopException.DEFAULT_MESSAGE}")
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
        2.  Check if string != Catalog.BISHOP.designation. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   rank_spec (Catalog)
            *   text_validator (StringValidator)

        # Returns:
        ValidationResult[str] containing either:
            - On success:   str in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotBishopDesignationException
            *   InvalidBishopException
        """
        method = "BishopValidator.verify_designation"
        try:
            # Test if the candidate is a safe designation.
            validation = text_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if designation is correct for a bishop.
            designation = validation.payload
            if designation.upper() != rank_spec.BISHOP.designation.upper():
                return ValidationResult.failure(
                    NotBishopDesignationException(f"{method}: {NotBishopDesignationException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified bishop.designation inside a ValidationResult.
            return ValidationResult.success(designation)
        
        # Finally, if there is an unhandled exception wrap an InvalidBishopException around it
        # then return the exception inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidBishopException(ex=ex, message=f"{method}: {InvalidBishopException.DEFAULT_MESSAGE}")
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
        2.  Check if ransom != Catalog.BISHOP.team_quota. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   rank_spec (Catalog)
            *   not_negative_validator (NumberValidator)

        # Returns:
        ValidationResult[int] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotBishopQuotaException
            *   InvalidBishopException
        """
        method = "BishopValidator.verify_team_quota"
        try:
            # Test if the candidate is a safe number.
            validation = number_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if team_quota is correct for a bishop.
            team_quota = validation.payload
            if team_quota != rank_spec.BISHOP.quota:
                return ValidationResult.failure(
                    NotBishopQuotaException(f"{method}: {NotBishopQuotaException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified bishop.team_quota inside a ValidationResult.
            return ValidationResult.success(team_quota)
        
        # Finally, if there is an unhandled exception wrap an InvalidBishopException around it
        # then return the exception inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidBishopException(ex=ex, message=f"{method}: {InvalidBishopException.DEFAULT_MESSAGE}")
            )