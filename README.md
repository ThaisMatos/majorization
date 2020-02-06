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

### Using Jupyter Notebook
In the Jupyter Notebook version: `GenerateSamples.ipynb` you can specify the dimension, number of pair of samples to be created and run the code to generate an output file.

### Using Python Script
With the Python script: `generate_samples.py` you can run it passing the arguments dimension and number of pair of samples to be created, respectively, inline as follows:
`python3.7 generate_samples.py 3 10`

**Note: All the combinations with the samples will be tested. So, if you choose 100 pairs of samples, 10000 combinations will be validated, in both ordenation (AB and BA).**