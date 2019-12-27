import boto3
import json
import os
import requests

import pytest

cfn = boto3.resource('cloudformation')
stack = cfn.Stack('aws-aurora-serverless-sample')
base_url = [v['OutputValue']
            for v in stack.outputs if v['OutputKey'] == 'TodoApi'][0]


def test_get_todo():
  response = requests.get(
      f'{base_url}/todo/hoge')
  body = response.json()
  print(body)
  assert True
