import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    # Send GET request
    response = requests.get(url, timeout=5)

    # Check for HTTP errors
    response.raise_for_status()

    # Convert JSON response into Python data
    users = response.json()

    print("API Data Fetched Successfully!")
    print("=" * 40)

    # Display all users
    for user in users:
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("City:", user["address"]["city"])
        print("-" * 40)

    # Search functionality
    search_name = input("\nEnter name to search: ").strip().lower()

    found = False

    for user in users:
        if search_name in user["name"].lower():
            print("\nUser Found!")
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("City:", user["address"]["city"])
            found = True

    if not found:
        print("User not found.")

except requests.exceptions.RequestException as e:
    print("API Error:", e)

except ValueError:
    print("Error: Invalid JSON response.")

except KeyError as e:
    print("Error: Missing key in JSON data:", e)