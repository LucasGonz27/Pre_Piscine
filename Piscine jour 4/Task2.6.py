n = int(input("Entrer une valeur entiere "))
liste=[]
for i in range(2, n//2  +1):
    for nb in  reversed(range(n)):
               if nb % i == 0 and nb != 0:
                   liste.append(nb)
      
          
    print(liste)
  
         
              
