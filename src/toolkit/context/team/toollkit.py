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
from validator import NumberValidator


class TeamContextToolkit(ContextToolkit[Team]):
    """
    Role:
        -   Container
        -   Data Holder
        
    Responsibilities:
        1.  Aggregates workers and services required for TeamContext build and validation tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.


    Attributes:
        DEPENDENCIES: List[Operation]
        SERVICE_DEPENDENCIES: List[Microservice]
        
        context_model_type: TeamContext
        null_context_exception: TeamContextNullException
        context_priming_validator: PrimingValidator
        number_validator: NumberValidator
        
    Provides:
    
    Super Class:
        ContextToolkit
    """
    context_model_type = TeamContext
    team_toolkit: TeamToolkit = TeamToolkit()
    null_context_exception =  TeamContextNullException()
    number_validator: NumberValidator = NumberValidator()