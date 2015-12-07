#!/usr/bin/env python2.7
# encoding: utf-8

"""
    @brief: 
    @author: icejoywoo
    @date: 15/12/7
"""


class Test:
    def check(self, a, b, c):
        if a == 0:
            self.str = b * 100
        else:
            self.str = c * 100


a = Test()


def example():
    for i in xrange(0, 100000):
        a.check(i, "b", "c")


class Test2:
    def check(self, a, b, c):
        self.str = b * 100
        self.check = self.check_post

    def check_post(self, a, b, c):
        self.str = c * 100


b = Test2()


def example2():
    for i in xrange(0, 100000):
        b.check(i, "b", "c")


if __name__ == '__main__':
    import profile
    profile.run("example()")
    profile.run("example2()")
