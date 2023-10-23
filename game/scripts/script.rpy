# O script do jogo fica nesse arquivo

label start:

    #Música tranquila
    
    #cutscene condomínio zoom out.
    #SFX alarme de incêndio
    #Música agitada
    #Hue red to white
    scene BG_Portaria # Mostra um cenário
    show CH_Porteiro  # Mostra um personagem
    with fadein       # Efeito de transição
    pause             # Pausa o jogo até input do mouse

    hide CH_Porteiro
    scene BG_Corredor
    pause 0.1

    #SFX Passos
    show CH_Multidao
    with movetoright
    pause 0.1

    #SFX_Passos
    hide CH_Multidao
    with movetoright
    pause 0.1

    scene BG_Portaria
    show CH_Porteiro
    with fadein

    # Adiciona linhas do diálogo com nome do personagem
    Ch_Carlos "Por favor, não corram, isso vai acabar machucando alguém!"

    scene BG_Corredor
    Sprite pessoas desgovernadas
    pause 0.1

    #SFX Passos
    show CH_Multidao
    with movetoright
    pause 0.1

    #SFX_Passos
    hide CH_Multidao
    with movetoright
    pause 0.1
    #Hue red to white

    # Esse comando pula para outra label
    jump cena01

    # Esse comando termina o jogo
    return

label cena01:

    #Música épica
    #Hue red to white
    scene BG_Portaria
    show CH_Porteiro
    with fadein
	
	Ch_Carlos "Organizadamente, peço que andem até a portaria, sem correria, pois vão acabar tropeçando e quem ainda está lá dentro não vai conseguir sair."
	"Os moradores então obedeceram, e apesar do nervosismo, caminharam até a portaria." # Adiciona linhas do diálogo sem nome do personagem

    hide CH_Porteiro with dissolve

    # Esse comando pula para outra label
    jump cena02

    # Esse comando termina o jogo
    return

label cena02:

    #Música tranquila
    scene BG_Portaria

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

    return