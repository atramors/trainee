PACK_VERSION=$(shell aws s3api list-object-versions --bucket newbucket666 --prefix cwmat --query 'Versions[?IsLatest].[VersionId]' --output text)
deploy: 
	aws cloudformation deploy --template-file ~/Desktop/intern/tmplate.yml \
	--stack-name mystack --capabilities CAPABILITY_IAM \
	--parameter-overrides \
	 PackVersion=$(PACK_VERSION)

