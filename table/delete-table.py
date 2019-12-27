#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import re
import sys

sys.path.append('../src')
from aws_utils import rds_execute_statement


def main():
  for path in glob.glob('./sql/*'):
    filename = path.split('/')[-1]

    result = re.match(r'(.+)_table.sql', filename)
    tablename = result.group(1)

    sql = f"DROP TABLE IF EXISTS {tablename}"
    rds_execute_statement(sql)


if __name__ == '__main__':
  main()
