from marshmallow import Schema, fields

class PatientSchema(Schema):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    sex = fields.Int(required=True)
    cp = fields.Int(required=True)
    trestbps = fields.Int(required=True)
    fbs = fields.Int(required=True)
    chol = fields.Int(required=True)
    thalach = fields.Float(required=True)
    exang = fields.Float(required=True)
    oldpeak = fields.Float(required=True)
    slope = fields.Int(required=True)
    ca = fields.Int(required=True)
    thal = fields.Int(required=True)
    restecg = fields.Int(required=True)


class PatientViewSchema(PatientSchema):
    """Define como um paciente será retornado
    """
    target = fields.Int(required=True)
