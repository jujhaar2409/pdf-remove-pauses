if [ -d "rmpauses" ]; then
    echo "Python Virtual Environment Exists"
else
    python3 -m venv rmpauses 
fi

source rmpauses/bin/activate
pip install -r requirements.txt
python remove_pauses.py
deactivate