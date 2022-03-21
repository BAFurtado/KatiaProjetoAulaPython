
import pickle

pickle_file_path = r'C:\Users\katia\PycharmProjects\AulaIpea\registros.pickle'

with open(pickle_file_path, 'rb') as file_obj:
    registros_convertidos = pickle.load(file_obj)

print(registros_convertidos)

primeiro_registro = registros_convertidos[0]
json_primeiro_registro = primeiro_registro[2]

print(json_primeiro_registro)
