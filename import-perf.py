#!/usr/bin/env python2.7
# encoding: utf-8

"""
    @brief: 
    @author: icejoywoo
    @date: 15/12/7
"""

import string

import perf


def lower_with_import():
    import string
    return string.lower('Python')


def lower_without_import():
    return string.lower('Python')


if __name__ == '__main__':
    print perf.perf(lower_with_import)
    print perf.perf(lower_without_import)
