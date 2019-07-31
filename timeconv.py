#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if s[0:2]!='12' and 'PM' in s:
        t=int(s[0:2])+12
        r=str(t) + s[2:8]
    elif s[0:2]=='12':
        t=int(s[0:2])
        d=t+12
        if 'AM' in s:
            t=int(s[0:2])+12
            if t>23 and t<25:
                t='00'
            r=t + s[2:8]
        else:
            r=str(t) + s[2:8]
        
    elif s[0:2]=='12' and s[8:10]=='AM':
        t=int(s[0:2])+12
        if t>23 and t<25:
            t='00'            
        r=t + s[2:8]
    elif 'AM' in s:
        #t=int(s[0:2])
        #r=str(t) + s[2:]
        r=s[0:8]
    else:
        t=int(s[0:2])
        r=str(t) + s[2:]
    return r
    
    
if __name__ == '__main__':
    

    s = input()

    result = timeConversion(s)

    print(result)
