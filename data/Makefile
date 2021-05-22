
SHELL=/bin/bash
UCSC_GENOME=http://hgdownload.cse.ucsc.edu/goldenPath/GENOMEBUILD/chromosomes
REPEATMASKER=http://www.repeatmasker.org/genomes/GENOMEBUILD/RepeatMasker-rm405-db20140131/GENOMEBUILD.fa.out.gz

define get_repmasker
	mkdir -p $(1)
	curl $(subst GENOMEBUILD,$(1),$(REPEATMASKER)) -C - --output $(1)/$(1).fa.out.gz; \
	gzip -c -d $(1)/$(1).fa.out.gz | poetry run parse_rm - > $(1).bed
endef

all: hg19 hg38 mm10/chr2.fa.gz.npz mm10.bed deepgrp_train mm10.chrom.sizes hg19.bed

mm10.bed:
	$(call get_repmasker,mm10)

hg19.bed:
	$(call get_repmasker,hg19)
%.fa.gz:
	mkdir -p $(firstword $(subst /, ,$*))
	curl $(subst GENOMEBUILD,$(firstword $(subst /, ,$*)),$(UCSC_GENOME))/$(lastword $(subst /, ,$*)).fa.gz -C - --output $*.fa.gz

.PRECIOUS: %.fa.gz

%.fa.gz.npz: %.fa.gz
	poetry run preprocess_sequence $*.fa.gz

%.fa: %.fa.gz
	gzip -dfk $<

deepgrp_train: hg19/chr11.fa.gz.npz hg19/chr20.fa.gz.npz

%.chrom.sizes:
	curl https://hgdownload.cse.ucsc.edu/goldenPath/$*/bigZips/$*.chrom.sizes -C - --output $*.chrom.sizes

hg19: hg19/chr1.fa \
		hg19/chr2.fa \
		hg19/chr3.fa \
		hg19/chr4.fa \
		hg19/chr5.fa \
		hg19/chr6.fa \
		hg19/chr7.fa \
		hg19/chr8.fa \
		hg19/chr9.fa \
		hg19/chr10.fa \
		hg19/chr11.fa \
		hg19/chr12.fa \
		hg19/chr13.fa \
		hg19/chr14.fa \
		hg19/chr15.fa \
		hg19/chr16.fa \
		hg19/chr17.fa \
		hg19/chr18.fa \
		hg19/chr19.fa \
		hg19/chr20.fa \
		hg19/chr21.fa \
		hg19/chr22.fa \
		hg19.chrom.sizes


hg38: hg38/chr1.fa \
		hg38/chr2.fa \
		hg38/chr3.fa \
		hg38/chr4.fa \
		hg38/chr5.fa \
		hg38/chr6.fa \
		hg38/chr7.fa \
		hg38/chr8.fa \
		hg38/chr9.fa \
		hg38/chr10.fa \
		hg38/chr11.fa \
		hg38/chr12.fa \
		hg38/chr13.fa \
		hg38/chr14.fa \
		hg38/chr15.fa \
		hg38/chr16.fa \
		hg38/chr17.fa \
		hg38/chr18.fa \
		hg38/chr19.fa \
		hg38/chr20.fa \
		hg38/chr21.fa \
		hg38/chr22.fa \
		hg38.chrom.sizes

.PHONY: hg19 hg38 deepgrp_train clean


clean:
	$(RM) -r hg19/ hg38/ mm10/ *.chrom.sizes *.bed
