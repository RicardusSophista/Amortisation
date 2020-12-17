# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:45:04 2020

@author: RicardusSophista
"""

import datetime as dt
import dateutil as du


def get_float(prompt,dp=None,mini=None,maxi=None):
    while True:
        raw = input(prompt + '\n>>> ')
        try:
            raw = float(raw)
            if dp != None:
                f = round(raw,dp)
                if f != raw:
                    print('{} has been rounded to {}.'.format(raw,f))
            else:
                f = raw
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

def get_str(prompt,valids=None,case_sensitive='N'):
    while True:
        s = input(prompt + '\n>>> ')
        if valids:
            if case_sensitive == 'N':
                valids = [v.upper() for v in valids]
                s = s.upper()
            
            if s not in valids:
                opts = ', '.join(valids)
                print('Please select from {}'.format(opts))
                continue
        return s

def get_int(prompt, mini=None,maxi=None):
    while True:
        raw = input(prompt + '\n>>> ')
        try:
            i = int(raw)
        except:
            print('Please enter a whole number.')
            continue
        
        if mini != None:
            if i < mini:
                print('c. Please enter a whole number that is greater than {}.'.format(mini))
                continue
            
        if maxi != None:
            if i > maxi:
                print('d. Please enter a whole number that is less than {}.'.format(maxi))
                continue
        return i
        
def get_date(prompt,earliest=None,latest=None):
    while True:
        raw = input(prompt + '\n>>> ')
        try:
            day, month, year = raw.split('/')
            d = dt.datetime(int(year), int(month), int(day))
        except:
            print('Please enter a valid date in the format DD/MM/YYYY')
            continue
        
        if earliest:
            if d < earliest:
                print('Please enter a date that is later than {}.'.format(earliest.strftime('%d/%m/%Y')))
                continue
        if latest:
            if d > latest:
                print('Please enter a date that is earlier than {}.'.format(latest.strftime('%d/%m/%Y')))
                continue
        
        return d
        

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
        if i == 1 and month_1 != None:
            curr_date = month_1
        else:
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
    day_0 = get_date('Input the drawdown date in the format DD/MM/YYYY')    
else:
    day_0 = dt.datetime.today()

q = get_str('Do you wish to specify a first payment date Y/N? (If N, the first payment will be one month after drawdown.)',valids=['Y','N'])
if q == 'Y':
    month_1 = get_date('Input the first payment date in the format DD/YY/MMMM', earliest=day_0)
else:
    month_1 = None

term = get_int('Input the term',mini=0)

non_capn(pr,pmt,nom,day_0=day_0,month_1=month_1,term=term)

        
        
    