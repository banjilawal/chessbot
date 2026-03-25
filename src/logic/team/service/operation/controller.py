# src/logic/team/service/operation/controller.py

"""
Module: logic.team.service.operation.manager
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from logic.team import TeamBuild, TeamDeploymentProcess, TeamValidation


class TeamOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations TeamService supports.
        
    Attributes:
        build: TeamBuild
        validate: TeamValidation
        deployment: TeamDeploymentProcess

    Provides:
    
    Parent:
    """
    _build: TeamBuild
    _validation: TeamValidation
    _deployment: TeamDeploymentProcess
    
    
    def __init__(
            self,
            build: TeamBuild = TeamBuild(),
            validation: TeamValidation = TeamValidation(),
            deployment: TeamDeploymentProcess = TeamDeploymentProcess(),
    ):
        """
        Args:
            build: TeamBuild
            validation: TeamValidation
            deployment: TeamDeployment
        """
        self._build = build
        self._validation = validation
        self._deployment = deployment
        
    @property
    def build(self) -> TeamBuild:
        return self._build
        
    @property
    def validation(self) ->TeamValidation:
        return self._validation

    @property
    def deployment(self) -> TeamDeploymentProcess:
        return self._deploymentr