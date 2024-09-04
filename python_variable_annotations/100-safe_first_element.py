#!/usr/bin/env python3
"""Define function safe_first_element"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a sequence if it exists, else None"""
    if lst:
        return lst[0]
    else:
        return None
