# transaction_adapter.py

from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory

class TransactionAdapter:
    def __init__(self, external_transaction):
        self.external_transaction = external_transaction

    def to_transaction(self):
        amount = self.external_transaction.amount
        category = TransactionCategory.INCOME # always income

        return Transaction(amount, category)
