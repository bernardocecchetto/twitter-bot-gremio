import tweepy
from bot_gremio.credentials import *
from datetime import datetime, timezone, timedelta
import time


def run():

    while True:
        data_e_hora_atuais = datetime.now()
        diferenca = timedelta(hours=-3)
        fuso_horario = timezone(diferenca)
        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
        data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%H:%M')

        if data_e_hora_sao_paulo_em_texto == '19:03':
            client = tweepy.Client(BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_SECRET)
            response = client.create_tweet(text='GRÊMIO')
            time.sleep(1800)
        else:
            print(data_e_hora_sao_paulo_em_texto + " - Aguardando a hora do GREMIO")
            time.sleep(1800)


run()



