"""Code to test python instalation.

It gets values from the filesystem and the internet
to check that everything works.
"""
from __future__ import division
from __future__ import print_function
import json
import os
import requests

LOCAL = os.path.dirname(os.path.realpath(__file__))


def check_vm_ID():
    """Look inside yourself.

    Gets a unique value from each VM to check that it's actually set up
    """
    # read it from the OS
    m = open(os.path.join(LOCAL, "/var/lib/dbus/machine-id"), "r")
    machine_id = m.read()
    m.close()
    print(machine_id)

    # Write it to a file in this repo
    f = open(os.path.join(LOCAL, '_checkID'), 'w')
    f.write(machine_id)
    f.close()

    # ultra belt and braces - was being strange in testing
    c = open(os.path.join(LOCAL, "_checkID"), "r")
    read_machine_id = c.read()
    c.close()
    if machine_id != read_machine_id:
        print(machine_id)
        print(read_machine_id)
        print("Something's not right here.")


def test_the_vm():
    """Inspect own filesystem.

    GETs a small JSON file and displays a message
    """
    width = 38

    gh_url = 'https://raw.githubusercontent.com/'
    repo = 'notionparallax/code1161base/'
    file_path = "master/week1/pySuccessMessage.json"
    url = gh_url + repo + file_path

    try:
        r = requests.get(url)
        message = json.loads(r.text)['message']
        subMessage = "All hail his noodly appendage!"
    except Exception as e:
        message = "We are in the darkness"
        subMessage = "Alas, all is lost"
        print("\nThe error message:", e)

    doesItWork = [
        "Let's test Python and Requests:\n",
        '*{s:{c}^{n}}*'.format(n=width, c='*', s=""),
        '*{s:{c}^{n}}*'.format(n=width, c=' ', s=""),
        '*{s:{c}^{n}}*'.format(n=width, c=' ', s=message),
        '*{s:{c}^{n}}*'.format(n=width, c=' ', s=""),
        '*{s:{c}^{n}}*'.format(n=width, c=' ', s=subMessage),
        '*{s:{c}^{n}}*'.format(n=width, c=' ', s=""),
        '*{s:{c}^{n}}*'.format(n=width, c='*', s="")]

    for line in doesItWork:
        print(line)

    f = open(os.path.join(LOCAL, '_requestsWorking'), 'w')
    for line in doesItWork:
        f.write(line)
    f.close()


if __name__ == "__main__":
    test_the_vm()
    check_vm_ID()
