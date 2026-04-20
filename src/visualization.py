import matplotlib.pyplot as plt

def plot_data(df):
    plt.plot(df['Close'])
    plt.show()