SHELL=/bin/bash

all: dna-nn/dna-brnn
	make -C data all
	mkdir -p ./figures
	$(MAKE) -C dfam
	$(MAKE) -C repeatmasker

submodules:
	git submodule init
	git submodule update

dna-nn/dna-brnn.c: submodules

repeatmasker/RepeatMasker/RepeatMasker: submodules

dna-nn/dna-brnn: dna-nn/dna-brnn.c
	$(MAKE) -C dna-nn

.PHONY: clean submodules

clean:
	$(RM) -rf ./figures
	$(MAKE) -C data clean
	$(MAKE) -C dna-nn clean
