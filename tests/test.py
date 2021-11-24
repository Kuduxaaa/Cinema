def test(filters = {}):
    url = 'https://example.com/api/v1/?x=1'
    for filter in filters:
        url = url + f'&filters[{filter}]={filters[filter]}&'
        
    return url[:(len(url) - 1)]

test({
    'genre': '200',
    'uploaded_by': 'dges'
})