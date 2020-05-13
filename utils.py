from configparser import ConfigParser


def get_auth0_variables(filename='auth0.properties'):
    config = ConfigParser()
    config.read(filename)
    config_vars = dict(config.items('AUTH_0'))
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
