target:
	$(info ${HELP_MESSAGE})
	@exit 0

test-local:
	cdk synth
	sam local invoke -t ./cdk.out/ResourceManager-Shared-Infra.template.json

dev-start:
	poetry shell

dev-end:
	poetry exit

install:
	poetry install

build:
	cdk synth

deploy:
	cdk deploy

define HELP_MESSAGE

	Environment variables to be aware of or to hardcode depending on your use case:

	Common usage:

	...::: Builds and packages all required dependencies in the project :::...
	$ make build
 
endef

# sam local invoke -t <path_to_sam_template_file>