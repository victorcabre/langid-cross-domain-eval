#!/bin/bash

#SBATCH --job-name=t         # Job name
#SBATCH --output=job.%j.out      # Name of output file (%j expands to jobId)
#SBATCH --cpus-per-task=1        # Schedule one core
#SBATCH --time=15:00:00          # Run time (hh:mm:ss) - run for one hour max
#SBATCH --partition=scavenge    # Run on scavenge queue
#SBATCH --mail-type=END          # Send an email when the job finishes
#SBATCH --mem=128G

echo "Training fasttext"

time ./fastText/fasttext supervised -epoch 2 -lr 0.8 -dim 256 -minCount 1000 -minn 2 -maxn 5 -bucket 1000000 -thread 64 -input data/all.train -output fastText.out
