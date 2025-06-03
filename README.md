# DVC Demo Project

This project demonstrates the usage of DVC (Data Version Control) in a machine learning project. DVC helps in managing data, models, and experiments effectively.

## Project Structure
```
.
├── data/                  # Data directory (tracked by DVC)
│   ├── raw/              # Raw data files
│   └── processed/        # Processed data files
├── models/               # Trained models (tracked by DVC)
├── src/                  # Source code
│   ├── data/            # Data processing scripts
│   ├── features/        # Feature engineering scripts
│   └── models/          # Model training scripts
├── notebooks/           # Jupyter notebooks
├── metrics/             # Model metrics and evaluation results
├── dvc.yaml            # DVC pipeline configuration
├── params.yaml         # Model parameters
└── .dvc/               # DVC configuration directory
```

## Why DVC is Critical?

1. **Data Versioning**: DVC helps track different versions of datasets, making it easy to reproduce experiments.
2. **Model Versioning**: Store and version ML models alongside their corresponding data and code.
3. **Experiment Tracking**: Track different experiments with their parameters and results.
4. **Reproducibility**: Ensures complete reproducibility of ML experiments.
5. **Storage Efficiency**: Uses Git for metadata while storing large files in remote storage.

## Complete Setup Guide

### 1. Local Project Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/dvc-demo-project.git
cd dvc-demo-project
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 2. DVC Setup

1. Initialize DVC:
```bash
dvc init
```

2. Set up remote storage (choose one option):

   a. Google Cloud Storage:
   ```bash
   dvc remote add -d myremote gs://your-bucket/path
   ```

   b. Amazon S3:
   ```bash
   dvc remote add -d myremote s3://your-bucket/path
   ```

   c. Azure Blob Storage:
   ```bash
   dvc remote add -d myremote azure://your-container/path
   ```

   d. Local storage (for testing):
   ```bash
   dvc remote add -d myremote /path/to/local/storage
   ```

3. Add data directories to DVC:
```bash
dvc add data/raw
dvc add data/processed
dvc add models/
```

### 3. GitHub Repository Setup

1. Create a new repository on GitHub:
   - Go to https://github.com/new
   - Name your repository (e.g., "dvc-demo-project")
   - Choose public or private
   - Don't initialize with README (we already have one)

2. Initialize Git and push to GitHub:
```bash
# Initialize Git repository
git init

# Add all files
git add .

# Initial commit
git commit -m "Initial commit: Project setup with DVC"

# Add GitHub remote
git remote add origin https://github.com/yourusername/dvc-demo-project.git

# Push to GitHub
git push -u origin main
```

### 4. Running the Project

1. Download and process data:
```bash
dvc repro prepare
```

2. Train the model:
```bash
dvc repro train
```

3. View metrics:
```bash
dvc metrics show
```

### 5. Making Changes and Collaboration

1. When making changes to data:
```bash
# After modifying data
dvc add data/raw
git add data/raw.dvc
git commit -m "Update data"
dvc push
git push
```

2. When running new experiments:
```bash
# Run the pipeline
dvc repro

# Push changes
dvc push
git add .
git commit -m "Update experiment results"
git push
```

3. For collaborators to get started:
```bash
# Clone the repository
git clone https://github.com/yourusername/dvc-demo-project.git
cd dvc-demo-project

# Install dependencies
pip install -r requirements.txt

# Pull the data
dvc pull
```

## DVC Commands Reference

- `dvc init`: Initialize DVC in a directory
- `dvc add <file/directory>`: Start tracking files with DVC
- `dvc push`: Push data to remote storage
- `dvc pull`: Pull data from remote storage
- `dvc repro`: Reproduce the pipeline
- `dvc metrics show`: Show metrics
- `dvc exp run`: Run experiments
- `dvc remote add`: Add remote storage
- `dvc remote list`: List configured remotes

## Important Notes

1. **DVC Files**: 
   - `.dvc` files are tracked by Git
   - They contain metadata about the actual data files
   - Always commit these files to Git

2. **Remote Storage**:
   - Keep your remote storage credentials secure
   - Don't commit credentials to Git
   - Use environment variables or secure credential storage

3. **Best Practices**:
   - Always run `dvc push` after `dvc add`
   - Keep your `.gitignore` updated
   - Document any changes to the pipeline
   - Use meaningful commit messages

## Troubleshooting

1. If `dvc pull` fails:
   - Check your remote storage configuration
   - Verify your credentials
   - Ensure you have the correct permissions

2. If `dvc repro` fails:
   - Check your pipeline configuration in `dvc.yaml`
   - Verify all dependencies are installed
   - Check file paths in your scripts

3. If Git push fails:
   - Ensure you have the correct permissions
   - Check your Git credentials
   - Verify your remote URL 