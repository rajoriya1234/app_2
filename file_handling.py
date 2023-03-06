import datetime
pun = "!#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
num = "123456789" 
with open('main.text',"r") as f:
    file = f.read()
    data = dict()
    for i in file:
        for j in i:
            if j not in data:
                data[j]=1
            elif j in pun:
                del data[j] 
            elif j in num:
                del data[j]   
            else:
                data[j]+=1           
    #print(data)
with open("new.text","a+") as f_1:
    tim = datetime.datetime.now()
    f_1.write(f"\n{tim}\n")
    
    sor = sorted(data.items())
    for i in sor:
        f_1.write(f"{i}")
             
                                                  
    
    
    
    
    

