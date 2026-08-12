# src/bootstrapper/validator/endpoint/destination/bootstrapper.py

"""
Module: bootstrapper.validator.endpoint.destination.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from sensor.analyzer import SquareTokenRelationAnalyzer
from err import (
    BlockedPathException, DestinationCertifierBootstrapperException, PartialTokenDestinationRelationException,
    TokenAlreadyAtDestinationException
)
from model import Square, Token
from report import DestinationApprovalReport, RelationReport
from util import LoggingLevelRouter


class DestinationCertifierBootstrapper:
    """
    Role
        -   Validation Worker
        -   Integrity Maintenance
        -   Consistency Assurance

    Responsibilities:
        1.  Verify a Token does not have either a partial or full bidirectional relation
            with the square it wants to visit.
        2.  Prevents visiting friendly squares.

    Attributes:
        relation_analyzer: Optional[SquareTokenRelationAnalyzer]
        
    Provides:
        -   ddef execute(self,) -> ValidationResult[Square]:

    Super Class:
    """
    _relation_analyzer: Optional[SquareTokenRelationAnalyzer]
    
    def __init__(self, relation_analyzer: Optional[SquareTokenRelationAnalyzer] | None = None):
        """
        Args:
            relation_analyzer: Optional[SquareTokenRelationAnalyzer]
        """
        self._relation_analyzer = relation_analyzer or SquareTokenRelationAnalyzer()
        

    @LoggingLevelRouter.monitor
    def execute(self, token: Token, destination: Square) -> DestinationApprovalReport:
        """
        Makes sure a Token can travel to a destination.

        Action:
            1.  Send an exception chan in the validation result if either:
                    -   The relation analysis is not completed.
                    -   The token is either fully or partially bound to the destination.
                    -   The destination is occupied by a friend.
            2.  Otherwise, send the success result.
        Args:
            token: Token
            destination: Square
            toolkit: TokenEndpointRelationToolkit
        Returns:
            ValidationResult
        Raises:
            DestinationCertifierBootstrapperException
            TokenAlreadyAtDestinationException
            PartialTokenDestinationRelationException
        """
        method = f"{self.__class__.__name__}.execute"
        
        
        # --- Run the relation analyzer. ---#
        relation_analysis_result = self._relation_analyzer.execute(
            candidate_primary=destination,
            candidate_satellite=token,
        )
        # Handle the case that, the relation_analysis is not completed.
        if relation_analysis_result.is_failure:
            # Send the exception chain on failure.
            return DestinationApprovalReport.deny(
                DestinationCertifierBootstrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DestinationCertifierBootstrapperException.MSG,
                    err_code=DestinationCertifierBootstrapperException.ERR_CODE,
                    ex=relation_analysis_result.exception,
                )
            )
        # --- Extract the relation report for additional tests. ---#
        relation = cast(RelationReport, relation_analysis_result.payload)
        
        # Handle the case that the token has an unexpected partial binding to the destination.
        if (
                relation.stale_link_exists or
                relation.registration_missing
        ):
            # Send the exception chain on failure.
            return DestinationApprovalReport.deny(
                DestinationCertifierBootstrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DestinationCertifierBootstrapperException.MSG,
                    err_code=DestinationCertifierBootstrapperException.ERR_CODE,
                    ex=PartialTokenDestinationRelationException(
                        msg=PartialTokenDestinationRelationException.MSG,
                        err_code=PartialTokenDestinationRelationException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the token is already at the destination.
        if relation.fully_exists:
            # Send the exception chain on failure.
            return DestinationApprovalReport.deny(
                DestinationCertifierBootstrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DestinationCertifierBootstrapperException.MSG,
                    err_code=DestinationCertifierBootstrapperException.ERR_CODE,
                    ex=TokenAlreadyAtDestinationException(
                        msg=TokenAlreadyAtDestinationException.MSG,
                        err_code=TokenAlreadyAtDestinationException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the destination is occupied by a friend.
        if token.is_friend(destination.occupant):
            # Send the exception chain on failure.
            return DestinationApprovalReport.deny(
                DestinationCertifierBootstrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DestinationCertifierBootstrapperException.MSG,
                    err_code=DestinationCertifierBootstrapperException.ERR_CODE,
                    ex=BlockedPathException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BlockedPathException.MSG,
                        err_code=BlockedPathException.ERR_CODE,
                    ),
                )
            )
        # --- Forward the work product to the caller. ---#
        return DestinationApprovalReport.grant(visitor=token, destination=destination)