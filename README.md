# Creating a synthetic hydrodynamic model with machine learning
Master thesis


- [Summary](#summary)
- [Repo structure](#repo-structure)
- [Working with the repo](#working-with-the-repo)


## Summary

Work with RN-Digital and 

Masters program Data Science in Oil&Gas, Lomonosov Moscow state university

## Repo structure

The project has the following structure:
- `codes/`: `.py` main codes with data, model, training and inference modules
- `notebooks/`: `.ipynb` Colab-friendly notebooks for data augmentation and model training
- `input/`: input data (can also be downloaded [here](https://drive.google.com/uc?id=1-zZFOjNTjPhiwxB3ZyyNjrifOq7JOptU))
- `output/`: model weights, configurations and figures exported from the notebooks


## Working with the repo

### Environment

To work with the repo, I recommend to create a virtual Conda environment from the `environment.yml` file:
```
conda env create --name bms --file environment.yml
conda activate bms
```

