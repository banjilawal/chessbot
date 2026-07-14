# src/toolkit/context/linegeo/toolkit.py

"""
Module: toolkit.context.linegeo.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from err import ExcessVectorOperandFlagsException, VectorContextToolkitException
from integrity import Toolkit
from model import Coord, VectorOperand, Vector
from result import ToolkitResult
from toolkit  import VectorContextToolkit

class VectorContextToolkit(Toolkit[VectorOperand]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Toolkit Process Owner

   Responsibilities:
        1.  Ensure a new VectorContext instance is born safe and reliable.

    Attributes:

    Provides:
        -   def __init__(
                    coord: Optional[Coord] = None,
                    vector: Optional[Vector] = None,
                    toolkit : VectorContextToolkit
            ) -> ToolkitResult[VectorContext]:

     Super Class:
         Toolkit
     """
    @classmethod
    def __init__(
            self,
            coord: Optional[Coord] = None,
            vector: Optional[Vector] = None,
            toolkit : VectorContextToolkit = VectorContextToolkit()
    ) -> ToolkitResult[VectorOperand]:
        """
        Toolkit a safe VectorContext.

        Action:
            1.  Send an exception in the ToolkitResult any of these conditions occur.
                    -   Both options are enabled.
                    -   Neither option is enabled.
                    -   Whichever attribute is set gets flgged by its validator.
            2.  Otherwise, toolkit the VectorContext.
            3.  Send the success result.
        Args:
            coord: Optional[Coord] = None,
            vector: Optional[Vector] = None,
            toolkit : VectorContextToolkit = VectorContextToolkit()
        Returns:
            ToolkitResult[VectorContext]
        Raises:
            TypeError
            VectorContextNullException
            ZeroVectorContextFlagsException
            VectorContextToolkitException
            ExcessVectorContextFlagsException
        """
        method = f"{cls.__name__}.toolkit"

        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [coord, vector]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                VectorContextToolkitException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorContextToolkitException.MSG,
                    err_code=VectorContextToolkitException.ERR_CODE,
                    ex=ZeroVectorContextFlagsException(
                        msg=ZeroVectorContextFlagsException.MSG,
                        err_code=ZeroVectorContextFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                VectorContextToolkitException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorContextToolkitException.MSG,
                    err_code=VectorContextToolkitException.ERR_CODE,
                    ex=ExcessVectorOperandFlagsException(
                        msg=ExcessVectorOperandFlagsException.MSG,
                        err_code=ExcessVectorOperandFlagsException.ERR_CODE,
                    )
                )
            )
        # --- Route to the appropriate Toolkit/toolkit branch. ---#
   
        
        # Toolkit the coord VectorContext if its flag is enabled.
        if coord is not None:
            toolkit_result = toolkit.coord_service.run.execute(coord)
            if toolkit_result.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    VectorContextToolkitException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=VectorContextToolkitException.MSG,
                        err_code=VectorContextToolkitException.ERR_CODE,
                        ex=ExcessVectorOperandFlagsException(
                            msg=ExcessVectorOperandFlagsException.MSG,
                            err_code=ExcessVectorOperandFlagsException.ERR_CODE,
                        )
                    )
                )
            # On Toolkit success, forward the work product.
            return ToolkitResult.success(VectorOperand(coord=coord))
        
        # Deal with the alternate case.
        toolkit_result = toolkit.vector_service.run.execute(vector)
        if toolkit_result.is_failure:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                VectorContextToolkitException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorContextToolkitException.MSG,
                    err_code=VectorContextToolkitException.ERR_CODE,
                    ex=toolkit_result.exception
                )
            )
        # --- Forward the work product to the caller ---#
        return ToolkitResult.success(VectorOperand(vector=vector))
            