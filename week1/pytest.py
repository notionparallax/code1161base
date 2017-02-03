import requests
import json


"""
Code to test python instalation
"""

with open('somefile.txt', 'a') as the_file:
    the_file.write('Hello\n')


def check_vm_ID():
    """
    Gets a unique value from each VM to check that it's actually set up
    """
    # read it from the OS
    m = open("/var/lib/dbus/machine-id", "r")
    machine_id = m.read()
    m.close()
    print machine_id

    # Write it to a file in this repo
    f = open('_checkID', 'w')
    f.write(machine_id)
    f.close()

    # ultra belt and braces - was being strange in testing
    c = open("_checkID", "r")
    read_machine_id = c.read()
    c.close()
    if machine_id != read_machine_id:
        print machine_id
        print read_machine_id
        print "Something's not right here."


def test_the_vm():
    """
    GETs a small JSON file and displays a message
    """
    width = 38

    gh_url = 'https://raw.githubusercontent.com/'
    repo = 'notionparallax/code1161base/'
    file_path = "master/week1/pySuccsessMessage.json"
    url = gh_url + repo + file_path

    try:
        r = requests.get(url)
        message = json.loads(r.text)['message']
        salutation = "All hail his noodly appendage!"
    except:
        message = "We are in the darkness"
        salutation = "Alas, all is lost"

    doesItWork = [
        "Let's test Python and Requests:\n",
        '*{s:{c}^{n}}*'.format(n=width, c='*', s=""),
        '*{s:{c}^{n}}*'.format(n=width, c=' ', s=""),
        '*{s:{c}^{n}}*'.format(n=width, c=' ', s=message),
        '*{s:{c}^{n}}*'.format(n=width, c=' ', s=""),
        '*{s:{c}^{n}}*'.format(n=width, c=' ', s=salutation),
        '*{s:{c}^{n}}*'.format(n=width, c=' ', s=""),
        '*{s:{c}^{n}}*'.format(n=width, c='*', s="")]

    for line in doesItWork:
        print line

    f = open('_requestsWorking', 'w')
    for line in doesItWork:
        f.write(line)
    f.close()


if __name__ == "__main__":
    test_the_vm()
    check_vm_ID()
