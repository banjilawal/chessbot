# src/domain/search/structure/node/dossier/context.py

"""
Module: domain.search.structure.node.dossier.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import StructureSearchContext, Dossier, Square, Token
from artifcat.report import AuthorizationDecision


class DossierNodeContext(StructureSearchContext[Dossier]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply a Node attribute-value tuple used to search a NodeChain.

    Attributes:
        offset: Optional[int]
        token: Optional[Token]
        source: Optional[Square]
        destination: Optional[Square]
        decision: Optional[AuthorizationDecision]

    Provides:
        - to_dict() -> Dict[str, Any]

    Super Class:
        NodeSearchContext
    """
    _token: Optional[Token]
    _source: Optional[Square]
    _destination: Optional[Square]
    _decision: Optional[AuthorizationDecision]
    
    def __init__(
            self,
            offset: Optional[int] | None = None,
            token: Optional[Token] | None = None,
            source: Optional[Square] | None = None,
            destination: Optional[Square] | None = None,
            decision: Optional[AuthorizationDecision] | None = None,
    ):
        """
        Args:
            offset: Optional[int]
            token: Optional[Token]
            source: Optional[Square]
            destination: Optional[Square]
            decision: Optional[AuthorizationDecision]
        """
        super().__init__(offset=offset)
        self._token = token
        self._source = source
        self._destination = destination
        self._decision = decision
    
    @property
    def token(self) -> Optional[Token]:
        return self._token
    
    @property
    def source(self) -> Optional[Square]:
        return self._source
    
    @property
    def destination(self) -> Optional[Square]:
        return self._destination
    
    @property
    def decision(self) -> Optional[AuthorizationDecision]:
        return self._decision
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "offset": self.offset,
            "token": self._token,
            "source": self._source,
            "destination": self._destination,
            "decision": self._decision,
        }