# src/chess/team/context/validator/validator.py

"""
Module: chess.team.context.validator.validator
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""
from typing import Any, cast

from chess.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.team import (
    InvalidTeamContextException, NoTeamContextFlagSetException, NullTeamContextException, TeamContext,
    TooManyTeamContextFlagsSetException
)


class TeamContextValidator(Validator[TeamContext]):
    
    @classmethod
    def validate(cls, candidate: Any, *args, **kwargs) -> ValidationResult[TeamContext]:
        
        @classmethod
        @LoggingLevelRouter.monitor
        def validate(
                cls,
                candidate: Any,
                coord_service: CoordService = CoordService(),
                identity_service: IdentityService = IdentityService(),
        ) -> ValidationResult[TeamContext]:
            """"""
            method = "TeamContextValidator.validate"
            
            try:
                if candidate is None:
                    return ValidationResult.failure(
                        NullTeamContextException(
                            f"{method}: "
                            f"{NullTeamContextException.DEFAULT_MESSAGE}"
                        )
                    )
                
                if not isinstance(candidate, TeamContext):
                    return ValidationResult.failure(
                        TypeError(
                            f"{method}: Expected TeamContext, got {type(candidate).__name__} instead."
                        )
                    )
                
                context = cast(TeamContext, candidate)
                
                if len(context.to_dict()) == 0:
                    return ValidationResult.failure(
                        NoTeamContextFlagSetException(
                            f"{method}: "
                            f"{NoTeamContextFlagSetException.DEFAULT_MESSAGE}"
                        )
                    )
                
                if len(context.to_dict()) > 1:
                    return ValidationResult.failure(
                        TooManyTeamContextFlagsSetException(
                            F"{method}: "
                            F"{TooManyTeamContextFlagsSetException.DEFAULT_MESSAGE}"
                        )
                    )
                
                if context.id is not None:
                    validation = identity_service.validate_id(candidate=context.id)
                    if validation.is_failure():
                        return ValidationResult.failure(validation.exception)
                    return ValidationResult.success(context)
                
                if context.name is not None:
                    validation = identity_service.validate_name(candidate=context.name)
                    if validation.is_failure():
                        return ValidationResult.failure(validation.exception)
                    return ValidationResult.success(context)
                
                if context.coord is not None:
                    validation = coord_service.validator.validate(
                        candidate=candidate,
                        validator=coord_service.validator
                    )
                    if validation.is_failure():
                        return ValidationResult.failure(validation.exception)
                    return ValidationResult.succes(context)
            
            except Exception as ex:
                return ValidationResult.failure(
                    InvalidTeamContextException(
                        ex=ex,
                        message=(
                            f"{method}: "
                            f"{InvalidTeamContextException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(TeamContext(id=id))
            
            if agent is not None:
                validation = agent_service.validator.validate(agent)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(TeamContext(agent=agent))
            
            if name is not None:
                validation = team_validator.validate_name(name)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(TeamContext(name=name))
            
            if color is not None:
                validation = team_validator.validate_color(color)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(TeamContext(color=color))
            
            if schema is not None:
                return BuildResult.success(TeamContext(schema=schema))
        
        except Exception as ex:
        return BuildResult.failure(
            PieceContextBuildFailedException(
                ex=ex,
                message=(
                    f"{method}: "
                    f"{PieceContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
        )