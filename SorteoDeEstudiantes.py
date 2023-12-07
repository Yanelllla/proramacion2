#SORTEO DE ESTUDIANTES
import random
orden=['sofi', 'giane', 'sabri', 'cele']
orden2=[]
for i in range(len(orden)):
       x=random.randint(0,len(orden)-1)
       orden2.append(orden[x])
       del (orden[x])
print("orden1: ",orden)
print("orden2: ",orden2)
