import flask
import psycopg2
from flask import request, jsonify
from psycopg2.extras import RealDictCursor

app =flask.Flask(__name__)
app.config["DEBUG"] = True

connection = psycopg2.connect(
    host="localhost",
    port="5432",
    database="pet_hotel"
)

@app.route('/owner', methods=['GET'])
def list_owners():
    cursor = connection.cursor(cursor_factory=RealDictCursor)

    postgreSQL_select_Query = "SELECT * FROM owner"
    # execute query
    cursor.execute(postgreSQL_select_Query)
    # Selecting rows from mobile table using cursor.fetchall
    owners= cursor.fetchall() 
    #respond, status 200 is added for us
    return jsonify(owners)

@app.route('/owner', methods=['POST'])
def add_owner():
    print('request.json is a dict!', request.json)
    print('if you\'re using multiform/form data, use request.form instead!', request.form)
    name = request.json['owner']
    # pets_id = request.json['pets_id']
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        print(name)
        insertQuery = "INSERT INTO owner (name) VALUES (%s)"

        cursor.execute(insertQuery, (name))
        connection.commit()
        count = cursor.rowcount
        print(count, "Owner Added")

        result = {'status': 'CREATED'}
        return jsonify(result), 201
    except (Exception,  psycopg2.Error) as error:

        print("Failed to insert owner", error)

        result = {'status': 'ERROR'}
        return jsonify(result), 500
    finally:
        if(cursor):
            cursor.close()

# @app.route('api/owners', methods=['PUT'])
# def update_owner():
#     try:
#         cursor = connection.cursor(cursor_factory=RealDictCursor)

#         print(name, pets_id )
#         updateQuery = "UPDATE"
app.run()    