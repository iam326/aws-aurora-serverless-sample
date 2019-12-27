import json
from aws_utils import rds_execute_statement


def lambda_handler(event, context):

  todo_id = event['pathParameters']['id']

  sql = '''
    DELETE FROM todo WHERE id = :todo_id;
  '''

  params = [
      {
          'name': 'todo_id',
          'value': {
                  'longValue': int(todo_id)
          }
      }
  ]

  res = rds_execute_statement(sql, params)

  return {
      "statusCode": 200,
      "body": json.dumps(res),
  }
