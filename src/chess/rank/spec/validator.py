# src/chess/rank/spec/validator.py

"""
Module: chess.rank.spec.validator
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from typing import Any, cast

from chess.rank import InvalidRankSpecException, NullRankSpecException, RankSpec
from chess.rank.spec.exception import (
    RankDesignationBoundsException, RankIdBoundsException, RankNameBoundsException,
    RankQuotaBoundsException, RankRansomBoundsException
)
from chess.system import (
    IdNullException, IdentityService, InvalidIdException, InvalidNameException, LoggingLevelRouter, NullNameException,
    NullNumberException,
    NullStringException, TextException,
    ValidationResult,
    Validator
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
        ## Validate signature:
               validate(candidate: Any) -> ValidationResult[RankSpec]:

        ## verify_id_in_spec signature:
               verify_id_in_spec(
                        candidate: Any,
                        team_spec_hedge: RankSpec = RankSpec(),
                ) -> ValidationResult[Int]:

        ## verify_name_in_spec signature:
               verify_name_in_spec(
                        candidate: Any,
                        team_spec_hedge: RankSpec = RankSpec(),
                ) -> ValidationResult[str]:

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
    def verify_in_id_spec(
            cls,
            candidate: Any
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Check candidate is not null and is an int instance. If both conditions are true
            cast to a number
        2.  If number is not inside the set of RankSpec.ids send a
            ValidationResult containing an exception.
        4.  If all checks pass return the id in a ValidationResult

        # PARAMETERS:
            *   candidate (Any)

        # Returns:
        ValidationResult[Int] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullRankSpecException
            *   TeamColorBoundsException
            *   InvalidIntException
        """
        method = "RankSpecValidator.verify_id_in_spec"
        
        try:
            # Start the error detection process.
            if candidate is None:
                return ValidationResult.failure(
                    IdNullException(f"{method}: {IdNullException.DEFAULT_MESSAGE}")
                )
            if not isinstance(candidate, int):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected int, got {type(candidate).__name__} instead.")
                )
            # cast candidate to Int for the last check.
            id = cast(int, candidate)
            
  
            if int() not in RankSpec.allowed_ids():
                return ValidationResult.failure(
                    RankIdBoundsException(f"{method}: {RankIdBoundsException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified color inside a ValidationResult.
            return ValidationResult.success(payload=id)
            
            # Finally, if there is an unhandled exception Wrap a InvalidIntException around it
            # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidIdException(ex=ex, message=f"{method}: {InvalidIdException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def verify_in_name_spec(
            cls,
            candidate: Any,
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[str]:
        """
        # ACTION:
        1.  Check candidate is not null and is a str instance. If both conditions are true
            cast to a str
        2.  If str is not inside the set of RankSpec.names send a
            ValidationResult containing an exception.
        4.  If all checks pass return the name in a ValidationResult

        # PARAMETERS:
            *   candidate (Any)
            *   team_spec_hedge (RankSpec)

        # Returns:
        ValidationResult[str] containing either:
            - On success:   str in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullStringException
            *   TeamNameBoundsException
            *   TextException
        """
        method = "RankSpecValidator.verify_name_in_spec"
        
        try:
            # Start the error detection process.
            name_validation = identity_service.validate_name(candidate)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            # Get the name from the validation payload on success.
            name = name_validation.payload
            
            if name.upper() not in RankSpec.allowed_upper_case_names():
                return ValidationResult.failure(
                    RankNameBoundsException(f"{method} {RankNameBoundsException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the name inside a ValidationResult.
            return ValidationResult.success(payload=name)
            
            # Finally, if there is an unhandled exception Wrap a TextException around it
            # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidNameException(ex=ex, message=f"{method} {InvalidNameException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_in_ransom_spec(
            cls,
            candidate: Any
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Check candidate is not null and is an int. If both conditions are true
            cast to an int otherwise return an exception inside the ValidationResult.
        2.  If value is not inside the set of RankSpec.ransoms send a
            ValidationResult containing an exception.
        4.  If all checks pass return the value in a ValidationResult

        # PARAMETERS:
            *   candidate (Any)

        # Returns:
        ValidationResult[Iint] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullNumberException
            *   TeamColorBoundsException
            *   InvalidIntException
        """
        method = "RankSpecValidator.verify_id_in_spec"
        
        try:
            # Start the error detection process.
            if candidate is None:
                return ValidationResult.failure(
                    NullNumberException(f"{method}: {NullNumberException.DEFAULT_MESSAGE}")
                )
            if not isinstance(candidate, int):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected int, got {type(candidate).__name__} instead.")
                )
            # cast candidate to Int for the last check.
            ransom = cast(int, candidate)
            
            if ransom not in RankSpec.allowed_ransoms():
                return ValidationResult.failure(
                    RankRansomBoundsException(f"{method}: {RankRansomBoundsException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified ransom value inside a ValidationResult.
            return ValidationResult.success(payload=ransom)
            
            # Finally, if there is an unhandled exception Wrap a InvalidIntException around it
            # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidIdException(ex=ex, message=f"{method}: {InvalidIdException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def verify_in_designation_spec(
            cls,
            candidate: Any,
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[str]:
        """
        # ACTION:
        1.  Check candidate is not null and is a str instance. If both conditions are true
            cast to a str
        2.  If str is not inside the set of RankSpec.names send a
            ValidationResult containing an exception.
        4.  If all checks pass return the name in a ValidationResult

        # PARAMETERS:
            *   candidate (Any)
            *   team_spec_hedge (RankSpec)

        # Returns:
        ValidationResult[str] containing either:
            - On success:   str in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullStringException
            *   TeamNameBoundsException
            *   TextException
        """
        method = "RankSpecValidator.verify_name_in_spec"
        
        try:
            # Start the error detection process.
            if candidate is None:
                return ValidationResult.failure(
                    NullStringException(f"{method}: {NullStringException.DEFAULT_MESSAGE}")
                )
            if not isinstance(candidate, str):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected str, got {type(candidate).__name__} instead.")
                )
            # Get the name from the validation payload on success.
            designation = cast(str, candidate)
            
            if designation.upper() not in RankSpec.allowed_upper_case_designations():
                return ValidationResult.failure(
                    RankDesignationBoundsException(f"{method} {RankDesignationBoundsException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the name inside a ValidationResult.
            return ValidationResult.success(payload=designation)
            
            # Finally, if there is an unhandled exception Wrap a TextException around it
            # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                TextException(ex=ex, message=f"{method} {TextException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_in_quota_spec(
            cls,
            candidate: Any
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Check candidate is not null and is an int instance. If both conditions are true
            cast to a number
        2.  If number is not inside the set of RankSpec.team_quotas send a
            ValidationResult containing an exception.
        4.  If all checks pass return the quota in a ValidationResult

        # PARAMETERS:
            *   candidate (Any)

        # Returns:
        ValidationResult[int] containing either:
            - On success:   int in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullNumberSpecException
            *   RankQuotaBoundsException
            *   InvalidNumberException
        """
        method = "RankSpecValidator.verify_in_quota_spec"
        
        try:
            # Start the error detection process.
            if candidate is None:
                return ValidationResult.failure(
                    NullNumberException(f"{method}: {NullNumberException.DEFAULT_MESSAGE}")
                )
            if not isinstance(candidate, int):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected int, got {type(candidate).__name__} instead.")
                )
            # cast candidate to Int for the last check.
            quota = cast(int, candidate)
            
            if quota not in RankSpec.allowed_quotas():
                return ValidationResult.failure(
                    RankQuotaBoundsException(f"{method}: {RankQuotaBoundsException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified color inside a ValidationResult.
            return ValidationResult.success(payload=id)
            
            # Finally, if there is an unhandled exception Wrap a InvalidIntException around it
            # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidNumberException(ex=ex, message=f"{method}: {InvalidNumberException.DEFAULT_MESSAGE}")
            )