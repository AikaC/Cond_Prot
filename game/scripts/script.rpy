# O script do jogo fica nesse arquivo

label start:
    
    #Música tranquila
    
    show BG_Exterior_Cond at zoom
    
    "Em uma manhã tranquila no condomínio CondEduc..."

    #SFX alarme de incêndio
    #Música agitada
    #Hue red to white
    show BG_Portaria # Mostra um cenário
    show CH_Porteiro  # Mostra um personagem
    hide BG_Exterior_Cond
    with fade         # Efeito de transição
    
    # Adiciona linhas do diálogo com nome do personagem
    ChP"Mas o quê?!"

    show BG_Corredor
    with dissolve

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
    with fade

    ChP "Por favor, não corram, isso vai acabar machucando alguém!"
    
    show BG_Corredor
    with dissolve

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
 #Hue red to white
 show BG_Portaria
 show CH_Porteiro
 with fade

 ChP "Organizadamente, peço que andem até a portaria, sem correria, pois vão acabar tropeçando e quem ainda está lá dentro não vai conseguir sair."
 "Os moradores então obedeceram, e apesar do nervosismo, caminharam até a portaria." # Adiciona linhas do diálogo sem nome do personagem
 
 hide CH_Porteiro
 hide BG_Portaria
 with dissolve

 # Esse comando pula para outra label
 jump minijogo03

 # Esse comando termina o jogo
 return

label cena02:

 #Música tranquila
 show BG_Portaria

 "Logo em seguida, apareceu o morador do Bloco A/:"

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
 return
