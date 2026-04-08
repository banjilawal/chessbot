# src/integrity/build/context/linegeo/builder.py

"""
Module: integrity.build.context.linegeo.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from err import ExcessVectorContextFlagsException, VectorContextBuildException
from integrity import Builder
from model import Coord, VectorContext, Vector
from result import BuildResult
from toolkit  import VectorContextToolkit

class VectorContextBuilder(Builder[VectorContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new VectorContext instance is born safe and reliable.

    Attributes:

    Provides:
        -   def build(
                    coord: Optional[Coord] = None,
                    vector: Optional[Vector] = None,
                    toolkit : VectorContextToolkit
            ) -> BuildResult[VectorContext]:

     Super Class:
         Builder
     """
    @classmethod
    def build(
            cls,
            coord: Optional[Coord] = None,
            vector: Optional[Vector] = None,
            toolkit : VectorContextToolkit = VectorContextToolkit()
    ) -> BuildResult[VectorContext]:
        """
        Build a safe VectorContext.

        Action:
            1.  Send an exception in the BuildResult any of these conditions occur.
                    -   Both options are enabled.
                    -   Neither option is enabled.
                    -   Whichever attribute is set gets flgged by its validator.
            2.  Otherwise, build the VectorContext.
            3.  Send the success result.
        Args:
            coord: Optional[Coord] = None,
            vector: Optional[Vector] = None,
            toolkit : VectorContextToolkit = VectorContextToolkit()
        Returns:
            BuildResult[VectorContext]
        Raises:
            TypeError
            VectorContextNullException
            ZeroVectorContextFlagsException
            VectorContextBuildException
            ExcessVectorContextFlagsException
        """
        method = f"{cls.__name__}.build"

        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [coord, vector]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                VectorContextBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorContextBuildException.MSG,
                    err_code=VectorContextBuildException.ERR_CODE,
                    ex=ZeroVectorContextFlagsException(
                        msg=ZeroVectorContextFlagsException.MSG,
                        err_code=ZeroVectorContextFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                VectorContextBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorContextBuildException.MSG,
                    err_code=VectorContextBuildException.ERR_CODE,
                    ex=ExcessVectorContextFlagsException(
                        msg=ExcessVectorContextFlagsException.MSG,
                        err_code=ExcessVectorContextFlagsException.ERR_CODE,
                    )
                )
            )
        # --- Route to the appropriate Build/build branch. ---#
   
        
        # Build the coord VectorContext if its flag is enabled.
        if coord is not None:
            build_result = toolkit.coord_service.validator.validate(coord)
            if build_result.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    VectorContextBuildException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=VectorContextBuildException.MSG,
                        err_code=VectorContextBuildException.ERR_CODE,
                        ex=ExcessVectorContextFlagsException(
                            msg=ExcessVectorContextFlagsException.MSG,
                            err_code=ExcessVectorContextFlagsException.ERR_CODE,
                        )
                    )
                )
            # On Build success, forward the work product.
            return BuildResult.success(VectorContext(coord=coord))
        
        # Deal with the alternate case.
        build_result = toolkit.vector_service.validator.validate(vector)
        if build_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                VectorContextBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorContextBuildException.MSG,
                    err_code=VectorContextBuildException.ERR_CODE,
                    ex=build_result.exception
                )
            )
        # --- Forward the work product to the caller ---#
        return BuildResult.success(VectorContext(vector=vector))
            