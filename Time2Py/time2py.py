# -*- coding: utf-8 -*-

import sys
import os
from io import StringIO
import contextlib
import subprocess
from Exception2Chinese import *
# -*- coding: utf-8 -*-


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line
    return buf


if __name__ == "__main__":
    st = get_stdin()
    # print(st)
    with stdoutIO() as s:
        try:
            tmpfold = os.getenv("TMPDIR", "/tmp")
            tmpfile = "%s/%s" % (tmpfold, "script.py")
            # print(tmpfile)
            f = open(tmpfile, 'w')
            print(st, file=f)
            f.close()
            p1 = subprocess.Popen(["python3", tmpfile], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p2, p3 = p1.stdout.read().decode('utf-8'), p1.stderr.read().decode('utf-8')
            if len(p2) > 0:
                print(p2)
            else:
                p3 = trans_exception_to_chinese(p3)
                print(p3)
        except BaseException as e:
            print(e)
    print(s.getvalue())
