# src/carrier_validator/validator/endpoint/destination/carrier_validator.py

"""
Module: carrier_validator.validator.endpoint.destination.carrier_validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from analyzer import SquareTokenRelationAnalyzer
from err import (
    BlockedPathException, DestinationCertifierBootstrapperException, PartialTokenDestinationRelationException,
    TokenAlreadyAtDestinationException
)
from model import Square, Token
from report import RelationReport
from result import ValidationResult
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
        token: Token
        destination: Square
        relation_analyzer: Optional[SquareTokenRelationAnalyzer]
        
    Provides:
        -   ddef execute(self,) -> ValidationResult[Square]:

    Super Class:
        Validator
    """
    
    _token: Token
    _destination: Square
    _relation_analyzer: Optional[SquareTokenRelationAnalyzer]
    
    def __init__(
            self,
            token: Token,
            destination: Square,
            relation_analyzer: Optional[SquareTokenRelationAnalyzer] |
                               None = SquareTokenRelationAnalyzer()
    ):
        """
        Args:
            token: Token
            destination: Square
            relation_analyzer: Optional[SquareTokenRelationAnalyzer]
        """
        self._token = token
        self._destination = destination
        self._relation_analyzer = relation_analyzer
        

    @LoggingLevelRouter.monitor
    def execute(self,) -> ValidationResult[Square]:
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
            candidate_primary=self._destination,
            candidate_satellite=self._token,
        )
        # Handle the case that, the relation_analysis is not completed.
        if relation_analysis_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
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
            return ValidationResult.failure(
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
            return ValidationResult.failure(
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
        occupant = self._destination.occupant
        if self._token.is_enemy(occupant):
            # Send the exception chain on failure.
            return ValidationResult.failure(
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
        return ValidationResult.success(self._destination)