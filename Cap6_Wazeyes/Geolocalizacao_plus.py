from geopy.gecoders import Nominatim
geolocator = Nominatim(user_agent="wazeyes")

endereco=input("Digite o endereço com o número e cidade"
               "\nExemplo: Avenida Paulista, 100 São Paulo: \n")
resultado = str(geolocator.gecode(endereco)).split(",")

if resultado[0]!='None':
    print("Endereço completo: ", resultado)
    print("Bairro: ", resultado[1])
    print("Cidade: ", resultado[2])
    print("Região: ", resultado[3])