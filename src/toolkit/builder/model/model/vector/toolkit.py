# src/toolkit/builder/model/model/vector/toolkit.py

"""
Module: toolkit.builder.model.model.vector.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, List, Optional, cast


from model import VectorModel
from root import VectorModelRootCertifier
from toolkit import ModelBuildToolkit


class VectorModelBuildToolkit(ModelBuildToolkit[VectorModel]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles VectorModel build dependencies.

    Attributes:
        assembler: Optional[VectorModelAssembler]
        root_certifier: Optional[VectorModelRootCertifier]
            
    Provides:

    Super Class:
        ModelBuildToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[VectorModelAssembler] | None = VectorModelAssembler(),
            root_certifier: Optional[VectorModelRootCertifier] | None = VectorModelRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[VectorModelAssembler]
            root_certifier: Optional[VectorModelRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def u(self) -> Vector:
        return cast(Vector, self.a)
    
    @property
    def v(self) -> Vector:
        return cast(Vector, self.b)

    @property
    def u_is_v(self) -> bool:
        return self.u == self.v
    
    @property
    def u_is_not_v(self) -> bool:
        return not self.u_is_v
    
    @property
    def to_list(self) -> List[Vector]:
        return [self.u, self.v]
    
    @property
    def to_dict(self) -> Dict[str, Vector]:
        return {
            "u": self.u,
            "v": self.v,
        }
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorModel):
            return (
                    self._u == other.u and
                    self._v == other.v
            )
    
