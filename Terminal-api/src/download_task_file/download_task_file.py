# -*- coding: future_fstrings -*-
import requests
import sys
import click
sys.path.append('./')
from src.error_codes.error_codes import handle_error
from src.utils.utils import *
from src.base_url.base_url import base_url
from src.download_file.download_file import save_file


@click.command()
@click.option('--task-id', type=str, help='which task', required=True)
@click.option('--format', help='The format of the archive', required=True, type=click.Choice(['zip', 'tar', 'tar.gz']))
def download_task_file(task_id, format):
    # use this to get requests

    response = response_get(task_id, format)
    # TODO add response.headers['Content-Type'] to the filename
    filename = save_file('archive' + format, response)
    print(f"{g}{h}Download successfully! Your file location: {e}%s" % ('./download/%s' % filename))


def response_get(task_id, format):
    this_url = "/api/v1/task/_download/%s.%s" % (task_id, format)
    response = requests.get(base_url + this_url, stream=True)
    if response.status_code != 200:
        handle_error(response.status_code, download_file=True)
        exit(0)
    return response


if __name__ == "__main__":
    download_task_file()    # pragma: no cover
