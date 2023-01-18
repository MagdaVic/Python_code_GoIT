NAME = 'Business District'
URL = 'Website'
list_element = '<ul><a href={url}>{name}</a></li>\n'

with open('Seatle_business_district_2018.csv', 'r') as file:
    with open('Seatle_business_district_2018.html', 'a') as html:
        html.write('<ul>\n')
        headers = []
        for line in file:
            data = line.split(',')
            data[-1] = data[-1][:-1]
            # print(data)
            if not headers:
                headers = data
                name_index = headers.index(NAME)
                url_index = headers.index(URL)

                continue

            name = data[name_index]
            url = data[url_index]

            html.write(list_element.format(url=url, name=name))
        html.write('</ul>\n')
