# Mood-Simulation-and-Analysis
The goal of this project is to simulate and analyze the end-of-day mood based on various influencing factors such as activities, free time, social interactions, sleep quality, and weather. The project employs probability distributions to model these factors and generates a mood value for each simulation.

### Project Output:
The project provides insights into the impact of different factors on end-of-day mood through a visual representation in the form of a histogram with a fitted normal distribution curve.
<p align="center">
  <img src="https://i.imgur.com/KjG7VZY.png">
</p>


#### 1. Mood Generation:
   - Simulation of different factors affecting mood, including classes, free time, social interactions, sleep quality, and weather.
   - Application of probability distributions to model these factors:
     - Class attendance: Continuous distribution (-8, 8)
     - Free time: Discrete distribution [-12, 5, 12]
     - Social interactions: Continuous distribution (-12, 12)
     - Sleep quality: Continuous distribution (-10, 10)
     - Weather: Discrete distribution [-15, 5, 15]
     - Initial mood: Normal distribution (50, 2)

#### 2. End-of-Day Mood Calculation:
   - Aggregation of the influence of all factors on mood.
   - Limiting the mood to the range [0, 100].
   - Generation and saving of data to a text file ('wyniki_symulacji.txt').

#### 3. Histogram Creation:
   - Creation of a histogram based on the simulation results.
   - Histogram parameters: 30 bins, color 'darkviolet', black edges, transparency 0.7.

#### 4. Fitting Normal Distribution Curve and Displaying Mean and Standard Deviation:
   - Computation of mean and standard deviation based on simulation results.
   - Generation of data for the normal distribution curve.
   - Plotting the fitting curve on the histogram.

#### 5. Saving the Plot:
   - Saving the plot in JPEG format ('wykres_histogram.jpeg').
   - Optimizing the layout of elements on the plot.
   - Displaying the plot.

