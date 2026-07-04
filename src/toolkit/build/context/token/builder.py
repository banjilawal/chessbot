# src/toolkit/context/token/toolkit.py

"""
Module: toolkit.context.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class TokenContextToolkit(Toolkit[TokenContext]):
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
    @classmethod
    @LoggingLevelRouter.monitor
    def __init__(
            self,
            id: Optional[int] = None,
            team: Optional[Team] = None,
            rank: Optional[Rank] = None,
            ransom: Optional[int] = None,
            color: Optional[GameColor] = None,
            designation: Optional[str] = None,
            current_position: Optional[Coord] = None,
            home_square_name: Optional[str] = None,
            workers: TokenContextIntegrityWorkers = TokenContextIntegrityWorkers(),
    ) -> ToolkitResult[TokenContext]:
        """
        Toolkit a TokenContext
        
        Action:
            1.  Send an exception chain in the ToolkitResult if any of the following
                occur
                    -   No optional param is enabled.
                    -   More than one optional param is enabled.
                    -   The enabled attribute fails a validation test.
                    -   There is no toolkit logic for the enabled attribute.
            2.  Otherwise, toolkit the TokenContext then, send the success result.
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
            ToolkitResult[TokenContext]
        Raises:
            TokenContextToolkitException
            ZeroTokenContextFlagsException
            TokenContextToolkitRouteException
            ExcessTokenContextFlagsException
        """
        method = f"{cls.__name__}.toolkit"
        
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
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                TokenContextToolkitException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=TokenContextToolkitException.OP,
                    msg=TokenContextToolkitException.MSG,
                    err_code=TokenContextToolkitException.ERR_CODE,
                    mthd_rslt_type=TokenContextToolkitException.MTHD_RSLT,
                    ex=ZeroTokenContextFlagsException(
                        msg=ZeroTokenContextFlagsException.MSG,
                        err_code=ZeroTokenContextFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                TokenContextToolkitException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=TokenContextToolkitException.OP,
                    msg=TokenContextToolkitException.MSG,
                    err_code=TokenContextToolkitException.ERR_CODE,
                    mthd_rslt_type=TokenContextToolkitException.MTHD_RSLT,
                    ex=ExcessTeamContextFlagsException(
                        msg=ExcessTeamContextFlagsException.MSG,
                        err_code=ExcessTeamContextFlagsException.ERR_CODE,
                    )
                )
            )
        #--- Route to the appropriate validation/toolkit branch. ---#
        
        # Toolkit the id TokenContext if its flag is enabled.
        if id is not None:
            validation = workers.identity_service.validate_id(id)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    TokenContextToolkitException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextToolkitException.OP,
                        msg=TokenContextToolkitException.MSG,
                        err_code=TokenContextToolkitException.ERR_CODE,
                        mthd_rslt_type=TokenContextToolkitException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return ToolkitResult.success(TokenContext(id=id))
        
        # Toolkit the designation TokenContext if its flag is enabled.
        if designation is not None:
            validation = workers.identity_service.validate_name(designation)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    TokenContextToolkitException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextToolkitException.OP,
                        msg=TokenContextToolkitException.MSG,
                        err_code=TokenContextToolkitException.ERR_CODE,
                        mthd_rslt_type=TokenContextToolkitException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return ToolkitResult.success(TokenContext(designation=designation))
        
        # Toolkit the home_square_name TokenContext if its flag is enabled.
        if home_square_name is not None:
            validation = workers.identity_service.validate_name(home_square_name)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    TokenContextToolkitException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextToolkitException.OP,
                        msg=TokenContextToolkitException.MSG,
                        err_code=TokenContextToolkitException.ERR_CODE,
                        mthd_rslt_type=TokenContextToolkitException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return ToolkitResult.success(TokenContext(home_square_name=home_square_name))
        
        # Toolkit the current_position TokenContext if its flag is enabled.
        if current_position is not None:
            validation = workers.coord_service.validate.build(current_position)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    TokenContextToolkitException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextToolkitException.OP,
                        msg=TokenContextToolkitException.MSG,
                        err_code=TokenContextToolkitException.ERR_CODE,
                        mthd_rslt_type=TokenContextToolkitException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return ToolkitResult.success(TokenContext(current_position=current_position))
        
        # Toolkit the rank TokenContext if its flag is enabled.
        if rank is not None:
            validation = workers.rank_service.validate.build(rank)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    TokenContextToolkitException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextToolkitException.OP,
                        msg=TokenContextToolkitException.MSG,
                        err_code=TokenContextToolkitException.ERR_CODE,
                        mthd_rslt_type=TokenContextToolkitException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return ToolkitResult.success(TokenContext(rank=rank))
        
        # Toolkit the team TokenContext if its flag is enabled.
        if team is not None:
            validation = workers.team_service.validate.build(team)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    TokenContextToolkitException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextToolkitException.OP,
                        msg=TokenContextToolkitException.MSG,
                        err_code=TokenContextToolkitException.ERR_CODE,
                        mthd_rslt_type=TokenContextToolkitException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller..
            return ToolkitResult.success(TokenContext(team=team))
        
        # Toolkit the color TokenContext if its flag is enabled.
        if color is not None:
            validation = workers.color_validator.build(color)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    TokenContextToolkitException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextToolkitException.OP,
                        msg=TokenContextToolkitException.MSG,
                        err_code=TokenContextToolkitException.ERR_CODE,
                        mthd_rslt_type=TokenContextToolkitException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return ToolkitResult.success(TokenContext(color=color))
        
        # Toolkit the ransom TokenContext if its flag is enabled.
        if ransom is not None:
            validation = workers.number_validator.build(
                candidate=ransom,
                floor=workers.rank_service.persona_service.min_ransom,
                ceiling=workers.rank_service.persona_service.max_ransom
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    TokenContextToolkitException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextToolkitException.OP,
                        msg=TokenContextToolkitException.MSG,
                        err_code=TokenContextToolkitException.ERR_CODE,
                        mthd_rslt_type=TokenContextToolkitException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return ToolkitResult.success(TokenContext(ransom=ransom))
        
        # Handle the case that, there was no toolkit route for the attribute
        return ToolkitResult.failure(
            TokenContextToolkitException(
                cls_mthd=method,
                cls_name=cls.__name__,
                op=TokenContextToolkitException.OP,
                msg=TokenContextToolkitException.MSG,
                err_code=TokenContextToolkitException.ERR_CODE,
                mthd_rslt_type=TokenContextToolkitException.MTHD_RSLT,
                ex=TokenContextToolkitRouteException(
                    msg=TokenContextToolkitRouteException.MSG,
                    err_code=TokenContextToolkitRouteException.ERR_CODE,
                )
            )
        )
