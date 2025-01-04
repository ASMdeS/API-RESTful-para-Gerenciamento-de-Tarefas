import requests

BASE = 'http://127.0.0.1:5000/tarefas'
response = requests.get(BASE + '/4')

print("Status Code:", response.status_code)
print("Response Text:", response.text)

''' response = requests.post(BASE, {
    'nome': 'assistir',
    'descricao': 'Televisao',
    'status': 'concluido',
    'data_vencimento': '2024-12-31'
})
print("Status Code:", response.status_code)
print("Response Text:", response.text)
'''