Envio Automático de Mensagens via WhatsApp Web

Este script em Python automatiza o envio de mensagens para uma lista de números de telefone através do WhatsApp Web, utilizando as bibliotecas pyautogui, webbrowser e time.

Como Funciona
    Leitura dos Telefones:
        O script lê uma lista de números de telefone a partir de um arquivo chamado telefones.txt.

        Cada linha do arquivo deve conter um número no formato internacional, sem espaços ou caracteres especiais (ex: 5511999999999).

    Automação de Envio:
        Para cada número, o script:

            Abre a URL do WhatsApp API para iniciar uma conversa (https://api.whatsapp.com/send?phone={telefone}).
            Aguarda o carregamento da página.

            Usa o pyautogui para clicar nos botões necessários ("Continuar para o WhatsApp Web" e na caixa de mensagem).

            Digita a mensagem pré-definida ("teste!!!") e envia.

    Finalização:
        Após enviar todas as mensagens, o script exibe um alerta confirmando que o envio foi concluído.

Requisitos
    Python instalado na máquina.

    Instalação das bibliotecas:
        pip install pyautogui
    Ter o arquivo telefones.txt no mesmo diretório do script.

    Estar logado no WhatsApp Web no navegador padrão.

Observações Importantes
    O script usa coordenadas fixas do mouse para clicar nos botões. Essas coordenadas podem variar dependendo da resolução e do navegador usado. Se necessário, ajuste os valores dos pyautogui.click(x, y) para seu ambiente.
    
    Recomenda-se rodar o script em um ambiente controlado, pois a automação do mouse pode ser sensível a movimentos ou interferências externas.

Exemplo do Arquivo telefones.txt
    5511999999999
    5511988888888
    5511977777777

Cada número deve estar em uma linha separada.