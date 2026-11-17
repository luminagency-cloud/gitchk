.PHONY: dist test install uninstall clean twine auto-completion

install:
	pip3 install -e .
uninstall:
	pip3 uninstall -e .
test:
	pytest tests --cov=./gitchk $(TEST_ARGS) -n=auto -vv
dist:
	python3 setup.py sdist
twine:
	twine upload dist/*
clean:
	git clean -fdx
auto-completion:
	@ mkdir -p auto-completion/bash
	@ mkdir -p auto-completion/zsh
	@ mkdir -p auto-completion/fish
	register-python-argcomplete gitchk -s bash > auto-completion/bash/.gitchk-completion.bash
	register-python-argcomplete gitchk -s zsh > auto-completion/zsh/_gitchk
	register-python-argcomplete gitchk -s fish > auto-completion/fish/gitchk
