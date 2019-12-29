#!/bin/bash

set -euo pipefail

readonly STACK_NAME="aws-aurora-serverless-sample"
readonly BUCKET_NAME="iam326.${STACK_NAME}"

readonly NAME_PREFIX="aws-aurora-sl-sample"
readonly DATABASE_CLUSTER_NAME="${NAME_PREFIX}-database-cluster"

# execute only the first time
# aws s3 mb "s3://${BUCKET_NAME}"

sam build

sam package \
  --output-template-file packaged.yaml \
  --s3-bucket ${BUCKET_NAME}

sam deploy \
  --template-file packaged.yaml \
  --stack-name ${STACK_NAME} \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides \
    NamePrefix=${NAME_PREFIX} \
    DatabaseClusterName=${DATABASE_CLUSTER_NAME}

rm packaged.yaml

aws rds modify-db-cluster \
  --db-cluster-identifier ${DATABASE_CLUSTER_NAME} \
  --enable-http-endpoint \
  --apply-immediately
