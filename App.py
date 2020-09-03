from flask import Flask, render_template, request, redirect, url_for,flash
from flask_mysqldb import MySQL

# MySQL Connection
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='xxxx'
app.config['MYSQL_PASSWORD']='xxxxxx!'
app.config['MYSQL_DB']='flask_contactos'
mysql = MySQL(app)
##############################
#Settign Session
app.secret_key = 'mysecret_key'
@app.route('/')
def Index():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM contacto')
    dato = cursor.fetchall()
    return render_template('index.html', contactos = dato)
    
@app.route('/add_contactos', methods=['POST'])
def add_contactos():
    if request.method =='POST':
        NombreCompleto = request.form['fullname']
        Telefono = request.form['telefono']
        Email = request.form['email']
        cur =  mysql.connection.cursor()
        cur.execute('INSERT INTO contacto (nombre, telefono, email) VALUES (%s, %s,%s)',(NombreCompleto, Telefono, Email))
        mysql.connection.commit()
        flash('Contacto Agregado Satisfactoriamente')
        return redirect(url_for('Index'))

@app.route('/editar_contacto/<id>')
def editar_contacto(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM contacto where idcontacto= %s', (id))
    dato = cursor.fetchall()
    return render_template('editar-contacto.html', contacto = dato[0])

@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
 if request.method=='POST':
    nombre = request.form['fullname']
    telefono = request.form['telefono']
    email = request.form['email']
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE contacto
        SET nombre =  %s,
             telefono= %s,
             email= %s
        WHERE idcontacto= %s
    """, (nombre, telefono, email, id))
    mysql.connection.commit()
    flash('Contacto Actualizado')
    return redirect(url_for('Index'))

@app.route('/delete_contacto/<string:id>')
def delete_contacto(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM contacto where idcontacto={0}'.format(id))
    mysql.connection.commit()
    flash('Contacto eliminado')
    return redirect(url_for('Index'))


if __name__=='__main__':
    app.run(port=3000, debug=True)
