/local2/nlapier2/metalign/tools/Bracken/bracken -d /local2/nlapier2/metalign/tools/kraken2/full_database/ -i timing/results/kraken2_report_fastq_version.txt -o timing/results/bracken_domain_level_fastq_version.txt -l D
/local2/nlapier2/metalign/tools/Bracken/bracken -d /local2/nlapier2/metalign/tools/kraken2/full_database/ -i timing/results/kraken2_report_fastq_version.txt -o timing/results/bracken_phylum_level_fastq_version.txt -l P
/local2/nlapier2/metalign/tools/Bracken/bracken -d /local2/nlapier2/metalign/tools/kraken2/full_database/ -i timing/results/kraken2_report_fastq_version.txt -o timing/results/bracken_class_level_fastq_version.txt -l C
/local2/nlapier2/metalign/tools/Bracken/bracken -d /local2/nlapier2/metalign/tools/kraken2/full_database/ -i timing/results/kraken2_report_fastq_version.txt -o timing/results/bracken_order_level_fastq_version.txt -l O
/local2/nlapier2/metalign/tools/Bracken/bracken -d /local2/nlapier2/metalign/tools/kraken2/full_database/ -i timing/results/kraken2_report_fastq_version.txt -o timing/results/bracken_family_level_fastq_version.txt -l F
/local2/nlapier2/metalign/tools/Bracken/bracken -d /local2/nlapier2/metalign/tools/kraken2/full_database/ -i timing/results/kraken2_report_fastq_version.txt -o timing/results/bracken_genus_level_fastq_version.txt -l G
/local2/nlapier2/metalign/tools/Bracken/bracken -d /local2/nlapier2/metalign/tools/kraken2/full_database/ -i timing/results/kraken2_report_fastq_version.txt -o timing/results/bracken_species_level_fastq_version.txt -l S
cat timing/results/bracken_domain_level_fastq_version.txt timing/results/bracken_phylum_level_fastq_version.txt timing/results/bracken_class_level_fastq_version.txt timing/results/bracken_order_level_fastq_version.txt timing/results/bracken_family_level_fastq_version.txt timing/results/bracken_genus_level_fastq_version.txt timing/results/bracken_species_level_fastq_version.txt > timing/results/bracken_results_fastq_version.txt
rm timing/results/bracken_domain_level_fastq_version.txt timing/results/bracken_phylum_level_fastq_version.txt timing/results/bracken_class_level_fastq_version.txt timing/results/bracken_order_level_fastq_version.txt timing/results/bracken_family_level_fastq_version.txt timing/results/bracken_genus_level_fastq_version.txt timing/results/bracken_species_level_fastq_version.txt
