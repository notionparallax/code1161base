import requests
import json

"""
Code to test python instalation
"""


def check_vm():
    machine_id = ""
    with open("/var/lib/dbus/machine-id", "r") as machine_id_contents:
        machine_id = machine_id_contents
    with open("machine_id", "w") as m:
        m.write(machine_id)


def test_the_vm():
    """
    GETs a small JSON file and displays a message
    """
    width = 38
    gh_url = 'https://raw.githubusercontent.com/'
    repo = 'notionparallax/code1161base/'
    file_path = "vmStartup/pySuccsessMessage.json"
    url = gh_url + repo + file_path

    try:
        r = requests.get(url)
        message = json.loads(r.text)['message']
        salutation = "All hail his noodly appendage!"
    except:
        message = "We are in the darkness"
        salutation = "Alas, all is lost"

    print "Let's test Python and Requests:\n"
    print '*{s:{c}^{n}}*'.format(n=width, c='*', s="")
    print '*{s:{c}^{n}}*'.format(n=width, c=' ', s="")
    print '*{s:{c}^{n}}*'.format(n=width, c=' ', s=message)
    print '*{s:{c}^{n}}*'.format(n=width, c=' ', s="")
    print '*{s:{c}^{n}}*'.format(n=width, c=' ', s=salutation)
    print '*{s:{c}^{n}}*'.format(n=width, c=' ', s="")
    print '*{s:{c}^{n}}*'.format(n=width, c='*', s="")


if __name__ == "__main__":
    test_the_vm()
