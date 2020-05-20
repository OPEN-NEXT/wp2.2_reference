#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later

#here's a comment by rafaella

from typing import Tuple


def quadratic(a: float, b: float, c: float) -> Tuple[float, float]:
    """Solve a quadratic equation"""
    x_1: float = (-b + (b**2 - 4*a*c)**(1/2)) / (2*a)
    x_2: float = (-b - (b**2 - 4*a*c)**(1/2)) / (2*a)

    return (x_1, x_2)

#here's another comment
