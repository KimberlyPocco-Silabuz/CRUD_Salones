from flask import Flask, render_template, flash, redirect,url_for, session, request
from app.forms import SalonesForm
from app import create_app
from app.db import db
from app.models.salones import Salon
#from app.models.alumnos import Alumno
app = create_app()

@app.route('/', methods=['GET', 'POST'])

def index(): #Registrar Salones
    salones_form=SalonesForm()

    if salones_form.validate_on_submit():
        print("El usuario envio informacion")
        salon= Salon(
            salones_form.aula.data,
            salones_form.hora_entrada.data
            
        )

        db.session.add(salon)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template("salones.html", salones_form=salones_form)  

@app.route('/salones')#listar salones
def salones():
    salones = Salon.query.all() #select * from salones
    return render_template("lista-salones.html", salones=salones)


@app.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar(id):
    salon=Salon.query.get(id)
    db.session.delete(salon)
    db.session.commit()
    return redirect(url_for('salones'))
    

@app.route('/actualizar/<int:id>', methods=['GET', 'POST'])
def vista_actualizar(id):
    salon=Salon.query.get(id)
    if request.method== 'POST':
        salon=Salon.query.get(id)
        salon.aula= request.form["aula"]
        salon.horaEntrada=request.form["horaEntrada"]
        db.session.commit() 
        return redirect(url_for('salones'))
    return render_template("actualizar-salones.html", salon=salon)
    
    

db.init_app(app)
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
