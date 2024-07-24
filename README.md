# Phi Recycling
New scenario unlocked with Phi vision model to sort trash and recycling at scale

## Overview 
The Phi family of models shows the power of small language models.  In this demonstration, we will be using Phi 3 with vision specifically.  

As small language models (SLM) are obviously smaller, the quality of image understanding may not be quite as good as with a large language model, but there are some advantages:
+ SLMs allow local execution, which is valuable for a number of reasons - lack of connectivity, latency constraints, or sharing-data-to-the-cloud concerns
+ SLMs allow you to call the model at great scale

## Setup for CUDA compatible GPU

Anaconda and Python are required downloads before running the commands below.

### First run
```
conda create --name recycling python=3.10 -y
conda activate recycling

pip install -r requirements.txt
python recycling.py
```

### Subsequent runs
```
conda activate recycling
python recycling.py
```

## Setup for CPU 

Python and git large file system extension are required downloads. 
Git LFS can be downloaded here: [LFS Link](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage?platform=windows) 
Then, run git lfs install in Git Bash

### First Run 
```
pip install huggingface-hub[cli]
pip install -r requirements.txt
huggingface-cli download microsoft/Phi-3-vision-128k-instruct-onnx-cpu --include cpu-int4-rtn-block-32-acc-level-4/* --local-dir .
pip install numpy
pip install --pre onnxruntime-genai
python cpu_recycling_run.py -m cpu-int4-rtn-block-32-acc-level-4
```

### Subsequent Runs
```
python cpu_recycling_run.py -m cpu-int4-rtn-block-32-acc-level-4
```