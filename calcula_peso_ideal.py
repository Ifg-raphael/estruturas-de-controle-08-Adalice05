# Sua solução aqui

h = float(input("Forneça a altura: "))
sexo = input("Forneça o sexo (M ou F): ")
 
if sexo == "M":
    peso_ideal = (72.7 * h) - 58
else:
    peso_ideal = (62.1 * h) - 44.7
    
print(f"{peso_ideal:.2f}")