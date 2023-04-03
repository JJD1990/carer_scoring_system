# Carer Scoring System

This project aims to create a carer scoring system in Python to serve the best carers first in search results based on provided data. The scoring system takes into account various fields, such as review scores, image problems, carer types, and more, to compute a single score for each carer. The carers are then sorted based on their scores, with the highest-scoring carers appearing first.

## Why Pandas?

I chose Pandas for this project because it is a powerful library in Python for data manipulation and analysis. It simplifies handling and processing large datasets and offers efficient data handling, data manipulation, and readability.

## Code Formatting and Standards

To ensure that the code meets high-quality standards, I used flake8 to check for PEP8 compliance. This tool helps make the code more readable, maintainable, and compliant with widely-accepted Python coding standards.

## Scoring System

Here are the weights I chose for each field in the scoring system:

```
weights = {
    'num_reviews': 0.2,
    'avg_review': 0.3,
    'img_problems': -0.25,
    'num_previous_clients': 0.1,
    'days_since_login': -0.2,
    'age': 0.05,
    'years_experience': 0.1,
    'type_numeric': 0.25
}
```

I picked these weights considering the importance of each field in determining the best carers:

num_reviews: Higher number of reviews indicates better experience, so I assigned it a weight of 0.2.
avg_review: A higher average review score gives less experienced carers a fair chance, so I assigned it a weight of 0.3.
img_problems: The first impression a carer makes is important, so I assigned a negative weight of -0.25.
num_previous_clients: This is related to the number of reviews and not as important, so I assigned a lower weight of 0.1.
days_since_login: Carer's engagement with the platform is important, so I assigned a negative weight of -0.2.
age: This is not a very important factor but is included in the brief, so I assigned a weight of 0.05.
years_experience: Carers should not be judged solely on their years of experience, so I assigned a weight of 0.1.
type_numeric: The skills a carer has are important, so I assigned a weight of 0.25.

## Usage

To run the carer scoring system,

` git clone https://github.com/JJD1990/carer_scoring_system.git`

Then simply execute the main Python script:

`python carer_scoring_system.py`

This will read the carers' data from the input CSV file (carers.csv), compute the scores, sort the carers based on their scores, and save the results to a new CSV file (sorted_carers.csv).
