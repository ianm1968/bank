
import pytest

from bank_api.bank import Bank, Account

class Report:
    bank: Bank()
    def __init__(self, bank: Bank):
        self.bank = bank
    
    def get_balance(self) -> decimal :
        return 1
    
@pytest.fixture
def bank() -> Bank:
    return Bank()


    
