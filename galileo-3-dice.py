import random
import pandas as pd
import matplotlib.pyplot as plt


def roll_dice(n):
    """Returns the sum of n dice rolls."""
    return sum(random.randint(1, 6) for _ in range(n))

# Simulate the sum of three dice rolls 10,000 times
results = [roll_dice(3) for _ in range(((100000)))]

# Create a dictionary to store the frequencies of each outcome
freq_dict = {}
for result in results:
    if result not in freq_dict:
        freq_dict[result] = 1
    else:
        freq_dict[result] += 1

# Create a pandas DataFrame from the frequency dictionary
freq_df = pd.DataFrame({'Outcome': list(freq_dict.keys()), 'Frequency': list(freq_dict.values())})
freq_df = freq_df.sort_values(by='Outcome')

# Divide the frequencies by the total number of simulations to get the proportions
freq_df['Proportion'] = freq_df['Frequency'] / len(results)

# Print the frequency table with proportions
print(freq_df)

# Plot a histogram of the results
plt.hist(results, bins=range(3, 19), align='left', edgecolor='black')
plt.xlabel('Sum of three dice rolls')
plt.ylabel('Frequency')
plt.title('Histogram of sum of three dice rolls')
plt.show()