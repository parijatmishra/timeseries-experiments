# timeseries-experiments

Jypyter notebooks, Python modules and sample data for learning about time series analysis and forecasting.

1. Before running the code, create a virtual environment and run: `pip -r requirements.txt` to install required packages.
2. Activate the virtualenv:

   Linux/MacOS:
   ```
   bash$ source .venv/bin/activate
   ```

   Windows (Powershell):
   ```
   PS C:\> Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
   PS C:> .venv\Scripts\Activate.ps1 -Verbose -Prompt "ts"
   ```

2. Before running code that needs data sets, downthem (see `Dataset download` below).

## Dataset download

1. Get Kaggle API key:
    - Login to [Kaggle](https://www.kaggle.com)
    - Go to [Settings](https://www.kaggle.com/settings)
    - Under 'API', click 'Create New Token', and save the resulting file as `api_keys/kaggle.json`

2. Run the script: `python scripts/data_download.py`
