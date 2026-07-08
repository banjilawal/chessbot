# src/rank/searcher/coord_stack_validator.py

"""
Module: logic.rank.searcher.coord_stack_validator
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from typing import Any, cast


from system import Validator, ValidationResult, LoggingLevelRouter
from logic.rank import (
    Rank, RankContext, InvalidRankContextException, NullRankContextException,
    MoreThanOneRankSearchOptionPickedException, NoRankSearchOptionSelectedException,
)

class RankContextValidator(Validator[RankContext]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1. Verify a rank is a RankContext that meets the application's safety contract before the client
        is allowed to use the RankContext object.
    2. Provide pluggable factories for validating different options separately.
    
    # PROVIDES:
      ValidationResult[RankContext] containing either:
            - On success: Rank in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    None
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
    ) -> ValidationResult[RankContext]:
        """
        # ACTION:
        Verifies rank is a RankContext in two steps.
            1. Test the rank is a valid SearchRankContext with a single searcher option switched on.
            2. Test the value passed to RankContext passes its validation contract.

        # PARAMETERS:
          * rank (Any): Object to verify is a Rank.
          * rank_validator (type[RankValidator]): Enforces safety requirements on row, column, rank targets.

          
        # RETURNS:
          ValidationResult[RankContext] containing either:
                - On success: RankContext in the payload.
                - On failure: Exception.

        Raises:
            * TypeError
            * InvalidRankContextException
            * NullRankContextException
            * NoRankSearchOptionSelectedException
            * MoreThanOneRankSearchOptionPickedException
        """
        method = "RankContextValidator.execute"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullRankContextException(f"{method} {NullRankContextException.MSG}")
                )
            
            if not isinstance(candidate, RankContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected RankContext, got {type(candidate).__column__} instead.")
                )
            
            rank_search_context = cast(RankContext, candidate)
            if len(rank_search_context.to_dict() == 0):
                return ValidationResult.failure(
                    NoRankSearchOptionSelectedException(
                        f"{method}: {NoRankSearchOptionSelectedException.MSG}"
                    )
                )
        
            if len(rank_search_context.to_dict()) > 1:
                return ValidationResult.failure(
                    MoreThanOneRankSearchOptionPickedException(
                        f"{method}: {MoreThanOneRankSearchOptionPickedException.MSG}"
                    )
                )
            
            return ValidationResult.success(payload=rank_search_context)
   
            
        except Exception as ex:
            return ValidationResult.failure(
                InvalidRankContextException(
                    f"{method}: {InvalidRankContextException.MSG}", ex
                )
            )
    #
    # @classmethod
    # @LoggingLevelRouter.monitor
    # def validate_row_search_option(
    #         cls,
    #         rank: Any,
    # ) -> ValidationResult[RankContext]:
    #     """
    #     # ACTION:
    #     Verify a row_candidate meets application RankContext safety requirements.
    #
    #     # PARAMETERS:
    #       * rank (Any): Object to verify is a row.
    #       * rank_validator (type[RankValidator]): Checks if rank complies with safety contract.
    #
    #     # RETURNS:
    #       ValidationResult[RankContext] containing either:
    #             - On success: RankContext in the payload.
    #             - On failure: Exception.
    #
    #     Raises:
    #         * InvalidRankContextException
    #     """
    #     method = "RankContextValidator.execute_id_search_option"
    #
    #     try:
    #         row_validation = rank_validator.execute_row(rank)
    #         if row_validation.is_failure():
    #             return ValidationResult.failure(row_validation.exception)
    #
    #         row = cast(int, row_validation.payload)
    #
    #         return ValidationResult.success(payload=RankContext(row=row))
    #     except Exception as ex:
    #         return ValidationResult.failure(
    #             InvalidRankContextException(
    #                 f"{method}: {InvalidRankContextException.MSG}",
    #                 ex
    #             )
    #         )
    #
    # @classmethod
    # @LoggingLevelRouter.monitor
    # def validate_column_search_option(
    #         cls,
    #         rank: Any,
    #         rank_validator: type[RankValidator] = RankValidator
    # ) -> ValidationResult[RankContext]:
    #     """
    #     # ACTION:
    #     Verify a column_candidate meets application RankContext safety requirements.
    #
    #     # PARAMETERS:
    #       * rank (Any): Object to verify is a column.
    #       * rank_validator (type[RankValidator]): Checks if rank complies with safety contract.
    #
    #     # RETURNS:
    #       ValidationResult[RankContext] containing either:
    #             - On success: RankContext in the payload.
    #             - On failure: Exception.
    #
    #     Raises:
    #         * InvalidRankContextException
    #     """
    #     method = "RankContextValidator.execute_column_search_option"
    #
    #     try:
    #         column_validation = rank_validator.execute(rank)
    #         if column_validation.is_failure():
    #             return ValidationResult.failure(column_validation.exception)
    #
    #         column = cast(str, column_validation.payload)
    #
    #         return ValidationResult.success(payload=RankContext(column=column))
    #     except Exception as ex:
    #         return ValidationResult.failure(
    #             InvalidRankContextException(
    #                 f"{method}: {InvalidRankContextException.MSG}",
    #                 ex
    #             )
    #         )
    #
    # @classmethod
    # @LoggingLevelRouter.monitor
    # def validate_rank_search_option(
    #         cls,
    #         rank: Any,
    #         rank_validator: type[RankValidator] = RankValidator
    # ) -> ValidationResult[RankContext]:
    #     """
    #     # ACTION:
    #     Verify a rank_candidate meets application RankContext safety requirements.
    #
    #     # PARAMETERS:
    #       * rank (Any): Object to verify is a rank.
    #       * rank_validator (type[RankValidator]): Checks if rank complies with safety contract.
    #
    #     # RETURNS:
    #       ValidationResult[RankContext] containing either:
    #             - On success: RankContext in the payload.
    #             - On failure: Exception.
    #
    #     Raises:
    #         * InvalidRankContextException
    #     """
    #     method = "RankContextValidator.execute_rank_search_option"
    #
    #     try:
    #         rank_validation = rank_validator.execute(rank)
    #         if rank_validation.is_failure():
    #             return ValidationResult.failure(rank_validation.exception)
    #
    #         rank = cast(Rank, rank_validation.payload)
    #
    #         return ValidationResult.success(payload=RankContext(rank=rank))
    #     except Exception as ex:
    #         return ValidationResult.failure(
    #             InvalidRankContextException(
    #                 f"{method}: {InvalidRankContextException.MSG}",
    #                 ex
    #             )
    #         )