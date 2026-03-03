#declarar

Qt_Litros : float = 0
Tmp_Percurso : int = 0
Velocidade_Média : float = 0
Distância : int = 0

#Inicio

Tmp_Percurso = int (input("Digite o tempo de percurso em HORAS: "))
Velocidade_Média = float (input("Digite a Velocidade Média (km/l): "))
Distância = Tmp_Percurso * Velocidade_Média
Qt_Litros = Distância / 12
print("A quatidade de litros gasta é: ",Qt_Litros)

#Fim