from flask import Flask, render_template, request
from resume_parser import parse_resume
from job_matcher import match_jobs
from suggestions_gpt import generate_suggestions
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['resume']
        if file:
            content = file.read()
            resume_data = parse_resume(io.BytesIO(content))
            job_matches = match_jobs(resume_data)
            suggestions = generate_suggestions(resume_data['text'])
            return render_template('index.html', resume=resume_data, jobs=job_matches, suggestions=suggestions)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
