import requests
from datetime import datetime, timedelta
from difflib import ndiff

url = ####
results_file = 'results.txt'

def check_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode('utf-8')
        with open(results_file, 'r') as file:
            yesterday_content = file.read()
        if yesterday_content:
            diff = ndiff(yesterday_content.splitlines(), content.splitlines())
            changes = [line for line in diff if line.startswith('+ ')]
            if changes:
                print(f'{url} has been updated!')
                with open(results_file, 'w') as file:
                    file.write(content)
                    print('\n'.join(changes))
            else:
                print(f'{url} has not been updated.')
        else:
            print(f'Initial run of {url}.')
            with open(results_file, 'w') as file:
                file.write(content)
    else:
        print(f'Error: {response.status_code}')

check_website(url)
