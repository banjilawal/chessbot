# src/chess/team/schema/service.py

"""
Module: chess.team.schema.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from chess.team.schema import TeamSchema


class TeamSchemaService:
    _schema: TeamSchema
    
    def __init__(self):
        self._schema = TeamSchema
        
     @classmethod
     def
