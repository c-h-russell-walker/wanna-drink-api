# wanna-drink-api
API for WannaDrink WebApp

## Pre-reqs - be sure to have 'virtualenv' available form the command line:
`virtualenv --version`
If not install using:
`pip install virtualenv`

1. Clone repo.
2. CD into repo directory.
3. Run (to note the 'wanna' virtualenv name is ignored in .gitignore):
```
virtualenv wanna
source wanna/bin/activate
```

## To install requirements:
(inside VM)
`pip install -r requirements.txt` OR `pip install -r requirements_dev.txt`

## To run:
In virtualenv (wanna) run:
`python run.py`
(To be in virtualenv run `source wanna/bin/activate` in the repo dir.)
