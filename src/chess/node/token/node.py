from __future__ import annotations

from chess.node.color import DiscoveryColor


class TokenNode:
    _token: Token
    _discovery_color: DiscoveryColor