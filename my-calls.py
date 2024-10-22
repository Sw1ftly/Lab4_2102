import httpx

url = "https://verbose-telegram-q77rj5wqqv45cg7x-5000.app.github.dev/"

# Example 1: Successful login
authData1 = {
    "id": "yasin.ahmed@uconn.edu",
    "token": "f99aa8b8573062e9802f4fc0807ae1cb"
}
response = httpx.post(url + "login", data=authData1)
print("Login attempt 1:")
print(response.status_code)
print(response.text)

# Example 2: Another successful login
authData2 = {
    "id": "yasin.ahmed@uconn.edu",
    "token": "f99aa8b8573062e9802f4fc0807ae1cb"
}
response = httpx.post(url + "login", data=authData2)
print("Login attempt 2:")
print(response.status_code)
print(response.text)

# Example 3: Failed login with incorrect token
authData3 = {
    "id": "yasin.ahmed@uconn.edu",
    "token": "wrong_token_value"
}
response = httpx.post(url + "login", data=authData3)
print("Login attempt 3:")
print(response.status_code)
print(response.text)

# Perform a protected request after successful login
headers = {"Authorization": f"Bearer {authData1['token']}"}
response = httpx.get(url + "some_protected_endpoint", headers=headers)
print("Access protected endpoint with valid token:")
print(response.status_code)
print(response.text)

# Perform a protected request with an invalid token
headers = {"Authorization": "Bearer invalid_token"}
response = httpx.get(url + "some_protected_endpoint", headers=headers)
print("Access protected endpoint with invalid token:")
print(response.status_code)
print(response.text)