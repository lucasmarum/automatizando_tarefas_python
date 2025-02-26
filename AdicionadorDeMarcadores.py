import pyperclip

texto = pyperclip.paste()

linhas = texto.split('\n')
for i in range (len(linhas)):
    linhas[i] = '* ' + linhas[i]
texto = '\n'.join(linhas)

pyperclip.copy(texto)