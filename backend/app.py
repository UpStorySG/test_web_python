from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from models import User, Product, Contact, db, generate_random_data

app = Flask(__name__)
CORS(app)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portal.db'
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)
db.init_app(app)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # user = User.query.filter_by(username=data['username']).first()
    if 'user'== data['username'] and '123456' == data['password']:
        access_token = create_access_token(identity=data['username'])
        return jsonify({"token": access_token}), 200
    return jsonify({"msg": "Invalid credentials"}), 401

@app.route('/api/logout', methods=['POST'])
@jwt_required()
def logout():
    return jsonify({"msg": "Successfully logged out"}), 200

@app.route('/api/products')
def get_products():
    
    
    '''
代码补充区域
代码补充区域
代码补充区域
'''
    pass

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    data = request.get_json()
    contact = Contact(
        name=data['name'],
        email=data['email'],
        message=data['message']
    )
    db.session.add(contact)
    db.session.commit()
    return jsonify({"msg": "Contact submitted successfully"}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        generate_random_data()
        # db.create_all()
    app.run(debug=True)
