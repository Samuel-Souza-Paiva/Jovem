import requests
from PIL import Image
 
def buscar_imagens_de_gatos():
    try:
        #URL da API TheCatApi
        resposta = requests.get("https://api.thecatapi.com/v1/images/search?limit=10")
        resposta.raise_for_status()
 
       
 
    except requests.RequestException as erro:
        print("Erro ao buscar imagens de gatos:", erro)
#Executar
buscar_imagens_de_gatos()
 
 