# backup-and-restore-postgres-python
This repository helps you in backing up and restoring your Postgresql database

## Setup dependencies
```
pip install pipenv
```
```
pipenv install
```

## Setup postgres config
- Setup your postgres credential in `config/potgres.yaml`

## How to run backup
Flag:   
`-f`: Backup file (recommend stored in .tar format)  
```
pipenv run python main.py backup -f "backup.tar" 
```

## How to run restore
Flag:   
`-f`: Backup file that you want to restore your postgres (recommend stored in .tar format)  
```
pipenv run python main.py restore -f "backup.tar" 
```
