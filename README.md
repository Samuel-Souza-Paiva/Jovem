HEAD
Enviar Email com Python

Este é um pequeno script em Python que simula o envio de e-mails para usuários específicos. O envio é controlado por um dicionário que contém combinações de nome, endereço e mensagem, retornando uma confirmação de envio.

Esse código simula envio e restorno de email, resultando em ennios ou falhas (de acordo com os dados)

#como funciona?
É necessario preencher as seguintes informações:
- Nome 
- Endereço 
- Mensagem 

Resposta:
- o sistema retorna uma resposta positiva, caso as informacões forem preenchidas corretamente. E caso as elas não baterem de acordo com o preenchimento, volta uma respota negativa. 


Testes:
- Você pode mudar alguma informação dos nomes, desse jeito podendo fazer testes e receber respostas no terminal. 

Exemplo:
enviar_email("Ana", "Rua A", "Olá")     # Sucesso
enviar_email("Luiza", "Rua L", "Alo")   # Falha
enviar_email("Maria", "Rua C", "Oie")   # Sucesso

