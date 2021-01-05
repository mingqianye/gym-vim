# To install Neovim, run `sudo apt-get install python3-neovim`

test:
	python3 -m unittest
twine:
	python3 setup.py sdist bdist_wheel && python3 -m twine upload dist/*
