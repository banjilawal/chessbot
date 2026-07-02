# src/logic/pair/tree/service/operation/schema.py

"""
Module: logic.pair.tree.service.operation.schema
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations

from model.node import NodeStackService
from graph.pair import NodeTree, NodeTreeValidator
from system import BuildResult, LoggingLevelRouter


class NodeTreeStackMigrator:
    """
    Role:Microservice, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Migrate unique nodes from the tree into a NodeStack

    Super Class:
        *   IntegrityMicroservice

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def migrate(
            cls,
            node_tree: NodeTree,
            node_tree_validator: NodeTreeValidator = NodeTreeValidator(),
    ) -> BuildResult[NodeStackService]:
        """
        Action:
            1. Put all the unique nodes into a NodeStackService for the graph.
            
        Args:
            node_tree: NodeTree
            node_tree_validator: NodeTreeValidator
            
        Returns:
            BuildResult[NodeStackService]
        """
        method = f"{cls.__class__.__name__}.convert"
        
        # Handle the case that, the node_tree does not pass a validation check.
        validation_result = node_tree_validator.execute(candidate=node_tree)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                NodeTreeStackMigratorException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=NodeTreeStackMigratorException.MSG,
                    err_code=NodeTreeStackMigratorException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # --- Create the return target, then insert the root node.---#
        node_stack_service = NodeStackService()
        insertion_result = node_stack_service.push(item=node_tree.root)
        
        # Handle the case that, the insertion produces no work.
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                NodeTreeStackMigratorException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=NodeTreeStackMigratorException.MSG,
                    err_code=NodeTreeStackMigratorException.ERR_CODE,
                    ex=insertion_result.exception,
                )
            )
        # Handle the case that the tree has no branches.
        if node_tree.is_empty:
            return BuildResult.success(node_stack_service)
            
        # --- Process the insertions from each branch.---#
        for branch in node_tree.branches:
            
            unique_node_search_result = node_tree.branch_service.unique_nodes(pair_list=branch)
            # Handle the case that, the search is not completed.
            if unique_node_search_result.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    NodeTreeStackMigratorException(
                        cls_mthd=method,
                        cls_name=cls.__class__.__name__,
                        msg=NodeTreeStackMigratorException.MSG,
                        err_code=NodeTreeStackMigratorException.ERR_CODE,
                        ex=insertion_result.exception,
                    )
                )
            # --- Push the nodes to the node_stack.---#
            for node in unique_node_search_result.payload:
                insertion_result = node_stack_service.push(item=node)
        
                # Handle the case that, the insertion produces no work.
                if validation_result.is_failure:
                    # Send the exception chain on failure.
                    return BuildResult.failure(
                        NodeTreeStackMigratorException(
                            cls_mthd=method,
                            cls_name=cls.__class__.__name__,
                            msg=NodeTreeStackMigratorException.MSG,
                            err_code=NodeTreeStackMigratorException.ERR_CODE,
                            ex=insertion_result.exception,
                        )
                    )
        # --- Send the work product. ---#
        return BuildResult.success(node_stack_service)
        