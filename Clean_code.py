# Função que recebe três parâmetros
def enviar_email(nome, endereco, mensagem):
    # Define um dicionário com endereços e mensagens para cada nome
    contato = {
        "Ana": {"endereco": "Rua A", "mensagem": "Olá"},
        "João": {"endereco": "Rua B", "mensagem": "Oi"},
        "Maria": {"endereco": "Rua C", "mensagem": "Oie"}
    }

    # Compara o endereço e a mensagem que o usuário passou com os dados corretos
    if nome in contato:
        regra = contato[nome]
        if endereco == regra["endereco"] and mensagem == regra["mensagem"]:
            # Resposta caso os dados estejam corretos 
            print(f"Email enviado para {nome}")
            return  # Sai da função após o envio

    # Se nome não estiver no dicionário ou dados não baterem
    print("Não foi possível enviar o email")

# Testes no terminal
enviar_email("Ana", "Rua A", "Olá")           # Deve funcionar
enviar_email("Luiza", "Rua L", "Alo")         # Deve falhar
enviar_email("Maria", "Rua C", "Oie")         # Deve funcionar
