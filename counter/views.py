from django.shortcuts import render

# b16It0m8yCTy+K7Pfu9saw==1Tmma4ijnlRUTV0U
def home(request):

    import requests
    import json

    if request.method == 'POST':

        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        requests_api = requests.get(api_url + query, headers={'X-Api-Key' : 'b16It0m8yCTy+K7Pfu9saw==1Tmma4ijnlRUTV0U'})

        try: 
            api = json.loads(requests_api.content)
            print(api)
        except Exception as e:
            api = 'oops! there is something wrong'
            print(e)
        return render(request, 'home.html', {'api': api} )

    else:
        return render(request, 'home.html', {'query' : 'Enter a valid query'})


# query = '1lb brisket and fries'
# api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
# response = requests.get(api_url, headers={'X-Api-Key': 'b16It0m8yCTy+K7Pfu9saw==1Tmma4ijnlRUTV0U'})
# if response.status_code == requests.codes.ok:
#     print(response.text)
# else:
#     print("Error:", response.status_code, response.text)