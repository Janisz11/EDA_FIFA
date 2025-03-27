import seaborn as sns
import matplotlib.pyplot as plt
from data_loader import load_data
def scatter_with_regression(df, x_col, y_col, reg_type='linear'):

    # Drop rows with missing values
    data = df[[x_col, y_col]].dropna()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=x_col, y=y_col, alpha=0.4)

    # Linear regression
    if reg_type == 'linear':
        sns.regplot(data=data, x=x_col, y=y_col, scatter=False, color='red')

    # LOWESS (locally weighted scatterplot smoothing)
    elif reg_type == 'lowess':
        sns.regplot(data=data, x=x_col, y=y_col, scatter=False, lowess=True, color='green')

    # Logarithmic regression (log x axis)
    elif reg_type == 'log':
        sns.regplot(data=data, x=x_col, y=y_col, scatter=False, logx=True, color='purple')

    else:
        raise ValueError("Invalid reg_type. Choose from: 'linear', 'lowess', 'log'")

    plt.title(f"{reg_type.capitalize()} Regression: {y_col} vs {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.tight_layout()
    plt.show()

df = load_data()
scatter_with_regression(df, "overall", "value_eur", reg_type="linear")
scatter_with_regression(df, "overall", "value_eur", reg_type="lowess")
scatter_with_regression(df, "overall", "value_eur", reg_type="log")
