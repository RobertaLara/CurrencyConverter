# Conversor de moedas
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

print("\n\n\tCONVERSOR DE MOEDAS\n\n")   # \n dá espaço de uma linha e \t dá um tab

print("Selecione a moeda origem:\n")    # Instrução para o usuário digitar a moeda de origem

inputOrigem = input("   Para Złoty, digite 1\n"     # input permiti usuário entrar com valor
          "   Para Dólar, digite 2\n"               # Usuário pode digitar 1, 2, 3 ou 4, de acordo com a descrição
          "   Para Euro, digite 3\n"                # Optei por colocar os 4 tipos de moedas mais comuns
          "   Para Real, digite 4\n")

while (inputOrigem != '1') and (inputOrigem != '2') and (inputOrigem != '3') and (inputOrigem != '4'):
    inputOrigem = input("   NÚMERO INVÁLIDO! DIGITE NOVAMENTE!\n")  # Caso usuário digite um número diferente da descrição

print("\nSelecione a moeda destino:\n")    # Instrução para o usuário digitar a moeda de destino

inputDestino = input("   Para Złoty, digite 1\n"     # input permiti usuário entrar com valor
          "   Para Dólar, digite 2\n"                # Usuário pode digitar 1, 2, 3 ou 4, de acordo com a descrição
          "   Para Euro, digite 3\n"                # Optei por colocar os 4 tipos de moedas mais comuns
          "   Para Real, digite 4\n")

while (inputDestino != '1') and (inputDestino != '2') and (inputDestino != '3') and (inputDestino != '4'):
    inputDestino = input("   NÚMERO INVÁLIDO! DIGITE NOVAMENTE!\n")  # Caso usuário digite um número diferente da descrição

valorConverter = input("\nDigite o valor a ser convertido: ")    # Instrução para o usuário digitar o valor a ser convertido

if (inputOrigem == '1'):        # Se a moeda origem for Złoty, ele verifica qual a moeda destino para fazer a conversão
    moedaOrigem = 'Złoty'       # Verificar tipo da moeda origem e dar uma resposta completa para o usuário
    if (inputDestino == '2'):
        valorConvertido = float(valorConverter) * 0.24      # Cálculo de conversao do Złoty para Dólar 
    elif (inputDestino == '3'):                                   # Obs.: float para converter string digitada em número decimal
        valorConvertido = float(valorConverter) * 0.22      # Cálculo de conversao do Złoty para Euro
    elif (inputDestino == '4'):
        valorConvertido = float(valorConverter) * 1.38      # Cálculo de conversao do Złoty para Real

if (inputOrigem == '2'):        # Se a moeda origem for Dólar, ele verifica qual a moeda destino para fazer a conversão
    moedaOrigem = 'Dólar'       # Verificar tipo da moeda origem e dar uma resposta completa para o usuário
    if (inputDestino == '1'):
        valorConvertido = float(valorConverter) * 4.16      # Cálculo de conversao do Dólar para Złoty
    elif (inputDestino == '3'):
        valorConvertido = float(valorConverter) * 0.92      # Cálculo de conversao do Dólar para Euro
    elif (inputDestino == '4'):
        valorConvertido = float(valorConverter) * 5.74      # Cálculo de conversao do Dólar para Real

if (inputOrigem == '3'):        # Se a moeda origem for Euro, ele verifica qual a moeda destino para fazer a conversão
    moedaOrigem = 'Euro'       # Verificar tipo da moeda origem e dar uma resposta completa para o usuário
    if (inputDestino == '1'):
        valorConvertido = float(valorConverter) * 4.55      # Cálculo de conversao do Euro para Złoty
    elif (inputDestino == '2'):
        valorConvertido = float(valorConverter) * 1.09      # Cálculo de conversao do Euro para Dólar
    elif (inputDestino == '4'):
        valorConvertido = float(valorConverter) * 6,27      # Cálculo de conversao do Euro para Real

if (inputOrigem == '4'):        # Se a moeda origem for Real, ele verifica qual a moeda destino para fazer a conversão
    moedaOrigem = 'Real'       # Verificar tipo da moeda origem e dar uma resposta completa para o usuário
    if (inputDestino == '1'):
        valorConvertido = float(valorConverter) * 0.72      # Cálculo de conversao do Real para Złoty
    elif (inputDestino == '2'):
        valorConvertido = float(valorConverter) * 0.17      # Cálculo de conversao do Real para Dólar
    elif (inputDestino == '3'):
        valorConvertido = float(valorConverter) * 0.16      # Cálculo de conversao do Real para Euro

if (inputDestino == '1'):       # Verificar tipo da moeda destino e dar uma resposta completa para o usuário
    moedaDestino = 'Złoty'
elif (inputDestino == '2'):
    moedaDestino = 'Dólar'
elif (inputDestino == '3'):
    moedaDestino = 'Euro'
elif (inputDestino == '4'):
    moedaDestino = 'Real'

print("\n\n\tValor convertido de",moedaOrigem,"para",moedaDestino,":",round(valorConvertido,2),"\n\n\n")
# Retorna ao usuário o nome da moeda origem e da destino, gerando uma resposta mais completa
# round é para arredondar o resultado, pois dinheiro físico possui somente duas casas decimais