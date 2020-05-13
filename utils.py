import os
from configparser import ConfigParser


def get_auth0_variables():
    config_vars = {
        'auth0_domain': os.environ['AUTH0_DOMAIN'],
        'algorithms': os.environ['ALGORITHMS'],
        'api_audience': os.environ['API_AUDIENCE'],
        'client_id': os.environ['CLIENT_ID'],
        'redirect_url': os.environ['REDIRECT_URL']
    }
    return config_vars


def get_lead_token(filename='auth0.properties'):
    config = ConfigParser()
    config.read(filename)
    config_vars = dict(config.items('TOKENS'))
    return config_vars['lead']


def get_member_token(filename='auth0.properties'):
    config = ConfigParser()
    config.read(filename)
    config_vars = dict(config.items('TOKENS'))
    return config_vars['member']
