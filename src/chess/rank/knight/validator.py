# src/chess/rank/knight/validator_.py

"""
Module: chess.rank.knight.validator
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Any, cast

from chess.rank import (
    Knight, NotKnightIdException, NotKnightRansomException, RankSpec, NullKnightException,
    InvalidKnightException, NotKnightDesignationException, NotKnightNameException, NotKnightQuotaException,
)
from chess.system import (
    IdentityService, LoggingLevelRouter, NumberValidator, TextValidator, ValidationResult, Validator
)


class KnightValidator(Validator[Knight]):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    Verifies a candidate is an instance of Knight, that meets integrity requirements, before the candidate is used.

    # PROVIDES:
    ValidationResult[Knight] containing either:
        - On success: Knight in the payload.
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
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[Knight]:
        """
        # ACTION:
        1.  Check candidate is not validation.
        2.  Check if candidate is a Rank.
        3.  Cast to candidate to its subclass.
        4.  Validate
                *   id      ->  with id_validator
                *   name    ->  with name_validator
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
                    NullKnightException(f"{method}: {NullKnightException.DEFAULT_MESSAGE}")
                )
            if not isinstance(candidate, Knight):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a Knight got {type(candidate).__name__} instead.")
                )
            knight = cast(Knight, candidate)
            
            # Verify the id
            id_validation = cls.verify_id(knight.id)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            # Verify the name
            name_validation = cls.verify_name(knight.name)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            # Verify designation
            designation_validation = cls.verify_designation(knight.designation)
            if designation_validation.is_failure():
                return ValidationResult.failure(designation_validation.exception)
            # Verify the quota
            quota_validation = cls.verify_team_quota(knight.team_quota)
            if quota_validation.is_failure():
                return ValidationResult.failure(quota_validation.exception)
            # Verify the ransom
            ransom_validation = cls.verify_ransom(knight.ransom)
            if ransom_validation.is_failure():
                return ValidationResult.failure(ransom_validation.exception)
            
            # If all the checks pass return the certified Knight.
            return ValidationResult.success(knight)
        # Finally, if there is an unhandled exception wap an InvalidKnightException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidKnightException(ex=ex, message=f"{method}: {InvalidKnightException.DEFAULT_MESSAGE}")
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
        2.  Check if id != RankSpec.KNIGHT.id. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   rank_spec (RankSpec)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[int] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotKnightIdException
            *   InvalidKnightException
        """
        method = "KnightValidator.verify_id"
        try:
            # Test if the candidate is a safe id.
            validation = identity_service.validate_id(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if id is correct for a knight.
            id = validation.payload
            if id != rank_spec.KNIGHT.id:
                return ValidationResult.failure(
                    NotKnightIdException(f"{method}: {NotKnightIdException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified knight.id inside a ValidationResult.
            return ValidationResult.success(id)
        
        # Finally, if there is an unhandled exception wap an InvalidKnightException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidKnightException(ex=ex, message=f"{method}: {InvalidKnightException.DEFAULT_MESSAGE}")
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
        1.  Verify candidate is a safe name using identity_service. If so convert to name. Else return failure.
        2.  Check if name != RankSpec.KNIGHT.name. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   rank_spec (RankSpec)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[str] containing either:
            - On success:   str in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotKnightNameException
            *   InvalidKnightException
        """
        method = "KnightValidator.verify_name"
        try:
            # Test if the candidate is a safe name.
            validation = identity_service.validate_name(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if name is correct for a knight.
            name = validation.payload
            if name.upper() != rank_spec.KNIGHT.name.upper():
                return ValidationResult.failure(
                    NotKnightNameException(f"{method}: {NotKnightNameException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified knight.name inside a ValidationResult.
            return ValidationResult.success(name)
        # Finally, if there is an unhandled exception Wrap an InvalidKnightException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidKnightException(ex=ex, message=f"{method}: {InvalidKnightException.DEFAULT_MESSAGE}")
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
        2.  Check if ransom != RankSpec.KNIGHT.ransom. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   rank_spec (RankSpec)
            *   number_validator (NumberValidator)

        # Returns:
        ValidationResult[int] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotKnightRansomException
            *   InvalidKnightException
        """
        method = "KnightValidator.verify_ransom"
        try:
            # Test if the candidate is a safe id.
            validation = number_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if id is correct for a knight.
            ransom = validation.payload
            if ransom != rank_spec.KNIGHT.ransom:
                return ValidationResult.failure(
                    NotKnightRansomException(f"{method}: {NotKnightRansomException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified knight.ransom inside a ValidationResult.
            return ValidationResult.success(ransom)
        
        # Finally, if there is an unhandled exception wrap an InvalidKnightException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidKnightException(ex=ex, message=f"{method}: {InvalidKnightException.DEFAULT_MESSAGE}")
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
        2.  Check if string != RankSpec.KNIGHT.designation. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   rank_spec (RankSpec)
            *   text_validator (TextValidator)

        # Returns:
        ValidationResult[str] containing either:
            - On success:   str in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotKnightDesignationException
            *   InvalidKnightException
        """
        method = "KnightValidator.verify_designation"
        try:
            # Test if the candidate is a safe name.
            validation = text_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if name is correct for a knight.
            designation = validation.payload
            if designation.upper() != rank_spec.KNIGHT.designation.upper():
                return ValidationResult.failure(
                    NotKnightDesignationException(f"{method}: {NotKnightDesignationException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified knight.designation inside a ValidationResult.
            return ValidationResult.success(designation)
        
        # Finally, if there is an unhandled exception wrap an InvalidKnightException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidKnightException(ex=ex, message=f"{method}: {InvalidKnightException.DEFAULT_MESSAGE}")
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
        2.  Check if ransom != RankSpec.KNIGHT.team_quota. If not, return failure.
        3.  If all checks pass the id in a success validation result.

        # PARAMETERS:
            *   candidate (Any)
            *   rank_spec (RankSpec)
            *   number_validator (NumberValidator)

        # Returns:
        ValidationResult[int] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NotKnightQuotaException
            *   InvalidKnightException
        """
        method = "KnightValidator.verify_team_quota"
        try:
            # Test if the candidate is a safe number.
            validation = number_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            # Next check if team_quota is correct for a knight.
            team_quota = validation.payload
            if team_quota != rank_spec.KNIGHT.team_quota:
                return ValidationResult.failure(
                    NotKnightQuotaException(f"{method}: {NotKnightQuotaException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified knight.team_quota inside a ValidationResult.
            return ValidationResult.success(team_quota)
        
        # Finally, if there is an unhandled exception wrap an InvalidKnightException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidKnightException(ex=ex, message=f"{method}: {InvalidKnightException.DEFAULT_MESSAGE}")
            )