# src/toolkit/context/team/toolkit.py

"""
Module: toolkit.context.team.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import TeamContextNullException
from model import Team, TeamContext
from toolkit import ContextToolkit, TeamToolkit
from validation import NumberValidator


class TeamContextToolkit(ContextToolkit[Team]):
    """
    Role:
        -   Container
        -   Data Holder
        
    Responsibilities:
        1.  Collection of workers and services that are required for Team tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        DEPENDENCIES: List[Operation]
        SERVICE_DEPENDENCIES: List[Microservice]
        
        context_model_type: TeamContext
        null_context_exception: TeamContextNullException
        context_validation_primer: ValidationBootstrapper
        number_validator: NumberValidator
        
    Provides:
    
    Super Class:
        ContextToolkit
    """
    context_model_type = TeamContext
    team_toolkit: TeamToolkit = TeamToolkit()
    null_context_exception =  TeamContextNullException()
    number_validator: NumberValidator = NumberValidator()