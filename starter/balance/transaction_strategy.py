# transaction_strategy.py

class TransactionStrategy:
    """Encapsulates how a transaction affects the balance."""
    def apply(self, balance, amount):
        raise NotImplementedError("Subclasses must implement apply().")


class IncomeStrategy(TransactionStrategy):
    """Strategy for income transactions."""
    def apply(self, balance, amount):
        balance.add_income(amount)


class ExpenseStrategy(TransactionStrategy):
    """Strategy for expense transactions."""
    def apply(self, balance, amount):
        balance.add_expense(amount)
