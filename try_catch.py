import requests

# a = 3
# b = [1, 0, 2]
# for elem in b:
#     try:
#         if elem == 0:
#             raise ZeroDivisionError("Mano customer error tekstas")
#         else:
#             print(f"Result is: {a / elem}")
#     except Exception as e:
#         pass


try:
    req = requests.get('https://616125ae9cc85')
    print(req.text)

except requests.exceptions.ConnectionError as e:
    with open("logs.txt", 'a') as f:
        f.write(str(e))
    print("Neveikia")





















