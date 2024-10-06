import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
           ]
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Simbols = [ '!', '#', '$', '%', '&', '(', ')', '*', '+']
if __name__ == '__main__':
    print("Selamat datang di PythonPassword Generator!")
    nr_letters = int(input("Berapa banyak password yang anda inginkan?\n"))
    nr_symbols = int(input(f"Berapa banyak simbol yang ingin ditambahkan?\n"))
    nr_numbers = int(input(f"Berapa banyak angka yang ingin dimasukkan?\n"))
    password = ""
    for char in range(1, nr_letters + 1):
        password += random.choice(letters)
    for char in range(1, nr_symbols + 1):
        password += random.choice(Simbols)
    for char in range(1, nr_numbers + 1):
        password += random.choice(Numbers)
    print(password)
    
    # Untuk kemudahan keamanan. 
    # Ini digunakan sebagai password generator.