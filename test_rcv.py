import pytest
import allure

@allure.tag('test')
def test_rcv():
	var = 3
	assert var == 3