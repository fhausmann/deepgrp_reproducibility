SHELL=/bin/bash

all: dna-nn/dna-brnn
	make -C data all
	mkdir -p ./figures
	$(MAKE) -C dfam
	$(MAKE) -C repeatmasker

dna-nn/dna-brnn:
	$(MAKE) -C dna-nn

.PHONY: clean

clean:
	$(RM) -rf ./figures
	$(MAKE) -C data clean
	$(MAKE) -C dna-nn clean
