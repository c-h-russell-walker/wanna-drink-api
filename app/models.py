import re


class ValidationError(Exception):
    pass


class WannaUser():

    def __init__(self, user_form, *args, **kwargs):
        self.username = user_form.get('username')
        self.password = user_form.get('password')
        self.preferred_styles = user_form.get('favStyles')
        self.favorites = user_form.get('favBeers')
        self.default_zip = user_form.get('zipcode')
        self.default_lat = user_form.get('latitude')
        self.default_long = user_form.get('longitude')


    def to_dict(self):
        return self.__dict__


    @staticmethod
    def is_valid(user_form):
        if not re.match(r'[^@]+@[^@]+\.[^@]+', user_form.get('username')):
            raise ValidationError('Username must be a valid email address.')
        return True
