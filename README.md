# Team Workshop - Pandas + Testing

## Activity: Pandas Joins & Filtering (15 min)

### Goal

Learn how to:
- write clean functions
- use pandas joins
- understand and test code using pytest
- use parametrized tests

---

## Your Task

Implement 2 functions in:

src/pandas_analytics_exercise.py

### 1. join_employees_with_projects
- Merge employees and projects on employee_id

Hint:
`my_dataframe.merge(df2, on="employee_id", how="<type of join>")`

---

### 2. filter_employees_by_month
- Filter employees by birth_month

Hint: `df[df["<column_name>"] == "name"]`

---

## Steps

### 1. Code
- Implement both functions
- Use clear naming and clean code

### 2. Run Tests 
```bash
> tox

OR

> pytest
```
---

### 3. Commit & Push 

```bash
# to create a new branch
git switch -C feature/<your_name>

# to push changes
git add .
git commit -m "feat: implement pandas activity"
git push origin feature/<your_name>
```
---

## Done

If all tests pass, you're good.