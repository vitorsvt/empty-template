"""Arquivo com os casos de teste"""


from pytest import CaptureFixture, raises
from inspect import signature

from src.hello import hello


def test_hello_recieves_no_args():
    sig = signature(hello)
    assert len(sig.parameters) == 0, 'hello() takes 0 parameters'

def test_hello_output(capsys: CaptureFixture[str]):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"

def test_hello_returns_none():
    assert hello() == None