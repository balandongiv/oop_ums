import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.utils.data as data
import copy
import seaborn as sns
np.random.seed(0)

# Define the range for random values
lower_bound = 100
upper_bound = 500
array_length = 200

# Generate random array and reshape it
random_array = (np.random.randint(lower_bound, upper_bound, array_length) / 10.0).reshape(-1, 1)

# Train-test split for time series
train_size = int(len(random_array) * 0.67)
train, test = random_array[:train_size], random_array[train_size:]

lookback = 10

def create_dataset(dataset, lookback):
    X = [dataset[i:i+lookback] for i in range(len(dataset)-lookback)]
    y = [dataset[i+1:i+lookback+1] for i in range(len(dataset)-lookback)]
    return torch.tensor(np.array(X)), torch.tensor(np.array(y))

X_train, y_train = create_dataset(train, lookback=lookback)
original_data = y_train[0]
mock_prediction = copy.deepcopy(original_data)
mock_prediction[-1] += 0.5

def create_time_steps(length):
    return list(range(-length, 0))

def show_plot(plot_data, delta, title):
    labels = ['Historical Data', 'Actual Future', 'Model Prediction']

    # We use different markers for different time series
    marker = ['o-', 's-', '^-', 'x-', '.-', '--']

    # Obtain the time steps for the output history and the true future
    time_steps = create_time_steps(plot_data[0].shape[0])

    future = delta if delta else 0
    plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    sns.set_style("whitegrid")  # Set Seaborn style
    plt.title(title)
    for i, data_time_series in enumerate(plot_data):
        if i:
            # Plot the future or the predicted values of the time series
            dis_y = data_time_series[-1]
            plt.plot(future, dis_y, marker[i], markersize=10, label=labels[i])
        else:
            # Plot the historical data
            plt.plot(time_steps, plot_data[i].flatten(), marker[i], label=labels[i])

    plt.legend()
    dis_axis = (future + 5) * 0.5
    plt.xlim([time_steps[0], dis_axis])
    plt.xlabel('Time-Step')
    plt.show()


show_plot([X_train[0], y_train[0], mock_prediction], 0, 'Sample Example')
