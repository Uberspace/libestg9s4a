
.PHONY: lint
lint:
	pylava libestg9s4a test
	isort --recursive --check-only libestg9s4a test

.PHONY: fixlint
fixlint:
	isort --recursive libestg3b test

.PHONY: test
test:
	tox
