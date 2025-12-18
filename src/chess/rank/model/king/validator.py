# src/chess/rank/model/king/validator_.py

"""
Module: chess.rank.model.king.validator
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Any, cast

from chess.rank import (
    King, NotKingIdException, NotKingRansomException, RankSpec, NullKingException,
    InvalidKingException, NotKingDesignationException, NotKingNameException, NotKingQuotaException,
)
from chess.system import (
    IdentityService, LoggingLevelRouter, NumberValidator, TextValidator, ValidationResult, Validator
)


class KingValidator(Validator[King]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    Verifies a candidate is an instance of King, that meets integrity requirements, before the candidate is used.

    # PROVIDES:
    ValidationResult[King] containing either:
        - On success: King in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
    No attributes
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            text_validator: TextValidator = TextValidator(),
            number_validator: NumberValidator = NumberValidator(),
            idservice: IdentityService = IdentityService(),
    ) -> ValidationResult[King]:
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
                    NullKingException(f"{method}: {NullKingException.DEFAULT_MESSAGE}")
                )
            if not isinstance(candidate, King):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a King got {type(candidate).__name__} instead.")
                )
            king = cast(King, candidate)
            
            # Verify the id
            id_validation = cls.verify_id(king.id)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            # Verify the designation
            name_validation = cls.verify_name(king.name)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            # Verify designation
            designation_validation = cls.verify_designation(king.designation)
            if designation_validation.is_failure():
                return ValidationResult.failure(designation_validation.exception)
            # Verify the quota
            quota_validation = cls.verify_team_quota(king.team_quota)
            if quota_validation.is_failure():
                return ValidationResult.failure(quota_validation.exception)
            # Verify the ransom
            ransom_validation = cls.verify_ransom(king.ransom)
            if ransom_validation.is_failure():
                return ValidationResult.failure(ransom_validation.exception)
            
            # If all the checks pass return the certified King.
            return ValidationResult.success(king)
        # Finally, if there is an unhandled exception wap an InvalidKingException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidKingException(ex=ex, message=f"{method}: {InvalidKingException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_id(
            cls,
            candidate: Any,
            rank_spec: RankSpec = RankSpec(),
            idservice: IdentityService = IdentityService(),
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Verify candidate is a safe id using identity_service. If so convert to id. Else return failure.
        2.  Check if id != Catalog.KING.id. If not, return failure.
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
            *   NotKingIdException
            *   InvalidKingException
        """
        method = "KingValidator.verify_id"
        try:
            # Test if the candidate is a safe id.
            validation = idservice.validate_id(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if id is correct for a king.
            id = validation.payload
            if id != rank_spec.KING.id:
                return ValidationResult.failure(
                    NotKingIdException(f"{method}: {NotKingIdException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified king.id inside a ValidationResult.
            return ValidationResult.success(id)
        
        # Finally, if there is an unhandled exception wap an InvalidKingException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidKingException(ex=ex, message=f"{method}: {InvalidKingException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_name(
            cls,
            candidate: Any,
            rank_spec: RankSpec = RankSpec(),
            idservice: IdentityService = IdentityService(),
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Verify candidate is a safe designation using identity_service. If so convert to designation. Else return failure.
        2.  Check if designation != Catalog.KING.designation. If not, return failure.
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
            *   NotKingNameException
            *   InvalidKingException
        """
        method = "KingValidator.verify_name"
        try:
            # Test if the candidate is a safe designation.
            validation = idservice.validate_name(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if designation is correct for a king.
            name = validation.payload
            if name.upper() != rank_spec.KING.name.upper():
                return ValidationResult.failure(
                    NotKingNameException(f"{method}: {NotKingNameException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified king.designation inside a ValidationResult.
            return ValidationResult.success(name)
        # Finally, if there is an unhandled exception Wrap an InvalidKingException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidKingException(ex=ex, message=f"{method}: {InvalidKingException.DEFAULT_MESSAGE}")
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
        1.  Verify candidate is a safe number using number_validator. If so convert to number. Else return failure.
        2.  Check if ransom != Catalog.KING.ransom. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   rank_spec (Catalog)
            *   number_validator (NumberValidator)

        # Returns:
        ValidationResult[int] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotKingRansomException
            *   InvalidKingException
        """
        method = "KingValidator.verify_ransom"
        try:
            # Test if the candidate is a safe id.
            validation = number_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if id is correct for a king.
            ransom = validation.payload
            if ransom != rank_spec.KING.ransom:
                return ValidationResult.failure(
                    NotKingRansomException(f"{method}: {NotKingRansomException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified king.ransom inside a ValidationResult.
            return ValidationResult.success(ransom)
        
        # Finally, if there is an unhandled exception wrap an InvalidKingException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidKingException(ex=ex, message=f"{method}: {InvalidKingException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_designation(
            cls,
            candidate: Any,
            rank_spec: RankSpec = RankSpec(),
            text_validator: TextValidator = TextValidator(),
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Verify candidate is a safe string using text_validator. If so convert to string. Else return failure.
        2.  Check if string != Catalog.KING.designation. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   rank_spec (Catalog)
            *   text_validator (TextValidator)

        # Returns:
        ValidationResult[str] containing either:
            - On success:   str in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotKingDesignationException
            *   InvalidKingException
        """
        method = "KingValidator.verify_designation"
        try:
            # Test if the candidate is a safe designation.
            validation = text_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if designation is correct for a king.
            designation = validation.payload
            if designation.upper() != rank_spec.KING.designation.upper():
                return ValidationResult.failure(
                    NotKingDesignationException(f"{method}: {NotKingDesignationException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified king.designation inside a ValidationResult.
            return ValidationResult.success(designation)
        
        # Finally, if there is an unhandled exception wrap an InvalidKingException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidKingException(ex=ex, message=f"{method}: {InvalidKingException.DEFAULT_MESSAGE}")
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
        1.  Verify candidate is a safe number using number_validator. If so convert to number. Else return failure.
        2.  Check if ransom != Catalog.KING.team_quota. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   rank_spec (Catalog)
            *   number_validator (NumberValidator)

        # Returns:
        ValidationResult[int] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotKingQuotaException
            *   InvalidKingException
        """
        method = "KingValidator.verify_team_quota"
        try:
            # Test if the candidate is a safe number.
            validation = number_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if team_quota is correct for a king.
            team_quota = validation.payload
            if team_quota != rank_spec.KING.team_quota:
                return ValidationResult.failure(
                    NotKingQuotaException(f"{method}: {NotKingQuotaException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified king.team_quota inside a ValidationResult.
            return ValidationResult.success(team_quota)
        
        # Finally, if there is an unhandled exception wrap an InvalidKingException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidKingException(ex=ex, message=f"{method}: {InvalidKingException.DEFAULT_MESSAGE}")
            )