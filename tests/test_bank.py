"""Unit tests for bank.py"""

import pytest

from bank_api.bank import Bank, Account


@pytest.fixture
def bank() -> Bank:
    return Bank()

@pytest.fixture
def account() -> Account:
    return Account()

# @pytest.fixture
# def name() -> str:
#     return name

# @pytest.fixture
# def amount() -> int:
#     return amount



def test_create_account_raises_error_if_name_blank(bank: Bank):
    # This means: assert an exception is raised during the following block
    with pytest.raises(Exception):
        bank.create_account('')

def test_bank_creates_empty(bank: Bank):
    assert len(bank.accounts) == 0
    assert len(bank.transactions) == 0

def test_can_create_and_get_account(bank: Bank):
    bank.create_account('Test')
    account = bank.get_account('Test')

    assert len(bank.accounts) == 1
    assert account.name == 'Test'

def test_get_account_raises_error_if_no_account_matches(bank: Bank):
    bank.create_account('Name 1')

    # This means: assert an exception is raised during the following block
    with pytest.raises(ValueError):
        bank.get_account('Name 2')

# TODO: Add unit tests for bank.add_funds()
def test_add_funds( bank: Bank ):
    name = 'Fred Bloggs'
    amount = 2
    bank.create_account(name)
    bank.add_funds(name, amount)
    assert len(bank.transactions) == 1
    assert bank.transactions[0].amount == amount
    assert bank.transactions[0].account.name == name

@pytest.mark.parametrize("amount", [1,2,3,99,100,1.1, 99.99,100,99.999,3.1415926,-9.99])    
def test_add_many_valid_funds( bank: Bank, amount: int ):
    name = 'Fred Bloggs'
    bank.create_account(name)
    bank.add_funds(name, amount)
    assert len(bank.transactions) == 1
    assert bank.transactions[0].amount == amount
    assert bank.transactions[0].account.name == name
    
def test_add_zero_funds_does_not_add_no_amount( bank: Bank ):
    name = 'Fred Bloggs'
    amount = 0
    bank.create_account(name)
    bank.add_funds(name, amount)
    assert len(bank.transactions) == 0
    
def test_add_minus_funds_is_valid( bank: Bank ):
    name = 'Fred Bloggs'
    amount = -1
    bank.create_account(name)
    bank.add_funds(name, amount)
    assert len(bank.transactions) == 1
    
def test_add_funds_raises_exception_if_no_name( bank: Bank ):
    with pytest.raises(ValueError):
        bank.add_funds('', 0 ) 

def test_add_multiple_funds( bank: Bank ):
    name = 'Fred Bloggs'
    bank.create_account(name)
    amount = 2
    for fundings in range(100):
        bank.add_funds(name, amount)
    assert len(bank.transactions) == 100
    


