# src/logic/schema/database/search/context/service/operation/build/builder.py

"""
Module: logic.schema.database.search.context.service.operation.build.builder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from catalog.schema import SchemaContextBuildException, SchemaContextBuildRouteException, ZeroSchemaContextFlagsException
from catalog.schema import SchemaContext, SchemaContextIntegrityWorkers
from system import BuildResult, Builder, GameColor, LoggingLevelRouter
from logic.team import ExcessTeamContextFlagsException


class SchemaContextBuilder(Builder[SchemaContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner
    
    Responsibilities:
        1.  SchemaContext creation process owner.
        2.  Ensure SchemaContext build resources meet satisfy contracts.
        3.  Guarantee new instances comply with business logic at birth.
    
    Attributes:
    
    Provides:
        -   def build(
                name: Optional[str] = None,
                color: Optional[GameColor] = None,
                workers: SchemaContextIntegrityWorkers,
            ) -> BuildResult[SchemaContext]:
    
     Super Class:
         Builder
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            name: Optional[str] = None,
            color: Optional[GameColor] = None,
            workers: SchemaContextIntegrityWorkers = SchemaContextIntegrityWorkers(),
    ) -> BuildResult[SchemaContext]:
        """
        Build a SchemaContext
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following
                occur
                    -   No optional param is enabled.
                    -   More than one optional param is enabled.
                    -   The enabled attribute fails a validation test.
                    -   There is no build logic for the enabled attribute.
            2.  Otherwise, build the SchemaContext then, send the success result.
        Args:
            name: Optional[str]
            color: Optional[GameColor]
            workers: SchemaContextIntegrityWorkers
        Returns:
            BuildResult[SchemaContext]
        Raises:
            SchemaContextBuildException
            ZeroSchemaContextFlagsException
            SchemaContextBuildRouteException
            ExcessSchemaContextFlagsException
        """
        method = f"{cls.__name__}.build"
        
        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [name, color,]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SchemaContextBuildException(
                    mthd=method,
                    title=cls.__name__,
                    op=SchemaContextBuildException.OP,
                    msg=SchemaContextBuildException.MSG,
                    err_code=SchemaContextBuildException.ERR_CODE,
                    rslt_type=SchemaContextBuildException.RSLT_TYPE,
                    ex=ZeroSchemaContextFlagsException(
                        msg=ZeroSchemaContextFlagsException.MSG,
                        err_code=ZeroSchemaContextFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SchemaContextBuildException(
                    mthd=method,
                    title=cls.__name__,
                    op=SchemaContextBuildException.OP,
                    msg=SchemaContextBuildException.MSG,
                    err_code=SchemaContextBuildException.ERR_CODE,
                    rslt_type=SchemaContextBuildException.RSLT_TYPE,
                    ex=ExcessTeamContextFlagsException(
                        msg=ExcessTeamContextFlagsException.MSG,
                        err_code=ExcessTeamContextFlagsException.ERR_CODE,
                    )
                )
            )
        #--- Route to the appropriate validation/build branch. ---#
        
        # Build the name SchemaContext if its flag is enabled.
        if name is not None:
            validation = workers.identity_service.validate_name(name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SchemaContextBuildException(
                        mthd=method,
                        title=cls.__name__,
                        op=SchemaContextBuildException.OP,
                        msg=SchemaContextBuildException.MSG,
                        err_code=SchemaContextBuildException.ERR_CODE,
                        rslt_type=SchemaContextBuildException.RSLT_TYPE,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return BuildResult.success(SchemaContext(name=name))
        
        # Build the color SchemaContext if its flag is enabled.
        if color is not None:
            validation = workers.color_validator.validate(color)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SchemaContextBuildException(
                        mthd=method,
                        title=cls.__name__,
                        op=SchemaContextBuildException.OP,
                        msg=SchemaContextBuildException.MSG,
                        err_code=SchemaContextBuildException.ERR_CODE,
                        rslt_type=SchemaContextBuildException.RSLT_TYPE,
                        ex=validation.exception,
                    )
                )
            # On validation success forward the work product to the caller.
            return BuildResult.success(SchemaContext(color=color))

        # Handle the case that, there was no build route for the attribute
        return BuildResult.failure(
            SchemaContextBuildException(
                mthd=method,
                title=cls.__name__,
                op=SchemaContextBuildException.OP,
                msg=SchemaContextBuildException.MSG,
                err_code=SchemaContextBuildException.ERR_CODE,
                rslt_type=SchemaContextBuildException.RSLT_TYPE,
                ex=SchemaContextBuildRouteException(
                    msg=SchemaContextBuildRouteException.MSG,
                    err_code=SchemaContextBuildRouteException.ERR_CODE,
                )
            )
        )
