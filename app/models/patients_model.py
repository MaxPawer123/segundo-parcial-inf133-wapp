from database import db


# Define la clase `Animal` que hereda de `db.Model`
# `Animal` representa la tabla `animals` en la base de datos
class Patient(db.Model):
    __tablename__ = "patients"

    # Define las columnas de la tabla `animals`
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)    
    ci = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.String(100), nullable=False)
    # Inicializa la clase `Animal`
    def __init__(self, name, lastname, ci,birth_date):
        self.name = name
        self.lastname = lastname
        self.ci = ci
        self.birth_date = birth_date


    # Guarda un animal en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los animales de la base de datos
    @staticmethod
    def get_all():
        return Patient.query.all()

    # Obtiene un animal por su ID
    @staticmethod
    def get_by_id(id):
        return Patient.query.get(id)

    # Actualiza un animal en la base de datos
    def update(self, name=None, lastname=None, ci=None,birth_date=None):
        if name is not None:
            self.name = name
        if lastname is not None:
            self.lastname = lastname
        if ci is not None:
            self.sabor = ci
        if birth_date is not None:
            self.birth_date = birth_date

        db.session.commit()

    # Elimina un animal de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()
