import pyperclip, re

celular_regex = re.compile(r'''(
    (\d{2}|\(\d{2}\))? # CÓDIGO DE ÁREA
    (\s|-)?            # SEPARADOR OPCIONAL
    (\d{2})?           # CÓDIGO DE REGIÃO
    (\s|-)?            # SEPARADOR OPCIONAL
    (\d{5})            # PRIMEIROS 5 DÍGITOS DO NÚMERO
    (\s|-)?            # SEPARADOR OPCIONAL
    (\d{4})            # ÚLTIMOS 4 DÍGITOS DO NÚMERO
)''', re.VERBOSE)



email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+    # PARTE LOCAL (ANTES DO @)
    @                    # SÍMBOLO @
    [a-zA-Z0-9.-]+       # DOMÍNIO
    \.[a-zA-Z]{2,}       # SUFIXO DE DOMÍNIO COM 2 OU MAIS CARACTERES
)''', re.VERBOSE)

texto = str(pyperclip.paste())

encontrados = []
for grupos in celular_regex.findall(texto):
    numero_telefone = '-'.join([grupos[5],grupos[7]])
    encontrados.append(numero_telefone)
for grupos in email_regex.findall(texto):
    encontrados.append(grupos)

if len(encontrados) > 0:
    pyperclip.copy('\n'.join(encontrados))
    print("Copiado!!")
    print('\n'.join(encontrados))
else:
    print("Nenhum numero de celular/emails encontrados.")