## Setting the environment

Follow the steps below to install anaconda and create the environment for running the starter code.

1. Download anaconda from https://www.anaconda.com/ and install
2. Create a new environment that has all the dependencies installed, e.g., if you decide to name this new
   environment `cs281-alpaca`, run the command

```bash
conda create -n cs281-alpaca python=3.8 -y
conda activate cs281-alpaca
pip install -r requirements.txt  # Run this from root of the repo.
```

## Starter Code
All starter code related to the first homework is in `alpaca.ipynb`. Your code should directly go in this file.

Submit your responses to the free-form questions in a separate file, called `alpaca_writeup.pdf`. Include both `alpaca_writeup.pdf` and `alpaca.ipynb` in your submitted zip file.

## Submission

Running the following will generate alpaca.zip which contains `alpaca.ipynb` and `alpaca_writeup.pdf`

```bash
bash make_submission.sh
```
Submit the zip file to Gradescope.
