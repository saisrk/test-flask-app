import json, os

from testapp import db
from testapp.app.users.models import Usertype, Samithi

base_dir = os.path.dirname(os.path.realpath(__file__))

def seed_samithis():
    with open(os.path.join(base_dir, 'seed_data', 'samithi.json'), 'r') as samithi_fp:
        samithi_data = json.load(samithi_fp)
        for samithi in samithi_data:
            samithi_instance = Samithi(
                id=samithi.get('id'),
                name=samithi.get('name'),
                slug=samithi.get('slug')
            )
            db.session.add(samithi_instance)
            db.session.commit()


def seed_user_types():
    with open(os.path.join(base_dir, 'seed_data', 'user_types.json'), 'r') as user_types_fp:
        user_types_data = json.load(user_types_fp)
        for user_type in user_types_data:
            user_type_instance = Usertype(
                id=user_type.get('id'),
                name=user_type.get('name'),
                slug=user_type.get('slug')
            )
            db.session.add(user_type_instance)
            db.session.commit()


def seed_data():
    # Seeding script
    seed_samithis()
    seed_user_types()
