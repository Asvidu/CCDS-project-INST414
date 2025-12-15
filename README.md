# Predicting Global Food Waste and Economic Loss

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

## Sprint 1 – Project Overview and Problem Definition

In Sprint 1, I defined the overall problem of global food waste and its economic impact. I explained why food waste is an important issue and identified key stakeholders affected by it. I outlined the project goal, which is to analyze food waste patterns and predict total food waste and economic loss using data science. I also identified potential data sources and described the basic analytical approach.

## Sprint 2 – Data Acquisition, Cleaning, and Exploratory Analysis

In Sprint 2, I obtained a global food wastage dataset from Kaggle and confirmed successful data access. I cleaned the dataset by removing rows with missing values, checking for duplicates, and reviewing data quality. I conducted exploratory data analysis to understand trends over time, differences across food categories and countries, and relationships between variables. Based on EDA, I refined the problem focus and identified a strong relationship between total food waste and economic loss.

## Sprint 3 – Modeling, Evaluation, and Interpretation

In Sprint 3, I built and compared multiple regression models, including Linear Regression, Decision Tree Regression, and Random Forest Regression. Separate models were trained for predicting total food waste and economic loss. Model performance was evaluated using RMSE and R². The results showed that Random Forest performed best for predicting total waste, while Linear Regression performed best for predicting economic loss. Feature importance analysis revealed strong feature dominance between total food waste and economic loss, which informed model interpretation and limitations.


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         dining_hall_food_waste_prediction and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── dining_hall_food_waste_prediction   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes dining_hall_food_waste_prediction a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------



