#!/bin/bash
kill -9 $(cat ~/.offlineimap/pid)
/opt/local/bin/offlineimap
