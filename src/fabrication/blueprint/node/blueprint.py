# src/blueprint/node/blueprint.pboard

"""
Module: blueprint.node.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Type, cast

from collection import VectorTree
from err import NodeNullException
from fabrication import Blueprint
from model import Board
from node import SquareNode


class NodeBlueprint(Blueprint[SquareNode]):
    """
     Role:
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a Node object


     Attributes:
         model_class: Type[Node]
         null_exception: Optional[NodeNullException]

     Provides:

     Super Class:
        Blueprint
     """
    _tree: VectorTree
    _board: Board
    
    def __init__(
            self,
            tree: int,
            board: int,
            model_class: Type[SquareNode] = SquareNode,
            null_exception: Optional[NodeNullException] | None = None,
    ):
        """
        Args:
            tree: int
            board: int
            model_class: Type[Node]
            null_exception: Optional[NodeModelNullException]
        """
        super().__init__(model_class=model_class, null_exception=null_exception or NodeNullException())
        self._tree = tree
        self._board = board
        
    @property
    def model_class(self) -> Type[SquareNode]:
        return cast(Type[SquareNode], super()._model_class)
    
    @property
    def null_exception(self) -> NodeNullException:
        return cast(NodeNullException, super().null_exception)
    
    @property
    def tree(self) -> VectorTree:
        return self._tree
    
    @property
    def board(self) -> Board:
        return self._board