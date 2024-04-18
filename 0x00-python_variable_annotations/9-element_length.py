#!/usr/bin/env python3
""" def function element_length """
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ ele length """
    return [(i, len(i)) for i in lst]
