# balance.py

from transaction.transaction_category import TransactionCategory
from balance.transaction_strategy import IncomeStrategy, ExpenseStrategy


class Balance:
    """Singleton to track the balance."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Balance, cls).__new__(cls)
            cls._instance.net_balance = 0.0
            cls._instance._observers = []
            cls._instance._transaction_strategies = {
                TransactionCategory.INCOME: IncomeStrategy(),
                TransactionCategory.EXPENSE: ExpenseStrategy(),
            }

        return cls._instance

    def __init__(self):
        """Initialize the balance. Prevent direct instantiation."""
        if hasattr(self, '_initialized') and self._initialized:
            return

        self._initialized = True

    @classmethod
    def get_instance(cls):
        """Get the singleton instance of Balance."""
        if cls._instance is None:
            cls._instance = cls()

        return cls._instance

    def register_observer(self, observer):
        """Register an observer"""
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        """Remove an observer"""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, transaction):
        """Notify registered observers about balance updates"""
        for observer in self._observers:
            observer.update(self, transaction)

    def reset(self):
        """Reset the net balance to zero."""
        self.net_balance = 0.0

    def add_income(self, amount):
        """Add income to the balance."""
        self.net_balance += amount

    def add_expense(self, amount):
        """Subtract expense from the balance."""
        self.net_balance -= amount

    def apply_transaction(self, transaction):
        """
        Apply a Transaction object to update the balance.

        Args:
            transaction (Transaction): The transaction to apply.
        """
        strategy = self._transaction_strategies.get(transaction.category)

        if strategy is None:
            raise ValueError("Invalid transaction category")

        strategy.apply(self, transaction.amount)
        self.notify_observers(transaction)

    def get_balance(self):
        """Get the current net balance."""
        return self.net_balance

    def summary(self):
        """Return a summary string of the net balance."""
        return f"Current Balance: ${self.net_balance:.2f}"
