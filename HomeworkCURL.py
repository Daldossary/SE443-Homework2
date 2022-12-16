import requests as req

respList = []

#URL request to return list of all users (GET 1)
getAllUsers = "https://reqres.in/api/users?page=2"

#URL request to return specific user (GET 2)
getSpecificUser = "https://reqres.in/api/users/2"

#URL request to return invalid user (GET 3)
getInvalidUser = "https://reqres.in/api/users/23"

#URL request to register a user (POST 1)
newUser = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
    }
postRegister = "https://reqres.in/api/register"

#URL request to login a user (POST 2)
existingUser = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
postLogin = "https://reqres.in/api/login"

#URL request to login without a password(POST 3)
invalidUser = {
    "email": "peter@klaven"
}

#Store responses after GET and POST commands to API
respList.append(req.get(getAllUsers))
respList.append(req.get(getSpecificUser))
respList.append(req.get(getInvalidUser))
respList.append(req.post(postRegister, json = newUser))
respList.append(req.post(postLogin, json = existingUser))
respList.append(req.post(postLogin, json = invalidUser))

#Adding a response that is purely numerical
respList.append(4423177.88)

#Ask user to enter their own API request for GET
getRequest = input("Enter GET URL: ")
respList.append(req.get(getRequest))

#Ask user to enter their own API request for POST (register):
registerJSON = input("Enter registration JSON for POST request: ").json()
respList.append(req.post(postRegister, json = registerJSON))

#Checking if responses are valid
for i in range(len(respList)):
    if not isinstance(respList[i], req.models.Response):
        print("\nINVALID RESPONSE: NOT STRING\n")
    else: 
        if respList[i].status_code == 200:
            print("\nRESPONSE VALID, JSON RETRIEVED: \n", respList[i].json())
        elif respList[i].status_code == 400:
            print("\nRESPONSE INVALID: BAD REQUEST, ERROR: \n", respList[i].json())
        elif respList[i].status_code == 404:
            print("\nRESPONSE INVALID: NO RESPONSE, ERROR: \n", respList[i].json())
        
