from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import PatientModel, db
from sqlalchemy.exc import SQLAlchemyError
from utils.ml_model import Model

from schemas.schemas import PatientSchema,PatientViewSchema

blp = Blueprint("Patients", "patients", description="Operações nos pacientes")


@blp.route("/patient/<int:patient_id>")
class Item(MethodView):
    @blp.response(200, PatientViewSchema)
    def get(self, patient_id):
        """Faz a busca de um paciente a partir do ID informado."""
        item = PatientModel.query.get_or_404(patient_id)
        return item

    def delete(self, patient_id):
        """Deleta um paciente a partir do ID informado."""
        patient = PatientModel.query.get_or_404(patient_id)
        db.session.delete(patient)
        db.session.commit()
        return {"message": "Patient deleted."}



@blp.route("/patient")
class ItemList(MethodView):
    @blp.response(200, PatientViewSchema(many=True))
    def get(self):
        """Faz a busca de todos os pacientes cadastrados"""
        return PatientModel.query.all()

    @blp.arguments(PatientSchema)
    @blp.response(201, PatientViewSchema)
    def post(self, patient_data):
        """Adiciona um novo paciente à base de dados"""

        # Carregando modelo
        ml_path = 'ml_model/heart_disease_knn.pkl'
        modelo = Model.carrega_modelo(self,ml_path)
        target = Model.preditor(modelo,patient_data)
        # Create a new item with the user_id
        patient = PatientModel(**patient_data, target=target)


        try:
            db.session.add(patient)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error ocurred while inserting the item.")
        return {"target": target}

