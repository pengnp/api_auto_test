import pytest

from utils import *

yaml_util = YamlUtil('bili.yml')


class TestBili:

    def setup_class(self):
        self.yaml_data = yaml_util.yaml_data

    def setup_method(self, method):
        data = self.yaml_data[method.__name__]
        self.url, self.method, self.params = data['url'], data['method'], data['params']

    @pytest.mark.smoking
    @pytest.mark.parametrize('mid', yaml_util.get_data('test_search')[0])
    @pytest.mark.parametrize('ps', yaml_util.get_data('test_search')[1])
    def test_search(self, mid, ps):
        self.params['mid'], self.params['ps'] = mid, ps
        rep = req.call(self.url, self.method, params=self.params).json()
        assert len(rep['data']['list']['vlist']) == ps

    @pytest.mark.UserHomePage
    @pytest.mark.aaa
    def test_locs(self):
        rep = req.call(self.url, self.method, params=self.params).json()
        assert rep['count'] == 1