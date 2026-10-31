#!/usr/bin/env sh
# Feasibility spike, not the build. Offline. Exit 0 if proof criteria 1, 2, 3 and 6 hold.
cd "$(dirname "$0")" && exec python3 -I absent_spike.py
