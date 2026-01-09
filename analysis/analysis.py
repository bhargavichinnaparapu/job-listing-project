# ================================
# Job Listing Analysis Project
# ================================

import pandas as pd
import matplotlib.pyplot as plt

# ----------------
# STEP 1: Load data
# ----------------
df = pd.read_csv("../data/job_listings.csv")

print("Dataset loaded successfully")
print("\nFirst 5 rows:")
print(df.head())

print("\n Columns in dataset:")
print(df.columns.tolist())

# -----------------------------
# STEP 2: Jobs count by location
# -----------------------------
if "Location" in df.columns:
    print("\nJobs by Location:")
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
    print("'Location' column not found")

# --------------------------
# STEP 3: Jobs count by role
# --------------------------
role_column = None
for col in df.columns:
    if "role" in col.lower() or "job" in col.lower():
        role_column = col
        break

if role_column:
    print(f"\nJobs by Role ({role_column}):")
    print(df[role_column].value_counts().head(10))

    plt.figure()
    df[role_column].value_counts().head(10).plot(kind="bar")
    plt.title("Top 10 Job Roles")
    plt.xlabel("Role")
    plt.ylabel("Number of Jobs")
    plt.tight_layout()
    plt.savefig("../charts/role_chart.png")
    plt.show()
else:
    print(" Role column not found")

# ---------- Skill Demand Analysis ----------

skills = ["Python", "SQL", "Excel", "Power BI"]
skill_count = {skill: 0 for skill in skills}

#Check skills in job titles or descriptions
for title in df["Role"]:
    for skill in skills:
        if skill.lower() in title.lower():
            skill_count[skill] += 1

#Convert to DataFrame
skill_df = pd.DataFrame(list(skill_count.items()), columns=["Skill", "Count"])

#Plot Skill Chart
plt.figure()
plt.bar(skill_df["Skill"], skill_df["Count"])
plt.xlabel("Skills")
plt.ylabel("Number of Jobs")
plt.title("Skill Demand from Job Listings")
plt.show()
