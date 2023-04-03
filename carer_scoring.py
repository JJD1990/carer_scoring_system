import pandas as pd

# The normalise function puts the data into the same scale
# (between 0 / 1) so that it is easier to calculate.


def normalize(df, columns):
    for column in columns:
        min_val = df[column].min()
        max_val = df[column].max()
        df[column] = (df[column] - min_val) / (max_val - min_val)
    return df

# This function takes in the csv data
# and applies the weights to computed the score.


def compute_score(df, weights):
    weighted_df = df.copy()
    for column, weight in weights.items():
        weighted_df[column] = df[column] * weight
    weighted_df['score'] = weighted_df[list(weights.keys())].sum(axis=1)
    return weighted_df

# this is the main function which puts
# the other functions together and returns the results.


def main():
    # Read CSV file
    data = pd.read_csv('carers.csv', encoding='utf-8-sig')

    # Convert the 'type' field to a numerical value
    type_mapping = {'basic': 1, 'advanced': 2, 'expert': 3}
    data['type_numeric'] = data['type'].map(type_mapping)

    # Normalize numerical fields
    normalized_data = normalize(data,
                                ['num_reviews',
                                 'avg_review',
                                 'img_problems',
                                 'num_previous_clients',
                                 'days_since_login',
                                 'age',
                                 'years_experience'])

    # Define weights for each field
    weights = {
        # I believe the number of reviews is an important
        #  figure as the higher the number of reviews,
        # in theory, the better the experience of the carer.
        'num_reviews': 0.2,
        # I believe the average number of reviews gives
        # the less experienced carers a fair chance of
        # getting a better score and makes the scoring
        # system fairer.
        'avg_review': 0.3,
        # This is the first impression a carer
        # will give their potential clients so
        # it is very important.
        'img_problems': -0.25,
        # This is the number of previous clients
        # a carer has had, I do not feel this is
        # a very important score as it can be related
        # to the number of reviews, it is not easy
        # to get all clients to provide a review.
        'num_previous_clients': 0.1,
        # I feel this is an important factor as
        # it takes the carers 'buy-in' to the
        # platform, the more the carer uses
        # the platform the better.
        'days_since_login': -0.2,
        # I do not feel this is an important
        # factor, and could actually get us
        # in trouble. However it is in the
        # brief so I have left it.
        'age': 0.05,
        # I do not feel this is an important
        # factor as each carer will have strengths
        # and weaknesses and should not be judged
        # on thier years of experience.
        'years_experience': 0.1,
        # I think the skills a carer
        # has is a very important thing to consider.
        'type_numeric': 0.25
    }

    # Compute scores
    scored_data = compute_score(normalized_data, weights)

    # Sort by score in descending order
    sorted_data = scored_data.sort_values('score', ascending=False)

    # Save the results to a new CSV file
    sorted_data.to_csv('sorted_carers.csv', index=False)


if __name__ == '__main__':
    main()
