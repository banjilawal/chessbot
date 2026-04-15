# src/analysis/collision/token/analyst.py

"""
Module: analysis.collision.token.analyst
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from analysis import CollisionAnalyst, CollisionReport
from err import SquareNameCollisionException, TokenDesignationCollisionException, TokenIdCollisionException
from model import Token, TokenBlueprint
from result import AnalysisResult
from stack import TokenStackService
from system import LoggingLevelRouter


class TokenCollisionAnalyst(CollisionAnalyst[Token]):
    """
     Role:
         - Collision Detection Worker
         - Consistency and Uniqueness Guarantor
         
     Responsibilities:
         1.  Report if any tokens are sharing attributes which should be unique.
         
     Attributes:
     Provides:
         -   detect(
                    cls,
                    target: Token,
                    token_stack: TokenStackService,
            ) -> CollisionReport
            
     Super:
        -   CollisionAnalyst[T]
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(
            cls,
            blueprint: TokenBlueprint,
            token_stack: TokenStackService,
    ) -> AnalysisResult[CollisionReport]:
        """
        Report if any schema member has the same id, designation or
        opening_square_name as the target.
        
        Action:
            1.  Send only exception chain in the CollisionReport if:
                    *   The target does not pass a validation check.
            2.  Otherwise, send:
                    *   The target.
                    *   The collider.
                    *   The exception indicating which unique property is shared.
        Args:
            blueprint: TokenBlueprint
            token_stack: TokenStackService
        Returns:
               CollisionReport[Token]
        Raises:
            TokenIdCollisionException
            TokenDesignationCollisionException
            TokenOpeningSquareCollisionException
            TokenCollisionDetectionException
        """
        method = f"{cls.__class__.__name__}.detect"
        
        # Handle the case that, the target does not pass a validation check.
        # validation_result = token_stack.service.validator.search_service(
        #     candidate=target
        # )
        # if validation_result.is_failure:
        #     return CollisionReport.failure(
        #         exception=TokenCollisionDetectionException(
        #             val=method,
        #             var="token failed integrity validation",
        #             msg=TokenCollisionDetectionException.MSG,
        #             err_code=TokenCollisionDetectionException.ERR_CODE,
        #             ex=validation_result.exception
        #         )
        #     )
        # --- Loop through the collider_candidates to find matches. ---#
        
        for token in token_stack.items:
            # Handle the case that, the target shares its id with a collider_candidates member.
            if token.id == blueprint.id:
                # Return the collider, id, and the exception.
                return AnalysisResult.success(
                    CollisionReport.collision_occurred(
                        collider=token,
                        colliding_variable="id",
                        collision_value=token.id,
                        exception=TokenIdCollisionException(
                            var="id",
                            val=f"{token.id}",
                            msg=TokenIdCollisionException.MSG,
                            err_code=TokenIdCollisionException.ERR_CODE
                        )
                    )
                )
            # Handle the case that, the target shares its designation with a collider_candidates member.
            if token.designation.upper() == blueprint.formation.designation.upper():
                # Return the collider, designation, and the exception.
                return AnalysisResult.success(
                    CollisionReport.collision_occurred(
                        collider=token,
                        colliding_variable="designation",
                        collision_value=f"{token.designation}",
                        exception=TokenDesignationCollisionException(
                            var="designation",
                            val=f"{token.designation}",
                            msg=TokenDesignationCollisionException.MSG,
                            err_code=TokenDesignationCollisionException.ERR_CODE,
                        )
                    )
                )
            # Handle the case that, the target shares its opening_square_name with a collider_candidates member.
            if token.opening_square_name.upper()== blueprint.formation.square_name.upper():
                # Return the collider, designation, and the exception.
                return AnalysisResult.success(
                    CollisionReport.collision_occurred(
                        collider=token,
                        colliding_variable="opening_square_name",
                        collision_value=f"{token.opening_square_name}",
                        exception=SquareNameCollisionException(
                            var="opening_square_name",
                            val=f"{token.opening_square_name}",
                            msg=SquareNameCollisionException.MSG,
                            err_code=SquareNameCollisionException.ERR_CODE,
                        )
                    )
                )
        # --- Send the no collisions detected report. ---#
        return AnalysisResult.success(CollisionReport.no_collision())
    