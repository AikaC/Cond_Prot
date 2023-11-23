#Sistema de pontos
init python:
 pontos = 0

# O script do jogo fica nesse arquivo

label start:
    
    #Música tranquila
    show CH_Porteiro  # Mostra um personagem
    with dissolve     # Efeito de transição
    ChP "Olá, sejam bem-vindos ao nosso exercício prático em formato de história interativa."
    ChP "Aqui veremos exemplos reais de coisas que podem acontecer na vida profissional de um porteiro."
    ChP "Seu papel será tomar as decisões certas de acordo com cada situação apresentada,"
    ChP "desse modo, poderemos entender como o porteiro influencia no funcionamento de um condomínio."
    ChP "Esse primeiro jogo fala sobre as normas e recomendações de como agir em caso de incêndio."
    ChP "Está preparado?"

    menu:
     "Sim":
      show screen noframe_pontos
      ChP "Que da hora!{p}Consegue ver essa barra de pontos ali em cima da tela?"
      ChP "Cada resposta certa faz a barra aumentar."
      ChP "Você só vai ganhar o jogo quando conseguir a pontuação máxima."
      ChP "Mas sem pressão.{p}Eu vou estar aqui o tempo todo para te ajudar."
      ChP "Hora de pôr mãos a obras."
      hide screen noframe_pontos
      jump cena_00
      return

     "Não":
      ChP "Não se preocupe, reveja o material se precisar."
      ChP "Respire fundo e vamos um passo de cada vez."
      ChP "Lembre-se, você sempre poderá recomeçar quando quiser."
      ChP "Vamos em frente?"
      menu:
       "Sim!":
        jump cena_00
        return

label cena_00:
    
    hide CH_Porteiro
    show BG_Exterior_Cond at zoom
    
    "Em uma manhã tranquila no condomínio CondEduc..."

    #SFX alarme de incêndio
    #Música agitada
    show BG_Portaria # Mostra um cenário
    show CH_Porteiro
    with flashbulb

    hide BG_Exterior_Cond
    
    # Adiciona linhas do diálogo com nome do personagem
    ChP"Mas o quê?!"

    show BG_Corredor
    with flashbulb

    #SFX Passos
    show CH_Multidao
    hide CH_Porteiro
    hide BG_Portaria
    with moveinright
    pause 0.5

    #SFX_Passos
    hide CH_Multidao
    with moveinright

    show BG_Portaria
    show CH_Porteiro
    hide BG_Corredor
    with flashbulb

    ChP "Por favor, não corram, isso vai acabar machucando alguém!"
    
    show BG_Corredor
    with flashbulb

    #SFX Passos
    show CH_Multidao
    hide CH_Porteiro
    hide BG_Portaria
    with moveinright
    pause 0.5

    #SFX_Passos
    hide CH_Multidao
    with moveinright
    #Hue red to white

    # Esse comando pula para outra label
    jump minijogo01

    # Esse comando termina o jogo
    return

label cena01:

 #Música épica
 show BG_Portaria
 show CH_Porteiro
 with flashbulb

 ChP "Organizadamente, peço que andem até a portaria, sem correria, pois vão acabar tropeçando e quem ainda está lá dentro não vai conseguir sair."
 "Os moradores então obedeceram, e apesar do nervosismo, caminharam até a portaria." # Adiciona linhas do diálogo sem nome do personagem
 
 hide CH_Porteiro
 hide BG_Portaria
 with flashbulb

 # Esse comando pula para outra label
 jump minijogo03

 # Esse comando termina o jogo
 return

label cena02:

 #Música tranquila
 show BG_Portaria
 hide screen noframe_pontos

 "Logo em seguida, apareceu o morador do Bloco A\:"

 show CH_Morador
 with dissolve

 Ch_M1 "Pessoal, quero pedir desculpas, mas não há incêndio nenhum…"
 Ch_M1 "Na verdade, fui eu quem esqueci o forno ligado e a fumaça subiu para o sinalizador."
 Ch_M1 "Sinto muito pelo transtorno."

 hide CH_Morador
 with dissolve

 "Mesmo que se tratasse apenas de um mal entendido,"
 "ainda sim fizemos certo em agir nesta situação,"
 "pois um acidente de verdade poderia ter ocorrido aqui."

 hide BG_Portaria
 jump cena_final
 return

label cena_final:

 "E aí? O que achou dessa aventura?"
 "Essa é uma forma que a CondEduc pensou para ajudar você, futuro porteiro de qualidade,"
 "A se divertir enquanto aprende."
 "Viu só quanta coisa aprendemos nos divertindo?"
 "Agora que você já está fera na parte de prevenção de combate e incêndio,"
 "vamos seguir em frente com os próximos assuntos."
 "Te vejo em breve."
