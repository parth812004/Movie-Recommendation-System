def send_request(url, data=None, method='GET'):
    import requests

    try:
        if method.upper() == 'GET':
            response = requests.get(url, params=data)
        elif method.upper() == 'POST':
            response = requests.post(url, json=data)
        else:
            raise ValueError("Unsupported HTTP method: {}".format(method))
        
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the response as JSON
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def handle_incoming_request(request):
    # Process the incoming request from the Streamlit app
    # This function can be expanded based on the specific requirements
    return request.json() if request.is_json else None