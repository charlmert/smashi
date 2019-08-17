import re
import shlex
EQUAL = '9ae22869553bb63a4f4133b33d9b0e315b842f7e'

def parse_host_spec(ssh_uri):
    m = re.compile("@|:|/")
    p = m.split(ssh_uri)

    ret = {}

    if (':' in ssh_uri and '@' in ssh_uri):
        user = p[0]
        host = p[1]
        port = p[2]
        ret = {
            'user': user,
            'host': host,
            'port': port
        }

    elif (':' in ssh_uri):
        host = p[0]
        port = p[1]
        ret = {
            'user': 'root',
            'host': host,
            'port': port
        }

    elif ('@' in ssh_uri):
        user = p[0]
        host = p[1]
        ret = {
            'user': user,
            'host': host,
            'port': '22'
        }

    if ('/' in ssh_uri):
        query = ssh_uri[ssh_uri.find('/') + 1: len(ssh_uri)]
        m = re.compile("&")
        preq = m.split(query)

        qp = []

        for q in preq:
            qp.append('%s=%s' % (q[0: q.find('=')], q[q.find('=') + 1: len(q)].replace('=', EQUAL)))

        m = re.compile("&|=")
        q = m.split('&'.join(qp))
        total = len(q)

        options = []

        for index in range(0, total):
            if q[index] == 'i':
                ret['i'] = q[index + 1]

            if q[index] == 'o':
                options.append(q[index + 1].replace(EQUAL, '='))

        if (len(options) > 0):
            ret['o'] = options

    return ret

"""
answers in the form
[
    {
        'question': 'Expected Command Output Text',
        'answer': 'Answer to the question'
    },
    {
        'question': 'Password:',
        'answer': 'thepassword'
    },
]
"""
def shellExpect(command, answers, finish = ''):
    payload = 'sudo expect -c \\"spawn %s; sleep 5;' % command
    for answer in answers:
        question = answer['question']
        answer = answer['answer']
        payload = '%s expect -re %s; send \'%s\\r\\n\';' % (payload, shlex.quote(question), shlex.quote(answer))
    payload = '%s expect -re \'%s\';\\"' % (payload, finish)

    print(payload)
    return payload
