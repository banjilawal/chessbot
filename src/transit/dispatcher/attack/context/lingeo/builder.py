# src/transit/dispatcher/attack/context/linegeo/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.context.linegeo.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from err import ExcessCartesianToggleFlagsException, VectorContextAttackException
from integrity import Attack
from domain.model import Coord, CartesianToggle, Vector
from artifcat import AttackResult
from operation.toolkit import VectorContextToolkit

class VectorContextAttack(Attack[CartesianToggle]):
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Attack Process Owner

   Responsibilities:
        1.  Ensure a new VectorContext instance is born safe and reliable.

    Attributes:

    Provides:
        -   def attack(
                    coord: Optional[Coord] = None,
                    vector: Optional[Vector] = None,
                    toolkit : VectorContextToolkit
            ) -> AttackResult[VectorContext]:

     Super Class:
         Attack
     """
    @classmethod
    def attack(
            cls,
            coord: Optional[Coord] = None,
            vector: Optional[Vector] = None,
            toolkit : VectorContextToolkit = VectorContextToolkit()
    ) -> AttackResult[CartesianToggle]:
        """
        Attack a safe VectorContext.

        Action:
            1.  Send an exception in the AttackResult any of these conditions occur.
                    - Both options are enabled.
                    - Neither option is enabled.
                    - Whichever attribute is set gets flgged by its validator.
            2.  Otherwise, attack the VectorContext.
            3.  Send the success result.
        Args:
            coord: Optional[Coord] = None,
            vector: Optional[Vector] = None,
            toolkit : VectorContextToolkit = VectorContextToolkit()
        Returns:
            AttackResult[VectorContext]
        Raises:
            TypeError
            VectorContextNullException
            ZeroVectorContextFlagsException
            VectorContextAttackException
            ExcessVectorContextFlagsException
        """
        method = f"{cls.__name__}.attack"

        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [coord, vector]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return AttackResult.failure(
                VectorContextAttackException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorContextAttackException.MSG,
                    err_code=VectorContextAttackException.ERR_CODE,
                    ex=ZeroVectorContextFlagsException(
                        msg=ZeroVectorContextFlagsException.MSG,
                        err_code=ZeroVectorContextFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return AttackResult.failure(
                VectorContextAttackException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorContextAttackException.MSG,
                    err_code=VectorContextAttackException.ERR_CODE,
                    ex=ExcessCartesianToggleFlagsException(
                        msg=ExcessCartesianToggleFlagsException.MSG,
                        err_code=ExcessCartesianToggleFlagsException.ERR_CODE,
                    )
                )
            )
        # --- Route to the appropriate Attack/attack branch. ---#
   
        
        # Attack the coord VectorContext if its flag is enabled.
        if coord is not None:
            attack_result = toolkit.coord_service.execute.execute(coord)
            if attack_result.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    VectorContextAttackException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=VectorContextAttackException.MSG,
                        err_code=VectorContextAttackException.ERR_CODE,
                        ex=ExcessCartesianToggleFlagsException(
                            msg=ExcessCartesianToggleFlagsException.MSG,
                            err_code=ExcessCartesianToggleFlagsException.ERR_CODE,
                        )
                    )
                )
            # On Attack success, forward the work product.
            return AttackResult.success(CartesianToggle(coord=coord))
        
        # Deal with the alternate case.
        attack_result = toolkit.vector_service.execute.execute(vector)
        if attack_result.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                VectorContextAttackException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorContextAttackException.MSG,
                    err_code=VectorContextAttackException.ERR_CODE,
                    ex=attack_result.exception
                )
            )
        # --- Forward the work product to the caller ---#
        return AttackResult.success(CartesianToggle(vector=vector))
            