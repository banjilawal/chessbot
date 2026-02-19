# src/chess/node/service/service.py

"""
Module: chess.node.service.service
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from chess.edge import Edge, EdgeService
from chess.node import (
    AddIncomingEdgeFailedException, AddOutgoingEdgeFailedException, IncomingEdgeWrongTailException, Node, NodeBuilder,
    NodeServiceException, NodeValidator, OutgoingEdgeWrongHeadException, RemoveIncomingEdgeFailedException,
    RemoveOutgoingEdgeFailedException
)
from chess.system import DeletionResult, EntityService, IdFactory, InsertionResult, LoggingLevelRouter


class NodeService(EntityService[Node]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Node microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Node state by providing single entry and exit points to Node
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    SERVICE_NAME = "NodeService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: NodeBuilder = NodeBuilder(),
            validator: NodeValidator = NodeValidator(),
            id: int = IdFactory.next_id(class_name="NodeService"),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (NodeFactory)
            *   validator (NodeValidator)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
    @property
    def builder(self) -> NodeBuilder:
        return cast(NodeBuilder, self.entity_builder)
    
    @property
    def validator(self) -> NodeValidator:
        return cast(NodeValidator, self.entity_validator)
    
    @LoggingLevelRouter.monitor
    def add_incoming_edge(self, node: Node, edge: Edge) -> InsertionResult:
        """
        # ACTION:
            1.  If either the node or edge are not certified as safe send an exception chain in the InsertionResult.
            2.  If the node is not the edge's tail send an exception chain in the InsertionResult.
            3.  Let the node's incoming_edges stack process the addition.
            4.  If  node.incoming_edges.push fails encapsulate its exception inside a NodeServiceException which is
                sent in the InsertionResult. Else, send the success result.
        # PARAMETERS:
            *   node (Node)
            *   edge (Edge)
        # RETURNS:
            *   InsertionResult containing either:
                    - On failure: Exception and bool.
                    - On success: bool.
        # RAISES:
            *   NodeStackException
            *   NodePushException
            *   AddingDuplicateNodeException
        """
        method = "NodeService.add_incoming_edge"
        
        # Handle the case that the node is not certified as safe.
        node_validation_result = self.validator.validate(candidate=node)
        if node_validation_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                    ex=AddIncomingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=node_validation_result.exception
                    )
                )
            )
        # Using the node.incoming_edges handle the case that the edge is not certified as safe.
        edge_validation_result = node.incoming_edges.integrity_service.validator.validate(candidate=edge)
        if edge_validation_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                    ex=AddIncomingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=edge_validation_result.exception
                    )
                )
            )
        # Handle the case that the node is not the edge's tail
        if edge.tail != node:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                    ex=AddIncomingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=IncomingEdgeWrongTailException(
                            f"{method}: {IncomingEdgeWrongTailException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- After the validation checks are passed process the edge insertion. ---#
        edge_insertion_result = node.incoming_edges.push(edge)
        
        # Most likely cause of insertion failure is the edge already exists in the stack.
        if edge_insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                    ex=AddIncomingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=edge_insertion_result.exception
                    )
                )
            )
        # --- Send the success result. ---#
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def add_incoming_edge(self, node: Node, edge: Edge) -> InsertionResult:
        """
        # ACTION:
            1.  If either the node or edge are not certified as safe send an exception chain in the InsertionResult.
            2.  If the node is not the edge's tail send an exception chain in the InsertionResult.
            3.  Let the node's incoming_edges stack process the addition.
            4.  If  node.incoming_edges.push fails encapsulate its exception inside a NodeServiceException which is
                sent in the InsertionResult. Else, send the success result.
        # PARAMETERS:
            *   node (Node)
            *   edge (Edge)
        # RETURNS:
            *   InsertionResult containing either:
                    - On failure: Exception and bool.
                    - On success: bool.
        # RAISES:
            *   NodeStackException
            *   NodePushException
            *   AddingDuplicateNodeException
        """
        method = "NodeService.add_incoming_edge"
        
        # Handle the case that the node is not certified as safe.
        node_validation_result = self.validator.validate(candidate=node)
        if node_validation_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                    ex=AddIncomingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=node_validation_result.exception
                    )
                )
            )
        # Using the node.incoming_edges handle the case that the edge is not certified as safe.
        edge_validation_result = node.incoming_edges.integrity_service.validator.validate(candidate=edge)
        if edge_validation_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                    ex=AddIncomingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=edge_validation_result.exception
                    )
                )
            )
        # Handle the case that the node is not the edge's tail
        if edge.tail != node:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                    ex=AddIncomingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=IncomingEdgeWrongTailException(
                            f"{method}: {IncomingEdgeWrongTailException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- After the validation checks are passed process the edge insertion. ---#
        edge_insertion_result = node.incoming_edges.push(edge)
        
        # Most likely cause of insertion failure is the edge already exists in the stack.
        if edge_insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                    ex=AddIncomingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=edge_insertion_result.exception
                    )
                )
            )
        # --- Send the success result. ---#
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def remove_incoming_edge(self, node: Node, edge: Edge) -> DeletionResult[Edge]:
        """
        # ACTION:
            1.  If either the node or edge are not certified as safe send an exception chain in the DeletionResult.
            2.  If the node is not the edge's tail send an exception chain in the DeletionResult.
            3.  Let the node's incoming_edges stack process the removal.
            4.  If  node.incoming_edges.pop fails encapsulate its exception inside a NodeServiceException which is
                sent in the InsertionResult. Else, send the success result.
        # PARAMETERS:
            *   node (Node)
            *   edge (Edge)
        # RETURNS:
            *   DeletionResult containing either:
                    - On failure: Exception.
                    - On success: Edge.
        # RAISES:
            *   NodeStackException
            *   NodePopException
            *   AddingDuplicateNodeException
        """
        method = "NodeService.remove_incoming_edge"
        
        # Handle the case that the node is not certified as safe.
        node_validation_result = self.validator.validate(candidate=node)
        if node_validation_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                NodeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                    ex=RemoveIncomingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {RemoveIncomingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=node_validation_result.exception
                    )
                )
            )
        # Using the node.incoming_edges handle the case that the edge is not certified as safe.
        edge_validation_result = node.incoming_edges.integrity_service.validator.validate(candidate=edge)
        if edge_validation_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                NodeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                    ex=RemoveIncomingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {RemoveIncomingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=edge_validation_result.exception
                    )
                )
            )
        deletion_result = node.incoming_edges.delete_by_label(edge.label)
        
        if deletion_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                NodeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                    ex=RemoveIncomingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {RemoveIncomingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=deletion_result.exception
                    )
                )
            )
        return deletion_result

    
    @LoggingLevelRouter.monitor
    def add_outgoing_edge(self, node: Node, edge: Edge) -> InsertionResult:
        """
        # ACTION:
            1.  If either the node or edge are not certified as safe send an exception chain in the InsertionResult.
            2.  If the node is not the edge's tail send an exception chain in the InsertionResult.
            3.  Let the node's outgoing_edges stack process the addition.
            4.  If  node.outgoing_edges.push fails encapsulate its exception inside a NodeServiceException which is
                sent in the InsertionResult. Else, send the success result.
        # PARAMETERS:
            *   node (Node)
            *   edge (Edge)
        # RETURNS:
            *   InsertionResult containing either:
                    - On failure: Exception and bool.
                    - On success: bool.
        # RAISES:
            *   NodeStackException
            *   NodePushException
            *   AddingDuplicateNodeException
        """
        method = "NodeService.add_outgoing_edge"
        
        # Handle the case that the node is not certified as safe.
        node_validation_result = self.validator.validate(candidate=node)
        if node_validation_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                    ex=AddOutgoingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {AddOutgoingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=node_validation_result.exception
                    )
                )
            )
        # Using the node.outgoing_edges handle the case that the edge is not certified as safe.
        edge_validation_result = node.outgoing_edges.integrity_service.validator.validate(candidate=edge)
        if edge_validation_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                    ex=AddOutgoingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {AddOutgoingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=edge_validation_result.exception
                    )
                )
            )
        # Handle the case that the node is not the edge's tail
        if edge.tail != node:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                    ex=AddOutgoingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {AddOutgoingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=OutgoingEdgeWrongHeadException(
                            f"{method}: {OutgoingEdgeWrongHeadException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- After the validation checks are passed process the edge insertion. ---#
        edge_insertion_result = node.outgoing_edges.push(edge)
        
        # Most likely cause of insertion failure is the edge already exists in the stack.
        if edge_insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                    ex=AddOutgoingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {AddOutgoingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=edge_insertion_result.exception
                    )
                )
            )
        # --- Send the success result. ---#
        return InsertionResult.success()


@LoggingLevelRouter.monitor
def remove_outgoing_edge(self, node: Node, edge: Edge) -> DeletionResult[Edge]:
    """
    # ACTION:
        1.  If either the node or edge are not certified as safe send an exception chain in the DeletionResult.
        2.  If the node is not the edge's tail send an exception chain in the DeletionResult.
        3.  Let the node's outgoing_edges stack process the removal.
        4.  If  node.outgoing_edges.pop fails encapsulate its exception inside a NodeServiceException which is
            sent in the InsertionResult. Else, send the success result.
    # PARAMETERS:
        *   node (Node)
        *   edge (Edge)
    # RETURNS:
        *   DeletionResult containing either:
                - On failure: Exception.
                - On success: Edge.
    # RAISES:
        *   NodeStackException
        *   NodePopException
        *   AddingDuplicateNodeException
    """
    method = "NodeService.remove_outgoing_edge"
    
    # Handle the case that the node is not certified as safe.
    node_validation_result = self.validator.validate(candidate=node)
    if node_validation_result.is_failure:
        # Return the exception chain on failure.
        return DeletionResult.failure(
            NodeServiceException(
                message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                ex=RemoveOutgoingEdgeFailedException(
                    message=f"ServiceId:{self.id}, {method}: {RemoveOutgoingEdgeFailedException.DEFAULT_MESSAGE}",
                    ex=node_validation_result.exception
                )
            )
        )
    # Using the node.outgoing_edges handle the case that the edge is not certified as safe.
    edge_validation_result = node.outgoing_edges.integrity_service.validator.validate(candidate=edge)
    if edge_validation_result.is_failure:
        # Return the exception chain on failure.
        return DeletionResult.failure(
            NodeServiceException(
                message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                ex=RemoveOutgoingEdgeFailedException(
                    message=f"ServiceId:{self.id}, {method}: {RemoveOutgoingEdgeFailedException.DEFAULT_MESSAGE}",
                    ex=edge_validation_result.exception
                )
            )
        )
    deletion_result = node.outgoing_edges.delete_by_label(edge.label)
    
    if deletion_result.is_failure:
        # Return the exception chain on failure.
        return DeletionResult.failure(
            NodeServiceException(
                message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                ex=RemoveOutgoingEdgeFailedException(
                    message=f"ServiceId:{self.id}, {method}: {RemoveOutgoingEdgeFailedException.DEFAULT_MESSAGE}",
                    ex=deletion_result.exception
                )
            )
        )
    return deletion_result
        
        