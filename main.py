from flask import Flask, jsonify, make_response, request
from datas import datas


app = Flask('datas')
@app.route('/datas', methods=['GET'])
def get_sensors(): return datas


# Visualizar dados
@app.route('/datas/<int:id>', methods=['GET'])
def getID_sensors(id):
    for i in datas:
        if i.get('id') == id: return jsonify(i)


# Inserir dados
@app.route('/datas', methods=['POST'])
def insert_sensors():
    data = request.json
    datas.append(data)
    return make_response(
        jsonify(msg='Dado inserido com sucesso!',
                data=data))


# Atualizar dados
@app.route('/datas/<int:id>', methods=['PUT'])
def up_sensors(id):
    alterDT = request.get_json()
    for i, data in enumerate(datas):
        if data.get('id') == id:
            datas[i].update(alterDT)
            return jsonify(datas[i])


# Deletar dados
@app.route('/datas/<int:id>', methods=['DELETE'])
def del_sensors(id):
    for i, data in enumerate(datas):
        if data.get('id') == id:
            del datas[i]
            return jsonify({'msg': 'Dado excluído com sucesso'})


# Run
app.run(port=5000, host='localhost')