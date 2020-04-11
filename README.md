Helper scripts for [bcbio-nextgen](https://github.com/bcbio/bcbio-nextgen)

Requirements: Git, Conda

To install:
```shell
git clone git@github.com:bcbio/bcbio-utils.git
conda env create --name bcbio-utils --file bcbio-utils/environment.yml
```
If you would like to use CWL scripts you will need to install `cwltool` separately:
```shell
conda activate bcbio-utils
pip install cwltool
```

Scripts:
* `analyze_complexity_by_starts.py` - create reads sequenced vs unique start sites graph for examining the quality of a library
* `analyze_quality_recal.py` - provide plots summarizing recalibration of quality scores
* `bam_to_fastq_region.py` - prepare paired end fastq files from a chromosome region in an aligned input BAM file
* `bam_to_wiggle.py` - convert BAM files to BigWig file format in a specified region
* `bcbio_prep_cwl_genomes.py` - clean and prepare a set of genomes for CWL usage and upload
* `broad_redo_analysis.py` - redo post-processing of Broad alignments with updated pipeline
* `build_compare_vcf.py` - build a test comparison dataset from an existing VCF file
* `build_gatk_jar.sh` - build a GATK jar without embedded dependencies from current git
* `cg_svevents_to_vcf.py` - convert Complete Genomics SvEvents file of structural variants to VCF
* `collect_metrics_to_csv.py` - collect alignment summary metrics from multiple lanes and summarize as CSV
* `convert_samplesheet_config.py` - convert Illumina SampleSheet CSV files to the run_info.yaml input file
* `find_clonal_svs.py` - find 10x structural variants present uniquely in parent or clones
* `format_dream_truthset.py` - format DREAM challenge truth sets to contain BED files of covered regions and SVs
* `gb2genome.py` - convert genbank to gtf
* `hla_loh_comparison.py` - run LOH heterogeneity comparison amongst multiple methods, focusing on HLA
* `hlas_to_pgroups.py` - collapse HLAs present in hg38 1000 genomes distribution to p-groups
* `hydra_to_vcf.py` - convert Hydra BEDPE output into VCF 4.1 format
* `monthly_billing_report.py` - retrieve from Galaxy a high level summary report of sequencing done in a month
* `plink_to_vcf.py` - convert Plink ped/map files into VCF format using plink and Plink/SEQ
* `rename_samples.py` - rename sample name in a BAM file, eliminating spaces and colon characters
* `resort_bam_karyotype.py` - resort a BAM file karyotypically to match GATK's preferred file order
* `rtg_to_callable.py` - convert RTG coverage statistics into a BED file of callable regions
* `sort_gatk_intervals.py` - sort GATK interval lists based on a sequence dictionary
* `summarize_gemini_tstv.py` - provide table summarizing Transition/Transversion ratios for variants
* `summarize_priority_variants.py` - summarize priority calls in annotated structural variants
* `summarize_timing.py` - convert time stamps from bcbio logs into hourly timings per step
* `tcga_to_bcbio.py` - handle pairing primary and metastasized tumors with blood or solid normals
* `test_resources.py` - ?
* `upload_to_synapse.py` - upload bcbio reference materials and inputs to a Synapse project
