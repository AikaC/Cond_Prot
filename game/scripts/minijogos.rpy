###### Os minijogos da visual novel vão nesse arquivo ######

### Minijogo 01 - Respirando com calma ###

label minijogo01 :

 # Musica agitada

 show BG_Portaria
 #show screen noframe_quest01
 with fade
 
"Antes de acalmar o próximo, precisamos primeiro nos acalmar."
 "Lembre-se: em qualquer situação de emergência, o resultado será melhor se agirmos com paciência."
 "Um botão irá aparecer no momento certo, respire fundo e clique nele."
 "Mas seja preciso e eficiente, se demorar demais ele pode acabar sumindo."
 "Ah! Não se desespere, se perder a oportunidade, o botão vai aparecer de novo."
 "É só esperar."
 "Preparado?"

 hide CH_Porteiro
 jump minijogo01_espera

label minijogo01_espera:

 #Musica calma
 pause 1.0
 
 jump minijogo01_aperta

 return

label minijogo01_aperta:

 menu:
  "Agora!":
   #hide screen noframe_quest01
   jump minijogo02
 pause 0.5
 jump minijogo01_espera

 return

### Minijogo 02 - Comunique-se ###

label minijogo02:

 "Precisamos chamar a atenção das pessoas. Clique em uma das três opções e escolha a ferramenta mais eficiente para isso."

 call screen Minijogo02
 return

 label megafone_resposta:
   "Muito bem, o megafone é um instrumento de ampliação de voz que não está conectado à rede elétrica."
   "Por isso, não haverá riscos de ser utilizado em caso de incêndio."
   jump minijogo03
   return

 label microfone_resposta:
   "Tem certeza que essa é a melhor opção?"
   "O microfone é um instrumento ligado à rede elétrica,"
   "usá-lo em um momento de incêncio pode trazer riscos para a sua segurança."
   "Tente novamente, na próxima vai!"
   jump minijogo02
   return

 label fone_resposta:
   "Tem certeza que essa é a melhor opção?"
   "O fone de ouvido não é um instrumento de comunicação direta com o público à sua volta."
   "Tente novamente, eu sei que você consegue."
   jump minijogo02
   return

### Minijogo 03 - Ajude os mais vulneráveis ###

label minijogo03:

 "Assim que todos se acalmaram e a maioria foi para o local indicado, Carlos percebeu que ainda haviam algumas pessoas para trás."
 "Após garantir a segurança da portaria, Carlos foi ajudar aqueles que precisavam."

 jump pergunta01
 return

label pergunta01:
 "Seguindo pelas escadas, conseguimos perceber várias pessoas que ficaram para trás." 
 "Quem salvar primeiro?"
 "Clique na imagem da pessoa que você acha ser a opção correta."

 call screen Minijogo03_pergunta01
 return

label idosa_resposta:
   "Isso mesmo, precisamos ajudar primeiro aqueles com mais dificuldade de agilidade"
   jump pergunta02
   return

label mulher_resposta:
   "Talvez seja melhor dar prioridade aos mais velhos e pessoas com dificuldade de locomoção, não?"
   jump pergunta01
   return

label pergunta02:

 "Quem salvar primeiro?"

 call screen Minijogo03_pergunta02
 return

label terno_resposta:
   "Não se deixe levar pelas aparências, ajude aqueles com dificuldade de locomoção."
   jump pergunta01
   return

label PernaQuebrada_resposta:
   "Em cheio! Precisamos ajudar primeiro aqueles com mais dificuldade de locomoção"
   jump pergunta03
   return

label pergunta03:

 "Quem salvar primeiro?"

 call screen Minijogo03_pergunta03
 return

label malas_resposta:
   "Talvez seja melhor orientar a mulher a deixar as malas por enquanto e dar mais atenção para a criança que possui menos autonomia."
   jump pergunta01
   return

label crianca_resposta:
   "Muito bem! Você já está a meio passo de se tornar um porteiro de alta eficiência. Continue assim."
   jump cena02
   return
