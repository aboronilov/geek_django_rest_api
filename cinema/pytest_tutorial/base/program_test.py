from program import summa
import pytest


class TestCase:
    a = 10

    @pytest.mark.parametrize('x, y, result', [
        (10, 5, 15),
        (12, 3, 15),
        (5, 3, 8)
    ])
    def test_summa1(self, x, y, result):
        assert summa(x, y) == result

    # провал этого теста = хорошо
    # raises - передать исключения, которые я ожидаю
    @pytest.mark.xfail(strict=True, raises=(ZeroDivisionError, TypeError))
    def test_useless(self):
        assert 1 + '1'

    # пропускает тест, нужно указать условие и reason
    # например на некоторых ОС тесты выполнять не надо, тогда фильтрация по версии ОС
    @pytest.mark.skipif(a > 5, reason='123')
    def test_useless_2(self):
        assert 1 + '1'
