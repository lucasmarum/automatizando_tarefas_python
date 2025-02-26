import pyperclip, sys
#GERENCIADOR DE SENHAS NADA SEGURO
senhas = {'Email': 'SENHASUPERFORTE123#',
          'Facebook': 'SENHAFACEBOOK123',
          'ZVIDEOS': 'SENHADESAPECA123#'}

if len(sys.argv) < 2:
    print("Digite a rede social desejada: ")
    sys.exit()
conta = sys.argv[1]

if conta in senhas:
    pyperclip.copy(senhas[conta])
    print("Senha de: " + conta + " foi copiada com sucesso!!")
else:
    print("conta não encontrada :(")