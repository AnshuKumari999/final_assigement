# Create a class BANK and with two function simple interest and compound interest. 
#  U need to create instance for pnb, icici and hdfc banks with corresponding input.

import math
class BANK():
    def __init__(s,a,rate,time,d):
        s.a=a
        s.rate=rate
        s.time =time
        s.d=d
    
    def simple(s):
        interest=(s.a*s.rate*s.time)/100
        print("printing the simple interest: ", interest)
        
    def compound(s):
        b=1+(s.rate/s.d)
        e=s.d*s.time
        f=math.pow(b,e)
        interest2=s.a*f
        print("Printing compound interest: ", interest2)
        
b_name= input("Enter The bank Name : " )
a= int(input("enter the Amount you have submitted: "))
time= int(input("enter the time in years:  "))
d= int(input("enter number of times interest is compounded per year: "))

if(b_name=="BOI"):
         
    pnb=BANK(a,2,time,d)
    pnb.simple()
    pnb.compound()
    
if(b_name=="ICIC"):

    ICIC=BANK(a,2,time,d)
    ICIC.simple()
    ICIC.compound()
    
    
if(b_name=="HDFC"):
    hdfc=BANK(a,2,time,d)
    hdfc.simple()
    hdfc.compound()

if(b_name=="PNB"):
    PNB=BANK(a,2,time,d)
    PNB.simple()
    PNB.compound()