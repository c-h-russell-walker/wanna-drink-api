
class WannaUser():

    def __init__(self, *args, **kwargs):
        username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.preferred_styles = kwargs.get('styles')
        self.favorites = kwargs.get('favorites')
        self.default_zip = kwargs.get('zipcode')

    @staticmethod
    def is_valid(user_form):
        return True
