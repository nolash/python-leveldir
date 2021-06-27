#!/bin/bash

set +x
export PYTHONPATH=.
for f in `ls tests/*.py`; do
	python $f
done
set -x
