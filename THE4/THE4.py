def finddescent(T,kat,dic):
    
    dic[T[0]]=kat
    
    kat+=1
   
    for j in range(1,len(T)):
        if type(T[j])!=list:
            dic[T[j]]=kat
        elif type(T[j])==list:
            findlowerdescent(T[j],kat,dic)
    

def findlowerdescent(T,kat,dic):
    dic[T[0]]=kat
    kat+=1
    
    for j in range(1,len(T)):
        if type(T[j])!=list:
            dic[T[j]]=kat
        elif type(T[j])==list:
            
            finddescent(T[j],kat,dic)
    
    




def findparents(T,allparents):
    
    for i in range(1,len(T)):
        if type(T[i])!=list:
            allparents[T[i]]=T[0]
        elif type(T[i])==list:
            allparents[T[i][0]]=T[0]
            findparents(T[i],allparents)
    
    



def findgender(T,males,females):

    for i in range(len(T)):
        if type(T[i])!=list:
            letter=ord(T[i][0])
            
            if letter in range(65,91):
                females.append(T[i])
                
            elif letter in range(97,123):
                males.append(T[i])
                
        elif type(T[i])==list:
            findgender(T[i],males,females)



def makenamelist(T,namelist):
    for i in range(len(T)):
        if type(T[i])!=list:
            namelist.append(T[i])
        elif type(T[i])==list:
            makenamelist(T[i],namelist)



def brothers(T,pname):
    allparents={}
    namelist=[]
    siblings=[]
    brother=[]
    sister=[]
    findparents(T,allparents)
    makenamelist(T,namelist)
    if pname==T[0]:
        return []
    else:
        for i in range(1,len(namelist)):
            parent=allparents[pname]
        
            if allparents[namelist[i]]==parent and namelist[i]!=pname:
                siblings.append(namelist[i])

    findgender(siblings,brother,sister)
    return brother



def sisters(T,pname):
    allparents_forsister={}
    namelist_forsister=[]
    siblings_forsister=[]
    brother_forsis=[]
    sister_forsis=[]
    findparents(T,allparents_forsister)
    makenamelist(T,namelist_forsister)
    if pname==T[0]:
        return []
    else:
        for i in range(1,len(namelist_forsister)):
            parent_sister=allparents_forsister[pname]
            if allparents_forsister[namelist_forsister[i]]==parent_sister and namelist_forsister[i]!=pname:
                siblings_forsister.append(namelist_forsister[i])

    findgender(siblings_forsister,brother_forsis,sister_forsis)
    return sister_forsis

def siblings(T,pname):
    allparents_forsibling={}
    namelist_forsibling=[]
    siblings_forall=[]
    findparents(T,allparents_forsibling)
    makenamelist(T,namelist_forsibling)
    if pname==T[0]:
        return []
    else:
        for i in range(1,len(namelist_forsibling)):
            parent_siblings=allparents_forsibling[pname]
            if allparents_forsibling[namelist_forsibling[i]]==parent_siblings and namelist_forsibling[i]!=pname:
                siblings_forall.append(namelist_forsibling[i])
    return siblings_forall

def uncles(T,pname):
    soylist_foruncle={}
    namelist_foruncle=[]
    parentlist_foruncle={}
    parentsiblings_uncle=[]
    uncles=[]
    aunts=[]
    finddescent(T,0,soylist_foruncle)
    makenamelist(T,namelist_foruncle)
    findparents(T,parentlist_foruncle)
    whichfloor=soylist_foruncle[pname]-1
    if soylist_foruncle[pname]<2:
        return []
    else:
        for i in range(1,len(namelist_foruncle)):
            if soylist_foruncle[namelist_foruncle[i]]==whichfloor:
                parent_pname=parentlist_foruncle[pname]
                if parentlist_foruncle[namelist_foruncle[i]]==parentlist_foruncle[parent_pname]:
                
                    if namelist_foruncle[i]!=parent_pname:
                        parentsiblings_uncle.append(namelist_foruncle[i])
    findgender(parentsiblings_uncle,uncles,aunts)
    return uncles

def aunts(T,pname):
    soylist_foraunt={}
    namelist_foraunt=[]
    parentlist_foraunt={}
    parentsiblings_aunt=[]
    uncles_foraunt=[]
    aunts_foraunt=[]
    finddescent(T,0,soylist_foraunt)
    makenamelist(T,namelist_foraunt)
    findparents(T,parentlist_foraunt)
    whichfloor=soylist_foraunt[pname]-1
    if soylist_foraunt[pname]<2:
        return []
    else:
        for i in range(1,len(namelist_foraunt)):
            if soylist_foraunt[namelist_foraunt[i]]==whichfloor:
                parent_pname=parentlist_foraunt[pname]
                if parentlist_foraunt[namelist_foraunt[i]]==parentlist_foraunt[parent_pname]:
                
                    if namelist_foraunt[i]!=parent_pname:
                        parentsiblings_aunt.append(namelist_foraunt[i])
    findgender(parentsiblings_aunt,uncles_foraunt,aunts_foraunt)
    return aunts_foraunt



def cousins(T,pname):
    soylist_forcou={}
    namelist_forcou=[]
    parentlist_forcou={}
    cousinlist=[]
    
    finddescent(T,0,soylist_forcou)
    makenamelist(T,namelist_forcou)
    findparents(T,parentlist_forcou)
    floor_pname=soylist_forcou[pname]

    if pname==T[0]:
        return []
    elif floor_pname<2:
        return []
    else:
        for i in range(1,len(namelist_forcou)):
            nameofperson=namelist_forcou[i]
            controlfloor=soylist_forcou[nameofperson]
            if controlfloor==floor_pname:
                parentofname=parentlist_forcou[pname]
                grandpar_pname=parentlist_forcou[parentofname]
                parentofsomebody=parentlist_forcou[nameofperson]
                grandpar_somebody=parentlist_forcou[parentofsomebody]
                if grandpar_pname==grandpar_somebody:
                    if parentofname!=parentofsomebody:
                        cousinlist.append(nameofperson)
           
    return cousinlist










 
    
