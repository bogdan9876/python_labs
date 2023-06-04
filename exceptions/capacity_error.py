"""
Module for capacity errors
"""

class CapacityError(Exception):
    """
    Class for capacity errors
    """

    def __init__(self, message="Inadmissible paper tray capacity."):
        super().__init__(message)
