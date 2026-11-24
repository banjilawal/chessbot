# src/controller/chain/vector/controller.py

"""
Module: controller.chain.vector.controller
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from collection import VectorChain
from controller.chain import ChainController
from microservice import (
    VectorChainTrimMicroservice, VectorNodeDeletionMicroservice, 
    VectorNodeInsertionMicroservice, VectorNodeSearchMicroservice
)

class VectorChainController(ChainController[VectorChain]):
    
    def __init__(
            self,
            chain: VectorChain,
            searcher: Optional[VectorNodeSearchMicroservice] | None = None,
            inserter: Optional[VectorNodeInsertionMicroservice] | None = None,
            deleter: Optional[VectorNodeDeletionMicroservice] | None = None,
            trimmer: Optional[VectorChainTrimMicroservice] | None = None,
    ):
        """
        Args:
            chain: VectorChain
            searcher: Optional[VectorNodeSearchMicroservice]
            inserter: Optional[VectorNodeInsertionMicroservice]
            deleter: Optional[VectorNodeDeletionMicroservice]
            trimmer: Optional[VectorChainTrimMicroservice]
        """
        super().__init__(
            chain=chain,
            searcher=searcher or VectorNodeSearchMicroservice(),
            inserter=inserter or VectorNodeInsertionMicroservice(),
            deleter=deleter or VectorNodeDeletionMicroservice(),
            trimmer=trimmer or VectorChainTrimMicroservice(),
        )
        
    @property
    def chain(self) -> VectorChain:
        return cast(VectorChain, super().chain)
    
    @property
    def searcher(self) -> VectorNodeSearchMicroservice:
        return cast(VectorNodeSearchMicroservice, super().searcher)
    
    @property
    def inserter(self) -> VectorNodeInsertionMicroservice:
        return cast(VectorNodeInsertionMicroservice, super().inserter)
    
    @property
    def deleter(self) -> VectorNodeDeletionMicroservice:
        return cast(VectorNodeDeletionMicroservice, super().deleter)
    
    @property
    def trimmer(self) -> VectorChainTrimMicroservice:
        return cast(VectorChainTrimMicroservice, super().trimmer)
    