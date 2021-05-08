all:
	cat README.txt

humrep.lib: humrep.fa
	poetry run ./create_repeatmasker_lib.py humrep.fa humrep.lib --repeatclass ../repeats.json

humrep.fa: humrep.ref
	poetry run ./embl_to_fasta.py humrep.ref humrep.fa --filter ../repeats.json

../data/%.fa:
	${MAKE} -C .. data/$*.fa

outputs/%.fa.out: ../data/%.fa repeatmasker
	@./run_linux.sh ../data/$*.fa
	mkdir -p outputs/${dir $*}
	-mv ../data/$*.fa.log outputs/${dir $*}
	-mv ../data/$*.fa.cat.gz outputs/${dir $*}
	-mv ../data/$*.fa.tbl outputs/${dir $*}
	mv ../data/$*.fa.out outputs/${dir $*}

protocol_linux.txt: ../data/hg19/chr1.fa \
					../data/hg19/chr2.fa \
					../data/hg19/chr3.fa \
					../data/hg19/chr4.fa \
					../data/hg19/chr5.fa \
					../data/hg19/chr6.fa \
					../data/hg19/chr7.fa \
					../data/hg19/chr8.fa \
					../data/hg19/chr9.fa \
					../data/hg19/chr10.fa \
					../data/hg19/chr11.fa \
					../data/hg19/chr12.fa \
					../data/hg19/chr13.fa \
					../data/hg19/chr14.fa \
					../data/hg19/chr15.fa \
					../data/hg19/chr16.fa \
					../data/hg19/chr17.fa \
					../data/hg19/chr18.fa \
					../data/hg19/chr19.fa \
					../data/hg19/chr20.fa \
					../data/hg19/chr21.fa \
					../data/hg19/chr22.fa \
					../data/hg38/chr1.fa
	@./run_linux.sh $^

running_time.csv: protocol_linux.txt
	@poetry run ./get_results.py protocol_linux.txt

repeats_hg38.tsv: outputs/hg38/chr1.fa.out \
				outputs/hg38/chr2.fa.out \
				outputs/hg38/chr3.fa.out \
				outputs/hg38/chr4.fa.out \
				outputs/hg38/chr5.fa.out \
				outputs/hg38/chr6.fa.out \
				outputs/hg38/chr7.fa.out \
				outputs/hg38/chr8.fa.out \
				outputs/hg38/chr9.fa.out \
				outputs/hg38/chr10.fa.out \
				outputs/hg38/chr11.fa.out \
				outputs/hg38/chr12.fa.out \
				outputs/hg38/chr12.fa.out \
				outputs/hg38/chr13.fa.out \
				outputs/hg38/chr14.fa.out \
				outputs/hg38/chr15.fa.out \
				outputs/hg38/chr16.fa.out \
				outputs/hg38/chr17.fa.out \
				outputs/hg38/chr18.fa.out \
				outputs/hg38/chr19.fa.out \
				outputs/hg38/chr20.fa.out \
				outputs/hg38/chr21.fa.out \
				outputs/hg38/chr22.fa.out
        ./repeatmasker_to_deepgrp.py --outfile repeats_hg38.tsv $^

repeats_hg19.tsv: outputs/hg19/chr1.fa.out \
				outputs/hg19/chr2.fa.out \
				outputs/hg19/chr3.fa.out \
				outputs/hg19/chr4.fa.out \
				outputs/hg19/chr5.fa.out \
				outputs/hg19/chr6.fa.out \
				outputs/hg19/chr7.fa.out \
				outputs/hg19/chr8.fa.out \
				outputs/hg19/chr9.fa.out \
				outputs/hg19/chr10.fa.out \
				outputs/hg19/chr11.fa.out \
				outputs/hg19/chr12.fa.out \
				outputs/hg19/chr12.fa.out \
				outputs/hg19/chr13.fa.out \
				outputs/hg19/chr14.fa.out \
				outputs/hg19/chr15.fa.out \
				outputs/hg19/chr16.fa.out \
				outputs/hg19/chr17.fa.out \
				outputs/hg19/chr18.fa.out \
				outputs/hg19/chr19.fa.out \
				outputs/hg19/chr20.fa.out \
				outputs/hg19/chr21.fa.out \
				outputs/hg19/chr22.fa.out
        ./repeatmasker_to_deepgrp.py --outfile repeats_hg19.tsv $^
