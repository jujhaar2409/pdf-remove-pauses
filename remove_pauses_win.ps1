$Folder = '.\rmpauses'
if (Test-Path -Path $Folder) {
    "Python Virtual Environment Exists"
} else {
    python -m venv rmpauses
}

.\rmpauses\Scripts\Activate
pip install -r requirements.txt
python remove_pauses.py
deactivate