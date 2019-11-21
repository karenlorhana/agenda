index = input("digite o que deseja fazer: "+
           "\n"+"1 - adicionar um contato na agenda"+
           "\n"+"2 - buscar o nome do contato na agenda"+
           "\n"+"3 - excluir um contato da agenda"+
           "\n"+"4 - editar um contato"+
           "\n"+"5 - para sair"+
           "\n")
agenda = {}
while index != "5":



  if index == "1":
      qtdNomes = int(input("digite quantos contatos que você deseja adicionar a agenda: "))
      print()

#adicionar contato
      for i in range(qtdNomes):
          print()
          nome = input("digite o nome do contato: ").upper()
          qtd = int(input("digite quantos números você deseja adicionar a " + nome+": "))
          contatos = []
          for x in range(qtd):
              numero = input("digite o número de telefone de " + nome +": ")
              contatos.append(numero)
          agenda[nome] = contatos
      print()
      print(agenda)
      print()
      print()
  index = input("digite o que deseja fazer: "+
           "\n"+"1 - adicionar um contato na agenda"+
           "\n"+"2 - buscar o nome do contato na agenda"+
           "\n"+"3 - excluir um contato da agenda"+
           "\n"+"4 - editar um contato"+
           "\n"+"5 - para sair"+
           "\n")
  print()

  if index == "2":
#buscar contato
      buscar = input("digite o nome do contato que deseja buscar na agenda: ").upper()
      if buscar in agenda:
          print()
          print("o número é: ",agenda[buscar])

      else:
          print("o contato não existe na agenda")
      print()
  if index == "3":
#remover contato
      print()
      remover = input("digite o nome do contato que deseja remover da agenda: ").upper()
      if remover in agenda:
          del(agenda[remover])
  print(agenda)

  if index == "4":
#editar contato: mudar numero, add numero, excluir numero
      print()

      editar = input("digite o que deseja alterar no contato:"+
            "\n"+"1 - mudar o número"+
            "\n"+"2 - adicionar um número"+
            "\n"+"3 - excluir um número"+
            "\n"+"4 - voltar"+
            "\n")
      if editar == "1":
          print()
          nomee =  input("digite o nome do contato que deseja mudar o número: ").upper()
          if nomee in agenda:
              novoNumero = input("digite o novo número que deseja para " + nomee)
              agenda[nomee] = novoNumero
      if editar == "2":
          print()
          nomee =  input("digite o nome do contato que deseja adicionar mais um número: ").upper()
          if nomee in agenda:
              maisNumero = input("digite mais um número que deseja para " + nomee)
              contatos.append(maisNumero)
              agenda[nomee] = contatos
      if editar == "3":
          nomee =  input("digite o nome do contato que deseja excluir um número: ").upper()
          print(agenda)
          if nomee in agenda:
              excluirNumero = str(input("digite o número que deseja excluir em " + nomee))
              if excluirNumero in agenda[nome]:
                  agenda[nome].remove(excluirNumero)
              else:
                  print('este contato não existe!!')
              #agenda[nomee].index(agenda[nomee].pop(excluirNumero))
      if editar == "4":
        index = input("digite o que deseja fazer: " +
                "\n" + "1 - adicionar um contato na agenda" +
                "\n" + "2 - buscar o nome do contato na agenda" +
                "\n" + "3 - excluir um contato da agenda" +
                "\n" + "4 - editar um contato" +
                "\n" + "5 - para sair")

  print(agenda)

  if index == "5":
      break