from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Job, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    jobs = Job.query.all()
    return render_template('index.html', jobs=jobs)

@main.route('/job/<int:id>')
def job_details(id):
    job = Job.query.get_or_404(id)
    return render_template('job_details.html', job=job)

@main.route('/post_job', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        company = request.form['company']
        location = request.form['location']

        new_job = Job(title=title, description=description, company=company, location=location)
        db.session.add(new_job)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('post_job.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/signup')
def signup():
    return render_template('signup.html')
