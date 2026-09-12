# A01: California Housing Boxplot

A small GitHub Bootcamp project for OPIM 5512 that demonstrates a full branch-based Git workflow: loading the California Housing dataset, generating a boxplot, and committing the result through a `dev` branch and pull request.

## Data

This project uses the **California Housing dataset**, loaded via `sklearn.datasets.fetch_california_housing`. It contains 20,640 California census block groups with features such as median income, house age, average rooms/bedrooms, population, and location (latitude/longitude), plus the median house value as the target.

## How to run

```bash
# install the requirements
pip install -r requirements.txt

# change into the repo directory
cd path/to/A01

# run the script
python src/boxplot.py
```

## Expected output

Running the script generates a boxplot of median income (`MedInc`) across California census block groups and saves it to `figs/boxplot.png`.
