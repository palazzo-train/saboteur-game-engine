# saboteur-game-engine

## Deploy to AWS serverless by VS Code + AWS SAM plug

1. In vscode, ctrl-shift-P
2. type : `AWS: create new SAMP Application`
    This will generate a template [folder](https://github.com/palazzo-train/saboteur-game-engine/tree/master/doc/aws-template-saboteur-game-engine)
3. Copy the template.yml
4. modify the template.yml
5. change the hander to hander object of [magnum](https://github.com/palazzo-train/saboteur-game-engine/blob/3aec2cf7333dbf13c4898c7e6cb8910ef1898cc4/template.yaml#L18)
6. In vscode, ctrl-shift-P
7. type : `AWS: Deploy`


### Quick help

#### VS Code, ctrl-shift-P
`AWS: View AWS Toolkit Logs`

#### SAM Errors
[ValidationError Stack:arn aws cloudformation stack is in ROLLBACK_COMPLETE state and can not be updated](https://stackoverflow.com/questions/57932734/validationerror-stackarn-aws-cloudformation-stack-is-in-rollback-complete-state)  
`Unzipped size must be smaller than 262144000 bytes (Service: AWSLambdaInternal; Status Code: 400; Error Code: InvalidParameterValueException; Request ID: 4a0e9e6a-bdcb-4393-bf93-e1f192edcb24; Proxy: null)`  
