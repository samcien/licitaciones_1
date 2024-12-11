from flask import Blueprint, request, jsonify
from . import mysql

api_bp = Blueprint('api', __name__)

# ==============================
# CRUD para la tabla Licitantes
# ==============================
@api_bp.route('/licitantes', methods=['GET'])
def get_licitantes():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Licitantes")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@api_bp.route('/licitantes', methods=['POST'])
def create_licitante():
    data = request.json
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "INSERT INTO Licitantes (nombre, direccion, telefono, correo) VALUES (%s, %s, %s, %s)"
    values = (data['nombre'], data['direccion'], data['telefono'], data['correo'])
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Licitante creado"}), 201

@api_bp.route('/licitantes/<int:id>', methods=['PUT'])
def update_licitante(id):
    data = request.json
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "UPDATE Licitantes SET nombre = %s, direccion = %s, telefono = %s, correo = %s WHERE id = %s"
    values = (data['nombre'], data['direccion'], data['telefono'], data['correo'], id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Licitante actualizado"})

@api_bp.route('/licitantes/<int:id>', methods=['DELETE'])
def delete_licitante(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "DELETE FROM Licitantes WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Licitante eliminado"})

# ===============================
# CRUD para la tabla Proveedores
# ===============================
@api_bp.route('/proveedores', methods=['GET'])
def get_proveedores():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Proveedores")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@api_bp.route('/proveedores', methods=['POST'])
def create_proveedor():
    data = request.json
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "INSERT INTO Proveedores (nombre, correo, telefono) VALUES (%s, %s, %s)"
    values = (data['nombre'], data['correo'], data['telefono'])
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Proveedor creado"}), 201

@api_bp.route('/proveedores/<int:id>', methods=['PUT'])
def update_proveedor(id):
    data = request.json
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "UPDATE Proveedores SET nombre = %s, correo = %s, telefono = %s WHERE id = %s"
    values = (data['nombre'], data['correo'], data['telefono'], id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Proveedor actualizado"})

@api_bp.route('/proveedores/<int:id>', methods=['DELETE'])
def delete_proveedor(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "DELETE FROM Proveedores WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Proveedor eliminado"})

# ================================
# CRUD para la tabla Licitaciones
# ================================
@api_bp.route('/licitaciones', methods=['GET'])
def get_licitaciones():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Licitaciones")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@api_bp.route('/licitaciones', methods=['POST'])
def create_licitacion():
    data = request.json
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "INSERT INTO Licitaciones (licitante_id, descripcion, fecha_fin, estado) VALUES (%s, %s, %s, %s)"
    values = (data['licitante_id'], data['descripcion'], data['fecha_fin'], data['estado'])
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Licitación creada"}), 201

@api_bp.route('/licitaciones/<int:id>', methods=['PUT'])
def update_licitacion(id):
    data = request.json
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "UPDATE Licitaciones SET licitante_id = %s, descripcion = %s, fecha_fin = %s, estado = %s WHERE id = %s"
    values = (data['licitante_id'], data['descripcion'], data['fecha_fin'], data['estado'], id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Licitación actualizada"})

@api_bp.route('/licitaciones/<int:id>', methods=['DELETE'])
def delete_licitacion(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "DELETE FROM Licitaciones WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Licitación eliminada"})

# ============================
# CRUD para la tabla Ofertas
# ============================
@api_bp.route('/ofertas', methods=['GET'])
def get_ofertas():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Ofertas")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@api_bp.route('/ofertas', methods=['POST'])
def create_oferta():
    data = request.json
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "INSERT INTO Ofertas (licitacion_id, proveedor_id, monto_ofrecido, estado) VALUES (%s, %s, %s, %s)"
    values = (data['licitacion_id'], data['proveedor_id'], data['monto_ofrecido'], data['estado'])
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Oferta creada"}), 201

@api_bp.route('/ofertas/<int:id>', methods=['PUT'])
def update_oferta(id):
    data = request.json
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "UPDATE Ofertas SET licitacion_id = %s, proveedor_id = %s, monto_ofrecido = %s, estado = %s WHERE id = %s"
    values = (data['licitacion_id'], data['proveedor_id'], data['monto_ofrecido'], data['estado'], id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Oferta actualizada"})

@api_bp.route('/ofertas/<int:id>', methods=['DELETE'])
def delete_oferta(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "DELETE FROM Ofertas WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Oferta eliminada"})

# ============================
# CRUD para la tabla Bitácoras
# ============================
@api_bp.route('/bitacoras', methods=['GET'])
def get_bitacoras():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Bitacoras")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@api_bp.route('/bitacoras', methods=['POST'])
def create_bitacora():
    data = request.json
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "INSERT INTO Bitacoras (descripcion, fecha, estado) VALUES (%s, %s, %s)"
    values = (data['descripcion'], data['fecha'], data['estado'])
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Bitácora creada"}), 201

@api_bp.route('/bitacoras/<int:id>', methods=['PUT'])
def update_bitacora(id):
    data = request.json
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "UPDATE Bitacoras SET descripcion = %s, fecha = %s, estado = %s WHERE id = %s"
    values = (data['descripcion'], data['fecha'], data['estado'], id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Bitácora actualizada"})

@api_bp.route('/bitacoras/<int:id>', methods=['DELETE'])
def delete_bitacora(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "DELETE FROM Bitacoras WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Bitácora eliminada"})
