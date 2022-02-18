class NoEnvException(Exception):
    pass


class Config:

    SUPPORTED_ENVS = ['dev', 'qa']

    def __init__(self, env):

        if env.lower() not in self.SUPPORTED_ENVS:
            raise NoEnvException(f'The "{env}" is not a supported environment. '
                                 f'Choose one of the environments {self.SUPPORTED_ENVS}.')

        self.base_url = {
            'dev': 'https://myamazingdjangoblog.herokuapp.com',
            'qa': 'https://myamazingdjangoblog.herokuapp.com',
        }[env]
