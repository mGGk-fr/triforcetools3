#!/usr/bin/env python3

import os, triforcetools, time, sys

if len(sys.argv) != 2:
    print("NO_GAME")
    quit()

triforcetools.connect("YOUR_IP", 10703)
triforcetools.HOST_SetMode(0, 1)
triforcetools.SECURITY_SetKeycode("\x00" * 8)
triforcetools.DIMM_UploadFile(sys.argv[1])
triforcetools.HOST_Restart()
triforcetools.TIME_SetLimit(10*60*1000)
