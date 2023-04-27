conda activate envGPU
conda install -c numpy matplotlib
conda install -c numba llvmlite
conda install conda-forge::cudatoolkit=11.5
export CUDA_HOME=/usr/local/cuda-11.7