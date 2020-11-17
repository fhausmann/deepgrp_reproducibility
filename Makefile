SHELL=/bin/bash
DATADIR=./data

UCSC_GENOME=http://hgdownload.cse.ucsc.edu/goldenPath/GENOMEBUILD/chromosomes
REPEATMASKER=http://www.repeatmasker.org/genomes/GENOMEBUILD/RepeatMasker-rm405-db20140131/GENOMEBUILD.fa.out.gz

GENOMEBUILD ?= hg19
TRAIN_CHR ?= chr11
VAL_CHR ?= chr20



define get_fasta
	curl $(subst GENOMEBUILD,$(1),$(UCSC_GENOME))/$(2).fa.gz -C - --output $(DATADIR)/$(1)/$(2).fa.gz; \
	preprocess_sequence $(DATADIR)/$(1)/$(2).fa.gz; \
	gzip -dfk $(DATADIR)/$(1)/$(2).fa.gz
endef

define get_repmasker
	mkdir -p $(DATADIR)/$(1)
	curl $(subst GENOMEBUILD,$(1),$(REPEATMASKER)) -C - --output $(DATADIR)/$(1)/$(1).fa.out.gz; \
	gzip -c -d $(DATADIR)/$(1)/$(1).fa.out.gz | parse_rm - > $(DATADIR)/$(1).bed
endef

all: traindata testdata dna-brnn all_hg19
	mkdir -p ./figures

$(DATADIR)/%.bed:
	$(call get_repmasker,$*)

traindata: $(DATADIR)/$(GENOMEBUILD).bed
	$(call get_fasta,$(GENOMEBUILD),$(TRAIN_CHR))
	$(call get_fasta,$(GENOMEBUILD),$(VAL_CHR))

testdata: test-hg19 test-hg38 test-mm10

test-hg19:
	$(call get_fasta,hg19,chr1)

test-hg38: $(DATADIR)/hg38.bed
	$(call get_fasta,hg38,chr1)

test-mm10: $(DATADIR)/mm10.bed
	$(call get_fasta,mm10,chr2)

dna-brnn:
	-git clone https://github.com/lh3/dna-nn
	$(MAKE) -C dna-nn

.PHONY: all_hg19 clean

all_hg19:
	mkdir -p $(DATADIR)/$(GENOMEBUILD)
	number=1 ; while [[ $$number -le 22 ]] ; \
	do $(call get_fasta,$(GENOMEBUILD),chr$$number); \
	((number = number + 1)); \
	done

clean:
	$(RM) -rf $(DATADIR)
	$(RM) -rf ./figures
