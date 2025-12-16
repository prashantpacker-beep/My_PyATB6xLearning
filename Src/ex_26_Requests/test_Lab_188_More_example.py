import pytest
import allure
import requests

@allure.title("TC#1 Verify that 2-2== 0")
@allure.description("This is Basic MATH Test")
@pytest.mark.tapas

def test_basic_math():
    assert 2-2==0

@allure.title("TC#2 Verify that 3-3= 0")
@allure.description("This is smoke test which check substraction is proper")
@pytest.mark.tapas
def test_basic_sub1():
    assert 3-3==0

@pytest.mark.skip(reason="Not working,skip it")
def test_sub2():
    assert 0-0!=0