# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:45:04 2020

@author: RicardusSophista
"""

import datetime as dt
import dateutil as du


def get_float(prompt,dp=None,mini=None,maxi=None):
    while True:
        f = input(prompt + '\n>>> ')
        try:
            f = float(f)
            if dp:
                f = round(f,dp)
        except:
            print('Please input a number.')
            continue
        
        if mini != None:
            if f < mini:
                print('Please input a number that is greater than {}.'.format(mini))
                continue
        
        if maxi != None:
            if f > maxi:
                print('Please input a number that is less than {}.'.format(maxi))
                continue
        
        return f

def get_str(prompt,valids=None):
    while True:
        s = input(prompt + '\n>>> ')
        if valids:
            if s not in valids:
                opts = ', '.join(valids)
                print('Please select from {}'.format(opts))
                continue
        return s
        

def cell_maker(content):
    return "|" + str(round(content,2)).rjust(8)

def non_capn(pr,pmt,nom,day_0=None,month_1=None,term=None):
   
    
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


pr = get_float('Input the amount borrowed',dp=2,mini=0)
pmt = get_float('Input the monthly payment amount',dp=2,mini=0)
nom = get_float('Input the nominal rate of interest (e.g., for 4.5%, input 4.5)',mini=0) / 100

q = get_str('Do you wish to specify a drawdown date Y/N? (If N, today\'s date will be used.)',valids=['Y','N'])
if q == 'Y':
    raw = input('Input the drawdown date in the format DD/MM/YYYY')
    day, month, year = raw.split('/')
    day_0 = dt.datetime(int(year), int(month), int(day))
    
else:
    day_0 = dt.datetime.today()

#MONTH_1 function to be added

term = float(input('Input the term'))

non_capn(pr,pmt,nom,day_0=day_0,term=term)

        
        
    