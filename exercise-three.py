import pandas as pd

student_scores = pd.DataFrame(
    {
        "Student": [1, 2, 3, 4, 5],
        "Before": [75, 30, 100, 50, 60],
        "After": [85, 50, 100, 52, 65],
    }
)
melted_dataframe = student_scores.melt(
    id_vars=["Student"], var_name="Time", value_name="Score"
)
print(melted_dataframe)
