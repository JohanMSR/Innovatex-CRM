from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelos de la base de datos
class Departamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    descripcion = db.Column(db.Text)

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    departamento = db.Column(db.String(50))
    cargo = db.Column(db.String(50))
    salario = db.Column(db.Float)
    fecha_contratacion = db.Column(db.DateTime, default=datetime.utcnow)
    activo = db.Column(db.Boolean, default=True)

# Rutas principales
@app.route('/')
def index():
    total_empleados = Empleado.query.count()
    empleados_activos = Empleado.query.filter_by(activo=True).count()
    departamentos = Departamento.query.count()
    return render_template('index.html', 
                         total_empleados=total_empleados,
                         empleados_activos=empleados_activos,
                         departamentos=departamentos)

@app.route('/empleados')
def empleados():
    empleados = Empleado.query.all()
    return render_template('empleados.html', empleados=empleados)

@app.route('/empleados/nuevo', methods=['GET', 'POST'])
def nuevo_empleado():
    if request.method == 'POST':
        try:
            empleado = Empleado(
                nombre=request.form['nombre'],
                apellido=request.form['apellido'],
                email=request.form['email'],
                telefono=request.form['telefono'],
                departamento=request.form['departamento'],
                cargo=request.form['cargo'],
                salario=float(request.form['salario']) if request.form['salario'] else None
            )
            db.session.add(empleado)
            db.session.commit()
            flash('Empleado agregado exitosamente', 'success')
            return redirect(url_for('empleados'))
        except Exception as e:
            flash('Error al crear el empleado. Verifica que el email no esté duplicado.', 'error')
            db.session.rollback()
    
    departamentos = Departamento.query.all()
    return render_template('nuevo_empleado.html', departamentos=departamentos)

@app.route('/empleados/<int:id>/editar', methods=['GET', 'POST'])
def editar_empleado(id):
    empleado = Empleado.query.get_or_404(id)
    if request.method == 'POST':
        try:
            empleado.nombre = request.form['nombre']
            empleado.apellido = request.form['apellido']
            empleado.email = request.form['email']
            empleado.telefono = request.form['telefono']
            empleado.departamento = request.form['departamento']
            empleado.cargo = request.form['cargo']
            empleado.salario = float(request.form['salario']) if request.form['salario'] else None
            db.session.commit()
            flash('Empleado actualizado exitosamente', 'success')
            return redirect(url_for('empleados'))
        except Exception as e:
            flash('Error al actualizar el empleado. Verifica que el email no esté duplicado y que el salario sea un número válido.', 'error')
            db.session.rollback()
    
    departamentos = Departamento.query.all()
    return render_template('editar_empleado.html', empleado=empleado, departamentos=departamentos)

@app.route('/empleados/<int:id>/eliminar', methods=['POST'])
def eliminar_empleado(id):
    empleado = Empleado.query.get_or_404(id)
    empleado.activo = False
    db.session.commit()
    flash('Empleado desactivado exitosamente', 'success')
    return redirect(url_for('empleados'))

@app.route('/departamentos')
def departamentos():
    departamentos = Departamento.query.all()
    
    # Contar empleados por departamento
    empleados_por_dept = {}
    for dept in departamentos:
        count = Empleado.query.filter_by(departamento=dept.nombre, activo=True).count()
        empleados_por_dept[dept.nombre] = count
    
    return render_template('departamentos.html', departamentos=departamentos, empleados_por_dept=empleados_por_dept)

@app.route('/departamentos/nuevo', methods=['GET', 'POST'])
def nuevo_departamento():
    if request.method == 'POST':
        departamento = Departamento(
            nombre=request.form['nombre'],
            descripcion=request.form['descripcion']
        )
        db.session.add(departamento)
        db.session.commit()
        flash('Departamento agregado exitosamente', 'success')
        return redirect(url_for('departamentos'))
    
    return render_template('nuevo_departamento.html')

@app.route('/api/empleados')
def api_empleados():
    empleados = Empleado.query.filter_by(activo=True).all()
    return jsonify([{
        'id': e.id,
        'nombre': f"{e.nombre} {e.apellido}",
        'email': e.email,
        'departamento': e.departamento,
        'cargo': e.cargo
    } for e in empleados])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Crear departamentos de ejemplo si no existen
        if not Departamento.query.first():
            dept1 = Departamento(nombre='Recursos Humanos', descripcion='Gestión de personal')
            dept2 = Departamento(nombre='Tecnología', descripcion='Desarrollo y IT')
            dept3 = Departamento(nombre='Ventas', descripcion='Comercial y marketing')
            db.session.add_all([dept1, dept2, dept3])
            db.session.commit()
    app.run(host="0.0.0.0", port=8080, debug=True) 