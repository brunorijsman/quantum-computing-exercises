import os
import qiskit

if "QX_API_TOKEN" not in os.environ:
    print("Set environment variable QX_API_TOKEN")
    exit(1)
QX_API_TOKEN = os.environ["QX_API_TOKEN"]

qiskit.register(QX_API_TOKEN, "https://quantumexperience.ng.bluemix.net/api")
print("Registered")

print("Available backends:")
print(qiskit.available_backends())
