#!/usr/bin/env python2.7
# encoding: utf-8

"""
    @brief: 
    @author: icejoywoo
    @date: 15/12/7
"""

import perf

s = ['hello', 'world', 'python', 'is', 'test', 'itself', 'instead', 'of', 'internationlization']


def upper_common():
    r = []
    for i in s:
        r.append(str.upper(i))
    return r


def upper_without_dots():
    r = []
    upper = str.upper
    for i in s:
        r.append(upper(i))
    return r


def upper_common_lc():
    """ list comprehension
    """
    return [str.upper(i) for i in s]


def upper_common_lc_2():
    """ list comprehension
    """
    return [i.upper() for i in s]


def upper_without_dots_lc():
    """ list comprehension
    """
    upper = str.upper
    return [upper(i) for i in s]


if __name__ == '__main__':
    print perf.perf(upper_common)
    print perf.perf(upper_without_dots)

    print perf.perf(upper_common_lc)
    print perf.perf(upper_common_lc_2)
    print perf.perf(upper_without_dots_lc)
