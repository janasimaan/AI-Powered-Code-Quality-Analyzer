#from crypt import methods
from analyzers import analyze_code, suggest_improvments
from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def upload_code():
    if request.method == "POST":
        code = request.form["code"] #get pasted code
        uploaded_file = request.files.get("code_file") #get uploaded file

        if uploaded_file:
            code = uploaded_file.read().decode("utf-8")
        if not code:
            return "no code provided!", 400 # Handle case where no input is give
        analysis_results = analyze_code(code)
        suggestions = suggest_improvments(code)
        return (f"""
                <h1>Analysis Results:</h1>
                <pre>{analysis_results}</pre>
                <h2> Improvement Suggestions</h2>
                <pre>{suggestions}</pre>
                """)
    return render_template("upload.html")



if __name__ == "__main__":
    app.run(debug=True)