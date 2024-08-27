from statistics import mean
import time
from web3 import Web3
import requests
import random
from datetime import datetime
import config
import fun
from fun import *
from modules import *



current_datetime = datetime.now()
print(f"\n\n {current_datetime}")
print(f'============================================= Плюшкин Блог =============================================')
print(f'subscribe to : https://t.me/plushkin_blog \n============================================================================================================\n')


keys_list = []
with open("private_keys.txt", "r") as f:
    for row in f:
        private_key=row.strip()
        if private_key:
            keys_list.append(private_key)

random.shuffle(keys_list)

i=0
for private_key in keys_list:
    string_list = private_key.split("	")
    private_key = string_list[0]
    wallet_out = string_list[1] if len(string_list) > 1 else ""    
    i+=1
    if config.proxy_use == 2:
        while True:
            try:
                requests.get(url=config.proxy_changeIPlink)
                fun.timeOut("teh")
                result = requests.get(url="https://yadreno.com/checkip/", proxies=config.proxies)
                print(f'Ваш новый IP-адрес: {result.text}')
                break
            except Exception as error:
                print(' !!! Не смог подключиться через Proxy, повторяем через 2 минуты... ! Чтобы остановить программу нажмите CTRL+C или закройте терминал')
                time.sleep(120)

    skolko_trans = random.randint(config.skolko_trans[0],config.skolko_trans[1])
    for _ in range(skolko_trans):
        try:
            inch_dex = Inch(private_key, "base")
            inch_dex.anyswap(0.0000001, 0.000005)
        except Exception as error:
            fun.log_error(f"Ошибка в main: {error}")
        
        timeOut("teh")


    timeOut()
    

    
log("Ну типа все, кошельки закончились!")