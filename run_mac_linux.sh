#!/bin/sh
cd "$(dirname "$0")"
python3 -m pip install -r requirements.txt
echo "Store:  http://localhost:8501"
echo "Admin:  http://localhost:8501/admin"
python3 -m streamlit run app.py
