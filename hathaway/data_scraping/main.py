from data_fetch import fetch_data
from data_analysis import analyze_data
from data_visualization import visualize_data


def main():
    user_ids = ['1234567890', '0987654321']
    data = fetch_data(user_ids)

    df, model = analyze_data(data)

    visualize_data(df)


if __name__ == '__main__':
    main()
