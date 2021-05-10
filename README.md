
# CWA Generator
This simple script that allows you to generate your CWA for UPRI. Microsoft Word needs to be installed in your machine for the doc2pdf converter to work.

## Quickstart

 1. Clone the repo and install dependencies using pipenv.
```
pipenv install
```
 2. Create `outputs` folder in the application root.
 3. Test your installation by running the main file using the default configuration. 
```
python main.py
```
 4. Check the result on the outputs folder.
 5. Edit `accomplishment.json` to set the date (key) and your accomplishments for that date as an array (value). A sample json is already provided.
 6. Copy your e-sig file on the resources folder. Make sure that it is a PNG file with the background already removed. Check out [this](https://www.remove.bg/) or [this](https://removal.ai/) to remove the backround in your file.
 7. Configure your global variable on `main.py` to change the following:
```
CONTRACTEE  =  Your full name in UPPERCASE
ESIG  =  Path to your esig.
ESIG_WIDTH  =  Width of your esig in mm
ESIG_HEIGHT  =  Height of your esig in mm
POSITION  =  The position under your contract
```
 8. Run the main script again.
```
python main.py
```
 
