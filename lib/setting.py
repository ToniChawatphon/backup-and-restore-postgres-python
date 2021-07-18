import os
from lib.utils import read_yaml
from lib.constant import CREDENTIALS


def get_postgres_credential() -> dict:
    """Get postgres credential from yaml to dict
        Return:
            env: (dict)
    """
    config      = read_yaml(CREDENTIALS)
    postgres = config.get('postgres')

    port     = postgres.get('PGPORT')
    host     = postgres.get('PGHOST')
    database = postgres.get('DATABASE')
    user     = postgres.get('PGUSER')
    password = postgres.get('PGPASSWORD')

    # ENV
    env = dict(os.environ)
    env['PGPORT']     = str(port)
    env['PGHOST']     = str(host)
    env['DATABASE']   = database
    env['PGUSER']     = user
    env['PGPASSWORD'] = password

    return env
