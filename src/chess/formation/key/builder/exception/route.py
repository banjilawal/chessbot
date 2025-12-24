from chess.system import ResultException, UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_FORMATION_SUPER_KEY_BUILD_ROUTE EXCEPTION #======================#
    "FormationSuperKeyBuildRouteException",
]


# ======================# UNHANDLED_FORMATION_SUPER_KEY_BUILD_ROUTE EXCEPTION #======================#
class FormationSuperKeyBuildRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that FormationSuperKeyBuilder did not handle one of the paths necessary to assure a candidate is a
        safe to use FormationSuperKey. There are different configurations of FormationSuperKey that are correct. Each
        configuration must have a build route to guarantee all FormationSuperKey products are safe. If a
        FormationSuperKey configuration does not have a build route the last step in the logic will return a
        BuildResult containing a FormationSuperKeyBuildRouteException.

    # PARENT:
        *   ResultException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_FORMATION_SUPER_KEY_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The FormationSuperKeyBuilder did not handle one of the paths necessary to guarantee FormationSuperKeys are "
        "safe products. Ensure all possible build branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-blocks."
    )