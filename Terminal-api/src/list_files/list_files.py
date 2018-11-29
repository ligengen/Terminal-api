# -*- coding: future_fstrings -*-
import requests
import sys
import click
sys.path.append('./')
from src.error_codes.error_codes import handle_error
from src.utils.utils import *
from src.base_url.base_url import base_url


@click.command()
@click.option('--task-id', type=str, help='which task', required=True)
@click.option('--path', help='the directory of the files')
def list_files(task_id, path):
    """
    :add 'list files' for listing files under given directory
    :param task_id: '--task-id 0' for example
    :param path: 'optional, string containing slashes ("/")' (relative to the root working directory)
                If not specified, list the root working directory.
    """
    # use this to get requests
    code, response_dic = list_files_call(task_id, path)

    print(f"{b}{h}Files of the specified directory is listed as follows: {e}")
    print(f"{y}{h}  relative path of the queried directory: {e}" + (response_dic['path'] if path is not None else './'))
    print(f"{y}{h}  entities: {e}")
    for entity in response_dic['entities']:
        print(f"{g}{h}    name: {e}" + entity['name'])
        print(f"{g}{h}    the UTC modify time: {e}" + entity['mtime'])
        if "isdir" in entity:
            print(f"{g}{h}    isdir: {e}" + str(entity['isdir']))
        print(f"{g}{h}    size in bytes: {e}" + str(entity['size']))


def list_files_call(taskid, path):
    if path is not None:
        url = base_url + "/api/v1/task/%s/_listdir/%s" % (taskid, path)
    else:
        url = base_url + "/api/v1/task/%s/_listdir/" % taskid
    response = requests.get(url)
    if response.status_code != 200:
        handle_error(response.status_code)
        exit(0)
    response_dic = response.json()
    return response.status_code, response_dic


if __name__ == "__main__":
    list_files()    # pragma: no cover
