#!/usr/bin/env python3
from .base import Base


class CPU(Base):
    # def process(self, handler, hostname):
    #     """
    #     获取cpu
    #     :return: 
    #     """
    #     ret = handler.cmd("dir", hostname)
    #     return ret

    def win(self, handler, hostname=None):
        ret = handler.cmd("dir", hostname)
        return ret

    def linux(self, handler, hostname=None):
        ret = handler.cmd("dir", hostname)
        return ret
    