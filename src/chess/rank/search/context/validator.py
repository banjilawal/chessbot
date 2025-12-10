# src/rank/searcher/context/coord_stack_validator.py

"""
Module: chess.rank.searcher.context.coord_stack_validator
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from typing import Any, cast


from chess.system import Validator, ValidationResult, LoggingLevelRouter
from chess.rank import (
    Rank, RankSearchContext, InvalidRankSearchContextException, NullRankSearchContextException,
    MoreThanOneRankSearchOptionPickedException, NoRankSearchOptionSelectedException,
)

class RankSearchContextValidator(Validator[RankSearchContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1. Verify a candidate is a RankSearchContext that meets the application's safety contract before the client
        is allowed to use the RankSearchContext object.
    2. Provide pluggable factories for validating different options separately.
    
    # PROVIDES:
      ValidationResult[RankSearchContext] containing either:
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
    ) -> ValidationResult[RankSearchContext]:
        """
        # Action:
        Verifies candidate is a RankSearchContext in two steps.
            1. Test the candidate is a valid SearchRankContext with a single searcher option switched on.
            2. Test the value passed to RankSearchContext passes its validation contract..

        # Parameters:
          * candidate (Any): Object to verify is a Rank.
          * rank_validator (type[RankValidator]): Enforces safety requirements on row, column, rank targets.

          
        # Returns:
          ValidationResult[RankSearchContext] containing either:
                - On success: RankSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * TypeError
            * InvalidRankSearchContextException
            * NullRankSearchContextException
            * NoRankSearchOptionSelectedException
            * MoreThanOneRankSearchOptionPickedException
        """
        method = "RankSearchContextValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullRankSearchContextException(f"{method} {NullRankSearchContextException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, RankSearchContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected RankSearchContext, got {type(candidate).__column__} instead.")
                )
            
            rank_search_context = cast(RankSearchContext, candidate)
            if len(rank_search_context.to_dict() == 0):
                return ValidationResult.failure(
                    NoRankSearchOptionSelectedException(
                        f"{method}: {NoRankSearchOptionSelectedException.DEFAULT_MESSAGE}"
                    )
                )
        
            if len(rank_search_context.to_dict()) > 1:
                return ValidationResult.failure(
                    MoreThanOneRankSearchOptionPickedException(
                        f"{method}: {MoreThanOneRankSearchOptionPickedException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(payload=rank_search_context)
   
            
        except Exception as ex:
            return ValidationResult.failure(
                InvalidRankSearchContextException(
                    f"{method}: {InvalidRankSearchContextException.DEFAULT_MESSAGE}", ex
                )
            )
    #
    # @classmethod
    # @LoggingLevelRouter.monitor
    # def validate_row_search_option(
    #         cls,
    #         candidate: Any,
    # ) -> ValidationResult[RankSearchContext]:
    #     """
    #     # Action:
    #     Verify a row_candidate meets application RankSearchContext safety requirements.
    #
    #     # Parameters:
    #       * candidate (Any): Object to verify is a row.
    #       * rank_validator (type[RankValidator]): Checks if candidate complies with safety contract.
    #
    #     # Returns:
    #       ValidationResult[RankSearchContext] containing either:
    #             - On success: RankSearchContext in the payload.
    #             - On failure: Exception.
    #
    #     # Raises:
    #         * InvalidRankSearchContextException
    #     """
    #     method = "RankSearchContextValidator.validate_id_search_option"
    #
    #     try:
    #         row_validation = rank_validator.validate_row(candidate)
    #         if row_validation.is_failure():
    #             return ValidationResult.failure(row_validation.exception)
    #
    #         row = cast(int, row_validation.payload)
    #
    #         return ValidationResult.success(payload=RankSearchContext(row=row))
    #     except Exception as ex:
    #         return ValidationResult.failure(
    #             InvalidRankSearchContextException(
    #                 f"{method}: {InvalidRankSearchContextException.DEFAULT_MESSAGE}",
    #                 ex
    #             )
    #         )
    #
    # @classmethod
    # @LoggingLevelRouter.monitor
    # def validate_column_search_option(
    #         cls,
    #         candidate: Any,
    #         rank_validator: type[RankValidator] = RankValidator
    # ) -> ValidationResult[RankSearchContext]:
    #     """
    #     # Action:
    #     Verify a column_candidate meets application RankSearchContext safety requirements.
    #
    #     # Parameters:
    #       * candidate (Any): Object to verify is a column.
    #       * rank_validator (type[RankValidator]): Checks if candidate complies with safety contract.
    #
    #     # Returns:
    #       ValidationResult[RankSearchContext] containing either:
    #             - On success: RankSearchContext in the payload.
    #             - On failure: Exception.
    #
    #     # Raises:
    #         * InvalidRankSearchContextException
    #     """
    #     method = "RankSearchContextValidator.validate_column_search_option"
    #
    #     try:
    #         column_validation = rank_validator.validate(candidate)
    #         if column_validation.is_failure():
    #             return ValidationResult.failure(column_validation.exception)
    #
    #         column = cast(str, column_validation.payload)
    #
    #         return ValidationResult.success(payload=RankSearchContext(column=column))
    #     except Exception as ex:
    #         return ValidationResult.failure(
    #             InvalidRankSearchContextException(
    #                 f"{method}: {InvalidRankSearchContextException.DEFAULT_MESSAGE}",
    #                 ex
    #             )
    #         )
    #
    # @classmethod
    # @LoggingLevelRouter.monitor
    # def validate_rank_search_option(
    #         cls,
    #         candidate: Any,
    #         rank_validator: type[RankValidator] = RankValidator
    # ) -> ValidationResult[RankSearchContext]:
    #     """
    #     # Action:
    #     Verify a rank_candidate meets application RankSearchContext safety requirements.
    #
    #     # Parameters:
    #       * candidate (Any): Object to verify is a rank.
    #       * rank_validator (type[RankValidator]): Checks if candidate complies with safety contract.
    #
    #     # Returns:
    #       ValidationResult[RankSearchContext] containing either:
    #             - On success: RankSearchContext in the payload.
    #             - On failure: Exception.
    #
    #     # Raises:
    #         * InvalidRankSearchContextException
    #     """
    #     method = "RankSearchContextValidator.validate_rank_search_option"
    #
    #     try:
    #         rank_validation = rank_validator.validate(candidate)
    #         if rank_validation.is_failure():
    #             return ValidationResult.failure(rank_validation.exception)
    #
    #         rank = cast(Rank, rank_validation.payload)
    #
    #         return ValidationResult.success(payload=RankSearchContext(rank=rank))
    #     except Exception as ex:
    #         return ValidationResult.failure(
    #             InvalidRankSearchContextException(
    #                 f"{method}: {InvalidRankSearchContextException.DEFAULT_MESSAGE}",
    #                 ex
    #             )
    #         )