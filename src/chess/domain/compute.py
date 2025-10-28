# src/chess/domain/compute.py
"""
Module: chess.domain.exception
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""


from chess.piece import Piece
from chess.system import Builder, BuildResult,
from chess.domain import Domain, DomainValidator,
from chess.system.build.builder import T


class DomainBuilder(Builder[Domain]):
    """"""
    
    @classmethod
    def build(cls, piece: Piece) -> BuildResult[Domain:
        """"""
        
        method = "DomainBuilder.build"