def authenticate():
    username = input("Enter login: ")
    password = input("Enter password: ")
    
    # Простая проверка (в реальном приложении нужно хэширование)
    if username == "admin" and password == "admin123":
        print("Authentication successful!")
        return True
    else:
        print("Authentication failed!")
        return False

if __name__ == "__main__":
    authenticate()
