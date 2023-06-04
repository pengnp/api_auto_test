import pytest


@pytest.mark.aaa
class TestDemo1:

    def test_01(self):
        print(1)
        assert 1 == 1

    def test_02(self):
        print(2)

    def test_03(self):
        print(3)


class TestDemo2:

    def test_01(self):
        print(1)

    def test_02(self):
        print(2)

    def test_03(self):
        print(3)


if __name__ == '__main__':
    pytest.main(['-sv'])