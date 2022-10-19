# Simple Monte Carlo simulation in Streamlit
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://adalseno-st-montecarlo-simulation-m7-app-71jr0q.streamlitapp.com/)

Simple app to show a Monte Carlo simulation in Streamlit.<br>

I refactored the original code to use numpy vectorization for better performance and used ~~`numexpr`~~ `numba` library for further improvment in the final calculation.

The range goes from 100 to 10,000,000 iterations. Up to 100,000 the result is immediatley shown. For 1,000,000 it takes a bllink, For 10,000,000, thanks to numba, it takes a couple of seconds.


![Screenshot 2022-10-12 01 53 55](https://user-images.githubusercontent.com/2405291/195219253-378f3c93-b424-4cd5-8f79-a389a2703ea2.png)


In the jupyter notebook I made a comparison among numpy, numexpr and numba.
These are the results:
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>numpy_mean</th>
      <th>numpy_std</th>
      <th>numexpr_mean</th>
      <th>numexpr_std</th>
      <th>numba_mean</th>
      <th>numba_std</th>
      <th>Delta</th>
      <th>Delta %</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>100</th>
      <td>0.000161</td>
      <td>0.000135</td>
      <td>0.000190</td>
      <td>0.000153</td>
      <td>0.054950</td>
      <td>0.387602</td>
      <td>-0.054760</td>
      <td>-28892.283888</td>
    </tr>
    <tr>
      <th>1000</th>
      <td>0.000703</td>
      <td>0.000127</td>
      <td>0.000687</td>
      <td>0.000076</td>
      <td>0.000407</td>
      <td>0.000126</td>
      <td>0.000280</td>
      <td>40.772931</td>
    </tr>
    <tr>
      <th>10000</th>
      <td>0.006341</td>
      <td>0.000231</td>
      <td>0.006060</td>
      <td>0.000046</td>
      <td>0.002381</td>
      <td>0.000382</td>
      <td>0.003679</td>
      <td>60.712667</td>
    </tr>
    <tr>
      <th>100000</th>
      <td>0.063277</td>
      <td>0.001100</td>
      <td>0.060028</td>
      <td>0.001089</td>
      <td>0.020787</td>
      <td>0.001920</td>
      <td>0.039241</td>
      <td>65.370916</td>
    </tr>
    <tr>
      <th>1000000</th>
      <td>0.652204</td>
      <td>0.008045</td>
      <td>0.606476</td>
      <td>0.002097</td>
      <td>0.189293</td>
      <td>0.018253</td>
      <td>0.417183</td>
      <td>68.788008</td>
    </tr>
    <tr>
      <th>10000000</th>
      <td>7.166785</td>
      <td>0.014803</td>
      <td>6.398878</td>
      <td>0.011248</td>
      <td>1.806638</td>
      <td>0.064650</td>
      <td>4.592240</td>
      <td>71.766331</td>
    </tr>
  </tbody>
</table>

![comparison](https://user-images.githubusercontent.com/2405291/196753126-1b7b959f-8894-4020-ab7e-2c1aec8c14f5.png)


As we can see, except for the first call (that isn't noticeable) due to compilation overhead, numba is way faster (even if the code needs some care since numba does not support each python object).
