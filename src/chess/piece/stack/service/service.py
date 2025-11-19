# src/chess/piece/stack/service/service.py

"""
Module: chess.piece.stack.service.service
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from typing import List, Optional



class PieceStackService:
    _pop_count: int
    _is_empty: bool
    _stack: PieceStack
    _current_piece: Piece
    _piece_service: PieceService
    _identity_service: IdentityService
    _validator: type[PieceStackValidator]
    
    def __init__(
            self,
            stack: PieceStack = PieceStack(),
            piece_service: PieceService = PieceService(),
            identity_service: IdentityService=IdentityService(),
            validator: type[PieceStackValidator]=PieceStackValidator,
    ):
        self._stack = stack
        self._validator = validator
        self._piece_service = piece_service
        
        self._pop_count = 0
        self._is_empty = self._stack.is_empty()
        self._current_piece = self._stack.current_piece
       
    @property
    def stack_size(self) -> int:
        return self._stack.size()
    
    @property
    def is_empty(self) -> bool:
        return self._stack.is_empty()
    
    @property
    def current_piece(self) -> Optional[Piece]:
        return self._stack.current_piece
        
    def pop_count(self) -> int:
        return self._pop_count
        
        
    @LoggingLevelRouter.monitor
    def push_piece(self, piece) -> Result[Piece]:
        
        method = "PieceStackService.push_piece"
        
        try:
            piece_validation = self._piece_service.validate_piece(piece)
            if piece_validation.is_failure():
                return Result.failure(piece_validation.exception)
            
            if piece in self._stack.items:
                return Result.failure(
                    PushingDuplicatePieceException(
                        f"{method}: {PushingDuplicatePieceException.DEFAULT_MESSAGE}"
                    )
                )
            
        except Exception as ex:
            return Result.failure(
                PieceStackServiceException(
                    f"{method}: {PieceStackServiceException.DEFAULT_MESSAGE}",
                    ex
                )
            )
        
        
    def undo_push(self) -> Result[Piece]:
        method = "PieceStackService.undo_push"
        
        try:
            if self._stack.is_empty():
                return Result.failure(
                    PopEmptyStackException(
                        f"{method}: {PopEmptyStackException.DEFAULT_MESSAGE}"
                    )
                )
            
            if self._pop_count == 1:
                return Result.failure(
                
                )
            
            piece = self._stack.items.pop()
            return Result.success(piece)
        
        except Exception as ex:
            return Result.failure(
                PieceStackServiceException(
                    f"{method}: {PieceStackServiceException.DEFAULT_MESSAGE}",
                    ex
                )
            )
        
        
    def find_tean(self, piece) -> SearchResult[Piece]:
        method = "PieceStackService.find_piece"
        
        try:
            piece_validation = self._piece_service.validate_piece(piece)
            if piece_validation.is_failure():
                return SearchResult.failure(piece_validation.exception)
            
            for piece in self._stack.items:
                if piece == piece:
                    return SearchResult.success(piece)
                
            return SearchResult.empty()
        except Exception as ex:
            return SearchResult.failure(
                PieceStackServiceException(
                    f"{method}: {PieceStackServiceException.DEFAULT_MESSAGE}",
                    ex
                )
            )
        
        
    def find_by_id(self, id: int) -> SearchResult[Piece]:
        method = "PieceStackService.find_by_id"
        
        try:
            id_validation = self._identity_service.validate_id(id)
            if id_validation.is_failure():
                return SearchResult.failure(id_validation.exception)
            
            for piece in self._stack.items:
                if piece.id == id:
                    return SearchResult.success(piece)
                
            return SearchResult.empty()
        
        except Exception as ex:
            return SearchResult.failure(
                PieceStackServiceException(
                    f"{method}: {PieceStackServiceException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    def find_by_name(self, name: str) -> SearchResult[List[Piece]]:
        method = "PieceStackService.find_by_name"
        
        try:
            name_validation = self._identity_service.validate_name(name)
            if name_validation.is_failure():
                return SearchResult.failure(name_validation.exception)
            
            matches = [piece for piece in self._stack if piece.name.upper() == name.upper()]
            
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(matches)
        
        except Exception as ex:
            return SearchResult.failure(
                PieceStackServiceException(
                    f"{method}: {PieceStackServiceException.DEFAULT_MESSAGE}",
                    ex
                )
            )