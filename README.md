# Sir Model Web App using Streamlit
This web application implements the SIR (Susceptible-Infectious-Recovered) model, a mathematical model that describes the spread of infectious diseases. The web application allows users to input various parameters to simulate the spread of the disease.

# Requirements
To run this web application, you will need the following libraries:

- streamlit
- pandas
- numpy
- matplotlib
-scikit-learn
You can install these libraries using pip by running the following command:
`
pip install streamlit pandas numpy matplotlib scikit-learn`
# Data Preparation
The SIR model requires the following parameters to simulate the spread of a disease:

- Population size
- Initial number of infected individuals
- Contact rate (the rate at which individuals come into contact with each other)
- Recovery rate (the rate at which infected individuals recover)
The web application allows users to input these parameters, as well as the number of days to simulate the spread of the disease.

# SIR Model
The SIR model is a compartmental model that divides the population into three compartments: susceptible (S), infectious (I), and recovered (R). The model assumes that the population size remains constant and that individuals can only move from the susceptible compartment to the infectious compartment and then to the recovered compartment.

The model is governed by the following set of differential equations:

- dS/dt = -beta * S * I / N
- dI/dt = beta * S * I / N - gamma * I
- dR/dt = gamma * I

where S is the number of susceptible individuals, I is the number of infectious individuals, R is the number of recovered individuals, beta is the contact rate, gamma is the recovery rate, and N is the population size.

# Results
The web application simulates the spread of the disease based on the user inputted parameters and displays the results using matplotlib. The results include the number of susceptible, infectious, and recovered individuals over time, as well as the peak number of infectious individuals.

# Conclusion
The SIR model is a useful tool for understanding the spread of infectious diseases. This web application allows users to input various parameters to simulate the spread of a disease and visualize the results using matplotlib. By adjusting the parameters, users can explore the effects of different interventions, such as vaccination or social distancing, on the spread of a disease.




