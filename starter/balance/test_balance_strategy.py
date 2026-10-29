import unittest

from balance.balance import Balance
from balance.transaction_strategy import IncomeStrategy, ExpenseStrategy
from transaction.transaction_category import TransactionCategory


class TestBalanceStrategy(unittest.TestCase):

    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()

    def test_income_strategy_updates_balance(self):
        IncomeStrategy().apply(self.balance, 200)
        self.assertEqual(self.balance.get_balance(), 200)

    def test_expense_strategy_updates_balance(self):
        ExpenseStrategy().apply(self.balance, 80)
        self.assertEqual(self.balance.get_balance(), -80)

    def test_balance_uses_strategy_lookup_for_category(self):
        income = type(
            "T",
            (),
            {"category": TransactionCategory.INCOME, "amount": 150},
        )()
        expense = type(
            "T",
            (),
            {"category": TransactionCategory.EXPENSE, "amount": 40},
        )()
        self.balance.apply_transaction(income)
        self.balance.apply_transaction(expense)
        self.assertEqual(self.balance.get_balance(), 110)


if __name__ == "__main__":
    unittest.main()
