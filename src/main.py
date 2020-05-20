#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later

# A Python 3 script that does a few simple operations

#this is an edit by rafaella
from quadratic import quadratic

def main() -> None:
    message: str = "Hello"
    print(message)

    # Solve an arbitrary quadratic equation
    a: float = 11
    b: float = 18
    c: float = 7
    x_1: float
    x_2: float
    x_1, x_2 = quadratic(a=a, b=b, c=c)
    print("Solving for x in the quadratic equation ax^2 + bx + c = 0 where")
    print("a = {0}\nb = {1}\nc = {2}".format(a, b, c))
    print("The two roots (x) are: {root_1:5.5} and {root_2:5.5}".format(
        root_1=x_1, root_2=x_2))


if __name__ == "__main__":
    main()
