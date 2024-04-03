#! /bin/bash -x

ZIP=function_with_deps.zip
rm ${ZIP}
cp dependencies.zip ${ZIP}
zip ${ZIP} main.py

aws s3 cp ${ZIP} s3://week10-lambda-zip/

aws lambda update-function-code \
    --region us-east-1 \
    --function-name  demo \
    --s3-bucket week10-lambda-zip \
    --s3-key ${ZIP} | cat

