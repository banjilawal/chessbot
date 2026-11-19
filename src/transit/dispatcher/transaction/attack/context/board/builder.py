# src/transit/dispatcher/attack/context/board/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.context.board.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional

from logic.arena import Arena, ArenaService
from system import Attack, AttackResult, IdentityService
from logic.board import (
    BoardContextAttackRouteException, ZeroBoardContextFlagsException, BoardContext, BoardContextAttackException,
    ArenaBoardContextFlagsException
)

class BoardContextAttack(Attack[BoardContext]):
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
    def attack(
            cls,
            id: Optional[int] = None,
            arena: Optional[Arena] = None,
            arena_service: ArenaService = ArenaService(),
            identity_service: IdentityService = IdentityService(),
    ) -> AttackResult[BoardContext]:
        """
        # ACTION:
            1.  If one-and-only-one context attribute is not null send an exception chain in the AttackResult.
            2.  If there is no attack route for the not-null context attribute send an exception chain in the AttackResult.
            3.  If the attack route exists and the context attribute is not verified send an exception chain in the
                AttackResult. Else attack the context and send it in the AttackResult's payload.
        # PARAMETERS:
            Only one these must be provided:
                *   id Optional[(int)]
                *   arena Optional[(Arena)]
            These Parameters must be provided:
                *   arena_service (ArenaService)
                *   identity_service (IdentityService)
        # RETURNS:
            *   AttackResult[BoardContext] containing either:
                    - On failure: Exception.
                    - On success: BoardContext in the payload.
        Raises:
            *   ZeroBoardContextFlagsException
            *   BoardContextAttackException
            *   ArenaBoardContextFlagsException
            *   BoardContextAttackRouteException
        """
        method = "BoardContextAttack.attack"
        
        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [id, arena]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return AttackResult.failure(
                BoardContextAttackException(
                    msg=f"{method}: {BoardContextAttackException.MSG}",
                    ex=ZeroBoardContextFlagsException(
                        f"{method}: {ZeroBoardContextFlagsException.MSG}"
                    )
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return AttackResult.failure(
                BoardContextAttackException(
                    msg=f"{method}: {BoardContextAttackException.MSG}",
                    ex=ArenaBoardContextFlagsException(
                        f"{method}: {ArenaBoardContextFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation/attack branch. ---#
        
        # Attack the id BoardContext if its flag is enabled.
        if id is not None:
            validation = identity_service.validate_id(candidate=id)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    BoardContextAttackException(
                        msg=f"{method}: {BoardContextAttackException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_BoardContext in the AttackResult.
            return AttackResult.success(BoardContext(id=id))
        
        # Attack the arena BoardContext if its flag is enabled.
        if arena is not None:
            validation = arena_service.execute.search_service(arena)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    BoardContextAttackException(
                        msg=f"{method}: {BoardContextAttackException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a arena_BoardContext in the AttackResult.
            return AttackResult.success(BoardContext(arena=arena))
        
        # Return the exception chain if there is no attack route for the context.
        return AttackResult.failure(
            BoardContextAttackException(
                msg=f"{method}: {BoardContextAttackException.MSG}",
                ex=BoardContextAttackRouteException(f"{method}: {BoardContextAttackRouteException.MSG}")
            )
        )