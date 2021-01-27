class Config():
    def __init__(self):
        api_key = 'YicmXHhlMFx4ZGRceDgxXHg4ZVx4ZDZpXHhjMlx4YjFceGYwXHgxZS5ceGFhXHhjNFx4OGVqXV1ceGFmXHg5OCc'
        self.headers = {'api-key': api_key, 'accept': 'application/json'}
        self.url = f"https://jobsearch.api.jobtechdev.se/search"
        #self.tag_list = ['Python','php','Wordpress','Javascript']
        #self.tag_list = ['lager','truck','montör']
        self.tag_list = ['städare', 'fönsterputsare', 'renhållnings']
        self.city = 'Göteborg'

    def get_tag_list(self):
        return self.tag_list

    def get_city(self):
        return self.city

    def set_city(self, string):
        self.city = string