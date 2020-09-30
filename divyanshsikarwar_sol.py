def hackerlandRadioTransmitters(a, n):
    a.sort()
    c=0
    j=0
    i=0
    l=0
    print(a)
    while(i<len(a)):
        j=i+1
        ctr=0
        while(ctr==0):
            
            if(j>=len(a)):
                ctr+=1
            elif(a[j]-a[i]<=n):
                print("j",a[i],a[j])
                j+=1
            elif(a[j]-a[i]>=n):
                ctr+=1
          
        k=j
        j-=1
        ctr=0
        
        
                    
        while(ctr==0):
            if(k>=len(a)):
                ctr+=1
            elif(a[k]-a[j]<=n):
                print("k",a[j],a[k])
                k+=1
            elif(a[k]-a[j]>n):
                ctr+=1
            
        c+=1
        i=k

        
    return (c)
