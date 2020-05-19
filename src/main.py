#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later

# A trivial Python 3 script


def quadratic(a, b, c):
    """Solve a quadratic equation"""
    x_1 = (-b + (b**2 - 4*a*c)**(1/2)) / (2*a)
    x_2 = (-b - (b**2 - 4*a*c)**(1/2)) / (2*a)

    return x_1, x_2


def main():
    message: str = "Hello"
    print(message)

    # Solve an arbitrary quadratic equation
    a = 11
    b = 18
    c = 7
    x_1, x_2 = quadratic(a=a, b=b, c=c)
    print("Solving for x in the quadratic equation ax^2 + bx + c = 0 where")
    print("a = {0}\nb = {1}\nc = {2}".format(a, b, c))
    print("The two roots (x) are: {root_1:5.5} and {root_2:5.5}".format(
        root_1=x_1, root_2=x_2))


if __name__ == "__main__":
    main()
