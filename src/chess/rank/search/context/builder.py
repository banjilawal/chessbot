# src/chess/rank/searcher/context/factory.py

"""
Module: chess.rank.searcher.context.builder
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import Optional


from chess.system import BuildResult, Builder, LoggingLevelRouter
from chess.rank import (
    Rank, RankValidator, RankSearchContext, RankSearchContextBuildFailedException,
    NoRankSearchOptionSelectedException, MoreThanOneRankSearchOptionPickedException,
)


class RankSearchContextBuilder(Builder[RankSearchContext]):
    """
    # ROLE: Builder, Data Integrity Guarantor

    # RESPONSIBILITIES:
        1. Manage conintuction of RankSearch instances that can be used safely by the client.
        2. Ensure params for RankSearch creation have met the application's safety contract.
        3. Provide pluggable factories for creating different RankSearchContext products.


    # PROVIDES:
      ValidationResult[RankSearchContext] containing either:
            - On success: RankSearchContext in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            id: Optional[int] = None,
            name: Optional[str] = None,
            ransom: Optional[int] = None,
            team_quota: Optional[int] = None,
            designation: Optional[str] = None,
            rank_validator: type[RankValidator] = RankValidator
    ) -> BuildResult[RankSearchContext]:
        """
        # Action:
            1. Use dependency injected validators to verify correctness of parameters required to
                builder a RankSearchContext instance.
            2. If the parameters are safe the RankSearchContext is built and returned.

        # Parameters:
            *   id (Optional[int]):                     selected if searcher target is an id.
            *   name (Optional[str]):                   selected if searcher target is a name.
            *   ransom (Optional[int]):                 selected if searcher target is a ransom.
            *   team_quota (Optional[int]):             selected if searcher target is a team quota.
            *   designation (Optional[str]):            selected if searcher target is a designation.
            *   rank_validator (type[RankValidator]):   validates an id-searcher-target

        # Returns:
          BuildResult[RankSearchContext] containing either:
                - On success: RankSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * RankSearchContextBuildFailedException
            * NoRankSearchOptionSelectedException
            * MoreThanOneRankSearchOptionPickedException
        """
        method = "RankSearchContextBuilder.builder"
        
        try:
            params = [id, name, ransom, team_quota, designation]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return BuildResult.failure(
                    NoRankSearchOptionSelectedException(
                        f"{method}: {NoRankSearchOptionSelectedException.DEFAULT_MESSAGE}"
                    )
                )
            
            if param_count > 1:
                return BuildResult.failure(
                    MoreThanOneRankSearchOptionPickedException(
                        f"{method}: {MoreThanOneRankSearchOptionPickedException.DEFAULT_MESSAGE}"
                    )
                )
            
            if id is not None:
                return cls.build_id_search_context(id=id, rank_validator=rank_validator)
            
            if name is not None:
                return cls.build_name_search_context(name=name, rank_validator=rank_validator)
            
            if ransom is not None:
                return cls.build_ransom_search_context(ransom=ransom, rank_validator=rank_validator)
            
            if ransom is not None:
                return cls.build_ransom_search_context(ransom=ransom, rank_validator=rank_validator)
            
            if designation is not None:
                return cls.build_designation_search_context(designation=designation, rank_validator=rank_validator)
        
        except Exception as ex:
            return BuildResult.failure(
                RankSearchContextBuildFailedException(
                    f"{method}: {RankSearchContextBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_id_search_context(
            cls,
            id: int,
            rank_validator: type[RankValidator] = RankValidator
    ) -> BuildResult[RankSearchContext]:
        """
        # Action:
        Build an id-RankSearchContext if RankValidator verifies searcher target is safe.

        # Parameters:
          * row (int): target id
          * rank_validator (type[RankValidator]): validates target.

        # Returns:
          ValidationResult[RankSearchContext] containing either:
                - On success: RankSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * InvalidRankSearchContextException
        """
        method = "RankSearchContextBuilder.build_id_search_context"
        try:
            match = id in rank_validator.get_all_ids()
        
        except Exception as ex:
            return BuildResult.failure(
                RankSearchContextBuildFailedException(
                    f"{method}: {RankSearchContextBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_column_search_context(
            cls,
            column: int,
            rank_validator: type[RankValidator] = RankValidator
    ) -> BuildResult[RankSearchContext]:
        """
        # Action:
        Build a column-RankSearchContext if RankValidator verifies searcher target is safe.

        # Parameters:
          * column (int): target column
          * rank_validator (type[RankValidator]): validates target.

        # Returns:
          ValidationResult[RankSearchContext] containing either:
                - On success: RankSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * InvalidRankSearchContextException
        """
        method = "RankSearchContextBuilder.build_column_search_context"
        
        try:
            column_validation = rank_validator(column)
            if column_validation.is_failure():
                return BuildResult.failure(column_validation.exception)
            
            return BuildResult.success(payload=RankSearchContext(column=column))
        
        except Exception as ex:
            return BuildResult.failure(
                RankSearchContextBuildFailedException(
                    f"{method}: {RankSearchContextBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_rank_search_context(
            cls,
            rank: Rank,
            rank_validator: type[RankValidator] = RankValidator
    ) -> BuildResult[RankSearchContext]:
        """
        # Action:
        Build a rank-RankSearchContext if RankValidator verifies searcher target is safe.

        # Parameters:
          * rank (Rank): target Rank
          * rank_validator (type[RankValidator]): validates target.

        # Returns:
          ValidationResult[RankSearchContext] containing either:
                - On success: RankSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * InvalidRankSearchContextException
        """
        method = "RankSearchContextBuilder.build_rank_search_context"
        
        try:
            rank_validation = rank_validator.validate(rank)
            if rank_validation.is_failure():
                return BuildResult.failure(rank_validation.exception)
            
            return BuildResult.success(payload=RankSearchContext(column=rank_validation.payload))
        
        except Exception as e:
            return BuildResult.failure(
                RankSearchContextBuildFailedException(
                    f"{method}: {RankSearchContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
