#!/bin/bash

#SBATCH --job-name=t         # Job name
#SBATCH --output=job.%j.out      # Name of output file (%j expands to jobId)
#SBATCH --cpus-per-task=1        # Schedule one core
#SBATCH --time=15:00:00          # Run time (hh:mm:ss) - run for one hour max
#SBATCH --partition=scavenge    # Run on scavenge queue
#SBATCH --mail-type=END          # Send an email when the job finishes

echo "CPU Info"

lscpu
