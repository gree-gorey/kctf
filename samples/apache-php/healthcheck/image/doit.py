#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pwnlib

if "raboof1337" in pwnlib.util.web.wget("http://localhost:1337/eval.php?eval=echo(strrev('foobar').(1338-1));"):
    exit(0)

exit(1)
