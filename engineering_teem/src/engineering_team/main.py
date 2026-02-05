#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from engineering_team.crew import EngineeringTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

os.makedirs('output', exist_ok=True)

requirements = """
    Design a class-based Account Management System for a trading simulation.

    **Core Features:**
    1. **Account Management**: Initialize with an account ID and initial funds.
    2. **Transactions**:
    - `deposit(amount)`: Add funds to the cash balance.
    - `withdraw(amount)`: Deduct funds from the cash balance.
    - `buy_shares(symbol, quantity)`: Deduct cash and increase share quantity.
    - `sell_shares(symbol, quantity)`: Increase cash and decrease share quantity.
    3. **Analytics**:
    - `calculate_portfolio_value()`: Return total value (Cash + Current Market Value of all shares).
    - `calculate_profit_loss()`: Return (Current Portfolio Value - Initial Deposit).
    - `get_holdings()`: Return a report of currently held shares.
    - `get_transactions()`: Return a log of all past actions (deposits, withdraws, trades).

    **Business Rules (Critical Constraints):**
    - **Insufficient Funds**: `withdraw` and `buy_shares` MUST fail (return False or raise error) if the user has insufficient cash. Do not allow negative balance.
    - **Insufficient Shares**: `sell_shares` MUST fail if the user attempts to sell more shares than they own.

    **Technical Requirements:**
    - The system utilizes a helper function `get_share_price(symbol)` to fetch real-time prices.
    - **Implementation Detail**: You MUST include a mock implementation of `get_share_price(symbol)` in the same file that returns fixed example prices for 'AAPL', 'TSLA', and 'GOOGL' to ensure the code is testable immediately.
"""
module_name = "accounts.py"
class_name = "Account"


def run():
    """
    Run the research crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    result = EngineeringTeam().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()