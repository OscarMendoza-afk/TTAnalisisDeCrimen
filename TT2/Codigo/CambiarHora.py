import pandas as pd
import math


df = pd.read_csv(r"/home/ozkr/Documentos/UpdateCrimenesENE.csv")

df.drop(df[df['Hora'] == 'NA'].index, inplace = True) 

df = df[df['Hora'].notna()]

#df = df.head(n=30)

print (df.Hora)

def SetHora(x):
   
    if x == 'False' : 
        
        hora = '00:00'
        
        return hora
    
    elif x == 0 : 
        
        hora = '00:00'
        
        return hora
    
    else : 
        
        x = (x/60)/60
        
        xd, xe = math.modf(x)
        
        xe = int(xe)
        
        min = (xd * 60)
        
        min = int(min)
        
        if xe < 10 :
            
            hora = '0' + str(xe) + ':' + str(min) + ':00'
            
            if min < 10 :
               
                hora = '0' + str(xe) + ':0' + str(min) + ':00'
                
            else :
                
                hora = '0' +str(xe) + ':' + str(min) + ':00'
            
        else :
            
            if min < 10 :
               
                hora = str(xe) + ':0' + str(min) + ':00'
                
            else :
                
                hora = str(xe) + ':' + str(min) + ':00'
        
        return hora
        

df['Hora'] = df['Hora'].apply(SetHora)



print (df.Hora)



print(df['Hora'].info)

df.to_csv("/home/ozkr/Documentos/UpdateCrimenesENE.csv", index=False)


