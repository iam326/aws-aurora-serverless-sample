#!/bin/bash

set -euo pipefail

readonly STACK_NAME="aws-aurora-serverless-sample"
readonly BUCKET_NAME="iam326.${STACK_NAME}"

# execute only the first time
# aws s3 mb "s3://${BUCKET_NAME}"

sam build

sam package \
  --output-template-file packaged.yaml \
  --s3-bucket ${BUCKET_NAME}

sam deploy \
  --template-file packaged.yaml \
  --stack-name ${STACK_NAME} \
  --capabilities CAPABILITY_IAM

rm packaged.yaml
