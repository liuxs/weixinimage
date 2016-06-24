#!/usr/bin/env python
# liuxs

import re

class WeXinImage:
    def __init__(self, datfile):
        datfile = datfile.lower()
        with open(datfile, 'rb') as f:
            buf = bytearray(f.read())
        buflist=list(buf)
        print buflist
        for i in range(len(buflist)):
            buflist[i] = self.replacestr(hex(buflist[i]))
            buflist[i]=int(buflist[i],16)
        imgfile = re.sub(r'.dat$', '.jpg', datfile)
        with open(imgfile, 'wb') as f:
            newbuf = bytearray(buflist)
            f.write(str(newbuf))
        sys.exit(0)
    def replacestr(self,str):
        temp=''
        temp= str.replace("0x", "")
        if(len(temp)<2):
            temp = "0"+temp
        temp = result = {
            '0': lambda :temp.replace("0", "D",1),
            '1': lambda :temp.replace("1", "c",1),
            '2': lambda :temp.replace("2", "f",1),
            '3': lambda :temp.replace("3", "e",1),
            '4': lambda :temp.replace("4", "9",1),
            '5': lambda :temp.replace("5", "8",1),
            '6': lambda :temp.replace("6", "b",1),
            '7': lambda :temp.replace("7", "a",1),
            '8': lambda :temp.replace("8", "5",1),
            '9': lambda :temp.replace("9", "4",1),
            'a': lambda :temp.replace("a", "7",1),
            'b': lambda :temp.replace("b", "6",1),
            'c': lambda :temp.replace("c", "1",1),
            'd': lambda :temp.replace("d", "0",1),
            'e': lambda :temp.replace("e", "3",1),
            'f': lambda :temp.replace("f", "2",1)
        }[temp[0]]()
        temp="0x"+temp
        return temp
if __name__ == '__main__':
    import sys
    datfile = sys.argv[:2]
    try:
        WeXinImage(datfile)
    except Exception as e:
        print e
        sys.exit(1)
    sys.exit(0)
