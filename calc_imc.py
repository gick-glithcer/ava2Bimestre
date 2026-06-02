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
    

#

