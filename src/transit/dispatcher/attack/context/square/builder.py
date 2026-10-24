# src/transit/dispatcher/attack/context/square/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.context.square.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


class SquareContextAttack(Attack[SquareContext]):
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
            name: Optional[str] = None,
            coord: Optional[Coord] = None,
            board: Optional[Board] = None,
            token: Optional[Token] = None,
            state: Optional[SquareState] = None,
            token_service: TokenService = TokenService(),
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
            square_validator: SquareValidator = SquareValidator(),
    ) -> AttackResult[SquareContext]:
        """
        # ACTION:
            1.  If the rank fails either
                    *   A null check.
                    *   A type check.
                Send an exception chain in the ValidationResult. Else, cast rank to SquareContext
                instance context.
            2.  Send an exception chain in the AttackResult if either
                    *   One and only one of attributes is not null.
                    *   There is no attack route for the enabled option.
                    *   The enabled attribute does not pass a validation check. by its service.
                are does not pass a validation check. by their services.
            3.  Attack the appropriate context, sed the attack success result.
            
        Args:
            id: Optional[int]
            name: Optional[str]
            coord: Optional[Coord]
            board: Optional[Board]
            token: Optional[Token]
            state: Optional[SquareState]
            board_service: BoardService
            coord_service: CoordService
            token_service: TokenService
            identity_service: IdentityService
            
        Returns:
            AttackResult[SquareContext]
            
        Raises:
            SquareContextAttackException
            ZeroSquareContextFlagsException
            ExcessSquareContextFlagsException
            SquareContextAttackRouteException
        """
        method = "SquareContextAttack.attack"

        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [id, name, coord, token,board, state,]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return AttackResult.failure(
                SquareContextAttackException(
                    msg=f"{method}: {SquareContextAttackException.MSG}",
                    ex=ZeroSquareContextFlagsException(
                        f"{method}: {ZeroSquareContextFlagsException.MSG}"
                    )
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return AttackResult.failure(
                SquareContextAttackException(
                    msg=f"{method}: {SquareContextAttackException.MSG}",
                    ex=ExcessSquareContextFlagsException(
                        f"{method}: {ExcessSquareContextFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation/attack branch. ---#
        
        # Attack the id SquareContext if its flag is enabled.
        if id is not None:
            validation = identity_service.validate_id(candidate=id)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    SquareContextAttackException(
                        msg=f"{method}: {SquareContextAttackException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_SquareContext in the AttackResult.
            return AttackResult.success(SquareContext(id=id))
        
        # Attack the schema SquareContext if its flag is enabled.
        if name is not None:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    SquareContextAttackException(
                        msg=f"{method}: {SquareContextAttackException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a name_SquareContext in the AttackResult.
            return AttackResult.success(SquareContext(name=name))
        
        # Attack the coord SquareContext if its flag is enabled.
        if coord is not None:
            validation = coord_service.execute.execute(coord)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    SquareContextAttackException(
                        msg=f"{method}: {SquareContextAttackException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a coord_SquareContext in the AttackResult.
            return AttackResult.success(SquareContext(coord=coord))
        
        # Attack the board SquareContext if its flag is enabled.
        if board is not None:
            validation = board_service.execute.execute(job=board)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    SquareContextAttackException(
                        msg=f"{method}: {SquareContextAttackException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a board_SquareContext in the AttackResult.
            return AttackResult.success(SquareContext(board=board))
        
        # Attack the state SquareContext if its flag is enabled.
        if token is not None:
            validation = square_validator.execute_square_state(candidate=state)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    SquareContextAttackException(
                        msg=f"{method}: {SquareContextAttackException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a state_SquareContext in the AttackResult.
            return AttackResult.success(SquareContext(state=state))
        
        # Return the exception chain if there is no attack route for the context.
        return AttackResult.failure(
            SquareContextAttackException(
                msg=f"{method}: {SquareContextAttackException.MSG}",
                ex=SquareContextAttackRouteException(f"{method}: {SquareContextAttackRouteException.MSG}")
            )
        )