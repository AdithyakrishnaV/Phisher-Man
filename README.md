# Phishing Detection
WebApp to detect phishing websites based on machine learning methods

### Phishing Detection API Setup
- create venv using 

```powershell
python -m venv phishing-venv
```

- Activate virtual environment
    - windows powershell
        ```powershell
        .\phishing-venv\Scripts\Activate.ps1
        ```
    - Linux bash
        ```bash
        source ./phishing-venv/bin/activate
        ```
- install the requirements using pip

```bash
    pip install -r requirements.txt
```
- Run the API server in shell

```bash
    uvicorn main:app --reload
```

# Web app setup

- Move to the ui folder

```bash
    cd ./phishing-ui
```
- Install the dependancies

```bash
    npm i
```
- Start the devlopment Server

```bash
    npm run dev
```