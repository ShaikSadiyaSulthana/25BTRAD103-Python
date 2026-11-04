#CareerPath AI – Smart Resume Analyzer and Career Recommendation Platform

from flask import Flask, request, render_template_string
import pymupdf
import re
import os
import tempfile

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

SKILLS = [
    "Python", "Java", "C++", "C", "SQL", "MySQL",
    "HTML", "CSS", "JavaScript", "React", "Flask",
    "Django", "Machine Learning", "Deep Learning",
    "Artificial Intelligence", "Data Science",
    "Data Analysis", "Pandas", "NumPy",
    "Scikit-learn", "TensorFlow", "PyTorch",
    "NLP", "Git", "GitHub", "Excel",
    "Power BI", "Tableau", "MongoDB", "AWS",
    "Azure", "Docker", "Linux", "Statistics"
]

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>CareerPath AI</title>
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
* {
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Segoe UI,Arial,sans-serif;
}

body {
    background:#0b1020;
    color:white;
}

nav {
    background:#151e35;
    padding:22px 8%;
    display:flex;
    justify-content:space-between;
    align-items:center;
    border-bottom:1px solid #303a55;
}

.logo {
    font-size:25px;
    font-weight:bold;
}

.logo span, h1 span {
    color:#a78bfa;
}

nav a {
    color:white;
    text-decoration:none;
    margin-left:20px;
}

.hero {
    padding:85px 10%;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:35px;
}

.hero-content {
    max-width:650px;
}

.tag {
    color:#a78bfa;
    letter-spacing:3px;
    font-size:13px;
    margin-bottom:20px;
}

h1 {
    font-size:45px;
    margin-bottom:20px;
}

p {
    color:#b6bfd2;
    line-height:1.7;
}

.btn {
    display:inline-block;
    background:#7655e8;
    color:white;
    padding:14px 25px;
    border:0;
    border-radius:8px;
    text-decoration:none;
    cursor:pointer;
    margin-top:20px;
}

.btn:hover {
    background:#9278f5;
}

.hero-card, .card {
    background:#151e35;
    border:1px solid #303a55;
    padding:30px;
    border-radius:15px;
}

.hero-card {
    width:300px;
}

.features {
    background:#10172b;
    padding:65px 8%;
    text-align:center;
}

.grid {
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:20px;
    margin-top:35px;
}

.card h3 {
    margin-bottom:12px;
    color:#c4b5fd;
}

.analyzer {
    padding:70px 20px;
    text-align:center;
}

form {
    max-width:650px;
    margin:30px auto;
    background:#151e35;
    border:1px solid #303a55;
    padding:35px;
    border-radius:15px;
    text-align:left;
}

label {
    display:block;
    margin:20px 0 10px;
}

input, textarea {
    width:100%;
    padding:14px;
    background:#0b1020;
    color:white;
    border:1px solid #414c69;
    border-radius:8px;
}

textarea {
    height:150px;
    resize:vertical;
}

button {
    width:100%;
    font-size:15px;
}

.error {
    color:#ff9999;
    margin:15px;
}

.results {
    max-width:1000px;
    margin:50px auto;
    padding:20px;
    text-align:center;
}

.score {
    font-size:55px;
    color:#a78bfa;
    font-weight:bold;
    margin:20px;
}

.progress {
    background:#303a55;
    height:12px;
    border-radius:20px;
    overflow:hidden;
    margin:20px 0;
}

.fill {
    background:#a78bfa;
    height:100%;
}

.result-grid {
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:20px;
    margin:30px 0;
    text-align:left;
}

.skill {
    display:inline-block;
    padding:8px 12px;
    background:#303a55;
    color:#ddd6fe;
    border-radius:20px;
    margin:5px;
    font-size:13px;
}

.matched {
    background:#164e3b;
    color:#a7f3d0;
}

.missing {
    background:#51212b;
    color:#fecaca;
}

footer {
    background:#10172b;
    text-align:center;
    padding:25px;
    color:#aab3c7;
}

@media(max-width:700px) {
    .hero {
        flex-direction:column;
        align-items:flex-start;
    }

    .hero-card {
        width:100%;
    }

    .grid, .result-grid {
        grid-template-columns:1fr;
    }

    h1 {
        font-size:34px;
    }
}
</style>
</head>

<body>

<nav>
    <div class="logo">CareerPath<span>AI</span></div>
    <div>
        <a href="/">Home</a>
        <a href="/#features">Features</a>
        <a href="/#analyzer">Analyzer</a>
    </div>
</nav>

{% if result %}

<section class="results">

    <p class="tag">YOUR ANALYSIS IS READY</p>
    <h1>Resume Analysis Results</h1>

    <div class="card">
        <h2>Resume Match Score</h2>
        <div class="score">{{ result.score }}%</div>

        <div class="progress">
            <div class="fill"
                 style="width:{{ result.score }}%">
            </div>
        </div>

        <p>Text similarity: {{ result.similarity }}%</p>
        <p>File: {{ result.filename }}</p>
    </div>

    <div class="result-grid">

        <div class="card">
            <h3>Skills Found</h3>
            {% for skill in result.skills %}
                <span class="skill">{{ skill }}</span>
            {% endfor %}
        </div>

        <div class="card">
            <h3>Matched Skills</h3>
            {% for skill in result.matched %}
                <span class="skill matched">{{ skill }}</span>
            {% else %}
                <p>No matched skills found.</p>
            {% endfor %}
        </div>

        <div class="card">
            <h3>Missing Skills</h3>
            {% for skill in result.missing %}
                <span class="skill missing">{{ skill }}</span>
            {% else %}
                <p>No missing skills identified.</p>
            {% endfor %}
        </div>

        <div class="card">
            <h3>Career Suggestions</h3>
            {% for suggestion in result.suggestions %}
                <p>• {{ suggestion }}</p>
            {% endfor %}
        </div>

    </div>

    <div class="card">
        <p>
        This score is an educational matching estimate,
        not a hiring prediction or employment guarantee.
        </p>
    </div>

    <a href="/" class="btn">Analyze Another Resume</a>

</section>

{% else %}

<section class="hero">

    <div class="hero-content">

        <p class="tag">AI POWERED CAREER ASSISTANT</p>

        <h1>
            Build Your Career With
            <span>Artificial Intelligence</span>
        </h1>

        <p>
            Analyze your resume, discover missing skills,
            compare your qualifications with job requirements
            and explore career development opportunities.
        </p>

        <a href="#analyzer" class="btn">
            Analyze My Resume →
        </a>

    </div>

    <div class="hero-card">
        <h2>Smart Resume Analysis</h2>
        <br>
        <p>✓ Resume text extraction</p>
        <p>✓ AI skill matching</p>
        <p>✓ Missing skill identification</p>
        <p>✓ Career suggestions</p>
    </div>

</section>

<section class="features" id="features">

    <h1>Our Features</h1>

    <p>Discover what CareerPath AI can do.</p>

    <div class="grid">

        <div class="card">
            <h3>Resume Analysis</h3>
            <p>Extract information from PDF resumes.</p>
        </div>

        <div class="card">
            <h3>Skill Matching</h3>
            <p>Compare your skills with job requirements.</p>
        </div>

        <div class="card">
            <h3>Career Guidance</h3>
            <p>Discover skills you can develop for your career.</p>
        </div>

    </div>

</section>

<section class="analyzer" id="analyzer">

    <h1>Analyze Your Resume</h1>

    <p>Upload your PDF resume and enter a job description.</p>

    {% if error %}
        <div class="error">{{ error }}</div>
    {% endif %}

    <form method="POST"
          action="/analyze"
          enctype="multipart/form-data">

        <label>Upload Resume (PDF, max 5 MB)</label>

        <input type="file"
               name="resume"
               accept=".pdf,application/pdf"
               required>

        <label>Target Job Description</label>

        <textarea name="job_description"
                  placeholder="Enter the job description..."
                  required></textarea>

        <button class="btn" type="submit">
            Analyze Resume →
        </button>

    </form>

</section>

{% endif %}

<footer>
    CareerPath AI | AI-Powered Resume Analyzer
    <br>
    Educational career guidance tool.
</footer>

</body>
</html>
"""


def extract_text(file_path):
    text = ""

    with pymupdf.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text() + " "

    return text


def extract_skills(text):
    found = []

    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text, re.IGNORECASE):
            found.append(skill)

    return found


def analyze_resume(resume_text, job_description):

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched = [
        skill for skill in job_skills
        if skill in resume_skills
    ]

    missing = [
        skill for skill in job_skills
        if skill not in resume_skills
    ]

    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform([
        resume_text,
        job_description
    ])

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    if job_skills:
        skill_score = len(matched) / len(job_skills)

        score = (
            0.4 * similarity +
            0.6 * skill_score
        ) * 100
    else:
        score = similarity * 100

    suggestions = [
        "Consider developing " + skill
        for skill in missing
    ]

    if not suggestions:
        suggestions = [
            "Continue improving your technical portfolio.",
            "Add relevant projects and practical experience."
        ]

    return {
        "score": round(score, 2),
        "similarity": round(similarity * 100, 2),
        "skills": resume_skills,
        "matched": matched,
        "missing": missing,
        "suggestions": suggestions
    }


@app.route("/")
def home():
    return render_template_string(
        HTML,
        result=None,
        error=None
    )


@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files.get("resume")
    job_description = request.form.get(
        "job_description", ""
    ).strip()

    if not file or not file.filename:
        return render_template_string(
            HTML, result=None,
            error="Please upload your resume."
        )

    if not file.filename.lower().endswith(".pdf"):
        return render_template_string(
            HTML, result=None,
            error="Only PDF files are supported."
        )

    if len(job_description) < 20:
        return render_template_string(
            HTML, result=None,
            error="Enter a detailed job description."
        )

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            suffix=".pdf", delete=False
        ) as temp:
            temp_path = temp.name
            file.save(temp_path)

        resume_text = extract_text(temp_path)

        if not resume_text.strip():
            raise ValueError(
                "No readable text found in PDF."
            )

        result = analyze_resume(
            resume_text,
            job_description
        )

        result["filename"] = file.filename

        return render_template_string(
            HTML,
            result=result,
            error=None
        )

    except Exception as error:
        app.logger.exception("Analysis failed")

        return render_template_string(
            HTML,
            result=None,
            error="Unable to analyze this PDF. "
                  "Please upload a readable PDF."
        )

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)


@app.errorhandler(413)
def file_too_large(error):
    return render_template_string(
        HTML,
        result=None,
        error="File size must be below 5 MB."
    ), 413


if __name__ == "__main__":
    app.run(debug=True)