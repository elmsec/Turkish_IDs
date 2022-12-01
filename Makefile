# For the docker users

# $make generate 56739412300
generate:
	docker run -it --rm --name turkish-id -v $(PWD):/usr/src/app -w /usr/src/app python:3 python main.py -g 10 -s $(filter-out $@,$(MAKECMDGOALS))

# $make validate 56739412300
validate:
	docker run -it --rm --name turkish-id -v $(PWD):/usr/src/app -w /usr/src/app python:3 python main.py --validate $(filter-out $@,$(MAKECMDGOALS))
