# -*- coding: future_fstrings -*-
import requests
import sys
import click
sys.path.append('./')
from src.error_codes.error_codes import handle_error
from src.utils.utils import *
from src.base_url.base_url import base_url


@click.command()
def exec_cleanup():
    # use this to get requests

    code, response_dic = response_post()
    print(f"{y}{h} %s{e}" % response_dic['statistics']["deleted_tasks"] + "have been deleted in this operation.")


def response_post():
    this_url = "/api/v1/_manage/cleanup"
    info = {

    }
    response = requests.post(base_url + this_url, json=info)

    if response.status_code != 200:
        handle_error(response.status_code)
        exit(0)
    response_dic = response.json()
    return response.status_code, response_dic


if __name__ == "__main__":
    exec_cleanup()      # pragma: no cover
