# UOTD

This repository contains the source code for the UUID of the Day website, [*uuidoftheday.com*](http://www.uuidoftheday.com/).

## Running Locally

The application can be started from the command line or from Visual Studio.

### Requirements

- Windows, Mac, or Linux
- Python 2.7 or 3.4
- setuptools, pip, virtualenv (Python 2.7 only)
- An Azure Storage account
- Python Tools for Visual Studio (optional)

### Environment Variables

The following environment variables must be set on your system:
- `STORAGE_NAME` - Azure Storage account name
- `STORAGE_KEY` - Azure Storage account key
- `STORAGE_TABLE_UOTD` - Azure Table name (can be anything you want)

If you are using Visual Studio these settings can be found in the project properties.

### Command Line

#### Clone the repository and `cd` into it

#### Create a virtual environment

For Python 2.7:
```
python -m virtualenv env
```

For Python 3.4:
```
python -m venv env
```

#### Activate virtual environment

On Windows:
```
env\scripts\activate
```

On Mac/Linux:
```
source env/bin/activate
```

#### Install dependencies

```
pip install -r requirements.txt
```

#### Run using development server

```
python runserver.py
```

The console will display the URL of the application.

### Visual Studio

#### Clone the repository and open the solution file

#### Create a virtual environment

Right-click on **Python Environments** and select **Add Virtual Environment...**.
In the window that appears make sure **Download and install packages** is selected and click **Create**.

#### Run using development server

Press F5 to start debugging.
