#! /bin/bash -x


stack_name=RDS
bucket=week10-lambda-zip
DBUsername=admin
DBPassword=123123123

aws cloudformation describe-stacks --stack-name ${stack_name} --region us-east-1 &>/dev/null
exist=$?

if [ ${exist} -ne 0 ]
then
  aws s3 cp rds.yml s3://${bucket}/
  template_url=https://${bucket}.s3.amazonaws.com/rds.yml
  echo "create stack"

  #    --role-arn ${role_arn} \ # I will use my root credential
  aws cloudformation create-stack \
    --stack-name ${stack_name} \
    --template-url  ${template_url}\
    --region us-east-1 \
    --parameters ParameterKey=DBUsername,ParameterValue=${DBUsername} \
                 ParameterKey=DBPassword,ParameterValue=${DBPassword}
fi

