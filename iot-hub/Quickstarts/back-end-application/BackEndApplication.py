# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.

# pylint: disable=E0611
import sys
import os
from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.protocol.models import CloudToDeviceMethod

# The service connection string to authenticate with your IoT hub.
# Using the Azure CLI:
# az iot hub show-connection-string --hub-name {your iot hub name} --policy-name service
CONNECTION_STRING = "{Your IoT hub service connection string}"
DEVICE_ID = "{Your IoTHub Device ID}"

# Details of the direct method to call.
METHOD_NAME = "SetTelemetryInterval"
METHOD_PAYLOAD = "10"

def iothub_devicemethod_sample_run():
    try:
        # Connect to your hub.
        registry_manager = IoTHubRegistryManager(CONNECTION_STRING)

        # Call the direct method.
        deviceMethod = CloudToDeviceMethod(
            method_name = METHOD_NAME,
            payload = METHOD_PAYLOAD
        )
        response = registry_manager.invoke_device_method(DEVICE_ID, deviceMethod)

        print ( "" )
        print ( "Device Method called" )
        print ( "Device Method name       : {0}".format(METHOD_NAME) )
        print ( "Device Method payload    : {0}".format(METHOD_PAYLOAD) )
        print ( "" )
        print ( "Response status          : {0}".format(response.status) )
        print ( "Response payload         : {0}".format(response.payload) )

        input("Press Enter to continue...\n")

    except Exception as ex:
        print("Unexpected error {0}".format(ex))
    except KeyboardInterrupt:
        print("iothub_registry_manager_sample stopped")

if __name__ == '__main__':
    print ( "IoT Hub Python quickstart #2..." )
    print ( "    Connection string = {0}".format(CONNECTION_STRING) )
    print ( "    Device ID         = {0}".format(DEVICE_ID) )

    iothub_devicemethod_sample_run()