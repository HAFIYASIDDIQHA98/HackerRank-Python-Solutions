# Topic: Professional Skill Analysis Logic (FactSet Style)

# Data for the test
required_skills = {"Python", "SQL", "Tableau", "Excel", "Power BI"}
candidate_skills = {"Python", "HTML", "SQL", "Java"}

# 1. SET LOGIC: Common and Missing Skills
common_skills = required_skills.intersection(candidate_skills)
missing_skills = required_skills.difference(candidate_skills)

print(f"Common Skills Found: {common_skills}")
print(f"Candidate needs to learn: {missing_skills}")

# 2. LIST COMPREHENSION: Filtering long skill names (>5 chars)
long_skills = [skill for skill in required_skills if len(skill) > 5]
print(f"Long Skill Names: {long_skills}")

# 3. DICTIONARY LOGIC: Mapping skill lengths
# Creating a dictionary: {Skill: Length}
skill_metrics = {skill: len(skill) for skill in required_skills}
print(f"Skill Metrics: {skill_metrics}")

# 4. BONUS: Logic for Employee Sales
sales = {"Ali": 150, "Sara": 250, "Hafiya": 300, "Zane": 90}
bonus_eligible = set()

for name, score in sales.items():
    if score > 200:
        bonus_eligible.add(name)

print(f"Employees Eligible for Bonus: {bonus_eligible}")
