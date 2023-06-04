import os


PATH = os.path.dirname(os.path.dirname(__file__))
ENV = {
    'live': {
        'host': 'https://api.bilibili.com'
    },

    'uat': {

    },

    'sit': {

    }

}

env_name = 'live'
host = ENV[env_name]['host']
