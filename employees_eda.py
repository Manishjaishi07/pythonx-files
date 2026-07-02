import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set style for visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Load the data
df = pd.read_csv('employees.csv')

print("="*80)
print("EXPLORATORY DATA ANALYSIS - EMPLOYEES DATASET")
print("="*80)

# 1. DATASET OVERVIEW
print("\n1. DATASET OVERVIEW")
print("-" * 80)
print(f"Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"\nColumn names and types:")
print(df.dtypes)

# 2. FIRST FEW ROWS
print("\n2. FIRST 5 ROWS")
print("-" * 80)
print(df.head())

# 3. DATA QUALITY CHECK
print("\n3. DATA QUALITY CHECK")
print("-" * 80)
print("Missing values:")
print(df.isnull().sum())
print(f"\nMissing values (%):")
print((df.isnull().sum() / len(df) * 100).round(2))
print(f"\nDuplicate rows: {df.duplicated().sum()}")

# 4. BASIC STATISTICS
print("\n4. BASIC STATISTICS")
print("-" * 80)
print(df.describe())

# 5. CATEGORICAL VARIABLES
print("\n5. CATEGORICAL VARIABLES ANALYSIS")
print("-" * 80)
print("\nGender distribution:")
print(df['Gender'].value_counts())
print(f"\nGender percentage:")
print(df['Gender'].value_counts(normalize=True) * 100)

print("\n\nTeam distribution:")
print(df['Team'].value_counts(dropna=False))

print("\n\nSenior Management distribution:")
print(df['Senior Management'].value_counts(dropna=False))

# 6. SALARY ANALYSIS
print("\n6. SALARY ANALYSIS")
print("-" * 80)
print(f"Salary Statistics:")
print(f"  Min: ${df['Salary'].min():,.2f}")
print(f"  Max: ${df['Salary'].max():,.2f}")
print(f"  Mean: ${df['Salary'].mean():,.2f}")
print(f"  Median: ${df['Salary'].median():,.2f}")
print(f"  Std Dev: ${df['Salary'].std():,.2f}")

print("\n\nSalary by Gender:")
print(df.groupby('Gender')['Salary'].agg(['count', 'mean', 'min', 'max']))

print("\n\nSalary by Team:")
print(df.groupby('Team')['Salary'].agg(['count', 'mean', 'min', 'max']).sort_values('mean', ascending=False))

print("\n\nSalary by Senior Management:")
print(df.groupby('Senior Management')['Salary'].agg(['count', 'mean', 'min', 'max']))

# 7. BONUS ANALYSIS
print("\n7. BONUS ANALYSIS")
print("-" * 80)
print(f"Bonus % Statistics:")
print(f"  Min: {df['Bonus %'].min()}%")
print(f"  Max: {df['Bonus %'].max()}%")
print(f"  Mean: {df['Bonus %'].mean():.2f}%")
print(f"  Median: {df['Bonus %'].median():.2f}%")

print("\n\nBonus % by Gender:")
print(df.groupby('Gender')['Bonus %'].agg(['mean', 'min', 'max']))

# 8. TENURE ANALYSIS
print("\n8. TENURE ANALYSIS")
print("-" * 80)
df['Start Date'] = pd.to_datetime(df['Start Date'])
reference_date = pd.Timestamp('2026-07-02')
df['Tenure_Years'] = (reference_date - df['Start Date']).dt.days / 365.25

print(f"Tenure Statistics (years):")
print(f"  Min: {df['Tenure_Years'].min():.2f} years")
print(f"  Max: {df['Tenure_Years'].max():.2f} years")
print(f"  Mean: {df['Tenure_Years'].mean():.2f} years")
print(f"  Median: {df['Tenure_Years'].median():.2f} years")

# 9. CORRELATION ANALYSIS
print("\n9. CORRELATION ANALYSIS")
print("-" * 80)
numeric_cols = df[['Salary', 'Bonus %', 'Tenure_Years']].copy()
print("Correlation Matrix:")
print(numeric_cols.corr())

# VISUALIZATIONS
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Salary distribution
axes[0, 0].hist(df['Salary'], bins=20, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Salary Distribution', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Salary ($)')
axes[0, 0].set_ylabel('Frequency')

# Salary by Gender
df.boxplot(column='Salary', by='Gender', ax=axes[0, 1])
axes[0, 1].set_title('Salary by Gender', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Gender')
axes[0, 1].set_ylabel('Salary ($)')
plt.sca(axes[0, 1])
plt.xticks(rotation=0)

# Bonus % distribution
axes[1, 0].hist(df['Bonus %'], bins=20, color='lightcoral', edgecolor='black')
axes[1, 0].set_title('Bonus % Distribution', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Bonus %')
axes[1, 0].set_ylabel('Frequency')

# Team distribution
team_counts = df['Team'].value_counts()
axes[1, 1].barh(team_counts.index, team_counts.values, color='lightgreen', edgecolor='black')
axes[1, 1].set_title('Employee Count by Team', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Count')

plt.tight_layout()
plt.savefig('employees_eda_overview.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved visualization: employees_eda_overview.png")
plt.show()

# Additional visualization: Salary by Team
fig, ax = plt.subplots(figsize=(12, 6))
df.boxplot(column='Salary', by='Team', ax=ax)
plt.title('Salary Distribution by Team', fontsize=14, fontweight='bold')
plt.suptitle('')  # Remove default title
plt.xlabel('Team')
plt.ylabel('Salary ($)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('employees_salary_by_team.png', dpi=300, bbox_inches='tight')
print("✓ Saved visualization: employees_salary_by_team.png")
plt.show()

# Scatter plot: Salary vs Bonus %
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(df['Salary'], df['Bonus %'], alpha=0.6, s=100, c=df['Tenure_Years'], cmap='viridis')
ax.set_xlabel('Salary ($)')
ax.set_ylabel('Bonus %')
ax.set_title('Salary vs Bonus % (colored by Tenure)', fontsize=12, fontweight='bold')
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Tenure (Years)')
plt.tight_layout()
plt.savefig('employees_salary_vs_bonus.png', dpi=300, bbox_inches='tight')
print("✓ Saved visualization: employees_salary_vs_bonus.png")
plt.show()

print("\n" + "="*80)
print("EDA COMPLETE!")
print("="*80)
