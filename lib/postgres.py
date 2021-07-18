import platform
from subprocess import Popen


def backup_postgres(env: dict, filename: str) -> None:
    '''
    Back up PostgreSQL database into .tar file
            Parameters:
                    env      (dict): postgres credential containing
                                    Ex
                                     {
                                        'PGPORT': '5432', 
                                        'PGHOST': '', 
                                        'DATABASE': '', 
                                        'PGUSER': '',
                                        'PGPASSWORD':''
                                     }
                    filename (str):  backup file name
            Returns:
                    None
    '''
    print("Backing up PostgreSQL ...")

    try:
        if platform.system() != 'Windows':
                process = Popen([f'pg_dump -f {filename} -F tar -w'],
                                shell=True, 
                                env=env
                            )
                process.wait()

        else:
            process = Popen(['pg_dump', '-f', filename, '-F', 'tar', '-w'], 
                            shell=True, 
                            env=env
                        )
            process.wait()

    except Exception as e:
        raise Exception("Backup PostgreSQL FAIL!", e)
    else:
        print("Backed up PostgreSQL! status: 'succeed'")


def restore_postgres(env: dict, filename: str) -> None:
    '''
    Restore PostgreSQL database from .tar file
            Parameters:
                    env      (dict): postgres credential containing
                                    Ex
                                     {
                                        'PGPORT': '5432', 
                                        'PGHOST': '', 
                                        'DATABASE': '', 
                                        'PGUSER': '',
                                        'PGPASSWORD':''
                                     }
                    filename (str): backup file name
            Returns:
                    None
    '''
    print("Restoring PostgreSQL ...")

    try:
        if platform.system() != 'Windows':
            process = Popen([f'pg_restore -C -d bubbletea -f {filename} -F tar'], 
                        shell=True, 
                        env=env
                    )
            process.wait()
        else:
            process = Popen(['pg_restore', '-C', '-d', 'bubbletea', '-f', filename, '-F', 'tar'], 
                        shell=True, 
                        env=env
                    )
            process.wait()
    except Exception as e:
        raise Exception("Restore PostgreSQL FAIL!", e)
    else:
        print("Restored PostgreSQL! status: 'succeed'")
