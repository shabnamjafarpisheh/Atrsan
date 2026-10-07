@echo off
chcp 65001 >nul
echo Installing Streamlit...
python -m pip install -r requirements.txt
echo.
echo Store:  http://localhost:8501
echo Admin:  http://localhost:8501/admin
python -m streamlit run app.py
pause
