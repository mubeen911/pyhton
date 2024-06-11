word="you"
with open("check.txt",'r') as f:
    data=True
    line=1
    while data:
        data=f.readline()

        if word in data:
            print ("word found at line no ",line)
       
        line+=1
        
        
    

    
