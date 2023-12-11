from models.db import db
import datetime

class PatientModel(db.Model):
    __tablename__ = 'pacientes'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column("Name", db.String(50))
    age = db.Column("Age", db.Integer)
    sex = db.Column("Gender", db.Integer)
    cp = db.Column("ChestPain", db.Integer)
    trestbps = db.Column("RestingBloodPressure", db.Integer)
    fbs = db.Column("Fasting Blood Sugar", db.Integer)
    chol = db.Column("Cholesterol", db.Integer)
    thalach = db.Column("MaximumHeartBeatOnExercise", db.Float)
    exang = db.Column("IfExerciseInducesAngina", db.Float)
    oldpeak = db.Column("ElectrocardiogramSTSegmentDepression", db.Float)
    slope = db.Column("ElectrocardiogramSTSegmentSlope", db.Integer)
    ca = db.Column("NumberMajorVessels", db.Integer)
    thal = db.Column("Thalassemia", db.Integer)
    restecg = db.Column("RestingElectrocardiogram", db.Integer)
    target = db.Column("Diagnostic", db.Integer, nullable=True)
    data_insercao = db.Column(db.DateTime, default=datetime.datetime.now())