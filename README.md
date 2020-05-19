# Modelando a  solução

  Informações que preciso saber:
  
    - Moeda origem
    - Moeda destino
    - Taxa de conversão
    
  Meu usuário vai escolher moedas ou vai ser fixo no programa?
  
    - Usuário vai escolher
    - Ele vai selecionar um valor correspondente a moeda de acordo com o que o programa descrever
  
  Quais opçõos de moeda para conversão serão possíveis?
  
    - Złoty e Real (comum no nosso cotidiano)
    - Dólar e Euro (moedas mais conhecidas)
  
  Resultado:
  
    - Valor da conversão
   
  

# Algorítmo

Perguntar ao usuário qual a moeda de origem (1-Złoty, 2-Dólar, 3-Euro, 4-Real)

Usuário digita valor correspondente à moeda de origem

Se valor for diferente dos descritos, emitir mensagem de erro e solicitar que o usuário digite novamente até o valor estar de acordo

Perguntar ao usuário qual a moeda de destino (1-Złoty, 2-Dólar, 3-Euro, 4-Real)

Usuário digita valor correspondente à moeda de destino

Se valor for diferente dos descritos, emitir mensagem de erro e solicitar que o usuário digite novamente até o valor estar de acordo

Perguntar ao usuário qual valor a ser convertido

Usuário digita valor a converter

Se a moeda origem for Złoty, verificar qual a moeda destino e efetuar a multiplicação do valor a ser convertido pela taxa de conversão devida

Se não for Złoty, verificar se é Dólar. Se a moeda origem for Dólar, verificar qual a moeda destino e efetuar a multiplicação do valor a ser convertido pela taxa de conversão devida

Se não for Dólar, verificar se é Euro. Se a moeda origem for Euro, verificar qual a moeda destino e efetuar a multiplicação do valor a ser convertido pela taxa de conversão devida

Se não for Euro, verificar se é Real. Se a moeda origem for Real, verificar qual a moeda destino e efetuar a multiplicação do valor a ser convertido pela taxa de conversão devida

Retornar para o usuário o valor da conversão, informando também qual a moeda origem e a destino
