import boto3
import json
import os
import requests

import pytest

cfn = boto3.resource('cloudformation')
stack = cfn.Stack('aws-aurora-serverless-sample')
base_url = [v['OutputValue']
            for v in stack.outputs if v['OutputKey'] == 'TodoApi'][0]

todo_id = None


def test_post_todo():
  data = json.dumps({
      'date': '2019-12-25',
      'title': 'dummy_title',
      'body': 'dummy_body'
  }).encode('utf-8')

  response = requests.post(
      f'{base_url}/todo', data=data)
  body = response.json()
  print(body)

  global todo_id
  todo_id = body['generatedFields'][0]['longValue']

  assert True


def test_get_todo():
  response = requests.get(
      f'{base_url}/todo/{todo_id}')
  body = response.json()
  print(body)

  assert True


def test_patch_todo():
  data = json.dumps({
      'title': 'patched_title',
      'body': 'patched_body'
  }).encode('utf-8')

  response = requests.patch(
      f'{base_url}/todo/{todo_id}', data=data)
  body = response.json()
  print(body)

  response = requests.get(
      f'{base_url}/todo/{todo_id}')
  body = response.json()
  print(body)

  assert True


def test_delete_todo():
  response = requests.delete(
      f'{base_url}/todo/{todo_id}')
  body = response.json()
  print(body)

  response = requests.get(
      f'{base_url}/todo/{todo_id}')
  body = response.json()
  print(body)

  assert True
