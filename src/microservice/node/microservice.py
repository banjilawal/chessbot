# src/microservice/node/microservice.py

"""
Module: microservice.node.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""
from microservice import Microservice
from model import Node


class NodeService(Microservice[Node]):
    """
    Role:Microservice, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Node microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Node state by providing single entry and exit points to Node
        lifecycle.

    Super Class:
        *   IntegrityMicroservice

    Provides:


    # INHERITED ATTRIBUTES:
        *   See IntegrityMicroservice for inherited attributes.
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
            *   schema (str)
            *   build (NodeFactory)
            *   validation (NodeValidator)
        # RETURNS:
            None
        Raises:
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
            1.  If either the node or edge are does not pass a validation check. send an exception chain in the InsertionResult.
            2.  If the node is not the edge's tail send an exception chain in the InsertionResult.
            3.  Let the node's incoming_edges schema exception the addition.
            4.  If  node.incoming_edges.push fails encapsulate its exception inside a NodeServiceException which is
                sent in the InsertionResult. Else, send the success result.
        # PARAMETERS:
            *   node (Node)
            *   edge (Edge)
        # RETURNS:
            *   InsertionResult containing either:
                    - On failure: Exception and bool.
                    - On success: bool.
        Raises:
            *   NodeStackException
            *   NodePushException
            *   AddingDuplicateNodeException
        """
        method = "NodeService.add_incoming_edge"
        
        # Handle the case that, the node does not pass a validation check.
        node_validation_result = self.validator.execute(candidate=node)
        if node_validation_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                    ex=AddIncomingEdgeFailedException(
                        msg=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.MSG}",
                        ex=node_validation_result.exception
                    )
                )
            )
        # Using the node.incoming_edges handle the case that the edge does not pass a validation check.
        edge_validation_result = node.incoming_edges.service.run.build(candidate=edge)
        if edge_validation_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                    ex=AddIncomingEdgeFailedException(
                        msg=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.MSG}",
                        ex=edge_validation_result.exception
                    )
                )
            )
        # Handle the case that, the node is not the edge's tail
        if edge.tail != node:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                    ex=AddIncomingEdgeFailedException(
                        msg=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.MSG}",
                        ex=IncomingEdgeWrongTailException(
                            f"{method}: {IncomingEdgeWrongTailException.MSG}"
                        )
                    )
                )
            )
        # --- After the validation checks are passed exception the edge insertion. ---#
        edge_insertion_result = node.incoming_edges.push(edge)
        
        # Most likely cause of insertion failure is the edge already exists in the schema.
        if edge_insertion_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                    ex=AddIncomingEdgeFailedException(
                        msg=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.MSG}",
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
            1.  If either the node or edge are does not pass a validation check. send an exception chain in the InsertionResult.
            2.  If the node is not the edge's tail send an exception chain in the InsertionResult.
            3.  Let the node's incoming_edges schema exception the addition.
            4.  If  node.incoming_edges.push fails encapsulate its exception inside a NodeServiceException which is
                sent in the InsertionResult. Else, send the success result.
        # PARAMETERS:
            *   node (Node)
            *   edge (Edge)
        # RETURNS:
            *   InsertionResult containing either:
                    - On failure: Exception and bool.
                    - On success: bool.
        Raises:
            *   NodeStackException
            *   NodePushException
            *   AddingDuplicateNodeException
        """
        method = "NodeService.add_incoming_edge"
        
        # Handle the case that, the node does not pass a validation check.
        node_validation_result = self.validator.execute(candidate=node)
        if node_validation_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                    ex=AddIncomingEdgeFailedException(
                        msg=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.MSG}",
                        ex=node_validation_result.exception
                    )
                )
            )
        # Using the node.incoming_edges handle the case that the edge does not pass a validation check.
        edge_validation_result = node.incoming_edges.service.run.build(candidate=edge)
        if edge_validation_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                    ex=AddIncomingEdgeFailedException(
                        msg=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.MSG}",
                        ex=edge_validation_result.exception
                    )
                )
            )
        # Handle the case that, the node is not the edge's tail
        if edge.tail != node:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                    ex=AddIncomingEdgeFailedException(
                        msg=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.MSG}",
                        ex=IncomingEdgeWrongTailException(
                            f"{method}: {IncomingEdgeWrongTailException.MSG}"
                        )
                    )
                )
            )
        # --- After the validation checks are passed exception the edge insertion. ---#
        edge_insertion_result = node.incoming_edges.push(edge)
        
        # Most likely cause of insertion failure is the edge already exists in the schema.
        if edge_insertion_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                    ex=AddIncomingEdgeFailedException(
                        msg=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.MSG}",
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
            1.  If either the node or edge are does not pass a validation check. send an exception chain in the DeletionResult.
            2.  If the node is not the edge's tail send an exception chain in the DeletionResult.
            3.  Let the node's incoming_edges schema exception the removal.
            4.  If  node.incoming_edges.pop fails encapsulate its exception inside a NodeServiceException which is
                sent in the InsertionResult. Else, send the success result.
        # PARAMETERS:
            *   node (Node)
            *   edge (Edge)
        # RETURNS:
            *   DeletionResult containing either:
                    - On failure: Exception.
                    - On success: Edge.
        Raises:
            *   NodeStackException
            *   NodePopException
            *   AddingDuplicateNodeException
        """
        method = "NodeService.remove_incoming_edge"
        
        # Handle the case that, the node does not pass a validation check.
        node_validation_result = self.validator.execute(candidate=node)
        if node_validation_result.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                NodeServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                    ex=RemoveIncomingEdgeFailedException(
                        msg=f"ServiceId:{self.id}, {method}: {RemoveIncomingEdgeFailedException.MSG}",
                        ex=node_validation_result.exception
                    )
                )
            )
        # Using the node.incoming_edges handle the case that the edge does not pass a validation check.
        edge_validation_result = node.incoming_edges.service.run.build(candidate=edge)
        if edge_validation_result.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                NodeServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                    ex=RemoveIncomingEdgeFailedException(
                        msg=f"ServiceId:{self.id}, {method}: {RemoveIncomingEdgeFailedException.MSG}",
                        ex=edge_validation_result.exception
                    )
                )
            )
        deletion_result = node.incoming_edges.delete_by_label(edge.label)
        
        if deletion_result.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                NodeServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                    ex=RemoveIncomingEdgeFailedException(
                        msg=f"ServiceId:{self.id}, {method}: {RemoveIncomingEdgeFailedException.MSG}",
                        ex=deletion_result.exception
                    )
                )
            )
        return deletion_result
    

    @LoggingLevelRouter.monitor
    def add_outgoing_edge(self, node: Node, edge: Edge) -> InsertionResult:
        """
        # ACTION:
            1.  If either the node or edge are does not pass a validation check. send an exception chain in the InsertionResult.
            2.  If the node is not the edge's tail send an exception chain in the InsertionResult.
            3.  Let the node's outgoing_edges schema exception the addition.
            4.  If  node.outgoing_edges.push fails encapsulate its exception inside a NodeServiceException which is
                sent in the InsertionResult. Else, send the success result.
        # PARAMETERS:
            *   node (Node)
            *   edge (Edge)
        # RETURNS:
            *   InsertionResult containing either:
                    - On failure: Exception and bool.
                    - On success: bool.
        Raises:
            *   NodeStackException
            *   NodePushException
            *   AddingDuplicateNodeException
        """
        method = "NodeService.add_outgoing_edge"
        
        # Handle the case that, the node does not pass a validation check.
        node_validation_result = self.validator.execute(candidate=node)
        if node_validation_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                    ex=AddOutgoingEdgeFailedException(
                        msg=f"ServiceId:{self.id}, {method}: {AddOutgoingEdgeFailedException.MSG}",
                        ex=node_validation_result.exception
                    )
                )
            )
        # Using the node.outgoing_edges handle the case that the edge does not pass a validation check.
        edge_validation_result = node.outgoing_edges.service.run.build(candidate=edge)
        if edge_validation_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                    ex=AddOutgoingEdgeFailedException(
                        msg=f"ServiceId:{self.id}, {method}: {AddOutgoingEdgeFailedException.MSG}",
                        ex=edge_validation_result.exception
                    )
                )
            )
        # Handle the case that, the node is not the edge's tail
        if edge.tail != node:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                    ex=AddOutgoingEdgeFailedException(
                        msg=f"ServiceId:{self.id}, {method}: {AddOutgoingEdgeFailedException.MSG}",
                        ex=OutgoingEdgeWrongHeadException(
                            f"{method}: {OutgoingEdgeWrongHeadException.MSG}"
                        )
                    )
                )
            )
        # --- After the validation checks are passed exception the edge insertion. ---#
        edge_insertion_result = node.outgoing_edges.push(edge)
        
        # Most likely cause of insertion failure is the edge already exists in the schema.
        if edge_insertion_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                    ex=AddOutgoingEdgeFailedException(
                        msg=f"ServiceId:{self.id}, {method}: {AddOutgoingEdgeFailedException.MSG}",
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
        1.  If either the node or edge are does not pass a validation check. send an exception chain in the DeletionResult.
        2.  If the node is not the edge's tail send an exception chain in the DeletionResult.
        3.  Let the node's outgoing_edges schema exception the removal.
        4.  If  node.outgoing_edges.pop fails encapsulate its exception inside a NodeServiceException which is
            sent in the InsertionResult. Else, send the success result.
    # PARAMETERS:
        *   node (Node)
        *   edge (Edge)
    # RETURNS:
        *   DeletionResult containing either:
                - On failure: Exception.
                - On success: Edge.
    Raises:
        *   NodeStackException
        *   NodePopException
        *   AddingDuplicateNodeException
    """
    method = "NodeService.remove_outgoing_edge"
    
    # Handle the case that, the node does not pass a validation check.
    node_validation_result = self.run.search_service(candidate=node)
    if node_validation_result.is_failure:
        # Send the exception chain on failure.
        return DeletionResult.failure(
            NodeServiceException(
                msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                ex=RemoveOutgoingEdgeFailedException(
                    msg=f"ServiceId:{self.id}, {method}: {RemoveOutgoingEdgeFailedException.MSG}",
                    ex=node_validation_result.exception
                )
            )
        )
    # Using the node.outgoing_edges handle the case that the edge does not pass a validation check.
    edge_validation_result = node.outgoing_edges.service.run.build(candidate=edge)
    if edge_validation_result.is_failure:
        # Send the exception chain on failure.
        return DeletionResult.failure(
            NodeServiceException(
                msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                ex=RemoveOutgoingEdgeFailedException(
                    msg=f"ServiceId:{self.id}, {method}: {RemoveOutgoingEdgeFailedException.MSG}",
                    ex=edge_validation_result.exception
                )
            )
        )
    deletion_result = node.outgoing_edges.delete_by_label(edge.label)
    
    if deletion_result.is_failure:
        # Send the exception chain on failure.
        return DeletionResult.failure(
            NodeServiceException(
                msg=f"ServiceId:{self.id}, {method}: {NodeServiceException.MSG}",
                ex=RemoveOutgoingEdgeFailedException(
                    msg=f"ServiceId:{self.id}, {method}: {RemoveOutgoingEdgeFailedException.MSG}",
                    ex=deletion_result.exception
                )
            )
        )
    return deletion_result
        
        