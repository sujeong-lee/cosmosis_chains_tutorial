#!/bin/bash

#SBATCH --mem=4G # 4 GBs RAM
#SBATCH -p common #only for members 
#SBATCH -n 128
#SBATCH -t 5400

source $HOME/cosmosis/config/setup-cosmosis

cd $HOME/cosmosis_chains_tutorial/configini/
mpiexec -n $SLURM_NTASKS cosmosis --mpi params_baseline_ext.ini 
