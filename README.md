# Phi Recycling
New scenario unlocked with Phi vision model to sort trash and recycling at scale

## Overview 
The Phi family of models shows the power of small language models.  In this demonstration, we will be using Phi 3 with vision specifically.  

As small language models (SLM) are obviously smaller, the quality of image understanding may not be quite as good as with a large language model, but there are some advantages:
+ SLMs allow local execution, which is valuable for a number of reasons - lack of connectivity, latency constraints, or sharing-data-to-the-cloud concerns
+ SLMs allow you to call the model at great scale

## Setup

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
