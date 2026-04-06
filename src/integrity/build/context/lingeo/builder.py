# src/integrity/build/context/linegeo/builder.py

"""
Module: integrity.build.context.linegeo.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from err import ExcessLinGeoContextFlagsException, LinGeoContextBuildException
from integrity import Builder
from model import Coord, LinGeoContext, Vector
from result import BuildResult
from tool import LinGeoContextToolSet

class LinGeoContextBuilder(Builder[LinGeoContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new LinGeoContext instance is born safe and reliable.

    Attributes:

    Provides:
        -   def build(
                    coord: Optional[Coord] = None,
                    vector: Optional[Vector] = None,
                    tool_set: LinGeoContextToolSet
            ) -> BuildResult[LinGeoContext]:

     Super Class:
         Builder
     """
    @classmethod
    def build(
            cls,
            coord: Optional[Coord] = None,
            vector: Optional[Vector] = None,
            tool_set: LinGeoContextToolSet = LinGeoContextToolSet()
    ) -> BuildResult[LinGeoContext]:
        """
        Build a safe LinGeoContext.

        Action:
            1.  Send an exception in the BuildResult any of these conditions occur.
                    -   Both options are enabled.
                    -   Neither option is enabled.
                    -   Whichever attribute is set gets flgged by its validator.
            2.  Otherwise, build the LingeoContext.
            3.  Send the success result.
        Args:
            coord: Optional[Coord] = None,
            vector: Optional[Vector] = None,
            tool_set: LinGeoContextToolSet = LinGeoContextToolSet()
        Returns:
            BuildResult[LinGeoContext]
        Raises:
            TypeError
            LinGeoContextNullException
            ZeroLinGeoContextFlagsException
            LinGeoContextBuildException
            ExcessLinGeoContextFlagsException
        """
        method = f"{cls.__name__}.build"

        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [coord, vector]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                LinGeoContextBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=LinGeoContextBuildException.MSG,
                    err_code=LinGeoContextBuildException.ERR_CODE,
                    ex=ZeroLinGeoContextFlagsException(
                        msg=ZeroLinGeoContextFlagsException.MSG,
                        err_code=ZeroLinGeoContextFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                LinGeoContextBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=LinGeoContextBuildException.MSG,
                    err_code=LinGeoContextBuildException.ERR_CODE,
                    ex=ExcessLinGeoContextFlagsException(
                        msg=ExcessLinGeoContextFlagsException.MSG,
                        err_code=ExcessLinGeoContextFlagsException.ERR_CODE,
                    )
                )
            )
        # --- Route to the appropriate Build/build branch. ---#
   
        
        # Build the coord LinGeoContext if its flag is enabled.
        if coord is not None:
            build_result = tool_set.coord_service.validator.validate(coord)
            if build_result.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    LinGeoContextBuildException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=LinGeoContextBuildException.MSG,
                        err_code=LinGeoContextBuildException.ERR_CODE,
                        ex=ExcessLinGeoContextFlagsException(
                            msg=ExcessLinGeoContextFlagsException.MSG,
                            err_code=ExcessLinGeoContextFlagsException.ERR_CODE,
                        )
                    )
                )
            # On Build success, forward the work product.
            return BuildResult.success(LinGeoContext(coord=coord))
        
        # Deal with the alternate case.
        build_result = tool_set.vector_service.validator.validate(vector)
        if build_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                LinGeoContextBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=LinGeoContextBuildException.MSG,
                    err_code=LinGeoContextBuildException.ERR_CODE,
                    ex=build_result.exception
                )
            )
        # --- Forward the work product to the caller ---#
        return BuildResult.success(LinGeoContext(vector=vector))
            