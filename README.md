# Majorization

## Install dependencies:
For don't have conflicts, we recommend to create a virtual environment for run the code.
The requirements of them are listed in the file: `requirements.txt`.

### Using Virtual Environment
- Install Python3 devel
- Create a virtual environment(venv) with Python 3.7
- Active venv
- Install requirements

Fedora Linux Ex:

```
sudo dnf install python3-devel

virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt
```

### No Virtual Environment
- Use Python 3.7
- Install requirements
`pip install -r requirements.txt --user`

## Run

### Generate Samples
In the Jupyter Notebook file: `data/GenerateSamples.ipynb` you can specify the dimension, number of pair of samples to be created and run the code to generate an output file.

### Train a Sequential model
After generate the samples by the previous step, you can use the Jupyter Notebook file: `ml_models/SequentialModel.ipynb` to train a Sequential Model that will be responsible to predict, given a pair of vectors A and B, if the first one majorates the second one. For the training, you need to specify the dimension, number of samples (total), number of training epochs and the optimizer name to update the weights of the model.
- The Jupyter Notebook `runner/run_sequential_training.ipynb` contains an example of how to trigger the training of multiple sequential models with different parameters.

### Self-Catalysis
Using a trained model and a set of samples, you can use the Jupyter Notebook `runner/self_catalysis.ipynb` to make self catalysis and check if the same model trained to predict majorization can predict self catalysis. In order to check the self catalysis performance, you need to specify the dimension and optimizer name.
- The Jupyter Notebook `runner/run_self_catlysis.ipynb` contains an example of how to trigger the self catalysis check of multiple dimensions and optimizers.

### Self-Self-Catalysis
Using a trained model and a set of samples, you can use the Jupyter Notebook `runner/self_self_catalysis.ipynb` to make self self catalysis and check if the same model trained to predict majorization can predict self self catalysis. In order to check the self self catalysis performance, you need to specify the dimension, optimizer name and set the prediction flag (True - use a sequential model to predict the self catalysis output / False - use the original formula to get the self catalysis output)
- The Jupyter Notebook `runner/run_self_self_catlysis.ipynb` contains an example of how to trigger the self self catalysis check of multiple dimensions and optimizers.


**Note: All the combinations with the samples will be tested. So, if you choose 100 pairs of samples, 10000 combinations will be validated, in both ordenation (AB and BA).**