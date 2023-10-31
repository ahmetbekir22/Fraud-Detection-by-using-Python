import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from matplotlib import style
import random
colors = ['red', 'blue', 'green',  'orange',  'cyan', 'magenta', 'brown', 'gray']

def retrieveData(filename, adaylar):
    # Create an empty list to store the data
    liste = []
    with open(filename) as file:
            reader = pd.read_csv(file)
            j = adaylar.split(",")
            for aday in j:
                liste.extend(reader[aday])

    return liste

# Call the function to retrieve data, but the returned data is not being stored or used
retrieveData(sys.argv[1], sys.argv[2])


# Open a file and write retrieved data into it
with open("retrieveData.txt", "w") as file2:
    file2.write(str(retrieveData(sys.argv[1], sys.argv[2])))


def DispBarPlot():
    with open(sys.argv[1]) as file:
        reader = pd.read_csv(file)

        style.use('ggplot')
        xpos = np.arange(len(reader["Obama"]))
        plt.figure(figsize=(30, 7))
        barWidth = 0.2
        plt.text(1, 1, "")
        ypos = np.arange(0, 9 * (10 ** 6), step=10 ** 6)
        y_eksen = [k*(10**6) for k in range(9)]

        # Create bar plots for Obama and Romney
        plt.bar(xpos, reader["Romney"], color='red', width=barWidth, label='Romney')
        plt.bar(xpos + 0.2, reader["Obama"], color='royalblue', width=barWidth, label='Obama')
        plt.xticks(rotation=90)
        plt.xticks(xpos + 0.3, reader["State of Dist"])
        plt.yticks(ypos, y_eksen)
        plt.xlabel("STATES")
        plt.ylabel("vote count")
        plt.legend()
    return plt.savefig("ComparativeVotes.pdf")

# Call the function to create the ComparativeVotes.pdf
DispBarPlot()


def compareVoteonBar(filename):
    reader = pd.read_csv(filename)

    nomines = ["Obama", "Romney", "Johnson", "Stein"]
    total_vote = sum(reader["Total Vote"])
    # Calculate vote percentages for each nominee
    vote_percentages = [(sum(reader[nominee]) / total_vote) * 100 for nominee in nomines]

    x = [f"{vote:.3f} %" for vote in vote_percentages]
    y = vote_percentages

    style.use('ggplot')
    plt.figure(figsize=(10, 6))
    bars = plt.bar(x, y, color=["royalblue", "red", "green", "purple"])
    plt.xlabel("Nominees")
    plt.ylabel("Vote percentages")
    plt.title("Comparative Vote Percentages of nominees")
    plt.xticks(rotation=0)

    # Add a legend for the nominees
    legend_labels = ["Obama", "Romney", "Johnson", "Stein"]
    plt.legend(bars, legend_labels)

    plt.savefig("CompVotePercs.pdf")
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the election data file as an argument.")
    else:
        compareVoteonBar(sys.argv[1])


def obtainHistogram(numbers):
    histogram = [0] * 10
    for num in numbers:
        ones = num % 10
        tens = num % 100 // 10
        histogram[ones] += 1
        histogram[tens] += 1

    total_digits = sum(histogram)
    frequencies = [count / total_digits for count in histogram]
    return frequencies

# Call the function to obtain the histogram
obtainHistogram(retrieveData(sys.argv[1], sys.argv[2]))



def plotHistogram(frequencies):
    y1 = 0.10
    bins = range(len(frequencies))

    # Plot the histogram
    plt.plot(bins, frequencies, label="Digit Dist")
    plt.plot(y1, color='red')
    plt.ylabel("Distribution")
    plt.xlabel("Digits")
    plt.xticks(bins)
    plt.title("Histogram of least sign. digits")
    plt.axhline(y=0.10, linestyle='dotted', color='green', label="Mean")
    plt.legend()
    plt.savefig("Histogram.pdf")
    plt.show()

# Call the function to create the Histogram.pdf
plotHistogram(obtainHistogram(retrieveData(sys.argv[1], sys.argv[2])))



def plotHistogramWithSample():
    sample_sizes = [10, 50, 100, 1000, 10000]

    for i, sample_size in enumerate(sample_sizes):
        sample = [random.randint(0, 100) for _ in range(sample_size)]
        color = random.choice(colors)
        histogram = [0] * 10
        for num in sample:
            ones = num % 10
            tens = (num % 100 - ones) // 10
            histogram[ones] += 1
            histogram[tens] += 1

        total_digits = sum(histogram)
        frequencies = [count / total_digits for count in histogram]

        plt.plot(frequencies, color=color)
        plt.axhline(y=0.10, linestyle='dotted', label="Mean")
        plt.ylabel("Distribution")
        plt.xlabel("Digits")
        plt.title(f"Histogram of least significant digits - Sample Size: {sample_size}")
        plt.legend()

        filename = f"HistogramofSample{i + 1}.pdf"
        plt.savefig(filename)
        plt.clf()  # Clear the plot for the next iteration

plotHistogramWithSample()


mean_list = [0.10]*10

def calculate_mse(list1, list2):

    formula_of_mse = [(a - b) ** 2 for a, b in zip(list1, list2)]

    # Calculate the mean of the squared differences
    mse = sum(formula_of_mse) / len(formula_of_mse)
    return f"MSE value of 2012 USA election is  {mse}"
frequency_distribution = obtainHistogram(retrieveData(sys.argv[1], sys.argv[2]))

mse= calculate_mse(frequency_distribution, mean_list)
print(mse)

