#!/usr/bin/env python3

""" def function sum_mixed_list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """  return sum float sum list """
    return float(sum(mxd_lst))
