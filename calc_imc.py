#Wylamys:lógica matematica
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc


#Arthur: Classificador de dados
def classficar(valor_imc):
    if valor_imc <25:
        return "NORMAL"
    else:
        return "ACIMA DO PESO"
    

#Mauricio: Especialista em Conteúdo
def gerar_aviso(status):
    if status == "NORMAL":
        return "Parabéns! Continue mantendo hábitos saudáveis."
    else:
        return "Atenção! Considere melhorar a alimentação e praticar atividades físicas."


#Samuel: Engenheiro de Integração
peso = float(input("Digite seu peso (kg):"))
altura = float(input("Digite sua altura (m):"))
imc = calcular_imc(peso,altura)
status = classficar(imc)
aviso = gerar_aviso(status)
print("\n=== RESULTADO DA AVALIAÇÃO ===")
print(f"IMC:{imc:.2f}")
print(f"Classificação:{status}")
print(f"Recomendação:{aviso}")