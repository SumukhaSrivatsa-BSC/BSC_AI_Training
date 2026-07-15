# Titanic Dataset Exploratory Data Analysis (EDA)

## Project Overview

This project performs an in-depth Exploratory Data Analysis (EDA) on the Titanic dataset using Python, Pandas, Matplotlib, and Seaborn. The objective is to understand passenger demographics, travel characteristics, family relationships, fare patterns, and factors that influenced survival.

The analysis includes:

- Data Cleaning
- Missing Value Treatment
- Univariate Analysis
- Bivariate Analysis
- Multivariate Analysis
- Feature Engineering
- Statistical Summaries
- Data Visualization
- Business Insights

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

# Dataset Description

The dataset contains information about Titanic passengers.

## Features

| Column | Description |
|----------|-------------|
| PassengerId | Unique Passenger ID |
| Survived | Survival Status (0 = No, 1 = Yes) |
| Pclass | Passenger Class (1st, 2nd, 3rd) |
| Name | Passenger Name |
| Sex | Gender |
| Age | Passenger Age |
| SibSp | Number of Siblings/Spouses Onboard |
| Parch | Number of Parents/Children Onboard |
| Ticket | Ticket Number |
| Fare | Ticket Fare |
| Cabin | Cabin Number |
| Embarked | Port of Embarkation |

---

# Project Workflow

## 1. Import Required Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

Visualization style:

```python
sns.set_style("whitegrid")
```

---

## 2. Load Dataset

```python
df = pd.read_csv("tested.csv")
```

Initial inspection performed using:

```python
df.head()
df.shape
df.info()
df.describe()
```

---

# Data Cleaning

## Missing Value Analysis

Missing values were identified using:

```python
df.isnull().sum()
```

### Age

Missing values replaced with median age.

```python
df['Age'].fillna(df['Age'].median(), inplace=True)
```

### Fare

Missing fare value replaced with median fare.

```python
df['Fare'].fillna(df['Fare'].median(), inplace=True)
```

### Cabin

Missing cabin values replaced with:

```python
"Unknown"
```

```python
df['Cabin'].fillna('Unknown', inplace=True)
```

---

## Duplicate Records

Duplicate rows checked using:

```python
df.duplicated().sum()
```

No significant duplicates were found.

---

# Univariate Analysis

Univariate analysis focuses on understanding the distribution of individual variables.

---

## Age Analysis

### Statistical Measures

- Mean
- Median
- Mode
- Minimum
- Maximum
- Variance
- Standard Deviation
- Skewness

### Visualizations

- Histogram
- Boxplot

### Findings

- Most passengers were between 20 and 40 years old.
- Distribution is slightly skewed.
- A few elderly passengers appear as outliers.

---

## Fare Analysis

### Statistical Measures

- Mean
- Median
- Mode
- Standard Deviation
- Skewness

### Visualizations

- Histogram
- Boxplot

### Findings

- Most passengers paid low fares.
- Fare distribution is highly right-skewed.
- Several extreme fare outliers are present.

---

## SibSp Analysis

### Description

Number of siblings/spouses aboard.

### Findings

- Majority traveled alone.
- Distribution concentrated around zero.
- Few large family groups exist.

### Visualizations

- Histogram
- Boxplot

---

## Parch Analysis

### Description

Number of parents/children aboard.

### Findings

- Most passengers traveled without parents or children.
- Few passengers traveled in larger families.

### Visualizations

- Histogram
- Boxplot

---

# Categorical Variable Analysis

---

## Survival Analysis

### Visualizations

- Count Plot
- Pie Chart

### Findings

- Dataset contains both survivors and non-survivors.
- Survival proportions can be clearly visualized.

---

## Gender Analysis

### Visualizations

- Count Plot
- Pie Chart

### Findings

- Passenger distribution varies between males and females.

---

## Passenger Class Analysis

### Classes

- First Class
- Second Class
- Third Class

### Findings

- Third-class passengers form the largest group.
- First-class passengers form the smallest group.

### Visualizations

- Count Plot
- Pie Chart

---

## Embarked Analysis

### Categories

- C = Cherbourg
- Q = Queenstown
- S = Southampton

### Findings

- Southampton was the most common embarkation point.
- Cherbourg and Queenstown had fewer passengers.

### Visualizations

- Count Plot
- Pie Chart

---

## Cabin Analysis

Large number of cabin values were missing.

Missing values replaced with:

```python
Unknown
```

### Visualization

- Known vs Unknown Cabin Countplot
- Cabin Availability Pie Chart

### Observation

Most passengers did not have cabin information recorded.

---

# Bivariate Analysis

Bivariate analysis explores relationships between two variables.

---

## Survival vs Gender

### Visualizations

- Countplot
- Survival Rate Bar Chart

### Findings

- Female passengers had significantly higher survival rates.
- Males accounted for most non-survivors.

---

## Survival vs Passenger Class

### Visualization

- Countplot

### Findings

- First-class passengers had better survival rates.
- Third-class passengers experienced lower survival rates.

---

## Survival vs Age

### Visualization

- Boxplot

### Findings

- Survivors and non-survivors show different age distributions.
- Certain age groups may have received priority.

---

## Survival vs Fare

### Visualization

- Boxplot

### Findings

- Passengers paying higher fares generally had better survival chances.

---

## Survival vs Embarked

### Visualization

- Countplot

### Findings

- Survival percentages differed by embarkation port.

---

## Passenger Class vs Gender

### Visualization

- Countplot

### Findings

- Gender distribution varies across passenger classes.

---

## Passenger Class vs Fare

### Visualization

- Boxplot

### Findings

- First-class passengers paid significantly higher fares.

---

## Age vs Fare

### Visualization

- Scatterplot

### Correlation

```python
df[['Age','Fare']].corr()
```

### Findings

- Weak positive relationship between Age and Fare.
- Age had little influence on ticket fare.

---

# Multivariate Analysis

---

## Correlation Heatmap

Generated using:

```python
sns.heatmap()
```

### Findings

- Reveals relationships among numerical variables.
- Passenger Class and Fare have strong associations.
- Age has weak correlation with most features.

---

## Passenger Class + Gender + Survival

### Visualization

```python
sns.catplot()
```

### Findings

- Survival patterns differ across class and gender combinations.
- Higher-class passengers generally survived more often.

---

## Pivot Table Analysis

Created to examine survival probabilities:

```python
pd.pivot_table()
```

### Findings

- Survival varies significantly across passenger class and gender.

---

## GroupBy Analysis

Average fare calculated across groups:

```python
df.groupby(['Sex','Pclass'])['Fare'].mean()
```

### Findings

- Higher passenger classes paid considerably more.

---

# Feature Engineering

---

## Family Size

Created new variable:

```python
FamilySize = SibSp + Parch + 1
```

### Purpose

Measure total family members traveling together.

### Findings

- Family size influences travel behavior.
- Certain family sizes show different survival patterns.

---

## Age Groups

Age categorized into:

- Child
- Teen
- Young Adult
- Adult
- Senior

Using:

```python
pd.cut()
```

### Findings

- Survival patterns vary across age groups.

---

# Pairplot Analysis

Numerical variables analyzed:

- Age
- Fare
- Pclass
- SibSp
- Parch

### Findings

- Presence of Fare outliers.
- Weak correlations among many variables.
- Visible clustering patterns.

---

# Key Insights

✅ Most passengers were between 20 and 40 years old.

✅ Fare distribution was highly right-skewed.

✅ Most passengers traveled alone.

✅ Third-class passengers formed the majority.

✅ Southampton was the most common embarkation port.

✅ Cabin information was missing for many passengers.

✅ Female passengers had higher survival rates.

✅ Higher-class passengers showed better survival outcomes.

✅ Passengers paying higher fares generally survived more often.

✅ Passenger class strongly influenced fare paid.

✅ Family size affected travel and survival patterns.

✅ Fare contains several extreme outliers.

✅ Age showed only a weak relationship with ticket fare.

---

# Visualizations Created

- Histograms
- Boxplots
- Countplots
- Pie Charts
- Scatter Plots
- Heatmaps
- Pairplots
- Catplots

---

# Conclusion

This Exploratory Data Analysis successfully identified important passenger characteristics, travel behaviors, and survival patterns within the Titanic dataset. The analysis revealed that passenger class, gender, fare, and family structure were significant factors related to survival outcomes. While age showed limited influence on fare, higher-class passengers generally paid more and experienced better survival rates. The project demonstrates how data cleaning, statistical analysis, feature engineering, and visualization can be combined to extract meaningful insights from real-world datasets.

---

# Learning Outcomes

After completing this project, the following skills were strengthened:

✅ Data Cleaning

✅ Missing Value Handling

✅ Exploratory Data Analysis (EDA)

✅ Statistical Analysis

✅ Data Visualization

✅ Feature Engineering

✅ Correlation Analysis

✅ GroupBy Operations

✅ Pivot Tables

✅ Business Insight Generation

✅ Matplotlib and Seaborn Visualization

✅ Real-World Dataset Interpretation
