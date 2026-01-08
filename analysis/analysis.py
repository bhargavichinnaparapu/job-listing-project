# ================================
# Job Listing Analysis Project
# ================================

import pandas as pd
import matplotlib.pyplot as plt

# ----------------
# STEP 1: Load data
# ----------------
df = pd.read_csv("../data/job_listings.csv")

print("✅ Dataset loaded successfully")
print("\nFirst 5 rows:")
print(df.head())

print("\n📌 Columns in dataset:")
print(df.columns.tolist())

# -----------------------------
# STEP 2: Jobs count by location
# -----------------------------
if "Location" in df.columns:
    print("\n📍 Jobs by Location:")
    print(df["Location"].value_counts().head(10))

    plt.figure()
    df["Location"].value_counts().head(10).plot(kind="bar")
    plt.title("Top 10 Job Locations")
    plt.xlabel("Location")
    plt.ylabel("Number of Jobs")
    plt.tight_layout()
    plt.show()
else:
    print("⚠️ 'Location' column not found")

# --------------------------
# STEP 3: Jobs count by role
# --------------------------
role_column = None
for col in df.columns:
    if "role" in col.lower() or "job" in col.lower():
        role_column = col
        break

if role_column:
    print(f"\n💼 Jobs by Role ({role_column}):")
    print(df[role_column].value_counts().head(10))

    plt.figure()
    df[role_column].value_counts().head(10).plot(kind="bar")
    plt.title("Top 10 Job Roles")
    plt.xlabel("Role")
    plt.ylabel("Number of Jobs")
    plt.tight_layout()
    plt.show()
else:
    print("⚠️ Role column not found")

# --------------------------------
# STEP 4: Skill demand analysis
# --------------------------------
skill_column = None
for col in df.columns:
    if "skill" in col.lower():
        skill_column = col
        break

if skill_column:
    print(f"\n🛠 Skill column detected: {skill_column}")

    skills = df[skill_column].dropna().str.lower().str.split(",")
    all_skills = skills.explode().str.strip()

    top_skills = all_skills.value_counts().head(10)

    print("\n🔥 Top 10 In-Demand Skills:")
    print(top_skills)

    # Plot skills
    plt.figure()
    top_skills.plot(kind="bar")
    plt.title("Top 10 In-Demand Skills")
    plt.xlabel("Skill")
    plt.ylabel("Job Count")
    plt.tight_layout()
    plt.show()

    # Save result
    top_skills.to_csv("../data/top_skills.csv")
    print("\n💾 Top skills saved to data/top_skills.csv")

else:
    print("⚠️ No skill-related column found")

print("\n🎉 Analysis completed successfully!")
