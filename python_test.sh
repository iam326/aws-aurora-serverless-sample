#!/bin/bash

set -euo pipefail

python -m pytest tests/api/ -v -s
