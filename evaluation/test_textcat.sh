#!/bin/bash

#SBATCH --job-name=train         # Job name
#SBATCH --output=job.%j.out      # Name of output file (%j expands to jobId)
#SBATCH --cpus-per-task=1        # Schedule one core
#SBATCH --time=05:00:00          # Run time (hh:mm:ss) - run for one hour max
#SBATCH --partition=scavenge    # Run on scavenge queue
#SBATCH --mail-type=END          # Send an email when the job finishes
#SBATCH --mem=64G



echo "Testing textcat"

time head -n 10000 data/cut.dev | cut -f 2 | ./textcat/text_cat_pred.pl -d ./textcat/lm -s -u 1.0 > textcat_pred.txt
