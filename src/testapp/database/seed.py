import json, os

from testapp import db
from testapp.app.users.models import User

base_dir = os.path.dirname(os.path.realpath(__file__))

def seed_users():
    with open(os.path.join(base_dir, 'seed_data', 'users.json'), 'r') as users_fp:
        user_data = json.load(users_fp)
        for user in user_data:
            user_instance = User(
                id=user.get('id'),
                name=user.get('name'),
                email=user.get('email')
            )
            db.session.add(user_instance)
            db.session.commit()


def seed_data():
    # Seeding script
    seed_users()
