#!/bin/bash
#########################################################

# PART 5: RUN SCRIPT
source sandbox/bin/activate
echo "Start to run Python Script"
python3 scriping-rcp.py

RC1=$?
if [ ${RC1} != 0 ]; then
    echo "PYTHON RUNNING FAILED"
    echo "[ERROR:] RETURN CODE:  ${RC1}"
    echo "[ERROR:] REFER TO THE LOG FOR THE REASON FOR THE FAILURE."
    exit 1
fi
echo "PROGRAM SUCCEEDED"
deactivate
exit 0