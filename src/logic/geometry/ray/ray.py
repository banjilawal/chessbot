from typing import List

from logic.coord import Coord

class CoordRay:
    """
    # ROLE: Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Identify the PerpendicularRayComputation method where the process failed.
    2.  wrap any debug exception created when a condition prevents the computational logic from producing
        a ray of vectors in the
            horizontal subdomains:
                *  the regions where [-n < i] or [i <= j < n] the domain is (x_i, y_i) -> R(:X_i,X_j)
            Vertical subdomains:
                *  the regions where [-n < i] or [i <= j < n] the domain is (x_i, y_i) -> R(:X_j,Y_-)

    # PARENT:
        *   ComputationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   op (Optional[str])
        *   rslt_type (Optional[str])

    # INHERITED ATTRIBUTES:
        *   See ComputationException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:)
        *   err_code (str)
        *   msg (str)
        *   ex (Optional[Exception])
        *   mthd (Optional[str])
        *   op (Optional[str])
        *   rslt_type (Optional[str])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See ComputationException class for inherited methods.
    """
    _origin: Coord
    _points: List[Coord]
    
    def __init__(self, origin: Coord, points: List[Coord]):
        self._origin = origin
        self._points = points
        
    @property
    def origin(self) -> Coord:
        return self._origin
    
    @property
    def points(self) -> List[Coord]:
        return self._points