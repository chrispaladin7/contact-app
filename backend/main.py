from flask import flash, jsonify
from config import app, db
from models import Contact

# GET Route
@app.route("/contacts",methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(),contacts))
    return jsonify({"contacts": json_contacts})


# check if main.py is run, run directly from here. Does not the entire file
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
