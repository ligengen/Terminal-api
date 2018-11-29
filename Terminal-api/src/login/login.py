# -*- coding: future_fstrings -*-
import requests
import sys
import click
sys.path.append('./')
from src.error_codes.error_codes import handle_error
from src.utils.utils import *
from src.base_url.base_url import base_url


@click.command()
@click.option('--usr-name', required=True)
@click.option('--password', required=True)
@click.option('--remember', type=bool, required=True)
def login(usr_name, password, remember):
    # use this to get requests
    this_url = "/api/v1/auth/_login"
    info = {
        'login': usr_name,
        'password': password,
        'remember': remember
    }
    response_dic = post(this_url, info)[1]
    print(response_dic['profile'])


def post(this_url, info):
    response = requests.post(base_url + this_url, json=info)

    if response.status_code != 200:
        handle_error(response.status_code)
        exit(0)
    response_dic = response.json()
    return response.status_code, response_dic


if __name__ == "__main__":
    login()     # pragma: no cover
