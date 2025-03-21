def area(Q,T):
    corners=[]
    indexsıracor=[]
    sıralıcorners=[]
    controllist=[]
    xlist=[]



    def kesişim(Q,T):
   
        forQ=Q[:]+[Q[0]]
        forT=T[:]+[T[0]]
    
        for i in range(len(forQ)-1):
            for k in range(len(forT)-1):
                A=forQ[i]
                B=forQ[i+1]
                C=forT[k]
                D=forT[k+1]

                try:
            
                    a=A[0]
                    b=A[1]
                    c=B[0]
                    d=B[1]
                    m=C[0]
                    l=C[1]
                    k=D[0]
                    r=D[1]
                    rangex=sorted([a,c,m,k])
                    rangey=sorted([b,d,l,r])
                    triax=sorted([m,k])
                    triay=sorted([l,r])
                    quarx=sorted([a,c])
                    quary=sorted([b,d])
                    pointx=(((a*d-a*b)/(c-a))-((m*r-m*l)/(k-m))+l-b)/(((d-b)/(c-a))-((r-l)/(k-m)))
                    pointy=((d-b)/(c-a))*(pointx-a)+b 

                
                    if pointx>=rangex[1] and pointx<=rangex[2]:
                        if pointy>=rangey[1] and pointy<=rangey[2]:
                            if pointx>=triax[0] and pointx<=triax[1]:
                                if pointy>=triay[0] and pointy<=triay[1]:
                                    if pointx>=quarx[0] and pointx<=quarx[1]:
                                        if pointy>=quary[0] and pointy<=quary[1]:

                                            corners.append((pointx,pointy))
        
                except ZeroDivisionError:
                    try:
                        if a==c:
                            zerodivx=sorted([m,k])
                            zerodivy=sorted([l,r])
                            if a<=zerodivx[1] and a>=zerodivx[0]:
                                pointx=a 
                                pointy=((r-l)/(k-m))*(pointx-m)+l
                                if pointy<=zerodivy[1] and pointy>=zerodivy[0]:
                                    if pointx>=triax[0] and pointx<=triax[1]:
                                        if pointy>=triay[0] and pointy<=triay[1]:
                                            if pointx>=quarx[0] and pointx<=quarx[1]:
                                                if pointy>=quary[0] and pointy<=quary[1]:

                                                    corners.append((pointx,pointy))
                        if m==k:
                            zerodivx=sorted([a,c])
                            zerodivy=sorted([b,d])
                            if m<=zerodivx[1] and m>=zerodivx[0]:
                                pointx=m 
                                pointy=((d-b)/(c-a))*(pointx-a)+b
                                if pointy<=zerodivy[1] and pointy>=zerodivy[0]:
                                    if pointx>=triax[0] and pointx<=triax[1]:
                                        if pointy>=triay[0] and pointy<=triay[1]:
                                            if pointx>=quarx[0] and pointx<=quarx[1]:
                                                if pointy>=quary[0] and pointy<=quary[1]:

                                                    corners.append((pointx,pointy))
                    except ZeroDivisionError:
                        continue


    def isitin(Q,T):
        
        def forTria(Q,T):
            point1=T[0]
            point2=T[1]
            point3=T[2]



            for i in range(len(Q)):
                Px=Q[i][0]
                Py=Q[i][1]
                bx=point2[0]-point1[0]
                by=point2[1]-point1[1]
                cx=point3[0]-point1[0]
                cy=point3[1]-point1[1]
                x=Px-point1[0]
                y=Py-point1[1]

                d=bx*cy-cx*by
            
                WA=((x*(by-cy)+y*(cx-bx)+bx*cy-cx*by)/d) 
                WB=((x*cy-y*cx)/d) 
                WC=((y*bx-x*by)/d) 
            

                if WA<1 and WA>0:
                    if WB<1 and WB>0:
                        if WC<1 and WC>0:
                            corners.append((Px,Py))

        def forQuar(Q,T):
            Newtria1=[Q[0],Q[1],Q[2]]
            Newtria2=[Q[0],Q[2],Q[3]]
            forTria(T,Newtria1)
            forTria(T,Newtria2)

        forTria(Q,T)
        forQuar(Q,T)
    
    
    def sırala(res):
        if len(res)>0:
            xlist=[]
            for i in range(len(res)):
                xlist.append(res[i][0])
            ylist=[]
            for i in range(len(res)):
                ylist.append(res[i][1])
    

            merkezx=sum(xlist)/len(res)
            merkezy=sum(ylist)/len(res)
    
            for i in range(len(res)):
                controllist.append((res[i][0]-merkezx,res[i][1]-merkezy))
        



            diction={}
            from math import atan2
            for i in range(len(controllist)):
    
    
                degree=atan2(controllist[i][0],controllist[i][1])
                diction[degree]=i
                arrangedeg=sorted(diction.keys())
            for i in range(len(arrangedeg)):
                indexsıracor.append(diction[arrangedeg[i]])
    
            for i in range(len(res)):
                sıralıcorners.append(corners[indexsıracor[i]])
        else:
            pass


    

    def alan(res):
        
        triangles=[]
        amountcorners=len(res)
        
        bunutoplarım=[]
        
  
        def alantria(A):
            
            xtoplam=0
            ytoplam=0
            
            listofx=[]
            listofy=[]
            for i in range(len(A)):
                listofx.append(A[i][0])
            for i in range(len(A)):
                listofy.append(A[i][1])
            
            listofx.append(listofx[0])
            listofy.append(listofy[0])
           
            
            for i in range(1,len(listofx)):
                xtoplam+=listofx[i-1]*listofy[i]
                
                
            
            for i in range(1,len(listofy)):
                ytoplam+=listofy[i-1]*listofx[i]
                
                

            bunutoplarım.append((abs(xtoplam-ytoplam))/2)

      

        
        if amountcorners<3:
            return 0
        elif amountcorners==3:
            triangles.append(res)

        elif amountcorners==4:
            triangles.append([res[0],res[1],res[2]])
            triangles.append([res[0],res[2],res[3]])

    
        elif amountcorners==5:
            
            triangles.append([res[0],res[1],res[2]])
            triangles.append([res[2],res[3],res[4]])
            triangles.append([res[0],res[2],res[4]])
            
            

        elif amountcorners==6:
           
            triangles.append([res[0],res[1],res[2]])
            triangles.append([res[2],res[3],res[4]])
            triangles.append([res[4],res[5],res[0]])
            triangles.append([res[0],res[2],res[4]])
        
            
        

        elif amountcorners==7:
            
            triangles.append([res[0],res[1],res[2]])
            triangles.append([res[2],res[3],res[4]])
            triangles.append([res[4],res[5],res[6]])
            triangles.append([res[0],res[2],res[6]])
            triangles.append([res[2],res[4],res[6]])

        
           

        elif amountcorners==8:
            
            triangles.append([res[0],res[1],res[2]])
            triangles.append([res[2],res[3],res[4]])
            triangles.append([res[4],res[5],res[6]])
            triangles.append([res[0],res[6],res[7]])
            triangles.append([res[0],res[2],res[4]])
            triangles.append([res[0],res[4],res[6]])


        
        
        
        for i in range(len(triangles)):
            alantria(triangles[i])
        return sum(bunutoplarım)


   


    kesişim(Q,T)
    
    isitin(Q,T)
    
    sırala(corners)

    
    return alan(sıralıcorners)



    
    


    
    
                    

    
