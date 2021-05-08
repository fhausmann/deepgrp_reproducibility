
all: hg38.dfam.bed running_time.csv

hg38_dfam.nrph.hits.gz:
	curl -o hg38_dfam.nrph.hits.gz https://dfam.org/releases/Dfam_3.3/annotations/hg38/hg38_dfam.nrph.hits.gz

hg38.dfam.bed: hg38_dfam.nrph.hits.gz
	poetry run ./dfam_to_repeatmasker.py

Dfam.hmm:
	curl -o Dfam.hmm.gz https://dfam.org/releases/current/families/Dfam.hmm.gz
	gzip -dk Dfam.hmm.gz

hmmer-3.3.2.tar.gz:
	curl -o hmmer-3.3.2.tar.gz http://eddylab.org/software/hmmer/hmmer-3.3.2.tar.gz

hmmer/configure: hmmer-3.3.2.tar.gz
	mkdir -p hmmer/ && tar -xzf hmmer-3.3.2.tar.gz -C hmmer/ --strip-components 1

hmmer/Makefile: hmmer/configure
	cd hmmer/ && ./configure --prefix ${PWD}

bin/phmmer: hmmer/Makefile
	make -C hmmer/
	make -C hmmer check
	make -C hmmer install

dfamscan.pl.gz:
	curl -o dfamscan.pl.gz https://dfam.org/releases/current/infrastructure/dfamscan.pl.gz

dfamscan.pl: dfamscan.pl.gz
	gzip -dk dfamscan.pl.gz
	chmod +x dfamscan.pl

Dfam_hg38.hmm: Dfam.hmm
	poetry run ./filter_hmm.py Dfam.hmm ../repeats.json Dfam_hg38.hmm -v

../data/%.fa:
	${MAKE} -C .. ../data/$*.fa

%.hmm.h3f: bin/phmmer %.hmm
	./bin/hmmpress $*.hmm

outputs/%.fa.DfamHits.out: ../data/%.fa Dfam_hg38.hmm.h3f
	mkdir -p outputs/${dir $*}
	@./run_linux.sh ../data/$*.fa

protocol_linux.txt: outputs/hg19/chr18.fa.DfamHits.out \
		outputs/hg19/chr19.fa.DfamHits.out \
		outputs/hg19/chr20.fa.DfamHits.out \
		outputs/hg19/chr21.fa.DfamHits.out \
		outputs/hg19/chr22.fa.DfamHits.out

running_time.csv: #protocol_linux.txt
	@poetry run ../repeatmasker/get_results.py protocol_linux.txt
