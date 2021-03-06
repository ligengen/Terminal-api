# -*- coding: future_fstrings -*-
import requests
import sys
import click
import ast
sys.path.append('./')
from src.error_codes.error_codes import handle_error
from src.utils.utils import *
from src.base_url.base_url import base_url
from src.query_tasks.query import parser


class PythonLiteralOption(click.Option):
    def type_cast_value(self, ctx, value):
        try:
            if value is None:
                return  # pragma: no cover
            return ast.literal_eval(value)
        except BaseException:   # pragma: no cover
            raise click.BadParameter(value)


def process_post(base_url, this_url, info):
    response = requests.post(base_url + this_url, json=info)
    if response.status_code != 200:
        handle_error(response.status_code, launch_task=True)
        exit(0)
    response_dic = response.json()
    return response.status_code, response_dic


@click.command()
@click.option('--task-id-list', help='task id list which you want to launch.', required=True, cls=PythonLiteralOption, type=list)
def batch_del(task_id_list):
    """
    :add 'batch del' for killing tasks in batch.
    :param task_id_list: '["id1", "id2", "id3"]' for example.
    """
    this_url = "/api/v1/task/_delete"
    # new a info and process it afterwards
    info = {
        'tasks': task_id_list
    }
    # use this to post requests
    code, response_dic = process_post(base_url, this_url, info)
    print(f"{g}{h}These tasks are deleted:{e}")
    if response_dic['tasks'] is not []:
        for i in response_dic['tasks']:
            print("   " + i)


@click.command()
@click.option('--task-id-list', help='task id list which you want to launch.', required=True, cls=PythonLiteralOption, type=list)
def batch_kill(task_id_list):
    """
    :add 'batch kill' for killing tasks in batch.
    :param task_id_list: '["id1", "id2", "id3"]' for example.
    """
    this_url = "/api/v1/task/_kill"
    # new a info and process it afterwards
    info = {
        'tasks': task_id_list
    }
    code, response_dic = process_post(base_url, this_url, info)
    print(f"{g}{h}These tasks are killed:{e}")
    if response_dic['tasks'] is not []:
        for i in response_dic['tasks']:
            if i is not None:
                pass  # TODO add according to backend


@click.command()
@click.option('--task-id-list', help='task id list which you want to launch.', required=True, cls=PythonLiteralOption, type=list)
def batch_query(task_id_list):
    """
    :add 'batch query' for querying tasks.
    :param task_id_list: '["id1", "id2", "id3"]' for example.
    """
    this_url = "/api/v1/task/_get"
    # new a info and process it afterwards
    info = {
        'tasks': task_id_list
    }
    code, response_dic = process_post(base_url, this_url, info)
    print(f"{g}{h}Document of tasks are listed as follows:{e}")
    if response_dic['tasks'] is not []:
        for i in response_dic['tasks']:
            parser(i, mode='single')
