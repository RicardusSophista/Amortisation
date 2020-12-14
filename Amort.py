# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:45:04 2020

@author: RicardusSophista
"""

import datetime as dt
import dateutil as du


def cell_maker(content):
    return "|" + str(round(content,2)).rjust(8)

def non_capn(pr,pmt,nom,day_0=None,month_1=None,term=None):
    day_0 = dt.datetime.strptime("2020-01-01","%Y-%m-%d")
    
    
    sched = []
    line = {}
    line['date'] = day_0.strftime("%d/%m/%Y")
    line['intr'] = 0
    line['pmt'] = 0
    line['pr'] = pr
    sched.append(line)
    
    i = 1
    prev_date = day_0
    
    while i < term:
        curr_date = prev_date + du.relativedelta.relativedelta(months=1)
        delta = curr_date - prev_date
        num_days = delta.days
        
        line = {}
        
        line['date'] = curr_date.strftime("%d/%m/%Y")
        intr = num_days * pr * (nom/366)
        line['intr'] = intr
        line['pmt'] = pmt
        pr = pr + intr - pmt
        line['pr'] = pr
        
        sched.append(line)
        
        i += 1
        prev_date = curr_date
    
    for l in sched:
        output = '|'
        output += str(l['date'])
        output += cell_maker(l['intr'])
        output += cell_maker(l['pmt'])
        output += cell_maker(l['pr'])
        output += '|'
        print(output)

non_capn(20000,310,0.045,term=60)

        
        
    