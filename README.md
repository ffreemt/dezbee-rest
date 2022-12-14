# dezbee-rest
[![pytest](https://github.com/ffreemt/dezbee-rest/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/dezbee-rest/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/dezrest.svg)](https://badge.fury.io/py/dezrest)

Serve [de|ez|dz]bee via FastAPI port 6666

## python 3.8 only


## Install it

### For Windows
```shell
pip install dezrest
# pip install git+https://github.com/ffreemt/dezbee-rest
# poetry add git+https://github.com/ffreemt/dezbee-rest
# git clone https://github.com/ffreemt/dezbee-rest && cd dezbee-rest
```

### For Linux and friends
The `fasttext`, `pycld2` and `pyicu` can be installed normally. Clone the repo, run
```
poetry export -f requirements.text -o requirements.txt
```
and replace the whl for `fasttext`, `pycld2` and `pyicu`

## Use it

```bash
# sart the server at port 5555 via `uvicorn` with 2 workers
python -m dezrest

# docs
http://127.0.0.1:5555/docs
```
