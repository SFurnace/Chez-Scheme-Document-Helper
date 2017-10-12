from json import dump

from bs4 import BeautifulSoup
from requests import get

data_file_path = './data'

source = 'https://cisco.github.io/ChezScheme/csug9.5/summary.html'
source_home = 'https://cisco.github.io/ChezScheme/csug9.5/'


def process_source():
    result = []
    source_content = BeautifulSoup(get(source).text, 'lxml')

    for r in source_content.find_all('tr')[2:]:
        form, category, page = r.find_all('td')
        url = page.a['href']

        form = form.tt.text.strip()
        category = category.text.strip()
        url = source_home + url if url.startswith('.') else url
        title = form.split()[0].strip('()') if form.startswith('(') else form

        result.append({
            "autocomplete": title,
            "subtitle": f"form: {form}\tcategory: {category}",
            "quicklookurl": url,
            "title": title,
            "arg": url
        })

    return result


if __name__ == '__main__':
    with open(data_file_path, 'w') as f:
        dump(process_source(), f)
