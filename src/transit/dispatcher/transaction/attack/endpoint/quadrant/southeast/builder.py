# src/transit/dispatcher/attack/endpoint/quadrant/southeast/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.endpoint.quadrant.southeast.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.model import Vector
from domain.struct.register import VectorRegister
from artifcat import AttackResult
from domain.schema.destination.quadrant import QuadrantDestination
from util import LoggingLevelRouter
from transit.dispatcher.validator import VectorValidator


class SoutheastQuadrantEndpointAttack:
    """
    Role:
        - Attack
        - Integrity Management

    Responsibilities:
        1.  Create a VectorRegister for the quadrant southeast of the origin.

    Attributes:
        origin: Vector
        destination: Vector
        vector_validator: Optional[VectorValidator]
        
    Provides:
        -   def execute() -> AttackResult[VectorRegister]

    Super Class:
    """
    _origin: Vector
    _destination: Vector
    _vector_validator: VectorValidator
    
    def __init__(
            self,
            origin: Vector,
            vector_validator: Optional[VectorValidator] | None = VectorValidator(),
    ):
        """
        Args:
            origin: Vector
            vector_validator: Optional[VectorValidator]
        """
        self._origin = origin
        self._vector_validator = vector_validator
        self._destination = QuadrantDestination.SOUTHEAST.vector
        
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def destination(self) -> Vector:
        return self._destination
    
    @LoggingLevelRouter.monitor
    def execute(self) -> AttackResult[VectorRegister]:
        """
        Construct the endpoints for a SouthernAxis instance.

        Action:
            1.  Send an exception chain in the AttackResult if the VectorValidator instance
                fails.
            2.  Otherwise, create the VectorRegister product and send in the success result.
        Args:
        Returns:
            AttackResult[VectorRegister]
        Raises:
             SouthernAxisEndPointAttackException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the origin is not safe to use.
        validation = self._vector_validator.execute(self._origin)
        # Send the exception chain in the result.
        if validation.is_failure:
            return AttackResult.failure(
                SoutheastQuadrantEndPointAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SoutheastQuadrantEndPointAttackException.MSG,
                    err_code=SoutheastQuadrantEndPointAttackException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # Create the endpoint register.
        vector_register = VectorRegister(
            u=cast(Vector, validation.authorization_applicant),
            v=self._destination,
        )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(vector_register)