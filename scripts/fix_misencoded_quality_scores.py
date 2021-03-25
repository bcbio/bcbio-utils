"""
When reprocessing old sequencing data sometimes 
there are bam with misencoded quality scores.
It is not Illumina PHRED+64 scale, 
but just some characters are outside of the allowed set.

https://support.illumina.com/help/BaseSpace_OLH_009008/Content/Source/Informatics/BS/QualityScoreEncoding_swBS.htm
samtools view -h file.bam | python fix.py | samtools view -b - > file_fixed.bam

even when fixed, such bams break picard, so to process them in bcbio:
- use the original reference (GRCh37), don't try to recode
- don't use bam_clean: picard
- tools_off: collectsequencingartifacts
"""

import sys

allowed=set(r"""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJ""")

def broken_tag(x):
    parts = x.split(":")
    return len(parts) != 3 or parts[1] not in ["i", "Z"]

for line in sys.stdin:
    if not line.startswith("@"):
        parts = line.split("\t")
        if len(parts) < 11 or not parts[-1].startswith(("MD:", "RG:")) or any(broken_tag(x) for x in parts[11:]):
            sys.stderr.write("Problem line, skipping %s\n" % line)
            continue
        qual = set(parts[10])
        if qual - allowed or len(parts[9]) != len(parts[10]):
            new_qual = [(x if x in allowed else "I") for x in parts[10]]
            if len(new_qual) != len(parts[9]):
                sys.stderr.write("Problem line, subbing qscores %s\n" % line)
                new_qual = ["I"] * len(parts[9])
            parts[10] = "".join(new_qual)
            assert len(parts[10]) == len(parts[9]), (len(line.split("\t")[9]), len(line.split("\t")[10]), len(new_qual))
            line = "\t".join(parts)
    sys.stdout.write(line)
