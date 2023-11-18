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

###### Declare os botões em imagens aqui ######

# Usado no segundo minijogo - atribui imagem ao botão
screen Minijogo02:
    hbox xsize 1920:
        imagebutton auto "Sprites/Sprite_Megafone_%s.jpg" action Jump("megafone_resposta") xalign 0.3
        imagebutton auto "Sprites/Sprite_microphone_%s.jpg" action Jump("microfone_resposta") xalign 0.5
        imagebutton auto "Sprites/Sprite_phone_%s.jpg" action Jump("fone_resposta") xalign 0.8

# Usado no terceiro minijogo - atribui imagem ao botão
screen Minijogo03_pergunta01:
    hbox xsize 1920:
        imagebutton auto "Personagens/CH_senhora_%s.jpg" action Jump("idosa_resposta") xalign 0.3
        imagebutton auto "Personagens/CH_mulher_jovem_%s.png" action Jump("mulher_resposta") xalign 0.8

screen Minijogo03_pergunta02:
    hbox xsize 1920:
        imagebutton auto "Personagens/CH_homem_terno_%s.jpg" action Jump("terno_resposta") xalign 0.3
        imagebutton auto "Personagens/CH_perna_quebrada_%s.png" action Jump("PernaQuebrada_resposta") xalign 0.8

screen Minijogo03_pergunta03:
    hbox xsize 1920:
        imagebutton auto "Personagens/CH_mulher_malas_%s.jpg" action Jump("malas_resposta") xalign 0.3
        imagebutton auto "Personagens/Ch_crianca_%s.jpg" action Jump("crianca_resposta") xalign 0.8
