import streamlit as st
import numpy as np
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import datetime

st.title("The SIR Model")
st.markdown("<h6 style='text-align: Left; color: black;'>A simple mathematical description of the spread of a disease in a population is the so-called SIR model, which divides the (fixed) population of N individuals into three compartments which may vary as a function of time, t:</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: Left; color: black;'>S(t) are those susceptible but not yet infected with the disease;</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: Left; color: black;'>I(t) is the number of infectious individuals;</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: Left; color: black;'>R(t) are those individuals who have recovered from the disease and now have immunity to it.</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: Left; color: black;'>The SIR model describes the change in the population of each of these compartments in terms of two parameters, β and γ. β describes the effective contact rate of the disease: an infected individual comes into contact with βN other individuals per unit time (of which the fraction that are susceptible to contracting the disease is S/N). γ is the mean recovery rate: that is, 1/γ is the mean period of time during which an infected individual can pass it on.</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: Left; color: black;'>The differential equations describing this model were first derived by Kermack and McKendrick [Proc. R. Soc. A, 115, 772 (1927)]:</h6>", unsafe_allow_html=True)
#Parameter
parameters = st.sidebar.title("Parameters")

total_pop = st.sidebar.number_input("Total Population")
d = st.sidebar.beta_expander("Description")
d.write("Total population, N.")

recovered = st.sidebar.number_input("Initial Recovered")
d1 = st.sidebar.beta_expander("Description")
d1.write("Initial Number of Recovered individuals. R0")

infected = st.sidebar.number_input("Initial infected")
d2 = st.sidebar.beta_expander("Description")
d2.write("Initial Number of Inefected individuals. I0")

contact_rate = st.sidebar.slider("Contact Rate(&)",0,20)
d3 = st.sidebar.beta_expander("Description")
d3.write("The rate at which individuals make contact with eatch other")

Trans_rate= st.sidebar.slider("Transmissibility(&)",0,10)
d4 = st.sidebar.beta_expander("Description")
d4.write("Probability of infection")
Transmissibility = Trans_rate/100

recovery_days = st.sidebar.slider("Duration of infections(days)",1,20)
d5 = st.sidebar.beta_expander("Description")
d5.write("The duration of which a person can be infectious")

min_date = datetime.datetime(2021,1,1)
max_date = datetime.date(2021,1,2)
a_date = st.date_input("Pick a date", (min_date, max_date))
te = a_date[-1] -a_date[0]
# A list of days, 0-160
#days = range(0,te.days)
# Total population, N.
N = total_pop
# Initial number of infected and recovered individuals, I0 and R0.
I0 = infected
R0 = recovered
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta =Transmissibility * contact_rate 
gamma = 1/recovery_days
# A grid of time points (in days)
t= range(0,te.days)
#t = np.linspace(0, 160, 160)

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Initial conditions vector
y0 = S0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered/Removed')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number (1000s)')
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
st.pyplot(fig)

st.title("SIR Model Theoretical Infection Compared with The real world data")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)
  filtered = st.multiselect("Select Date and daily infections", options=list(df.columns), default=None)
  st.write(df[filtered])
  df2 = df[filtered]
  #st.write(df2.iloc[:, 0])
  df2.iloc[:, 0]=pd.to_datetime(df2.iloc[:, 0], format="%Y/%m/%d")
  ep_date = df2.iloc[:, 0]
  ep_infection = df2.iloc[:, 1]

  fig3, ax = plt.subplots()
  ax = plt.plot_date(ep_date, ep_infection, linestyle='solid')
  plt.xlabel('Date')
  plt.ylabel('Daily infections')
  column_1, column_2 = st.beta_columns(2)
  with column_1:
          st.title('Theoretical')
          st.pyplot(fig)
  with column_2:
          st.title('Real')
          st.pyplot(fig3)
