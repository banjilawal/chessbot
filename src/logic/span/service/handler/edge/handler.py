# src/logic/span/service/handler/edge/handler.py

"""
Module: logic.span.service.handler.edge.handler
Author: Banji Lawal
Created: 2026-03-11
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict, List

from logic.node import Node
from logic.graph import Graph
from logic.edge import Edge, EdgeBuilder, PushingEdgeException
from logic.system import BuildResult, InsertionResult, LoggingLevelRouter
from logic.span import AsymmetricEdgeBuildException, NodeEdgeHandlerException, SymmetricEdgeBuildException

class NodeEdgeHandler:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_symmetric_edges(
            cls,
            node_dict: Dict[str, Node],
            edge_builder: EdgeBuilder = EdgeBuilder(),
    ) -> BuildResult[List[Edge]]:
        """
        Action:
            Build a dictionary of adjacent edges from a square hashtable., from a square hashtable.
            
        Args:
            edge_builder: EdgeBuilder
            node_dict: Dict[str, Node]
            
        Returns:
            BuildResult[Dict[str, Edge]]
            
        Raises:
            SymmetricEdgeBuildException
        """
        method = f"{cls.__class__.__name__}.build"
        
        edges: List[Edge] = []
        for key in node_dict:
            
            tail_node: Node = None
            head_node: Node = node_dict[key]

            if key.upper() == "head".upper:
                tail_node = node_dict["tail"]
            else:
                tal_node = node_dict["head"]
                
            build_result = edge_builder.build(
                head=head_node,
                tail=tail_node,
            )   
            # Handle the case that, the edge is not built
            if build_result.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    NodeEdgeHandlerException(
                        cls_mthd=method,
                        cls_name=cls.__class__.__name__,
                        msg=NodeEdgeHandlerException.MSG,
                        err_code=NodeEdgeHandlerException.ERR_CODE,
                        ex=SymmetricEdgeBuildException(
                            mthd=method,
                            op=SymmetricEdgeBuildException.OP,
                            msg=SymmetricEdgeBuildException.MSG,
                            err_code=SymmetricEdgeBuildException.ERR_CODE,
                            ex=build_result.exception
                        )
                    )
                )
            edges.append(build_result.payload)
        return BuildResult.success(edges)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build__edge(
            cls,
            node_dict: Dict[str, Node],
            edge_builder: EdgeBuilder = EdgeBuilder(),
    ) -> BuildResult[List[Edge]]:
        """
        Action:
            Build a dictionary of adjacent edges from a square hashtable., from a square hashtable.

        Args:
            edge_builder: EdgeBuilder
            node_dict: Dict[str, Square]

        Returns:
            BuildResult[List[Edge]]

        Raises:
            AsymmetricEdgeBuildException
        """
        method = f"{cls.__class__.__name__}.build"
        
        build_result = edge_builder.build(
            head=node_dict["head"],
            tail=node_dict["tail"],
        )
        # Handle the case that, the edge is not built
        if build_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                NodeEdgeHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=NodeEdgeHandlerException.MSG,
                    err_code=NodeEdgeHandlerException.ERR_CODE,
                    ex=AsymmetricEdgeBuildException(
                        mthd=method,
                        op=AsymmetricEdgeBuildException.OP,
                        msg=AsymmetricEdgeBuildException.MSG,
                        err_code=AsymmetricEdgeBuildException.ERR_CODE,
                        ex=build_result.exception
                    )
                )
            )
        return BuildResult.success(List[build_result.payload])
    
    @classmethod
    @LoggingLevelRouter.monitor
    def insert_edges(
            cls,
            graph: Graph,
            edges: List[Edge],
    ) -> InsertionResult:
        """
        Args:
            graph: Graph
            edge_dict: Dict[str, Edge]
        """
        method = f"{cls.__class__.__name__}.add_edge_pair_to_graph"
        
        for edge in edges:
            push_result = graph.edges.push(item=edge)
            # Handle the case that the edge is not in the graph.
            if push_result.is_failure:
                # Return the exception chain on failure.
                return InsertionResult.failure(
                    NodeEdgeHandlerException(
                        cls_mthd=method,
                        cls_name=cls.__class__.__name__,
                        msg=NodeEdgeHandlerException.MSG,
                        err_code=NodeEdgeHandlerException.ERR_CODE,
                        ex=PushingEdgeException(
                            mthd=method,
                            op=PushingEdgeException.OP,
                            msg=PushingEdgeException.MSG,
                            err_code=PushingEdgeException.ERR_CODE,
                            rslt_type=PushingEdgeException.RSLT_TYPE,
                            ex=push_result.exception
                        )
                    )
                )
        return InsertionResult.success()
    
        