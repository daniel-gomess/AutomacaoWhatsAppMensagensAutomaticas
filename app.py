import pyautogui
import webbrowser
from time import sleep


telefones = []

with open('telefones.txt', 'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
#    print(telefones)

for telefone in telefones:
    #Abrindo o WhatsApp Web
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    # Clicando em "Continuar para o WhatsApp Web"
    pyautogui.click(1097,251, duration=1)
    sleep(5)
    # Clicando na caixa de texto
    pyautogui.click(758,989, duration=1)
    sleep(1)
    # Escrevendo a mensagem
    pyautogui.typewrite('teste!!!')
    sleep(3)
    pyautogui.press('enter')
    sleep(3)
    # Encerrando automação
    pyautogui.alert(text='Mensagens enviadas com sucesso!', title='Atenção!')