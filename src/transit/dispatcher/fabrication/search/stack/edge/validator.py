# src/transit/dispatcher/fabrication/search/stack/edge/validator.py

"""
Module: transit.dispatcher.fabrication.search.stack.edge.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


class EdgeContextValidator(ContextValidator[Edge]):
    """
     Role:Build, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a EdgeContext instance is certified safe, reliable, and consistent before use.
    2.  If verification fails indicate the reason in an exception returned to the caller.

    Super Class:
        *   Validator

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            edge_service: EdgeService = EdgeService(),
            identity_service: IdentityService = IdentityService()
    ) -> BuildResult[Edge]:
        """
        # ACTION:
            1.  If Candidate fails existence or type checks return the exception chain in the BuildResult. Else,
                test how many optional attributes are not null.
            2.  If only one attribute is one and only one attribute is not null return the exception chain in the
                BuildResult.
            3.  If no route is found for the enabled attribute send an exception chain in the BuildResult.
            4.  If a build route exists return the outcome of the build to the caller.
        # PARAMETERS:
            *   rank (Any)
            *   board_service (BoardService)
            *   coord_service (CoordService)
            *   edge_service (EdgeService)
            *   identity_service (IdentityService):
        # RETURNS:
            *   BuildResult[Edge] containing either:
                    - On failure:   Exception.
                    - On success:   EdgeContext in the payload.
        Raises:
            *   TypeError
            *   NullEdgeContextException
            *   ZeroEdgeContextFlagsException
            *   ArenaEdgeContextFlagsException
            *   EdgeContextBuildRouteException
            *   EdgeContextValidatorException
        """
        method = "EdgeContextValidator.execute"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return BuildResult.failure(
                EdgeContextValidatorException(
                    msg=f"{method}: {EdgeContextValidatorException.MSG}",
                    ex=NullEdgeContextException(f"{method}: {NullEdgeContextException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, EdgeContext):
            # Send the exception chain on failure.
            return BuildResult.failure(
                EdgeContextValidatorException(
                    msg=f"{method}: {EdgeContextValidatorException.MSG}",
                    ex=TypeError(
                        f"{method}: Was expecting a EdgeContext, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast the candidate into EdgeContext for additional tests. ---#
        context = cast(EdgeContext, priming.payload)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Send the exception chain on failure.
            return BuildResult.failure(
                EdgeContextValidatorException(
                    msg=f"{method}: {EdgeContextValidatorException.MSG}",
                    ex=ZeroEdgeContextFlagsException(f"{method}: {ZeroEdgeContextFlagsException.MSG}")
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Send the exception chain on failure.
            return BuildResult.failure(
                EdgeContextValidatorException(
                    msg=f"{method}: {EdgeContextValidatorException.MSG}",
                    ex=ArenaEdgeContextFlagsException(
                        f"{method}: {ArenaEdgeContextFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate build branch. ---#
        
        # Build for the search-by-id target.
        if context.id is not None:
            build = identity_service.validate_id(candidate=context.id)
            if build.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    EdgeContextValidatorException(
                        msg=f"{method}: {EdgeContextValidatorException.MSG}",
                        ex=validator.exception
                    )
                )
            # On build success return the id_EdgeContext in the BuildResult.
            return BuildResult.success(payload=context)
        
        # Build for the search-by-schema target.
        if context.name is not None:
            build = identity_service.validate_name(context.name)
            if build.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    EdgeContextValidatorException(
                        msg=f"{method}: {EdgeContextValidatorException.MSG}",
                        ex=validator.exception
                    )
                )
            # On build success return the name_EdgeContext in the BuildResult.
            return BuildResult.success(payload=context)
        
        # Build for the search-by-coord target.
        if context.coord is not None:
            build = coord_service.execute.execute(context.coord)
            if build.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    EdgeContextValidatorException(
                        msg=f"{method}: {EdgeContextValidatorException.MSG}",
                        ex=validator.exception
                    )
                )
            # On build success return the coord_EdgeContext in the BuildResult.
            return BuildResult.success(payload=context)
        
        # Build for the search-by-board target.
        if context.board is not None:
            build = board_service.execute.execute(context.board)
            if build.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    EdgeContextValidatorException(
                        msg=f"{method}: {EdgeContextValidatorException.MSG}",
                        ex=validator.exception
                    )
                )
            # On build success return the board_EdgeContext in the BuildResult.
            return BuildResult.success(payload=context)
        
        # Build for the search-by-occupant target.
        if context.occupant is not None:
            build = edge_service.execute.execute(context.occupant)
            if build.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    EdgeContextValidatorException(
                        msg=f"{method}: {EdgeContextValidatorException.MSG}",
                        ex=validator.exception
                    )
                )
            # On build success return the board_EdgeContext in the BuildResult.
            return BuildResult.success(payload=context)
        
        # Build for the search-by-state.
        if context.state is not None:
            if not isinstance(context.state, EdgeState):
                # Send the exception chain on failure.
                return BuildResult.failure(
                    EdgeContextValidatorException(
                        msg=f"{method}: {EdgeContextValidatorException.MSG}",
                        ex=TypeError(
                            f"{method}: Was expecting a EdgeState, got {type(candidate).__name__} instead."
                        )
                    )
                )
            # On build success return the board_EdgeContext in the BuildResult.
            return BuildResult.success(payload=context)
        
        # Return the exception chain if there is no build route for the context.
        return BuildResult.failure(
            EdgeContextValidatorException(
                msg=f"{method}: {EdgeContextValidatorException.MSG}",
                ex=EdgeContextBuildRouteException(
                    f"{method}: {EdgeContextBuildRouteException.MSG}"
                )
            )
        )

