from bs4 import BeautifulSoup
import urllib.request

def instagramdownload():
    opt = str(input("Digite 1 para foto\nDigite 2 para video\nQual opção deseja? "))

    if opt == "1":
        # ler html site
        url = str(input("Link da foto Instagram: "))
        x = urllib.request.urlopen(url)
        html = x.read().decode('utf-8')

        # ler metatag que contenha property com name=og:image
        soup = BeautifulSoup(html, 'html.parser')
        meta_tag = soup.head.find('meta', attrs={'property': 'og:image'})
        ogimage = [ogimage.strip() for ogimage in meta_tag['content'].split(',')]

        print("Imagem carregada")

        for k in ogimage:
            nomeimg = str(input("Digite o nome do arquivo: "))

        urllib.request.urlretrieve(k, nomeimg + ".jpg")

        print("Imagem salva")
    elif opt == "2":
        # ler html site
        url = str(input("Link do video Instagram: "))
        x = urllib.request.urlopen(url)
        html = x.read().decode('utf-8')

        # ler metatag que contenha property com name=og:image
        soup = BeautifulSoup(html, 'html.parser')
        meta_tag = soup.head.find('meta', attrs={'property': 'og:video'})
        ogvideo = [ogvideo.strip() for ogvideo in meta_tag['content'].split(',')]

        print("Video carregado")

        for k in ogvideo:
            nomevideo = str(input("Digite o nome do arquivo: "))

        urllib.request.urlretrieve(k, nomevideo + ".mp4")

        print("Video salvo")
    else:
        print("digite uma opção valida!")

while True:
    instagramdownload()