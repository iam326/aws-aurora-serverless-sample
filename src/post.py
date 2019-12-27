import json
from aws_utils import rds_execute_statement


def lambda_handler(event, context):

  body = json.loads(event['body'])

  sql = '''
    INSERT INTO todo
      (`date`, `title`, `body`)
    VALUES
      (:date, :title, :body);
  '''

  params = [
      {
          'name': 'date',
          'value': {
                  'stringValue': f"{body['date']}"
          }
      },
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
      }
  ]

  res = rds_execute_statement(sql, params)

  return {
      "statusCode": 200,
      "body": json.dumps(res),
  }
