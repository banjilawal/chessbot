# src/domain/metadata/blueprint/node/dossier/blueprint.py

"""
Module: domain.metadata.blueprint.node.dossier.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from err import DossierNodeNullException
from fabrication import NodeBlueprint
from domain.model import Dossier
from domain.structure.node import DossierNode


class DossierNodeBlueprint(NodeBlueprint):
    """
     Role:
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a DossierNode object

     Attributes:
        dossier: Dossier
        model_class: Type[DossierNode]
        null_exception: Optional[DossierNodeNullException]

     Provides:

     Super Class:
        NodeBlueprint
     """
    _dossier: Dossier
    
    def __init__(
            self,
            dossier: Dossier,
            model_class: Type[DossierNode] = DossierNode,
            null_exception: Optional[DossierNodeNullException] | None = None,
    ):
        """
        Args:
            dossier: Dossier
            model_class: Type[DossierNode]
            null_exception: Optional[DossierNodeNullException]
        """
        super().__init__(model_class=model_class, null_exception=null_exception or DossierNodeNullException())
        self._dossier = dossier
        
    @property
    def dossier(self) -> Dossier:
        return self._dossier
 
    @property
    def model_class(self) -> Type[DossierNode]:
        return cast(Type[DossierNode], super().model_class)
    
    @property
    def null_exception(self) -> DossierNodeNullException:
        return cast(DossierNodeNullException, super().null_exception)