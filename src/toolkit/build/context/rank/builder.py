# src/toolkit/context/rank/toolkit.py

"""
Module: toolkit.context.rank.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from system import ToolkitResult, Toolkit, LoggingLevelRouter
from logic.rank import (
    Rank, RankValidator, RankContext, RankContextToolkitException,
    NoRankSearchOptionSelectedException, MoreThanOneRankSearchOptionPickedException,
)


class RankContextToolkit(Toolkit[RankContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Toolkit Process Owner

   Responsibilities:
        1.  Ensure a new Token instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(
                    owner: Team,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    team_validator: TeamValidator,
            ) -> ToolkitResult[Token]

     Super Class:
         Toolkit
     """

    @LoggingLevelRouter.monitor
    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
            ransom: Optional[int] = None,
            team_quota: Optional[int] = None,
            designation: Optional[str] = None,
            rank_validator: type[RankValidator] = RankValidator
    ) -> ToolkitResult[RankContext]:
        """
        # ACTION:
            1. Use dependency injected validators to verify correctness of parameters required to
                toolkit a RankContext instance.
            2. If the parameters are safe the RankContext is built and returned.

        # PARAMETERS:
            *   id (Optional[int]):                     selected if searcher target is an id.
            *   designation (Optional[str]):                   selected if searcher target is a designation.
            *   ransom (Optional[int]):                 selected if searcher target is a ransom.
            *   team_quota (Optional[int]):             selected if searcher target is a team quota.
            *   designation (Optional[str]):            selected if searcher target is a designation.
            *   rank_validator (type[RankValidator]):   validates an id-searcher-target

        # RETURNS:
          ToolkitResult[RankContext] containing either:
                - On success: RankContext in the payload.
                - On failure: Exception.

        Raises:
            * RankContextToolkitException
            * NoRankSearchOptionSelectedException
            * MoreThanOneRankSearchOptionPickedException
        """
        method = "RankContextToolkit.toolkit"
        
        try:
            params = [id, name, ransom, team_quota, designation]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return ToolkitResult.failure(
                    NoRankSearchOptionSelectedException(
                        f"{method}: {NoRankSearchOptionSelectedException.MSG}"
                    )
                )
            
            if param_count > 1:
                return ToolkitResult.failure(
                    MoreThanOneRankSearchOptionPickedException(
                        f"{method}: {MoreThanOneRankSearchOptionPickedException.MSG}"
                    )
                )
            
            if id is not None:
                return cls.toolkit_id_search_context(id=id, rank_validator=rank_validator)
            
            if name is not None:
                return cls.toolkit_name_search_context(name=name, rank_validator=rank_validator)
            
            if ransom is not None:
                return cls.toolkit_ransom_search_context(ransom=ransom, rank_validator=rank_validator)
            
            if ransom is not None:
                return cls.toolkit_ransom_search_context(ransom=ransom, rank_validator=rank_validator)
            
            if designation is not None:
                return cls.toolkit_designation_search_context(designation=designation, rank_validator=rank_validator)
        
        except Exception as ex:
            return ToolkitResult.failure(
                RankContextToolkitException(
                    f"{method}: {RankContextToolkitException.MSG}", ex
                )
            )

    @LoggingLevelRouter.monitor
    def __init___id_search_context(
            self,
            id: int,
            rank_validator: type[RankValidator] = RankValidator
    ) -> ToolkitResult[RankContext]:
        """
        # ACTION:
        Toolkit an id-RankContext if RankValidator verifies searcher target is safe.

        # PARAMETERS:
          * row (int): target id
          * rank_validator (type[RankValidator]): validates target.

        # RETURNS:
          ValidationResult[RankContext] containing either:
                - On success: RankContext in the payload.
                - On failure: Exception.

        Raises:
            * InvalidRankContextException
        """
        method = "RankContextToolkit.toolkit_id_search_context"
        try:
            match = id in rank_validator.get_all_ids()
        
        except Exception as ex:
            return ToolkitResult.failure(
                RankContextToolkitException(
                    f"{method}: {RankContextToolkitException.MSG}", ex
                )
            )

    @LoggingLevelRouter.monitor
    def __init___column_search_context(
            self,
            column: int,
            rank_validator: type[RankValidator] = RankValidator
    ) -> ToolkitResult[RankContext]:
        """
        # ACTION:
        Toolkit a column-RankContext if RankValidator verifies searcher target is safe.

        # PARAMETERS:
          * column (int): target column
          * rank_validator (type[RankValidator]): validates target.

        # RETURNS:
          ValidationResult[RankContext] containing either:
                - On success: RankContext in the payload.
                - On failure: Exception.

        Raises:
            * InvalidRankContextException
        """
        method = "RankContextToolkit.toolkit_column_search_context"
        
        try:
            column_validation = rank_validator(column)
            if column_validation.is_failure():
                return ToolkitResult.failure(column_validation.exception)
            
            return ToolkitResult.success(payload=RankContext(column=column))
        
        except Exception as ex:
            return ToolkitResult.failure(
                RankContextToolkitException(
                    f"{method}: {RankContextToolkitException.MSG}", ex
                )
            )

    @LoggingLevelRouter.monitor
    def __init___rank_search_context(
            self,
            rank: Rank,
            rank_validator: type[RankValidator] = RankValidator
    ) -> ToolkitResult[RankContext]:
        """
        # ACTION:
        Toolkit a rank-RankContext if RankValidator verifies searcher target is safe.

        # PARAMETERS:
          * rank (Rank): target Rank
          * rank_validator (type[RankValidator]): validates target.

        # RETURNS:
          ValidationResult[RankContext] containing either:
                - On success: RankContext in the payload.
                - On failure: Exception.

        Raises:
            * InvalidRankContextException
        """
        method = "RankContextToolkit.toolkit_rank_search_context"
        
        try:
            rank_validation = rank_validator.execute(rank)
            if rank_validation.is_failure():
                return ToolkitResult.failure(rank_validation.exception)
            
            return ToolkitResult.success(payload=RankContext(column=rank_validation.payload))
        
        except Exception as e:
            return ToolkitResult.failure(
                RankContextToolkitException(
                    f"{method}: {RankContextToolkitException.MSG}"
                )
            )
