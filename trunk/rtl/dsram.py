# -*- coding: utf-8 -*-
"""
    dsram.py
    ========

    Dual port synchronous ram
    
    :copyright: Copyright (c) 2010 Jian Luo.
    :author-email: jian <dot> luo <dot> cn <at> gmail <dot> com.
    :license: BSD, see LICENSE for details.
    :revision: $Id$
"""

from myhdl import *
from defines import *
from functions import *

def DSRAM(dat_o, adr_i, ena_i, dat_w_i, adr_w_i, wre_i, clock,
           width=32, size=8):
    """
    Dual port synchronous RAM with New Data Read-During-Write Behavior
    """
    ram = [Signal(intbv(0)[width:]) for i in range(2**size)]
    #read_addr = Signal(intbv(0)[len(adr_i):])
    @always(clock.posedge)
    def logic():
        if ena_i:
            if wre_i:
                ram[int(adr_w_i)].next = dat_w_i
            dat_o.next = ram[int(adr_i)]
            #read_addr.next = adr_i
                # XXX: Hacked to assure read after write
                #if adr_w_i == adr_i:
                    #dat_o.next = dat_w_i
                #else:
                    #dat_o.next = ram[int(adr_i)]
            #else:
                #dat_o.next = ram[int(adr_i)]
    #@always_comb
    #def passthrough():
        #dat_o.next = ram[int(read_addr)]

    return instances()
                
### EOF ###
# vim:smarttab:sts=4:ts=4:sw=4:et:ai:tw=80:

