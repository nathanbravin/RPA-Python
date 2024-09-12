import pyautogui
import time
import requests
import webbrowser


def get_random_tweet():
    url = "https://uselessfacts.jsph.pl/random.json?language=pt"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['text']
    else:
        return "Fato não disponível no momento."
    
tweet = 'TESTE TWEET AUTOMATICO'

def open_twitter():
    # Abre o Safari diretamente usando o webbrowser
    webbrowser.get("safari").open('https://x.com/i/flow/login')
    time.sleep(2)  # Espera o navegador abrir e carregar a página

def login_twitter(username,password):
    # Espera para garantir que a página esteja completamente carregada
    time.sleep(2)
    # Localiza a caixa de login pela imagem e clica
    login_posicao = (654,469)
    pyautogui.moveTo(login_posicao)
    pyautogui.click()
    pyautogui.write(username)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write(password)
    pyautogui.press('enter')         
    
def escrever_tweet(tweet):
    time.sleep(6)
    posicao_escrever = (423,187)
    pyautogui.moveTo(posicao_escrever)
    pyautogui.click()
    pyautogui.write(tweet)
    time.sleep(2)
    posicao_botao = (846,281)
    pyautogui.moveTo(posicao_botao)
    pyautogui.click()
  

# Chama as funções para executar o RPA
open_twitter()
login_twitter('login','password')
escrever_tweet(tweet)

