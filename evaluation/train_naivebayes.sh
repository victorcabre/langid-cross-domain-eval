#!/bin/bash

#SBATCH --job-name=t         # Job name
#SBATCH --output=job.%j.out      # Name of output file (%j expands to jobId)
#SBATCH --cpus-per-task=1        # Schedule one core
#SBATCH --time=15:00:00          # Run time (hh:mm:ss) - run for one hour max
#SBATCH --partition=scavenge    # Run on scavenge queue
#SBATCH --mail-type=END          # Send an email when the job finishes
#SBATCH --mem=128G


module load Python/3.12.3-GCCcore-13.3.0
source .venv/bin/activate
cd naivebayes
time python3.12 train.py
