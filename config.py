
#то что ниже обязательно заполнить своими данными
proxy_use = 0 #  0 - не использовать, 1 - Ротируемый прокси(Каждый запрос с нового ip адресса) , 2 - прокси со ссылкой для смены ip
proxy_login = 'plude'
proxy_password = '5l'
proxy_address = 'gate.nodemaven.com'
proxy_port = '8080'
proxy_changeIPlink = "none"



INCH_API_KEY = "upZ2" #надо зарегаться и получить ключ

skolko_trans = [6,8] # указывайте диапазон сколько делать транзакций на каждом кошельке.

#укажите паузу в работе между кошельками, минимальную и максимальную. 
#При смене каждого кошелька будет выбрано случайное число. Значения указываются в секундах
timeoutMin = 10 #минимальная 
timeoutMax = 30 #максимальная
#задержки между операциями в рамках одного кошелька
timeoutTehMin = 30 #минимальная 
timeoutTehMax = 100 #максимальная


skolko_ostavit = { 
"base":[0.0001,0.0002],
}


#то что ниже можно менять только если понимаешь что делаешь
proxies = { 'all': f'http://{proxy_login}:{proxy_password}@{proxy_address}:{proxy_port}',}
if proxy_use:
    request_kwargs = {"proxies":proxies, "timeout": 120}
else:
    request_kwargs = {"timeout": 120}
gas_kef=1.11 #коэфициент допустимого расхода газа на подписание транзакций. можно выставлять от 1.1 до 2
gas_kef_price=1.1 
gas_kef_priority=1 # оставляйте всегда 1,  поднимать только если транзакции слишком долго исполняются при перегруженной сети


prices = {
    "ETH": 2690,    
    "last_update": 0
}



