import streamlit as st
import numpy as np
import pandas as pd


# Helper function that creates distribution and statistics
def Hist(trials:int)-> tuple[np.array, pd.DataFrame]:
   
    # Vectorized version, much faster (Annual interest from 40% to 70% random normal)
    distribution = (1+np.random.normal(0.4, 0.7, (12,trials))/12)
    interest = np.array([range(12,0,-1)]).T
    res = (10*((distribution)**interest)).sum(axis=0)
   
    # Add statistics
    avg = np.mean(res)  # Mean
    sigma = np.std(res)  # Std
    lowb = (avg - 1.96 * sigma / np.sqrt(trials))  # Low Bound
    upb = (avg + 1.96 * sigma / np.sqrt(trials))  # Upper Bound
    width = (upb - lowb)

    # Create DataFrame with statistics 
    stat_df = pd.DataFrame({"Trials": f"{trials:,}", "Average": f"$ {avg:.2f}", "St. Dev": f"$ {sigma:.2f}", 
                    "Upper Bound": f"$ {upb:.2f}", "Low Bound": f"$ {lowb:.2f}", "Width": f"$ {width:.2f}"}, 
                    index=["Monte Carlo Simulation"])
    return res, stat_df


# Title and subtitle
st.title('Monte Carlo simulation')
st.subheader("Cumulative Account Balance with a Monthly $10 Dollar Investment and Variable Annual Interest")

    
# Select number of trials from listbox
trial_range = map(lambda x: int(np.power(10,x)), range(2,7)) # from 100 to 1_000_000

# I used a comma to seprate thousands for better readability
trials = st.selectbox('Select number of trials', trial_range, format_func=lambda x: f"{x:,}")

# Get data
data_load_state = st.text('Computing data...')
data, stat_df = Hist(trials)
data_load_state.text("Done!")

# Get bounds
bound_min = int(data.min().round(0))
bound_max = int(data.max().round(0))

# Get data for histogram 
y = np.histogram(data, bins=24, density=True)[0]
x = np.linspace(bound_min, bound_max, len(y), dtype=int)

# Create Series for better management
hist_values = pd.Series(y, index=x, name="Final Balance $")

# Display statistics (the values are strings)
st.table(stat_df)

# Plot histogram
st.bar_chart(hist_values)