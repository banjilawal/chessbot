# src/domain/search/context/chain/dossier/context.py

"""
Module: domain.search.context.chain.dossier.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import ChainSearchContext, Dossier, Square
from artifcat.report import AuthorizationDecision


class DossierNodeContext(ChainSearchContext[Dossier]):
        """
        Role:
            -   Selection
            -   Routing mask
            -   Data-Holder
    
        Responsibilities:
            1.  Supply a Dossier attribute-value search filter.
    
        Attributes:
            destination: Optional[Square]
            decision: Optional[AuthorizationDecision]
    
        Provides:
            -   to_dict() -> Dict[str, Any]
    
        Super Class:
            Context
        """
        _destination: Optional[Square]
        _decision: Optional[AuthorizationDecision]

        
        def __init__(
            self,
            destination: Optional[Square] | None = None,
            decision: Optional[AuthorizationDecision] | None = None,
            offset: Optional[int] | None = None,
        ):
            """
            Args:
                destination: Optional[Square]
                decision: Optional[AuthorizationDecision]
                offset: Optional[int]
            """
            super().__init__(offset=offset)
            self._destination = destination
            self._decision = decision
        
        @property
        def destination(self) -> Optional[Square]:
            return self._destination
        
        @property
        def decision(self) -> Optional[AuthorizationDecision]:
            return self._decision
    
        @property
        def to_dict(self) -> Dict[str, Any]:
            return {
                "destination": self._destination,
                "decision": self._decision,
                "offset": self.offset
            }