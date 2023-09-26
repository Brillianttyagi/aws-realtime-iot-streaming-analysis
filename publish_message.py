"""
This Python script generates and publishes random user location data to an AWS IoT 
topic. It uses the AWS SDK (boto3) to interact with AWS IoT services.

The script performs the following tasks:

1. Imports necessary libraries:
   - `datetime` for generating timestamps.
   - `json` for encoding data in JSON format.
   - `random` for generating random data.
   - `time` for introducing a delay.
   - `boto3` for interfacing with AWS services.
   - `typing` for type hinting.

2. Defines a list of user names (`userNames`) to simulate multiple users.

3. Initializes the AWS IoT client using the `boto3` library.

4. Defines a function `get_random_location` that generates random user location data, 
   including latitude, longitude, user ID, and timestamp.

5. Enters an infinite loop to continuously generate and publish location data.

6. Within the loop:
   - Sleeps for 1 second using `time.sleep(1)` to control the data generation rate.
   - Calls `get_random_location` to obtain random location data in JSON format.
   - Prints the generated location data to the console.
   - Publishes the location data to the AWS IoT topic "aws-iot-location" using the AWS 
     IoT client.

This script can be used for testing or simulating location-based data publishing to an 
AWS IoT topic. It continuously generates and publishes random location data for the 
specified users with timestamps.

Note: Ensure that AWS credentials and IoT configuration are properly set up for this 
script to work with AWS IoT services.
"""

import datetime
import json
import random
import time
from typing import Dict, Union

import boto3

# List of user names
userNames = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

# Initialize AWS IoT client
iot = boto3.client("iot-data")


def get_random_location() -> Dict[str, Union[float, str]]:
    """
    Generates a random user location.

    Returns:
        Dict[str, Union[float, str]]: A dictionary containing latitude, longitude,
        userId, and dateTime.
    """
    data = {}
    data["latitude"] = round(
        random.uniform(35.0, 45.0), 6
    )  # Random latitude within a range
    data["longitude"] = round(
        random.uniform(-120.0, -70.0), 6
    )  # Random longitude within a range
    data["userId"] = random.choice(userNames)  # Randomly select a user name
    data["dateTime"] = datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )  # Current date and time
    return data


while True:
    time.sleep(1)  # Sleep for 1 second
    location_data = json.dumps(
        get_random_location()
    )  # Generate random location location_data
    print(location_data)
    response = iot.publish(
        topic="aws-iot-location",  # AWS IoT topic for location location_data
        payload=location_data,  # Publish the location_data to the topic
    )
