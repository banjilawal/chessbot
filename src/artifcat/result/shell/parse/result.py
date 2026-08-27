# src/artifact/result/shell/parse/result.py

"""
Module: artfifact.result.shell.parse.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ParseState, ShellResult
from shell import Command


class ParseResult(ShellResult[Command]):
    """
    Role:
        - Data Transport
        -  Error Transport

    Responsibilities:
        1.  Contains the outcome of a parse.

    Attributes:
        state: ParseState
        payload: Optional[Command]
        exception: Optional[Exception]
        
        is_timed_out: bool
        is_success: bool
        is_failure: bool
        nothing_to_parse: bool

    Provides:
        - def success(payload: T) -> ParseResu[Command]
        - def failure(exception: Exception) -> ParseResu[Command]
        - def timed_out(exception: Exception) -> ParseResult
        - def nothing_to_parse() -> ParseResult

    Super Class:
        ShellResult
    """
    _state = ParseState
    
    def __init__(
            self,
            state: ParseState,
            payload: Optional[Command] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: ParseState
            payload: Optional[Command]
            exception: Optional[Exception]
        """
        super().__init__(
            payload=payload,
            exception=exception,
        )
        """INTERNAL: Use build methods instead of direct constructor."""
        self._state = state
        
    @property
    def state(self) -> ParseState:
        return self._state
    
    @property
    def payload(self) -> Optional[Command]:
        return cast(Command, super().payload)
    
    @property
    def is_success(self) -> bool:
        return (
            self.payload is not None and
            self.exception is None and
            self._state == ParseState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == ParseState.FAILURE or
                self._state == ParseState.TIMED_OUT
        )
    
    @property
    def nothing_to_parse(self) -> bool:
        return (
                self.payload is None and
                self.exception is None and
                self._state == ParseState.NOTHING_TO_PARSE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == ParseState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: Command) -> ParseResult:
        return cls(
            payload=payload,
            exception=None,
            state=ParseState.SUCCESS,
        )
    
    @classmethod
    def nothing(cls,) -> ParseResult:
        return cls(
            payload=None,
            exception=None,
            state=ParseState.NOTHING_TO_PARSE,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> ParseResult:
        return cls(
            payload=None,
            exception=exception,
            state=ParseState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> ParseResult:
        return cls(
            payload=None,
            exception=exception,
            state=ParseState.TIMED_OUT,
        )

