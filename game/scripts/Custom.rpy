###### Declare as transições aqui ######

# Usado na primeira transição do jogo, dá zoom no BG_Exterior_Cond
transform zoom:
 block:
        xalign 0.5 yalign 0.5
        rotate 0 zoom 1
        linear 2.0 zoom 1.2

# Usado na primeira cena da visual novel, alarme de incendio
define flashbulb = Fade(0.4, 0.0, 0.8, color='#ff0000')

transform breath:
 block:
       xalign 0.5 yalign 0.5
       rotate 0 zoom 1
       linear 2.0 zoom 2
       linear 2.0 zoom 1
       pause 0.5
       repeat

###### Declare as notificações aqui ######

# Usado no primeiro minijogo - enunciado
screen noframe_quest01:
  hbox:
    spacing 6
    xalign 0.1 yalign 0.1

    text _("Respire fundo e clique na tela no momento certo.")