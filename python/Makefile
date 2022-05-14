ARTIFACTS_DIR := artifacts
ZIP_FILE_NAME := lambda
LAMBDA_FUNCTION_NAME := utility-costs-notifier
ARTIFACTS_KEY := utility-costs-notifier

deploy:
	mkdir -p $(ARTIFACTS_DIR)
	cp lambda_function.py $(ARTIFACTS_DIR)
	cp tokyo_gas.py $(ARTIFACTS_DIR)
	cp tokyo_suido.py $(ARTIFACTS_DIR)
	cp next_power.py $(ARTIFACTS_DIR)
	curl -SL https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip > chromedriver.zip
	unzip -o chromedriver.zip -d $(ARTIFACTS_DIR)
	rm -f chromedriver.zip
	pip install -r requirements.txt -t $(ARTIFACTS_DIR)
	cd $(ARTIFACTS_DIR) && zip $(ZIP_FILE_NAME) -r .
	aws s3 cp $(ARTIFACTS_DIR)/$(ZIP_FILE_NAME).zip s3://${ARTIFACTS_BUCKET}/${ARTIFACTS_KEY}/$(ZIP_FILE_NAME).zip
	aws lambda update-function-code --function-name $(LAMBDA_FUNCTION_NAME) --s3-bucket ${ARTIFACTS_BUCKET} --s3-key $(ARTIFACTS_KEY)/$(ZIP_FILE_NAME).zip
