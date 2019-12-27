#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
from boto3.session import Session

session = Session(region_name='ap-northeast-1')
rds = boto3.client('rds-data')
cfn = boto3.resource('cloudformation')

stack = cfn.Stack('aws-aurora-serverless-sample')


def get_cfn_output(key, outputs):
  result = [v['OutputValue'] for v in outputs if v['OutputKey'] == key]
  return result[0] if len(result) > 0 else ''


database_name = get_cfn_output('DatabaseName', stack.outputs)
db_cluster_arn = get_cfn_output('DatabaseClusterArn', stack.outputs)
db_credentials_secrets_store_arn = get_cfn_output(
    'DatabaseSecretArn', stack.outputs)


def formatField(field):
  return list(field.values())[0]


def formatRecord(record):
  return [formatField(field) for field in record]


def formatRecords(meta, records):
  keys = [item['name'] for item in meta]
  return [dict(zip(keys, formatRecord(record))) for record in records]


def rds_execute_statement(sql, parameters=[]):
  response = rds.execute_statement(
      secretArn=db_credentials_secrets_store_arn,
      database=database_name,
      resourceArn=db_cluster_arn,
      includeResultMetadata=True,
      sql=sql,
      parameters=parameters
  )

  if 'columnMetadata' in response and 'records' in response:
    response = formatRecords(response['columnMetadata'], response['records'])

  return response
