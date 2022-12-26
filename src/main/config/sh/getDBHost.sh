#!/bin/bash
cat dbHosts | cut -d ":" -f1 | sed 's|"||g'