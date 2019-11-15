#!/bin/bash
#SBATCH -o $HOME/cosmosis_chains_tutorial/jobscript/slurm.out
#SBATCH -e slurm.err
#SBATCH -p common
#SBATCH -N 2 

cd $HOME/cosmosis
source config/setup-cosmosis

cd $HOME/cosmosis_chains_tutorial/configini/
mpiexec -n $SLURM_NTASKS cosmosis --mpi params_baseline.ini

