NAME = tgmeetup
OS = $(shell uname -s)

help:
	@echo '    install'
	@echo '    To install setup.py.'
	@echo '    clean'
	@echo '    To clean up .pyc , .pyo, events.json.'

all: clean python

clean:
	rm -f **/*.pyc
	rm -f **/*.pyo
	du -a community conference | grep events.json | awk '{print $2}' | xargs rm
	@echo "Cleaning up .pyc , .pyo, events.json"

install:
	sudo python setup.py install

run:
	tgmeetup
