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

