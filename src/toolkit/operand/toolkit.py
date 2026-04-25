# src/toolkit/operand/toolkit.py

"""
Module: toolkit.operand.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from toolkit import Toolkit
from model import VectorOperand
from microservice import CoordService, VectorService


class VectorOperandToolkit(Toolkit[VectorOperand]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Collection of workers and services that are required for VectorOperand tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.
    
    Attributes:
        coord_service: CoordService
        vector_service: VectorService
    
    Provides:
    
    Super Class:
        Toolkit
    """
    _coord_service: CoordService
    _vector_service: VectorService
    
    def __init__(
            self,
            coord_service: CoordService | None = None,
            vector_service: VectorService | None = None,
    ):
        """
        Args:
            coord_service: CoordService
            vector_service: VectorService
        """
        super().__init__()
        self._coord_service = coord_service or CoordService()
        self._vector_service = vector_service or VectorService()
    
    @property
    def coord_service(self) -> CoordService:
        return self._coord_service
    
    @property
    def vector_service(self) -> VectorService:
        return self._vector_service