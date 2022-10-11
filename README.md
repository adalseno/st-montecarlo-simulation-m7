# Simple Monte Carlo simulation in Streamlit
Simple app to show a Monte Carlo simulation in Streamlit
I refactored the original code to use numpy vectorization for better performance and used `numexpr` library for further improvment in the final calculation.
The range goes from 100 to 10,000,000 iterations. Up to 100,000 the result is immediatley shown. For 1,000,000 it takes a bllink, For 10,000,000 it takes a few seconds (about 5).
![Screenshot 2022-10-12 01 53 55](https://user-images.githubusercontent.com/2405291/195219253-378f3c93-b424-4cd5-8f79-a389a2703ea2.png)

The interactive app can be found on [Streamlit](https://adalseno-st-montecarlo-simulation-m7-app-71jr0q.streamlitapp.com/)
