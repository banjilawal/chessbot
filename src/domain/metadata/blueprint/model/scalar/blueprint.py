# src/domain/metadata/blueprint/scalar/blueprint.py

"""
Module: domain.metadata.blueprint.scalar.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import ModelBlueprint, Scalar
from err import ScalarNullException


class ScalarBlueprint(ModelBlueprint[Scalar]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Scalar.

    Attributes:
        magnitude: int
        scalar_type: Scalar
        domain_null_exception: ScalarNullException
        
    Provides:

     Super Class:
        ModelBlueprint
     """
    _magnitude: int
    
    def __init__(
            self,
            magnitude: int,
            domain_class: Optional[Type[Scalar]] | None = None,
            domain_null_exception: Optional[ScalarNullException] | None = None,
    ):
        """
        Args:
            magnitude: int
            domain_class: Optional[Type[Scalar]]
            domain_null_exception: Optional[ScalarNullException]
        """
        super().__init__(
            domain_class=domain_class or Type[Scalar],
            domain_null_exception=domain_null_exception or ScalarNullException(),
        )
        self._magnitude = magnitude
        
    @property
    def domain_class(self) -> Type[Scalar]:
        return cast(Type[Scalar], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ScalarNullException:
        return cast(ScalarNullException, super().domain_null_exception)

