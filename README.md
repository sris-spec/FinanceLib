# FinanceLib

## Package Overview
FinanceLib is easy-to-use Python library that has modules for representing the visualisations and analysis of commonly used finance related terms through graphs and charts.
  
## Table of Contents
 ### Usage
 This module can be used for the below given puposes:
 * Calculating the interest earned over the amount deposited.
 * Representation of change of Interest,Balance with respect to years through line or bar graphs.
 * Representation of ratios between Deposit and interest applied over it through pie chart.
 * Calculating and visualisition of Relative stock index.
 * Measures and visualizes the Volatility of a Stock 
 
 ### Modules Included
   This Library mainly consists of three modules , namely :
   ### 1. [**analysis**](https://github.com/sris-spec/FinanceLib/blob/master/src/FinanceLib/analysis.py):
   This module is further subdivided into two very important stock analysis  fuctions which are widely used in financial risk management.
   * Relative Strength Index (Function name - rsi)
   * Volatility (Function name - volatility)
   > Sample Code
   > ```python
   > import FinanceLib.analysis as anl
   > anl.rsi('GOOG','Google','2020,01,01') 
   > ```
   
   ### 2. [**genBanking**](https://github.com/sris-spec/FinanceLib/blob/master/src/FinanceLib/genBanking.py):
   This module is further subdivided into two most commonly used finance terms namely,
   * Equated Monthly Interest (Function name - EMI)
   * * Fixed Deposit (Function name - FD)
   > Sample Code
   > ```python
   > import FinanceLib.genBanking as gen
   > gen.EMI(500000,10.5,2)
   > ```

   ### 3. [**interest**](https://github.com/sris-spec/FinanceLib/blob/master/src/FinanceLib/interest.py):
   This module is further subdivided into two basic interests calculations which are widely used and are the building blocks of any financial calculations.
   * Simple Interest (Function name - simple_interest)
   * Compound Interest (Function name - compound_interest)
   > Sample Code
   >```python
   >import FinanceLib.interest as inter
   >inter.simple_interest(5000,5.5,5)
   >```
   
  ### Package Structure
  ```bash
  FinanceLib
      __init__.py
      analysis.py
      genBanking.py
      interest.py
   ```
  ### Installation
  ```bash
  pip install FinanceLib
  ```
  ### Licence
  All the codes included in this packaging library is licensed under MIT License.
   
 
