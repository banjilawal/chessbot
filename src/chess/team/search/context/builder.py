# src/chess/piece/event/transaction
"""
Module: chess.piece.event.transaction
Author: Banji Lawal
Created: 2025-09-28

# SCOPE:
* The limits of the module, defined by what it does not do.
* Where to look for related features this models does not provide because of its limitations.

# THEME:
* Highlight the core feature (thread-safety)
* Explain the how-and-why of implementation choices.

# PURPOSE:
* Function and role in the system.
* Why the module exists in the application architecture
* What problem it fundamentally solves

# DEPENDENCIES:

# CONTAINS:
 * ``
"""
from typing import Optional

from chess.rank import Rank, RankValidator
from chess.team import TeamSearchContext
from chess.system import IdValidator, NameValidator, Builder, BuildResult, BuilderException

class TeamSearchContextBuilder(Builder[TeamSearchContext]):
    """
    ROLE:
    ----
    RESPONSIBILITIES:
    ----------------
    PROVIDES:
    --------
    ATTRIBUTES:
    ----------
    """

    def build (
        cls,
        piece_id: Optional[int],
        roster_number: Optional[int],
        name: Optional[str],
        rank: Optional[Rank]
        ) -> BuildResult[TeamSearchContext]:
        """
        Action:
        Parameters:
        Returns:
        Raises:
        MethodNameException wraps
        """
        method = "TeamSearchContextBuilder.build"

        params = [piece_id, roster_number, name, rank]
        param_count = sum(bool(p) for p in params)

        if param_count == 0:
            raise Error("Cannot build TeamSearchContext with no params")

        if param_count > 1:
            raise Error("A TeamSearchContext can only have one field not null.")

        if piece_id is not None:
            id_validation = IdValidator.validate(piece_id)
            if not id_validation.is_success():
                raise id_validation.exception
            return TeamSearchContext(piece_id=piece_id)

        if roster_number is not None:
            if roster_number < 1 or roster_number > 16:
                raise Error("Roster number must be between 1 and 16.")
            return TeamSearchContext(roster_number=roster_number)

        if name is not None:
            name_validation = NameValidator.validate(name)
            if not name_validation.is_success():
                raise name_validation.exception
            return TeamSearchContext(name=name)