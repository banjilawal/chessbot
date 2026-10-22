# src/authorization/interface/applicant/interface.py

"""
Module: authorization.interface.applicant.interface
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from authorization import Checkable


class Attributable(Checkable, ABC):
    pass