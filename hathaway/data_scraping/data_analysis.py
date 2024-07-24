import pandas as pd
from sklearn.linear_model import LinearRegression


def analyze_data(data):
    df = pd.DataFrame(data)

    corr_matrix = df[['fans_count', 'reposts_count', 'comments_count']].corr()
    print("Correlation Matrix:")
    print(corr_matrix)

    X = df[['fans_count', 'reposts_count']]
    y = df['comments_count']

    model = LinearRegression()
    model.fit(X, y)

    print(f'Coefficients: {model.coef_}')
    print(f'Intercept: {model.intercept_}')

    return df, model


if __name__ == '__main__':
    data = [
        {'user_id': '1234567890', 'fans_count': 1000, 'reposts_count': 500, 'comments_count': 200},
        {'user_id': '0987654321', 'fans_count': 1500, 'reposts_count': 700, 'comments_count': 300}
    ]
    analyze_data(data)
