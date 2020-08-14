from testapp.app.users.models import User
from testapp import db

def get_all_users():
    users = User.query.all()
    users = [u.to_json() for u in users]
    return users


def get_user_by_email(email):
    user = User.query.filter_by(email=email).first_or_404(
        description='There is no data with {}'.format(email))
    if user:
        return user
    else:
        return None

def get_user_by_id(id):
    user = User.query.get(id).to_json()
    if user:
        return user
    else:
        return None

def add_user(users):
    try:
        last_user = User.query.all()[-1]
        last_id = last_user.id
        name = users.get('name')
        email = users.get('email')
        if not name or not email:
            return {
                "message": "Missing name or email in request"
            }

        user = User(
            id=last_id + 1,
            name=name,
            email=email
        )
        db.session.add(user)
        db.session.commit()

        return {
            "message": "User added successfully"
        }
    except Exception as err:
        return {
            "message": "Adding user unsuccessful",
            "error": "%s" % err
        }

def update_user(id, user):
    try:
        res = User.query.get(id)
        if not res:
            return {
                "message": "No user for the id"
            }
        name = user.get('name')
        email = user.get('email')
        
        if name:
            res.name = name
        
        if email:
            res.email = email
        db.session.commit()

        return {
            "message": "User updated successfully"
        }
    except Exception as err:
        return {
            "message": "updating user unsuccessful",
            "error": "%s" % err
        }
