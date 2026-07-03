# src/builder/context/token/builder.py

"""
Module: builder.context.token.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class TokenContextBuilder(Builder[TokenContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

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
            ) -> BuildResult[Token]

     Super Class:
         Builder
     """
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            id: Optional[int] = None,
            team: Optional[Team] = None,
            rank: Optional[Rank] = None,
            ransom: Optional[int] = None,
            color: Optional[GameColor] = None,
            designation: Optional[str] = None,
            current_position: Optional[Coord] = None,
            opening_square_name: Optional[str] = None,
            workers: TokenContextIntegrityWorkers = TokenContextIntegrityWorkers(),
    ) -> BuildResult[TokenContext]:
        """
        Build a TokenContext
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following
                occur
                    -   No optional param is enabled.
                    -   More than one optional param is enabled.
                    -   The enabled attribute fails a validation test.
                    -   There is no build logic for the enabled attribute.
            2.  Otherwise, build the TokenContext then, send the success result.
        Args:
            id: Optional[int]
            team: Optional[Team]
            rank: Optional[Rank]
            ransom: Optional[int]
            color: Optional[GameColor]
            designation: Optional[str]
            current_position: Optional[Coord]
            opening_square_name: Optional[str]
            workers: TokenContextIntegrityWorkers
        Returns:
            BuildResult[TokenContext]
        Raises:
            TokenContextBuilderException
            ZeroTokenContextFlagsException
            TokenContextBuildRouteException
            ExcessTokenContextFlagsException
        """
        method = f"{cls.__name__}.build"
        
        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [
            id,
            team,
            rank,
            color,
            ransom,
            designation,
            current_position,
            opening_square_name,
        ]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenContextBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=TokenContextBuilderException.OP,
                    msg=TokenContextBuilderException.MSG,
                    err_code=TokenContextBuilderException.ERR_CODE,
                    mthd_rslt_type=TokenContextBuilderException.MTHD_RSLT,
                    ex=ZeroTokenContextFlagsException(
                        msg=ZeroTokenContextFlagsException.MSG,
                        err_code=ZeroTokenContextFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenContextBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=TokenContextBuilderException.OP,
                    msg=TokenContextBuilderException.MSG,
                    err_code=TokenContextBuilderException.ERR_CODE,
                    mthd_rslt_type=TokenContextBuilderException.MTHD_RSLT,
                    ex=ExcessTeamContextFlagsException(
                        msg=ExcessTeamContextFlagsException.MSG,
                        err_code=ExcessTeamContextFlagsException.ERR_CODE,
                    )
                )
            )
        #--- Route to the appropriate validation/build branch. ---#
        
        # Build the id TokenContext if its flag is enabled.
        if id is not None:
            validation = workers.identity_service.validate_id(id)
            if validation.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuilderException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextBuilderException.OP,
                        msg=TokenContextBuilderException.MSG,
                        err_code=TokenContextBuilderException.ERR_CODE,
                        mthd_rslt_type=TokenContextBuilderException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return BuildResult.success(TokenContext(id=id))
        
        # Build the designation TokenContext if its flag is enabled.
        if designation is not None:
            validation = workers.identity_service.validate_name(designation)
            if validation.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuilderException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextBuilderException.OP,
                        msg=TokenContextBuilderException.MSG,
                        err_code=TokenContextBuilderException.ERR_CODE,
                        mthd_rslt_type=TokenContextBuilderException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return BuildResult.success(TokenContext(designation=designation))
        
        # Build the opening_square_name TokenContext if its flag is enabled.
        if opening_square_name is not None:
            validation = workers.identity_service.validate_name(opening_square_name)
            if validation.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuilderException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextBuilderException.OP,
                        msg=TokenContextBuilderException.MSG,
                        err_code=TokenContextBuilderException.ERR_CODE,
                        mthd_rslt_type=TokenContextBuilderException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return BuildResult.success(TokenContext(opening_square_name=opening_square_name))
        
        # Build the current_position TokenContext if its flag is enabled.
        if current_position is not None:
            validation = workers.coord_service.validator.execute(current_position)
            if validation.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuilderException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextBuilderException.OP,
                        msg=TokenContextBuilderException.MSG,
                        err_code=TokenContextBuilderException.ERR_CODE,
                        mthd_rslt_type=TokenContextBuilderException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return BuildResult.success(TokenContext(current_position=current_position))
        
        # Build the rank TokenContext if its flag is enabled.
        if rank is not None:
            validation = workers.rank_service.validator.execute(rank)
            if validation.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuilderException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextBuilderException.OP,
                        msg=TokenContextBuilderException.MSG,
                        err_code=TokenContextBuilderException.ERR_CODE,
                        mthd_rslt_type=TokenContextBuilderException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return BuildResult.success(TokenContext(rank=rank))
        
        # Build the team TokenContext if its flag is enabled.
        if team is not None:
            validation = workers.team_service.validator.execute(team)
            if validation.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuilderException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextBuilderException.OP,
                        msg=TokenContextBuilderException.MSG,
                        err_code=TokenContextBuilderException.ERR_CODE,
                        mthd_rslt_type=TokenContextBuilderException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller..
            return BuildResult.success(TokenContext(team=team))
        
        # Build the color TokenContext if its flag is enabled.
        if color is not None:
            validation = workers.color_validator.execute(color)
            if validation.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuilderException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextBuilderException.OP,
                        msg=TokenContextBuilderException.MSG,
                        err_code=TokenContextBuilderException.ERR_CODE,
                        mthd_rslt_type=TokenContextBuilderException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return BuildResult.success(TokenContext(color=color))
        
        # Build the ransom TokenContext if its flag is enabled.
        if ransom is not None:
            validation = workers.number_validator.execute(
                candidate=ransom,
                floor=workers.rank_service.persona_service.min_ransom,
                ceiling=workers.rank_service.persona_service.max_ransom
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuilderException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenContextBuilderException.OP,
                        msg=TokenContextBuilderException.MSG,
                        err_code=TokenContextBuilderException.ERR_CODE,
                        mthd_rslt_type=TokenContextBuilderException.MTHD_RSLT,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return BuildResult.success(TokenContext(ransom=ransom))
        
        # Handle the case that, there was no build route for the attribute
        return BuildResult.failure(
            TokenContextBuilderException(
                cls_mthd=method,
                cls_name=cls.__name__,
                op=TokenContextBuilderException.OP,
                msg=TokenContextBuilderException.MSG,
                err_code=TokenContextBuilderException.ERR_CODE,
                mthd_rslt_type=TokenContextBuilderException.MTHD_RSLT,
                ex=TokenContextBuildRouteException(
                    msg=TokenContextBuildRouteException.MSG,
                    err_code=TokenContextBuildRouteException.ERR_CODE,
                )
            )
        )
