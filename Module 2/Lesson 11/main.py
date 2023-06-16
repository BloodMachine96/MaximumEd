class Windows:
    def __init__(self, version, country):
        self.version = version
        self.country = country


windows11 = Windows(11, 'Russian Federation')
# print(windows11._country)
# windows11.country = 'China'
# print(windows11._country)

print(windows11._Windows__version)
# windows11.__version = 10
# print(windows11.__version)