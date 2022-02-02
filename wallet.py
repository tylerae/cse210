import time 

class Wallet:
    
    class Transaction:
        
        def __init__(self, amount):
                self.amount = amount
                self._timestamp = time.time()
            
        def get_amount(self):
            return self.amount


    def __init__(self, intial_amount):
        self._amount = intial_amount
        self._transactions = []
        self._transactions.append(Wallet.Transaction(intial_amount))
        pass

    def add_transaction(self, tx_amount):
        self._transactions.append(Wallet.Transaction(tx_amount))

    def _sum_transactions(self):
        total = 0
        for tx in self._transactions:
            total += tx.get_amount()
        return total

    def get_balance(self):
        return self._sum_transactions()

    def __str__(self):
        return str(self.get_balance())
        

wallet = Wallet(50)
wallet.add_transaction(-25)
print(wallet.get_balance())