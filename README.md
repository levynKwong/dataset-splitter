# Dataset Splitter

This repository contains a Python script to split a dataset of `.jpg` and `.txt` files into training, validation, and test sets. The script randomly shuffles the data and splits it into 70% training, 20% validation, and 10% test sets.

## Directory Structure

The script organizes the dataset into the following directory structure:



## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/dataset-splitter.git
    cd dataset-splitter
    ```

2. Place your dataset of `.jpg` and `.txt` files in the `dataset` directory.

3. Run the script:
    ```bash
    python split_dataset.py
    ```

## Requirements

- Python 3.x

## How It Works

1. The script lists all `.jpg` files in the `dataset` directory.
2. It shuffles the list of files.
3. It calculates the number of files for each split based on the specified proportions (70% train, 20% validation, 10% test).
4. It moves the files to their respective directories (train, validation, test), ensuring that the corresponding `.txt` files are also moved if they exist.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

