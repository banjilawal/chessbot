# src/artifact/interface/transactional/interface.py

"""
Module: artifact.interface.transactional.interface
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from artifcat import ArtifactInterface


class Transactional(ArtifactInterface, ABC):
    pass