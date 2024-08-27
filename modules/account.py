import time
import random

from typing import Dict
from eth_account import Account as EthereumAccount
from web3.exceptions import TransactionNotFound

import config
from data.addresses import ADDRESSES
from fun import *


class Account:
    def __init__(self, private_key: str, chain: str) -> None:
        self.private_key = private_key
        self.chain = chain
        self.explorer = self.scan = ADDRESSES[chain]["scan"]

        self.w3 = Web3(Web3.HTTPProvider(ADDRESSES[self.chain]["rpc"], request_kwargs=config.request_kwargs))
        self.account = EthereumAccount.from_key(private_key)
        self.address = self.account.address

    def get_tx_data(self, value: int = 0):
        tx = {
            "chainId": self.w3.eth.chain_id,
            "from": self.address,
            "value": value,
            "gasPrice": int(self.w3.eth.gas_price*config.gas_kef_price),
            "nonce": self.w3.eth.get_transaction_count(self.address),
        }
        return tx


    def need_gas_fee(self, transaction):
        gas = self.w3.eth.estimate_gas(transaction)
        gas = int(gas * config.gas_kef)
        gas_price = int(self.w3.eth.gas_price*config.gas_kef_price)

        return gas * gas_price
    
    # передаем колную коммиссию которую надо  и если это перевод ETH  то передаем сумму которую отпарвляем или платим за что-то.
    def check_allowed_fee(self, full_fee, amount_wei = 0):

        full_fee_USD = Web3.from_wei(full_fee*config.prices[ADDRESSES[self.chain]['native']] , "ether")

        if  full_fee_USD > config.max_komissia:
            log(f" чето очень дорого. просит {full_fee_USD}$ > готов отдать {config.max_komissia}$ ")
            return False
        
        balance = self.get_balance_native()['balance']
        if(balance < full_fee*config.gas_kef + amount_wei):
            log("   low balance")
            return False

        return True
    

    def get_contract(self, contract_address: str, abi=None):
        contract_address = self.w3.to_checksum_address(contract_address)

        if abi is None:
            abi = erc20_abi

        contract = self.w3.eth.contract(address=contract_address, abi=abi)

        return contract

    # можно использовать как адресс так и тикер
    def get_balance(self, contract_address: str) -> Dict:
        if not len(contract_address) == 42 or not contract_address.startswith("0x"):
            contract_address = ADDRESSES[self.chain]['TOKENS'][contract_address]
        contract_address = self.w3.to_checksum_address(contract_address)
        contract = self.get_contract(contract_address)

        symbol = contract.functions.symbol().call()
        decimal = contract.functions.decimals().call()
        balance = contract.functions.balanceOf(self.address).call()
        balance_decimal = 0 if balance == 0 else balance / 10 ** decimal
        balance_USD = balance_decimal * config.prices.get(symbol, 1)

        return {"balance": balance, "balance_decimal": balance_decimal, "symbol": symbol, "decimal": decimal, "balance_USD": balance_USD}

    # можно получить просто баланс, а моджно если отпарвить True получить баланс за вычетом остатков.
    def get_balance_native(self, ostavit = False) -> Dict:
        balance = self.w3.eth.get_balance(self.address)
        if ostavit:
            skolko_ostavit = random.uniform(config.skolko_ostavit[self.chain][0], config.skolko_ostavit[self.chain][1])
            balance = balance - Web3.to_wei(skolko_ostavit, 'ether')
        balance_decimal = float(Web3.from_wei(balance, 'ether'))
        balance_USD = balance_decimal*config.prices[ADDRESSES[self.chain]['native']]

        return {"balance": balance, "balance_decimal": balance_decimal, "balance_USD": balance_USD}

    def get_amount(
            self,
            from_token: str,
            min_amount: float,
            max_amount: float,
            decimal: int,
            all_amount: bool,
            min_percent: int,
            max_percent: int
    ) -> [int, float, float]:
        random_amount = round(random.uniform(min_amount, max_amount), decimal)
        random_percent = random.randint(min_percent, max_percent)
        percent = 1 if random_percent == 100 else random_percent / 100

        if from_token == ADDRESSES[self.chain]['native']:
            balance = self.get_balance_native(True)
            amount_wei = int(balance["balance"] * percent) if all_amount else self.w3.to_wei(random_amount, "ether")
            amount = self.w3.from_wei(amount_wei, "ether")
        else:
            balance = self.get_balance(ADDRESSES[self.chain]['TOKENS'][from_token])
            amount_wei = int(balance["balance"] * percent) \
                if all_amount else int(random_amount * 10 ** balance["decimal"])
            amount = balance["balance_decimal"] * percent if all_amount else random_amount

        balance = balance["balance"]
        return amount_wei, amount, balance

    def check_allowance(self, token_address: str, contract_address: str) -> float:
        token_address = self.w3.to_checksum_address(token_address)
        contract_address = self.w3.to_checksum_address(contract_address)

        contract = self.w3.eth.contract(address=token_address, abi=erc20_abi)
        amount_approved = contract.functions.allowance(self.address, contract_address).call()

        return amount_approved

    def approve(self, amount: int, token_address: str, contract_address: str):
        token_address = self.w3.to_checksum_address(token_address)
        contract_address = self.w3.to_checksum_address(contract_address)

        contract = self.w3.eth.contract(address=token_address, abi=erc20_abi)

        allowance_amount = self.check_allowance(token_address, contract_address)

        if amount > allowance_amount or amount == 0:
            log(f"  [{self.address}] Make approve")

            # approve_amount = 2 ** 128 if amount > allowance_amount else 0
            approve_amount = amount if amount > allowance_amount else 0

            tx_data = self.get_tx_data()

            transaction = contract.functions.approve(
                contract_address,
                approve_amount
            ).build_transaction(tx_data)

            signed_txn = self.sign(transaction)

            txn_hash = self.send_raw_transaction(signed_txn)

            self.wait_until_tx_finished(txn_hash)

            timeOut("teh")

    def wait_until_tx_finished(self, hash: str, max_wait_time=180):
        start_time = time.time()
        while True:
            try:
                receipts = self.w3.eth.get_transaction_receipt(hash)
                status = receipts.get("status")
                if status == 1:
                    log_ok(f"  [{self.address}] {self.explorer}/{hash} successfully!")
                    return True
                elif status is None:
                    time.sleep(1)
                else:
                    log_error(f"  [{self.address}] {self.explorer}/{hash} transaction failed!")
                    return False
            except TransactionNotFound:
                if time.time() - start_time > max_wait_time:
                    log_error(f"  [{self.address}] {self.explorer}{hash} Не дождался исполнения транзакции за {max_wait_time} секунд. Исполнится она или нет мы не знаем.")
                    return False
                time.sleep(1)

    def sign(self, transaction):
        gas = self.w3.eth.estimate_gas(transaction)
        gas = int(gas * config.gas_kef)

        transaction.update({"gas": gas})
        if ADDRESSES[self.chain]['type']:
            maxPriorityFeePerGas = int(self.w3.eth.max_priority_fee * config.gas_kef_priority)
            fee_history = self.w3.eth.fee_history(10, 'latest', [10, 90])
            baseFee=round(mean(fee_history['baseFeePerGas']))
            maxFeePerGas = maxPriorityFeePerGas + round(baseFee * config.gas_kef_price)

            del transaction['gasPrice']
            transaction['maxFeePerGas'] = maxFeePerGas
            transaction['maxPriorityFeePerGas'] = maxPriorityFeePerGas

        signed_txn = self.w3.eth.account.sign_transaction(transaction, self.private_key)

        return signed_txn
    

    def send_raw_transaction(self, signed_txn):
        try:
            txn_hash = self.w3.to_hex(self.w3.eth.send_raw_transaction(signed_txn.rawTransaction))
        except Exception as error:
            txn_hash = self.w3.to_hex(self.w3.eth.send_raw_transaction(signed_txn.raw_transaction))
        return txn_hash


    def send_transaction(self, transaction):
        try:
            signed_txn = self.sign(transaction)
            txn_hash = self.send_raw_transaction(signed_txn)
            self.wait_until_tx_finished(txn_hash)
            return txn_hash
        except Exception as error:
            return log_error(f'send transaction false: {error}')
