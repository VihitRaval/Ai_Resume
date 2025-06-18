
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open('job_descriptions.json', 'r') as f:
    job_data = json.load(f)

def match_jobs(resume_data):
    resume_text = resume_data['text']
    job_descriptions = [job['description'] for job in job_data]
    
    vectorizer = TfidfVectorizer().fit_transform([resume_text] + job_descriptions)
    vectors = vectorizer.toarray()

    similarity = cosine_similarity([vectors[0]], vectors[1:])[0]
    job_scores = list(zip(job_data, similarity))
    job_scores.sort(key=lambda x: x[1], reverse=True)
    return [job[0] for job in job_scores[:5]]
