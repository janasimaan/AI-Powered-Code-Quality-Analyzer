import pylint.lint
import os
from transformers import pipeline
def analyze_code(code):
    temp_file = "temp_code.py"
    with open("temp_code.py", "w") as file:
        file.write(code)
    try:
        results = pylint.lint.Run([temp_file], do_exit=False)
        stats = results.linter.stats
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)
    return stats

code_model = pipeline("text-generation",model="microsoft/CodeGPT-small")

def suggest_improvments(code_snippet):
    suggestions = code_model(f"improve this code: \n{code_snippet}", max_length=200)
    return suggestions[0]["generated_text"]