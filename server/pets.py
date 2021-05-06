import flask
import psycopg2
from flask import request, jsonify
from psycopg2.extras import RealDictCursor

app = flask.Flask(__name__)
app.config["DEBUG"] = True

connection = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="pet_hotel"
)

@app.route('/', methods=['GET'])
def list_pets():
    cursor = connection.cursor(cursor_factory=RealDictCursor)

    postgreSQL_select_Query = "SELECT * FROM pets JOIN owner ON owner.pets_id = pets.id"

    cursor.execute(postgreSQL_select_Query)

    pets = cursor.fetchall()

    return jsonify(pets) 

    # end GET for pets


@app.route('/api/pets', methods=['POST'])
def add_pet():
    print('request.json is a dict!', request.json)
    print('if you\'re using multipart/form data, use request.form instead!', request.form)
    pet = request.json['pet']
    breed = request.json['breed']
    color = reqest.json['color']
    checked_in = request.json['checked_in']
    # owner_name = request.json['owner_name']
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        print(pet_name, owner_name, breed, color, checked_in)
        insertQuery = "INSERT INTO pets (pet_name, breed, color, checked_in) VALUES (%s, %s, %s, %s)"

        cursor.execute(insertQuery, (pet_name, breed, color, checked_in))
        connection.commit()
        count = cursor.rowcount
        print(count, "Pet Added")

        result = {'status': 'CREATED'}
        return jsonify(result), 201
    except (Exception, psycopg2.Error) as error:

        print("Failed to insert book", error)
        
        result = {'status': 'ERROR'}
        return jsonify(result), 500
    finally: 
        if(cursor):
            cursor.close()


app.run()