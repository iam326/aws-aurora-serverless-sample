#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import sys

sys.path.append('../src')
from aws_utils import rds_execute_statement


def main():
  for path in glob.glob('./sql/*'):
    with open(path, 'r') as table:
      sql = table.read()
      rds_execute_statement(sql)


if __name__ == '__main__':
  main()
