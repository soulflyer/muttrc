#!/bin/bash
kill -9 $(cat ~/.offlineimap/pid)
/usr/bin/offlineimap
