#! /bin/bash -x

cd ..
cd .venv/lib/python3.11/site-packages/
zip -r dependencies .
cd -
mv -f .venv/lib/python3.11/site-packages/dependencies.zip week10/dependencies.zip