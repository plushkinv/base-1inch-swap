from config import INCH_API_KEY
from .account import Account
from fun import *


        
class Inch(Account):
    def __init__(self, private_key: str, chain: str) -> None:
        super().__init__(private_key=private_key, chain=chain)

        self.headers = {"Authorization": f"Bearer {INCH_API_KEY}", "accept": "application/json"}

        self.proxy = ""


    def build_tx(self, from_token: str, to_token: str, amount: int, slippage: int):
        url = f"https://api.1inch.dev/swap/v6.0/{self.w3.eth.chain_id}/swap"

        params = {
            "src": self.w3.to_checksum_address(from_token),
            "dst": self.w3.to_checksum_address(to_token),
            "amount": amount,
            "from": self.address,
            "slippage": slippage,
        }

        time.sleep(1)
        response = requests.request(url=url, params=params, headers=self.headers, method="GET")

        transaction_data = response.json()

        return transaction_data

    def tokens(self):
        url = f"https://api.1inch.dev/swap/v6.0/{self.w3.eth.chain_id}/tokens"
        params = {
        }
        time.sleep(1)
        response = requests.request(url=url, params=params, headers=self.headers, method="GET")
        transaction_data = response.json()
        return transaction_data
    
    def spender(self):
        url = f"https://api.1inch.dev/swap/v6.0/{self.w3.eth.chain_id}/approve/spender"
        params = {
        }
        time.sleep(1)
        response = requests.request(url=url, params=params, headers=self.headers, method="GET")
        transaction_data = response.json()
        return transaction_data





    def anyswap(
            self,
            min_amount: float,
            max_amount: float,
    ):
        tokens = self.tokens()
        tokens = tokens['tokens']

        # Удаление первых двух строк
        keys_to_remove = list(tokens.keys())[:2]
        for key in keys_to_remove:
            del tokens[key]

        # Выбор случайной строки
        token_address = random_key = random.choice(list(tokens.keys()))
        random_value = tokens[random_key]
        decimals = random_value['decimals']
        token = random_value['symbol']
        
        ADDRESSES[self.chain]['TOKENS'][token] = token_address

        # inch_dex.swap(from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent)
        self.swap("ETH", token, min_amount, max_amount, 18, 1, False, 1, 1)
        timeOut("teh")
        self.swap(token, "ETH", 0.1, 0.1, decimals, 1, True, 20, 80)

    def swap(
            self,
            from_token: str,
            to_token: str,
            min_amount: float,
            max_amount: float,
            decimal: int,
            slippage: int,
            all_amount: bool,
            min_percent: int,
            max_percent: int
    ):
        amount_wei, amount, balance = self.get_amount(
            from_token,
            min_amount,
            max_amount,
            decimal,
            all_amount,
            min_percent,
            max_percent
        )

        log(
            f"[{self.address}] Swap on 1inch – {from_token} -> {to_token} | {amount} {from_token}"
        )

        from_token = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE" if from_token == "ETH" else ADDRESSES[self.chain]['TOKENS'][from_token]
        to_token = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE" if to_token == "ETH" else ADDRESSES[self.chain]['TOKENS'][to_token]

        if from_token != "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE":
            transaction_data = self.spender()
            contract_addres = transaction_data['address']
            self.approve(amount_wei, from_token, contract_addres)

        transaction_data = self.build_tx(from_token, to_token, amount_wei, slippage)

        tx_data = self.get_tx_data()
        tx_data.update(
            {
                "to": self.w3.to_checksum_address(transaction_data["tx"]["to"]),
                "data": transaction_data["tx"]["data"],
                "value": int(transaction_data["tx"]["value"]),
            }
        )

        signed_txn = self.sign(tx_data)

        txn_hash = self.send_raw_transaction(signed_txn)

        self.wait_until_tx_finished(txn_hash)
