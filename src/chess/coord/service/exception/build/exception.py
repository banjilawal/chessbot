

from chess.system import BuildFailedException,  CoordServiceException

__all__ = ["CoordServiceBuildFailedException"]

# ====================== COORD_SERVICE BUILD EXCEPTIONS #======================#
class CoordServiceBuildFailedException(CoordServiceException, BuildFailedException):
    """Catchall Exception for CoordServiceBuilder when it stops because of an error."""
    ERROR_CODE = "COORD_SERVICE_BUILD_FAILED"
    DEFAULT_MESSAGE = "CoordService build failed."