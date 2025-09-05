independece_stages = ["Inicio", "Organizacion", "Resistencia", "Consumación"]
print(independece_stages[0])
print(len(independece_stages))

#List Methods
leaders = []
leaders.append("Miguel Hidalgo")
leaders.append("Vicente Guerrero")
#leaders.extend(independece_stages) //mixed list together
leaders.insert(1, "Jose Maria Morelos")
#leaders.remove("Vicente Guerrero") //remove specific information
leaders.append("Agustin de Iturbide")
#leaders.pop(1) //delete an index
#leaders.clear()// remove everything form the list
print(leaders.index("Miguel Hidalgo"))   #encontrar la posision del elemento
print(leaders.count("Vicente Guerrero"))  #contar cuantas veces aparece
#leaders.sort()   #acomodar elementos en orden alfabetico o acendente
#leaders.reverse()  # cambiar el orde de atras para adelante
new_leaders = leaders.copy()

print(leaders)
print(new_leaders)
