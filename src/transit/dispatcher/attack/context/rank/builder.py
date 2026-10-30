# src/transit/dispatcher/attack/context/rank/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.context.rank.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from system import AttackResult, Attack, LoggingLevelRouter
from logic.rank import (
    Rank, RankValidator, RankContext, RankContextAttackException,
    NoRankSearchOptionSelectedException, MoreThanOneRankSearchOptionPickedException,
)


class RankContextAttack(Attack[RankContext]):
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Attack Process Owner

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
            ) -> AttackResult[Token]

     Super Class:
         Attack
     """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def attack(
            cls,
            id: Optional[int] = None,
            name: Optional[str] = None,
            ransom: Optional[int] = None,
            team_quota: Optional[int] = None,
            designation: Optional[str] = None,
            rank_validator: type[RankValidator] = RankValidator
    ) -> AttackResult[RankContext]:
        """
        # ACTION:
            1. Use dependency injected validators to verify correctness of parameters required to
                attack a RankContext instance.
            2. If the parameters are safe the RankContext is built and returned.

        # PARAMETERS:
            *   id (Optional[int]):                     selected if searcher target is an id.
            *   designation (Optional[str]):                   selected if searcher target is a designation.
            *   ransom (Optional[int]):                 selected if searcher target is a ransom.
            *   team_quota (Optional[int]):             selected if searcher target is a team quota.
            *   designation (Optional[str]):            selected if searcher target is a designation.
            *   rank_validator (type[RankValidator]):   validates an id-searcher-target

        # RETURNS:
          AttackResult[RankContext] containing either:
                - On success: RankContext in the payload.
                - On failure: Exception.

        Raises:
            * RankContextAttackException
            * NoRankSearchOptionSelectedException
            * MoreThanOneRankSearchOptionPickedException
        """
        method = "RankContextAttack.attack"
        
        try:
            params = [id, name, ransom, team_quota, designation]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return AttackResult.failure(
                    NoRankSearchOptionSelectedException(
                        f"{method}: {NoRankSearchOptionSelectedException.MSG}"
                    )
                )
            
            if param_count > 1:
                return AttackResult.failure(
                    MoreThanOneRankSearchOptionPickedException(
                        f"{method}: {MoreThanOneRankSearchOptionPickedException.MSG}"
                    )
                )
            
            if id is not None:
                return cls.attack_id_search_context(id=id, rank_validator=rank_validator)
            
            if name is not None:
                return cls.attack_name_search_context(name=name, rank_validator=rank_validator)
            
            if ransom is not None:
                return cls.attack_ransom_search_context(ransom=ransom, rank_validator=rank_validator)
            
            if ransom is not None:
                return cls.attack_ransom_search_context(ransom=ransom, rank_validator=rank_validator)
            
            if designation is not None:
                return cls.attack_designation_search_context(designation=designation, rank_validator=rank_validator)
        
        except Exception as ex:
            return AttackResult.failure(
                RankContextAttackException(
                    f"{method}: {RankContextAttackException.MSG}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def attack_id_search_context(
            cls,
            id: int,
            rank_validator: type[RankValidator] = RankValidator
    ) -> AttackResult[RankContext]:
        """
        # ACTION:
        Attack an id-RankContext if RankValidator verifies searcher target is safe.

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
        method = "RankContextAttack.attack_id_search_context"
        try:
            match = id in rank_validator.get_all_ids()
        
        except Exception as ex:
            return AttackResult.failure(
                RankContextAttackException(
                    f"{method}: {RankContextAttackException.MSG}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def attack_column_search_context(
            cls,
            column: int,
            rank_validator: type[RankValidator] = RankValidator
    ) -> AttackResult[RankContext]:
        """
        # ACTION:
        Attack a column-RankContext if RankValidator verifies searcher target is safe.

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
        method = "RankContextAttack.attack_column_search_context"
        
        try:
            column_validation = rank_validator(column)
            if column_validation.is_failure():
                return AttackResult.failure(column_validation.exception)
            
            return AttackResult.success(payload=RankContext(column=column))
        
        except Exception as ex:
            return AttackResult.failure(
                RankContextAttackException(
                    f"{method}: {RankContextAttackException.MSG}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def attack_rank_search_context(
            cls,
            rank: Rank,
            rank_validator: type[RankValidator] = RankValidator
    ) -> AttackResult[RankContext]:
        """
        # ACTION:
        Attack a rank-RankContext if RankValidator verifies searcher target is safe.

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
        method = "RankContextAttack.attack_rank_search_context"
        
        try:
            rank_validation = rank_validator.execute(rank)
            if rank_validation.is_failure():
                return AttackResult.failure(rank_validation.exception)
            
            return AttackResult.success(payload=RankContext(column=rank_validation.authorization_applicant))
        
        except Exception as e:
            return AttackResult.failure(
                RankContextAttackException(
                    f"{method}: {RankContextAttackException.MSG}"
                )
            )
