import qiskit

QX_CONFIG = {
    # pylint:disable=line-too-long
    "APItoken": "d57067d82fb2a81735d2aef295be55cdb139e98aa5176ccf5dd33451048895499bd927844ab4e00e0f14f6ca461eb0fab344014dfb4afbb1021509452bdc787e",
    "url":"https://quantumexperience.ng.bluemix.net/api"}

qiskit.register(QX_CONFIG['APItoken'], QX_CONFIG['url'])
print("Registered")

print("Available backends:")
print(qiskit.available_backends())
