import pytest
import allure

@allure.tag('test')
def test_rcv():
	var = 3
	assert var == 3

@allure.tag('test2')
def test_jal():
	var = 7
	assert var == 3
