#Wylamys:lógica matematica
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


#Arthur:Classificador de dados
def classificar(valor_imc):
    if valor_imc < 25:
        return "NORMAL"
    else:
        return "ACIMA DO PESO"
    

#Mauricio:Especialista em Conteúdo
def gerar_aviso(status):
    if status == "NORMAL":
        return "Parabéns! Continue mantendo hábitos saudáveis."
    else:
        return "Atenção! Considere melhorar a alimentação e praticar atividades físicas."


#Samuel:Engenheiro de Integração
altura = (input("Digite sua Altura(m)"))
peso = float(input("Digite seu Peso(kg)"))

imc = calcular_imc(peso, altura)
classificacao = classficar(imc)
status = gerar_aviso(classificacao)

print(f"\nResultado da Avaliação: {imc:.2f}")
print(f"Classificar dados: {classificacao}")
print(f"Recomendação: {status}")