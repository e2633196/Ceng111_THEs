def check_month(x):
   
    A=[]
    B=[]
    numberlist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    numbforuseindex=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

    #rule1
    momnew=x[:]
    
    n=x.count("m")
    

    if n>0:
        mama=x.index("m")
        del momnew[(mama)::5]
    
    if n==0:
        A.append(0)

    
    elif momnew.count("m")==0:
        A.append(10*x.count("m"))
    

    else:
        B.append(1)



    #rule2

    weekendlist=x[0:5]+["sat","sun"]+x[5:10]+["sat","sun"]+x[10:15]+["sat","sun"]+x[15:20]+["sat","sun"]+x[20:]
       
    

    if x.count("f")>0:
        fat=weekendlist.index("f")
        fatnew=weekendlist[(fat+2)::]
    
    

    if x.count("f")==0:
        A.append(0)

    elif x.count("f") ==1:
        A.append(20)

    elif x.count("f")==2 and fatnew.count("f")==1:
        A.append(40)

    else:
        B.append(2)
        
   


        #rule3
    
    numblistfornanny=[num for num in numbforuseindex if num<len(weekendlist)]
    wetakeindex=[num for num in numblistfornanny if weekendlist[num]=="b"]
    lenofmoneycheck=[num for num in numbforuseindex if num<(len(wetakeindex)-1)]
    forextraday=[(wetakeindex[num+1]-wetakeindex[num]-1) for num in lenofmoneycheck if (wetakeindex[num+1]-wetakeindex[num]-1)<3]
    
    if x.count("b")==0:
        A.append(0)
    else:
        A.append(30*x.count("b")+30*sum(forextraday))
    
        #indexlerinin oldugu liste yaptın#





        #rule4

    grandnew=x[2::5]



    if grandnew.count("g")>1:
        B.append(4)

    else:
        A.append(50*x.count("g"))



        #rule5
    aunty1=x[:]
    ant=aunty1[0::5]+aunty1[2::5]+aunty1[3::5]
    
    if x.count("a1")==0:
        A.append(0)
        
    elif ant.count("a1")>0:
        B.append(5)
    else:
        A.append(32*x.count("a1"))


        #rule6
    indexfora2=[num for num in numblistfornanny if weekendlist[num]=="a2"]
    a1_controllist=[(num-1) for num in indexfora2 if num>0 ]
    isthere_a1=[num for num in a1_controllist if weekendlist[num]=="a1"]
    
    
    if x.count("a2")==0:
        A.append(0)
    elif len(isthere_a1)>0:
        B.append(6)
    else:
        A.append(27*x.count("a2"))
    





        #rule7

    neighbourany=x.count("n")
    ne_check=x[3::5]+x[4::5]
    numbneg=x.count("n")
    costlist=[num for num in numberlist if num<numbneg]
    moneysne=[5**num for num in costlist]

    if neighbourany==0:
        A.append(0)
    elif ne_check.count("n")>0:
        B.append(7)
    else:
        A.append(sum(moneysne))




    if len(B)>0:
        return B
    else:
        return sum(A)


        
        



 
        



   












