import click
from lib.setting import get_postgres_credential
from lib.postgres import backup_postgres, restore_postgres


@click.group()
def main():
    pass

@main.command()
@click.option('--backup_file', '-f', default='backup.tar', help='Your backup file name')
def backup(backup_file: str):
    env = get_postgres_credential()
    backup_postgres(env, backup_file)

@main.command()
@click.option('--backup_file', '-f', default='backup.tar', help='Your backup file name')
def restore(backup_file: str):
    env = get_postgres_credential()
    restore_postgres(env, backup_file)
    

if __name__ == '__main__':
    main()
