###### Os minijogos da visual novel vão nesse arquivo ######

### Minijogo 01 - Respirando com calma ###

label minijogo01 :

 # Musica agitada

 show BG_Portaria
 #show screen noframe_quest01
 with fade
 "Respire fundo e clique na tela no momento certo."

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

 menu:
  "megafone":
   "Muito bem, o megafone é um instrumento de ampliação de voz que não está conectado à rede elétrica."
   "Por isso, não haverá riscos de ser utilizado em caso de incêndio."
   jump minijogo03
   return

  "microfone":
   "Tem certeza que essa é a melhor opção?"
   jump minijogo02
   return

  "fone de ouvido":
   "Tem certeza que essa é a melhor opção?"
   jump minijogo02
   return

### Minijogo 03 - Ajude os mais vulneráveis ###

label minijogo03:

 "Assim que todos se acalmaram e a maioria foi para o local indicado, Carlos percebeu que ainda haviam algumas pessoas para trás."
 "Após garantir a segurança da portaria, Carlos foi ajudar aqueles que precisavam."

 jump pergunta01
 return

label pergunta01:
 "Quem salvar primeiro?"

 menu:
  "Uma idosa":
   "Isso mesmo, precisamos ajudar primeiro aqueles com mais dificuldade de agilidade"
   jump pergunta02
   return

  "Uma jovem mulher":
   "Talvez seja melhor dar prioridade aos mais velhos e pessoas com dificuldade de locomoção, não?"
   jump pergunta01
   return

label pergunta02:

 "Quem salvar primeiro?"

 menu:
  "Um homem de terno":
   "Não se deixe levar pelas aparências, ajude aqueles com dificuldade de locomoção."
   jump pergunta01
   return

  "Um homem com a perna quebrada":
   "Em cheio! Precisamos ajudar primeiro aqueles com mais dificuldade de locomoção"
   jump pergunta03
   return

label pergunta03:

 "Quem salvar primeiro?"

 menu:
  "Uma mulher cheia de malas":
   "Talvez seja melhor orientar a mulher a deixar as malas por enquanto e dar mais atenção para a criança que possui menos autonomia."
   jump pergunta01
   return

  "Uma criança":
   "Muito bem! Você já está a meio passo de se tornar um porteiro de alta eficiência. Continue assim."
   jump cena02
   return
