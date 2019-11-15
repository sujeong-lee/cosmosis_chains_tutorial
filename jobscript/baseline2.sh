#SBATCH --constraint=haswell
#SBATCH --job-name=ext_nolimber
#SBATCH --nodes=1
#SBATCH --time=00:01:00
#SBATCH --qos=debug
#SBATCH --mail-user=lee.5922@osu.edu
#SBATCH --mail-type=ALL

#OpenMP settings:
#export OMP_NUM_THREADS=2
#export OMP_PLACES=threads
#export OMP_PROC_BIND=spread

cd $HOME/cosmosis
source config/setup-cosmosis-nersc

cd $HOME/DMASS-analysis/systematics/
srun -n 64 cosmosis --mpi params_ggl_shear_ext_nolimber.ini

