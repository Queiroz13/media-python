#autor: Arthur
print ("=============================")
print ("=========Média Aluno=========")
print ("E.E LUCIANE DO ESPIRITO SANTO")
print ("=============================")
nome=input ("digite o nome do aluno:")
def calcular_media(notas):
  return sum(notas) / len(notas) if notas else 0  # Calcula a média

def verificar_aprovacao(media):
  if media >= 7.0:
      return "Aprovado"
  else:
      return "Reprovado"

def main():
  notas = []  # Lista para armazenar as notas
  numero_de_notas = int(input("Quantas notas você deseja inserir? "))  # Pergunta ao usuário quantas notas ele quer inserir

  for i in range(numero_de_notas):
      nota = float(input(f"Digite a nota {i + 1}: "))  # Solicita a nota
      notas.append(nota)  # Adiciona a nota à lista

  media = calcular_media(notas)  # Calcula a média das notas
  status = verificar_aprovacao(media)  # Verifica se o aluno foi aprovado ou reprovado

  print(f"A média das notas é: {media:.2f}")  # Exibe a média formatada com duas casas decimais
  print(f"O aluno está: {status}")  # Exibe o status de aprovação

# Executa o programa
if __name__ == "__main__":
  main()