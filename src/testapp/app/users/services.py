from testapp.app.users.models import User

def get_all_users():
    users = User.query.all()[:5]
    return users


def get_user_by_email(email):
    user = User.query.filter_by(email=email).first_or_404(
        description='There is no data with {}'.format(email))
    if user:
        return user
    else:
        return None

def get_user_by_id(id):
    user = User.query.get(id)
    if user:
        return user
    else:
        return None