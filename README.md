# Automatização de Envio de Mensagens WhatsApp

Este projeto utiliza Selenium e Tkinter para automatizar o envio de mensagens pelo WhatsApp Web.

## Pré-requisitos

* Certifique-se de ter o Python instalado.

* Crie o ambiente isolado com o comando:

```bash
python3 -m venv .venv
```
* Caso o venv não esteja instalado, utilize o comando:

```bash
sudo apt install python3-venv
```

* Depois de criado, temos que ativar este ambiente para usá-lo.

```bash
source .venv/bin/activate
```

* Você pode instalar as dependências necessárias usando o seguinte comando:

```bash
pip install -r requirements.txt
```
## Certifique-se de ter o navegador Firefox instalado no seu sistema.

# Configuração

Antes de executar o projeto, certifique-se de ter um arquivo CSV válido com a lista de contatos chamado 'lista-de-clientes.csv' e a coluna com os números dos contatos chamada 'Telefone'.

# Execução

Execute o script principal main.py para iniciar a automação:

```bash
python3 main.py
```
A interface gráfica será exibida, permitindo que você insira a mensagem desejada. Clique no botão "Enviar Mensagens" para iniciar o envio de mensagens para os contatos da lista.

# Aviso
### Este script utiliza automação na interface web e interações com o WhatsApp Web, o que pode violar os Termos de Serviço do WhatsApp. Use-o com responsabilidade e esteja ciente dos riscos associados.