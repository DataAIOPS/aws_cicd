# House Price Prediction with DVC, Git, and Flask

This project demonstrates a machine learning pipeline for predicting house prices, using DVC (Data Version Control) for tracking data and pipeline stages, Git for version control, and Flask for deploying the model as a web application.

## Project Overview

The project workflow includes:

- Data preprocessing
- Model training
- Evaluation and metrics tracking
- Serving the model with a Flask web application

DVC is used to manage the data and track the pipeline, while Git keeps track of code and metadata changes. A simple Flask app allows users to input house features and receive price predictions.

## Setup Instructions

### Prerequisites

- Conda (for environment management)
- DVC (for pipeline management)
- Git (for version control)

### Installation

1. Clone the repository and navigate to the project directory:

    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. Set up the Conda environment:

    ```bash
    conda create -n dvc_venv python=3.8
    conda activate dvc_venv
    ```

3. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Initialize Git and DVC:

    ```bash
    git init
    dvc init
    ```

## Working with DVC

### Add and Track the Raw Data with DVC:

```bash
dvc add data/raw/house_data.csv
```

### Add Data to Git:
```bash
git add data/raw/house_data.csv.dvc data/raw/.gitignore
```

### Run the DVC Pipeline:
```bash
dvc repro
```
### Commit Changes to Git:
```bash
git add .
git commit -m "Initial pipeline setup"
```

### Make Subsequent Changes and Run DVC:
```bash
dvc repro
```

#### Track changes and commit:
```bash
git add .
git commit -m "Updated pipeline"
```
### Viewing Metrics:
```bash
dvc metrics show
```

#### To compare metrics with previous runs:
```bash
dvc metrics diff
```

### Running the Flask Application
```bash
python app.py
```