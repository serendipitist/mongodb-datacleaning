frfom bs4 import import BeautifulSoup
def options(soup,id):
    options_value =[]
    carrier_list= soup.find(id=id)
    for option in carrier_list.find_all('option'):
        option_values.append(option['values'])
        return options_values
    def print_list(label):
    