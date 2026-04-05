# src/integrity/build/context/token/builder.py

"""
Module: integrity.build.context.token.builder
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
        -   Process Runner
    
    Responsibilities:
        1.  TokenContext creation process owner.
        2.  Ensure TokenContext build resources meet satisfy contracts.
        3.  Guarantee new instances comply with business logic at birth.
    
    Attributes:
    
    Provides:
        -   def build(
                    workers: TokenContextIntegrityWorkers,
                    id: Optional[int] = None,
                    team: Optional[Team] = None,
                    rank: Optional[Rank] = None,
                    ransom: Optional[int] = None,
                    current_position: Optional[Coord] = None,
                    color: Optional[GameColor] = None,
                    designation: Optional[str] = None,
                    opening_square_name: Optional[str] = None,
            ) -> BuildResult[TokenContext]:
    
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
            TokenContextBuildException
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
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenContextBuildException(
                    mthd=method,
                    title=cls.__name__,
                    op=TokenContextBuildException.OP,
                    msg=TokenContextBuildException.MSG,
                    err_code=TokenContextBuildException.ERR_CODE,
                    rslt_type=TokenContextBuildException.RSLT_TYPE,
                    ex=ZeroTokenContextFlagsException(
                        msg=ZeroTokenContextFlagsException.MSG,
                        err_code=ZeroTokenContextFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenContextBuildException(
                    mthd=method,
                    title=cls.__name__,
                    op=TokenContextBuildException.OP,
                    msg=TokenContextBuildException.MSG,
                    err_code=TokenContextBuildException.ERR_CODE,
                    rslt_type=TokenContextBuildException.RSLT_TYPE,
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
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuildException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenContextBuildException.OP,
                        msg=TokenContextBuildException.MSG,
                        err_code=TokenContextBuildException.ERR_CODE,
                        rslt_type=TokenContextBuildException.RSLT_TYPE,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return BuildResult.success(TokenContext(id=id))
        
        # Build the designation TokenContext if its flag is enabled.
        if designation is not None:
            validation = workers.identity_service.validate_name(designation)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuildException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenContextBuildException.OP,
                        msg=TokenContextBuildException.MSG,
                        err_code=TokenContextBuildException.ERR_CODE,
                        rslt_type=TokenContextBuildException.RSLT_TYPE,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return BuildResult.success(TokenContext(designation=designation))
        
        # Build the opening_square_name TokenContext if its flag is enabled.
        if opening_square_name is not None:
            validation = workers.identity_service.validate_name(opening_square_name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuildException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenContextBuildException.OP,
                        msg=TokenContextBuildException.MSG,
                        err_code=TokenContextBuildException.ERR_CODE,
                        rslt_type=TokenContextBuildException.RSLT_TYPE,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return BuildResult.success(TokenContext(opening_square_name=opening_square_name))
        
        # Build the current_position TokenContext if its flag is enabled.
        if current_position is not None:
            validation = workers.coord_service.validator.validate(current_position)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuildException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenContextBuildException.OP,
                        msg=TokenContextBuildException.MSG,
                        err_code=TokenContextBuildException.ERR_CODE,
                        rslt_type=TokenContextBuildException.RSLT_TYPE,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return BuildResult.success(TokenContext(current_position=current_position))
        
        # Build the rank TokenContext if its flag is enabled.
        if rank is not None:
            validation = workers.rank_service.validator.validate(rank)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuildException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenContextBuildException.OP,
                        msg=TokenContextBuildException.MSG,
                        err_code=TokenContextBuildException.ERR_CODE,
                        rslt_type=TokenContextBuildException.RSLT_TYPE,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return BuildResult.success(TokenContext(rank=rank))
        
        # Build the team TokenContext if its flag is enabled.
        if team is not None:
            validation = workers.team_service.validator.validate(team)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuildException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenContextBuildException.OP,
                        msg=TokenContextBuildException.MSG,
                        err_code=TokenContextBuildException.ERR_CODE,
                        rslt_type=TokenContextBuildException.RSLT_TYPE,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller..
            return BuildResult.success(TokenContext(team=team))
        
        # Build the color TokenContext if its flag is enabled.
        if color is not None:
            validation = workers.color_validator.validate(color)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuildException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenContextBuildException.OP,
                        msg=TokenContextBuildException.MSG,
                        err_code=TokenContextBuildException.ERR_CODE,
                        rslt_type=TokenContextBuildException.RSLT_TYPE,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return BuildResult.success(TokenContext(color=color))
        
        # Build the ransom TokenContext if its flag is enabled.
        if ransom is not None:
            validation = workers.number_validator.validate(
                candidate=ransom,
                floor=workers.rank_service.persona_service.min_ransom,
                ceiling=workers.rank_service.persona_service.max_ransom
            )
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TokenContextBuildException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenContextBuildException.OP,
                        msg=TokenContextBuildException.MSG,
                        err_code=TokenContextBuildException.ERR_CODE,
                        rslt_type=TokenContextBuildException.RSLT_TYPE,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return BuildResult.success(TokenContext(ransom=ransom))
        
        # Handle the case that, there was no build route for the attribute
        return BuildResult.failure(
            TokenContextBuildException(
                mthd=method,
                title=cls.__name__,
                op=TokenContextBuildException.OP,
                msg=TokenContextBuildException.MSG,
                err_code=TokenContextBuildException.ERR_CODE,
                rslt_type=TokenContextBuildException.RSLT_TYPE,
                ex=TokenContextBuildRouteException(
                    msg=TokenContextBuildRouteException.MSG,
                    err_code=TokenContextBuildRouteException.ERR_CODE,
                )
            )
        )
