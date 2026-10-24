# src/transit/dispatcher/attack/context/token/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.context.token.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


class TokenContextAttack(Attack[TokenContext]):
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
            team: Optional[Team] = None,
            rank: Optional[Rank] = None,
            ransom: Optional[int] = None,
            color: Optional[GameColor] = None,
            designation: Optional[str] = None,
            current_position: Optional[Coord] = None,
            home_square_name: Optional[str] = None,
            workers: TokenContextIntegrityWorkers = TokenContextIntegrityWorkers(),
    ) -> AttackResult[TokenContext]:
        """
        Attack a TokenContext
        
        Action:
            1.  Send an exception chain in the AttackResult if any of the following
                occur
                    - No optional param is enabled.
                    - More than one optional param is enabled.
                    - The enabled attribute fails a validation test.
                    - There is no attack logic for the enabled attribute.
            2.  Otherwise, attack the TokenContext then, send the success result.
        Args:
            id: Optional[int]
            team: Optional[Team]
            rank: Optional[Rank]
            ransom: Optional[int]
            color: Optional[GameColor]
            designation: Optional[str]
            current_position: Optional[Coord]
            home_square_name: Optional[str]
            workers: TokenContextIntegrityWorkers
        Returns:
            AttackResult[TokenContext]
        Raises:
            TokenContextAttackException
            ZeroTokenContextFlagsException
            TokenContextAttackRouteException
            ExcessTokenContextFlagsException
        """
        method = f"{cls.__name__}.attack"
        
        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [
            id,
            team,
            rank,
            color,
            ransom,
            designation,
            current_position,
            home_square_name,
        ]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return AttackResult.failure(
                TokenContextAttackException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=TokenContextAttackException.OP,
                    msg=TokenContextAttackException.MSG,
                    err_code=TokenContextAttackException.ERR_CODE,
                    mthd_rslt_type=TokenContextAttackException.MTHD_RSLT,
                    ex=ZeroTokenContextFlagsException(
                        msg=ZeroTokenContextFlagsException.MSG,
                        err_code=ZeroTokenContextFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return AttackResult.failure(
                TokenContextAttackException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=TokenContextAttackException.OP,
                    msg=TokenContextAttackException.MSG,
                    err_code=TokenContextAttackException.ERR_CODE,
                    mthd_rslt_type=TokenContextAttackException.MTHD_RSLT,
                    ex=ExcessTeamContextFlagsException(
                        msg=ExcessTeamContextFlagsException.MSG,
                        err_code=ExcessTeamContextFlagsException.ERR_CODE,
                    )
                )
            )
        #--- Route to the appropriate validation/attack branch. ---#
        
        # Attack the id TokenContext if its flag is enabled.
        if id is not None:
            validation = workers.identity_service.validate_id(id)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    TokenContextAttackException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextAttackException.OP,
                        msg=TokenContextAttackException.MSG,
                        err_code=TokenContextAttackException.ERR_CODE,
                        mthd_rslt_type=TokenContextAttackException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return AttackResult.success(TokenContext(id=id))
        
        # Attack the designation TokenContext if its flag is enabled.
        if designation is not None:
            validation = workers.identity_service.validate_name(designation)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    TokenContextAttackException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextAttackException.OP,
                        msg=TokenContextAttackException.MSG,
                        err_code=TokenContextAttackException.ERR_CODE,
                        mthd_rslt_type=TokenContextAttackException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return AttackResult.success(TokenContext(designation=designation))
        
        # Attack the home_square_name TokenContext if its flag is enabled.
        if home_square_name is not None:
            validation = workers.identity_service.validate_name(home_square_name)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    TokenContextAttackException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextAttackException.OP,
                        msg=TokenContextAttackException.MSG,
                        err_code=TokenContextAttackException.ERR_CODE,
                        mthd_rslt_type=TokenContextAttackException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return AttackResult.success(TokenContext(home_square_name=home_square_name))
        
        # Attack the current_position TokenContext if its flag is enabled.
        if current_position is not None:
            validation = workers.coord_service.execute.execute(current_position)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    TokenContextAttackException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextAttackException.OP,
                        msg=TokenContextAttackException.MSG,
                        err_code=TokenContextAttackException.ERR_CODE,
                        mthd_rslt_type=TokenContextAttackException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return AttackResult.success(TokenContext(current_position=current_position))
        
        # Attack the rank TokenContext if its flag is enabled.
        if rank is not None:
            validation = workers.rank_service.execute.execute(rank)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    TokenContextAttackException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextAttackException.OP,
                        msg=TokenContextAttackException.MSG,
                        err_code=TokenContextAttackException.ERR_CODE,
                        mthd_rslt_type=TokenContextAttackException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return AttackResult.success(TokenContext(rank=rank))
        
        # Attack the team TokenContext if its flag is enabled.
        if team is not None:
            validation = workers.team_service.execute.execute(team)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    TokenContextAttackException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextAttackException.OP,
                        msg=TokenContextAttackException.MSG,
                        err_code=TokenContextAttackException.ERR_CODE,
                        mthd_rslt_type=TokenContextAttackException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller..
            return AttackResult.success(TokenContext(team=team))
        
        # Attack the color TokenContext if its flag is enabled.
        if color is not None:
            validation = workers.color_validator.execute(color)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    TokenContextAttackException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextAttackException.OP,
                        msg=TokenContextAttackException.MSG,
                        err_code=TokenContextAttackException.ERR_CODE,
                        mthd_rslt_type=TokenContextAttackException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return AttackResult.success(TokenContext(color=color))
        
        # Attack the ransom TokenContext if its flag is enabled.
        if ransom is not None:
            validation = workers.number_validator.execute(
                job=ransom,
                floor=workers.rank_service.persona_service.min_ransom,
                ceiling=workers.rank_service.persona_service.max_ransom
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    TokenContextAttackException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextAttackException.OP,
                        msg=TokenContextAttackException.MSG,
                        err_code=TokenContextAttackException.ERR_CODE,
                        mthd_rslt_type=TokenContextAttackException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return AttackResult.success(TokenContext(ransom=ransom))
        
        # Handle the case that there was no attack route for the attribute
        return AttackResult.failure(
            TokenContextAttackException(
                cls_mthd=method,
                cls_name=cls.__name__,
                op=TokenContextAttackException.OP,
                msg=TokenContextAttackException.MSG,
                err_code=TokenContextAttackException.ERR_CODE,
                mthd_rslt_type=TokenContextAttackException.MTHD_RSLT,
                ex=TokenContextAttackRouteException(
                    msg=TokenContextAttackRouteException.MSG,
                    err_code=TokenContextAttackRouteException.ERR_CODE,
                )
            )
        )
