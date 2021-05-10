
# CWA Generator
This simple script allows you to generate your CWA for UPRI. 

## Quickstart

 1. Clone the repo and install dependencies using pipenv.
```
pipenv install
```
 2. Test your installation by running the main file using the default configuration. 
```
python main.py
```
 3. Check the result on the outputs folder.
 4. Edit `accomplishment.json` to set the date (key) and your accomplishments for that date as an array (value). A sample json is already provided.
 5. Copy your e-sig file on the resources folder. Make sure that it is a PNG file with the background already removed. Check out [this](https://www.remove.bg/) or [this](https://removal.ai/) to remove the backround in your file.
 6. Configure your global variable on `main.py` to change the following:
```
CONTRACTEE  =  Your full name in UPPERCASE
ESIG  =  Path to your esig.
ESIG_WIDTH  =  Width of your esig in mm
ESIG_HEIGHT  =  Height of your esig in mm
POSITION  =  The position under your contract
```
 7. Run the main script again.
```
python main.py
```
 
