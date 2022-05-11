mat=int(input("Ingrese el numero de materias que cursa: "))
materias =[]
notas=[]

for i in range(mat):
    materias.append(input(f"Cual es su {i+1} materia "))

for text in materias:
    notas.append(float(input(f"Cual es su nota en {text} ")))


print("\nTus notas son\n")
for x in range(0,len(notas)):
    if (notas[x])<3.0:
       print(f"Usted debe repetir {materias[x]} ya que su nota fue: {notas[x]}")
      #  notas.pop(x)
      #  materias.pop(x)