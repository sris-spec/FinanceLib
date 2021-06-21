# FinanceLib

## Package Overview
FinanceLib is easy-to-use Python library that has modules for representing the visualizations and analysis of commonly used finance related terms through graphs and charts.
  
## Table of Contents
 ### Usage
 This module can be used for the below given puposes:
 * Calculating the interest earned over the amount deposited.
 * Representation of change of Interest,Balance with respect to years through line or bar graphs.
 * Representation of ratios between Deposit and interest applied over it through pie chart.
 * Calculating and visvalisition of Relative stock index.
 * Measures and visualizes the Volatility of a Stock 
 
 ### Modules Included
   This Library mainly consists of three modules , namely :
   ### 1. [**analysis**](https://github.com/sris-spec/FinanceLib/tree/master/src/FinanceLib/analysis):
   This module is further subdivided into two very important stock analysis  fuctions which are widely used in financial risk management.
   * Relative Strength Index (RSI)
   * Volatility
   > Sample Code
   > ```python
   > from FinanceLib.analysis import volatility as vt
   > vt.volatility('GOOG','2020,01,01') 
   > ```
   
   ### 2. [**genBanking**](https://github.com/sris-spec/FinanceLib/tree/master/src/FinanceLib/genBanking):
   This module is further subdivided into two most commonly used finance terms namely,
   * Fixed Deposit (FD)
   * Equated Monthly Interest (EMI)
   > Sample Code
   > ```python
   > from FinanceLib.genBanking import EMI as emi
   > emi.EMI(500000,10.5,2)
   > ```

   ### 3. [**interest**](https://github.com/sris-spec/FinanceLib/tree/master/src/FinanceLib/interest):
   This module is further subdivided into two basic interests calculations which are widely used and are the building blocks of any financial calculations.
   * Simple Interest
   * Compound Interest
   > Sample Code
   >```python
   >from FinanceLib.interest import Compound_interest as ci
   >ci.Compound_Interest(20000,5,10,'annually')
   >```
   
  ### Package Structure
  ```bash
  ├── FinanceLib
│   ├── analysis
│   │   ├── __init__.py
│   │   ├── rsi.py
│   │   ├── volatility.py
│   ├── genBanking
│   │   ├── __init__.py
│   │   ├── EMI.py
│   │   ├── Fixed Deposit.py
│   └── interest
│       ├── __init__.py
│       ├── simpleinterest.py
│       └── Compound_interest.py
└── __init__.py    
  ```
  ### Installation
  ```bash
  pip install FinanceLib==0.0.2
  ```
  ### Licence
  All the codes included in this packaging library is licensed under MIT License.
   
 
