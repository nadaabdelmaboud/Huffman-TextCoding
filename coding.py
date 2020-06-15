# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import Counter
import heapq
import sys
sys.setrecursionlimit(10**6)
class Node():
    def __init__(self,data):
        self.data=data
        self.char=None
        self.leftchild=None
        self.rightchild=None
    def add_char(self,char):
        self.char=char      
    def add_leftchild(self,leftch):
        self.leftchild=leftch
    def add_rightchild(self,rightch):
        self.rightchild=rightch
    def __lt__(self,other):
        return self.data < other.data
freqDict={}
length=0
print("start encoding")
with open("input.txt","r",encoding='utf-8') as Original:
        text = Original.read()
        length=len(text)
        freqDict = Counter(text)


unique=freqDict.keys()

    
Original=open("input.txt","r",encoding='utf-8')
        
propabilities=[]
prop={}
def probability():
    for item in unique:
        prop[item]=round((freqDict[item]/length),4)
        n=Node(prop[item])
        n.add_char(item)
        propabilities.append(n)
probability()


heapq.heapify(propabilities)

counter=len(propabilities)

while (len(propabilities)>1):
    min1=heapq.heappop(propabilities)
    min2=heapq.heappop(propabilities)
    
    n=Node(min1.data+min2.data)
    n.add_leftchild(min1)
    n.add_rightchild(min2)
    heapq.heappush(propabilities,n)
    counter-=1
result=heapq.heappop(propabilities)
  
encode={}
encoded_txt=""

def get_leaves(node,str):
    if(node.leftchild== None and node.rightchild == None):
        encode[node.char]=str
        return
    else:
        get_leaves(node.leftchild,str+'0')
        get_leaves(node.rightchild,str+'1')  
get_leaves(result,"")
Original=open("input.txt","r",encoding='utf-8')
Output=open("encoded.bin","wb")
datalength=0
restlength=0

text=Original.read()
b_arr = bytearray()
for i in range(len(text)):
    encoded_txt+=encode[text[i]]
    if(len(encoded_txt)>8):
        b_arr.append(int(encoded_txt[0:8], 2))
        encoded_txt=encoded_txt[8:len(encoded_txt)]
if(len(encoded_txt)>8):
    b_arr.append(int(encoded_txt[0:8], 2))
    encoded_txt=encoded_txt[8:len(encoded_txt)]
if(len(encoded_txt)>0):
    restlength=8-len(encoded_txt)

if(restlength != 0):
    encoded_txt = encoded_txt+restlength * "0"

b_arr.append(int(encoded_txt[0:8], 2))

Output.write(b_arr)
Output.close()    







'''decoding'''

print("start decoding")

Inpencoded=open("encoded.bin","rb")
enctext=""
byte = Inpencoded.read(1)
while len(byte) > 0:
    enctext += f"{bin(ord(byte))[2:]:0>8}"
    byte = Inpencoded.read(1)

def get_key(val): 
    for key, value in encode.items(): 
         if val == value: 
             return key 
    return None    
Outpencoded=open("decoded.txt","w",encoding='utf-8')    
cmpstr=""
index=0
while (index<len(enctext)-restlength):
    c=enctext[index]
    if not c:
        break
    cmpstr+=c
    index+=1
    if get_key(cmpstr):
       Outpencoded.write(get_key(cmpstr))
       cmpstr=""
       continue
Outpencoded.close()
        
        
    
    
    
    
    
    
    
    
    
