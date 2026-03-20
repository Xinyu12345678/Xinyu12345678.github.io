country=["UK","China","Italy","Brazil","USA"]
pop2024=[69.2,1410,58.9,212.0,340.1]
pop2020=[66.7,1426,59.4,208.6,331.6]
population_changes={}
for i in range (len(pop2020)):
    percent=(pop2024[i]-pop2020[i])*100/pop2020[i]
    population_changes[country[i]]=percent
    print(country[i],":",percent)
print(population_changes)
import matplotlib.pyplot as plt
import numpy as np
ind=np.arange(5)
plt.bar(ind,population_changes.values(),width=0.5)
plt.show()