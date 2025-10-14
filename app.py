from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///edu_rural.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# -------------------- DATABASE MODELS -------------------- #
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(300))

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

# -------------------- USER LOADER -------------------- #
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# -------------------- ROUTES -------------------- #
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/courses')
@login_required
def courses():
    all_courses = Course.query.all()
    enrolled_courses = [e.course_id for e in Enrollment.query.filter_by(user_id=current_user.id)]
    return render_template('courses.html', courses=all_courses, enrolled=enrolled_courses)

@app.route('/enroll/<int:course_id>')
@login_required
def enroll(course_id):
    if not Enrollment.query.filter_by(user_id=current_user.id, course_id=course_id).first():
        enrollment = Enrollment(user_id=current_user.id, course_id=course_id)
        db.session.add(enrollment)
        db.session.commit()
        flash("Successfully enrolled in the course!", "success")
    return redirect(url_for('courses'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials!", "danger")
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash("Username already exists!", "warning")
        else:
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Account created! Please login.", "success")
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/dashboard')
@login_required
def dashboard():
    enrolled_courses = Enrollment.query.filter_by(user_id=current_user.id).all()
    courses = [Course.query.get(e.course_id) for e in enrolled_courses]
    return render_template('dashboard.html', courses=courses)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# -------------------- RUN APP -------------------- #
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Add sample courses if not exist
        if not Course.query.first():
            db.session.add_all([
                Course(name="Mathematics", description="Interactive math lessons"),
                Course(name="Science", description="Fun science experiments"),
                Course(name="English", description="Grammar & communication skills")
            ])
            db.session.commit()
    app.run(debug=True)
