def lenLeven(fir,sec ):
    """Algorytm obliczania odległości zainspirowany artykułem
    https://pl.wikipedia.org/wiki/Odleg%C5%82o%C5%9B%C4%87_Levenshteina
    """
    if fir == sec:
        return 0
    elif len(fir) == 0:
        return len(sec)
    elif len(sec) == 0:
        return len(fir)
    row1 = [None] * (len(sec) + 1)
    row2 = [None] * (len(sec) + 1)
    for i in range(len(row1)):
        row1[i] = i
    for i in range(len(fir)):
        row2[0] = i + 1
        for j in range(len(sec)):
            c = 0 if fir[i] == sec[j] else 1
            row2[j + 1] = min(row2[j] + 1, row1[j + 1] + 1, row1[j] + c)
        for j in range(len(row1)):
            row1[j] = row2[j]
                
    return row2[len(sec)]
    
    
    
def main():
    file = open("slowa.txt","r")
    inpList=[]
    word = input()
    k = input()
    n=int(k)
    inpList=file.readlines()
    smallest = (int)(lenLeven(word,inpList[0][:3]))
    listK=[]
    listV=[]
    result=[]
    cond=False
    for i in range(len(inpList)):
                   tmpK=inpList[i][:len(inpList[i])-1]
                   tmpV=(int)(lenLeven(word,tmpK))
                   if tmpV==1:
                       result.append(tmpK)
                       if len(result)==n:
                           cond=True
                           break
                   elif tmpV <= smallest:
                       listV.append(tmpV)
                       listK.append(tmpK)
                       smallest=tmpV
    if cond:
        print (result)
    else:
        if(listK[len(listK)-1]!=word):
            result.append(listK[len(listK)-1])
            
        
                    
        for i in range(len(listK)-2,len(listK)-n-2,-1):
                    if len(result)<n:
                       result.append(listK[i])
        print(result)   
    
    

    
main()
