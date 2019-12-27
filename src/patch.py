import json
from aws_utils import rds_execute_statement


def lambda_handler(event, context):

  todo_id = event['pathParameters']['id']
  body = json.loads(event['body'])

  sql = '''
    UPDATE
      todo
    SET
      title = :title, body = :body
    WHERE
      id = :todo_id;
  '''

  params = [
      {
          'name': 'title',
          'value': {
                  'stringValue': f"{body['title']}"
          }
      },
      {
          'name': 'body',
          'value': {
                  'stringValue': f"{body['body']}"
          }
      },
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
