# ==================================
# Job Listing Analysis Project
# ==================================

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# STEP 1: Load the dataset
# -------------------------
df = pd.read_csv("../data/job_listings.csv")

print("Dataset loaded successfully")
print("\nFirst 5 rows of the dataset:")
print(df.head())

print("\nColumns available in the dataset:")
print(df.columns.tolist())

# ----------------------------------
# STEP 2: Job count by location
# ----------------------------------
if "Location" in df.columns:
    print("\nTop 10 job locations:")
    print(df["Location"].value_counts().head(10))

    plt.figure()
    df["Location"].value_counts().head(10).plot(kind="bar")
    plt.title("Top 10 Job Locations")
    plt.xlabel("Location")
    plt.ylabel("Number of Jobs")
    plt.tight_layout()
    plt.savefig("../charts/location_chart.png")
    plt.show()
else:
    print("Location column not found in dataset")

# ----------------------------------
# STEP 3: Job count by role
# ----------------------------------
role_column = None

for col in df.columns:
    if "role" in col.lower() or "job" in col.lower():
        role_column = col
        break

if role_column:
    print(f"\nTop 10 job roles based on '{role_column}':")
    print(df[role_column].value_counts().head(10))

    plt.figure()
    df[role_column].value_counts().head(10).plot(kind="bar")
    plt.title("Top 10 Job Roles")
    plt.xlabel("Job Role")
    plt.ylabel("Number of Jobs")
    plt.tight_layout()
    plt.savefig("../charts/role_chart.png")
    plt.show()
else:
    print("No role-related column found in dataset")

# ----------------------------------
# STEP 4: Skill demand analysis
# ----------------------------------
skills = ["Python", "SQL", "Excel", "Power BI"]
skill_count = {skill: 0 for skill in skills}

# Check skills in job role titles
if role_column:
    for title in df[role_column].dropna():
        for skill in skills:
            if skill.lower() in title.lower():
                skill_count[skill] += 1
else:
    print("Skill analysis skipped because role column was not found")

# Convert skill counts to DataFrame
skill_df = pd.DataFrame(skill_count.items(), columns=["Skill", "Count"])

print("\nSkill demand from job listings:")
print(skill_df)

# Plot skill demand chart
plt.figure()
plt.bar(skill_df["Skill"], skill_df["Count"])
plt.title("Skill Demand from Job Listings")
plt.xlabel("Skill")
plt.ylabel("Number of Jobs")
plt.tight_layout()
plt.savefig("../charts/skill_chart.png")
plt.show()
