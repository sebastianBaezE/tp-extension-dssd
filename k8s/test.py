import requests
import time

# Configurations
KUBERNETES_SERVICE_URL = "http://api-sorteo.local/generate-token"  # Replace with your Kubernetes service URL
POINT_ID = "12345"  # Example point ID for testing
NUMBER_OF_REQUESTS = 10000000000000000 # Number of test requests to send
DELAY_BETWEEN_REQUESTS = 2  # Delay between requests in seconds


def test_generate_token():
    """
    Sends multiple POST requests to the /generate-token endpoint
    to test Kubernetes functionality.
    """
    print(f"Testing Kubernetes service at {KUBERNETES_SERVICE_URL}")
    
    for i in range(1, NUMBER_OF_REQUESTS + 1):
        payload = {"id_punto": POINT_ID}
        try:
            # Send a POST request to the endpoint
            response = requests.post(KUBERNETES_SERVICE_URL, json=payload)
            
            # Print the results
            if response.status_code == 200:
                print(f"Request {i}: Success")
                print(f"Response: {response.json()}")
            else:
                print(f"Request {i}: Failed with status code {response.status_code}")
                print(f"Error: {response.text}")
        except Exception as e:
            print(f"Request {i}: Error occurred - {str(e)}")
        
        # Wait between requests
        # time.sleep(DELAY_BETWEEN_REQUESTS)


if __name__ == "__main__":
    test_generate_token()
