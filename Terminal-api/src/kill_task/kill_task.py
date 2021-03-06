# -*- coding: future_fstrings -*-
import requests
import sys
import click
sys.path.append('./')
from src.error_codes.error_codes import handle_error
from src.utils.utils import *
from src.base_url.base_url import base_url


@click.command()
@click.option('--task-id', help='task id which you want to launch.', required=True)
def kill_task(task_id):
    """
    :add 'kill task' for killing a task.
    """
    response_post(task_id)
    print(f"{y}{h}You have been successfully killed task %s{e}" % task_id)


def response_post(task_id):
    this_url = "/api/v1/task/%s/_kill" % task_id
    # new a info and process it afterwards
    info = {

    }
    # use this to post requests
    response = requests.post(base_url + this_url, json=info)
    if response.status_code != 200:
        handle_error(response.status_code, launch_task=True)
        exit(0)
    return response.status_code, response.json()


if __name__ == '__main__':
    kill_task()     # pragma: no cover
