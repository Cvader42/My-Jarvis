class FinancialManager:
    def __init__(self):
        self.account_balances = {}
        self.expenses = []
        self.investments = {}

    def get_account_balance(self, account_type):
        # This method gets the account balance for a given account type.
        return self.account_balances.get(account_type, 0)

    def track_expenses(self, expense_type, amount):
        # This method tracks an expense.
        self.expenses.append({"expense_type": expense_type, "amount": amount})

    def get_investment_performance(self, investment_type):
        # This method gets the investment performance for a given investment type.
        return self.investments.get(investment_type, "No data available for this investment.")

# Create an instance of FinancialManager
fin_manager = FinancialManager()
