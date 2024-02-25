#!/bin/bash

#Submit this script with: sbatch thefilename

##################################################################
## SLURM Defintions
##################################################################
#SBATCH --time=8:00:00                                 # walltime
#SBATCH --nodes=1                                       # number of nodes
#SBATCH --ntasks=1                                      # limit to one node
#SBATCH --cpus-per-task=8                               # number of processor cores (i.e. threads)
#SBATCH --partition=alpha
#SBATCH --mem-per-cpu=8G                             # memory per CPU core
#SBATCH --gres=gpu:1                                    # number of gpus
#SBATCH -J "mcrpy"                           # job name
#SBATCH --output=slurm_out/mcrpy-%j.out
#SBATCH --mail-user=christian.duereth@tu-dresden.de     # email address
#SBATCH --mail-type=BEGIN,END,FAIL,REQUEUE,TIME_LIMIT,TIME_LIMIT_90
#SBATCH -A p_autoshear
##################################################################
##################################################################


ml release/23.04  GCC/11.3.0  OpenMPI/4.1.4 TensorFlow/2.11.0-CUDA-11.7.0

source .venv_mcrpy/bin/activate

dir="/lustre/ssd/ws/dchristi-3dseg/MCRpy/data/160_10-layer/00/subvolumes/"
dirout="/lustre/ssd/ws/dchristi-3dseg/MCRpy/results/"

for file in "$dir"/*; do
    python mcrpy/characterize.py --microstructure_filenames $file --limit_to 32 --descriptor_types Correlations --data_folder $dirout
done

