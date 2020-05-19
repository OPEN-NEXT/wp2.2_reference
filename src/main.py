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
    message: str = "Hello world"
    print(message)

    # Solve an arbitrary quadratic equation
    a = 1
    b = 5
    c = 6
    x_1, x_2 = quadratic(a=a, b=b, c=c)
    print(str(x_1) + " " + str(x_2))

if __name__ == "__main__":
    main()