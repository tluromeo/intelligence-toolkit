# Developing 

## Requirements

- Python 3.11 ([Download](https://www.python.org/downloads/))
- wkhtmltopdf (used to generate PDF reports)

    - Windows: [Download wkhtmltopdf installer](https://wkhtmltopdf.org/downloads.html)

    - Linux:  `sudo apt-get install wkhtmltopdf`

    - MacOS: `brew install homebrew/cask/wkhtmltopdf`   


## Setup:

1. Set up a virtual environment:

    `python -m venv ./venv`

    or
    
    `python3 -m venv ./venv`

## OpenAI API

You can use OpenAI with key-based access or Azure OpenAI with [Entra ID authentication](
https://learn.microsoft.com/en-us/azure/ai-services/authentication#authenticate-with-microsoft-entra-id) access. For Azure OpenAI, ensure your account has access to the endpoint then run `az login` to connect.

### Key-based API access

Use the following instructions to set up key-based API access using environment variables.

This step is optional: you may also set up key-based API access via the Settings page of the app.

#### Linux:
Open /venv/bin/activate, add the following lines at the end of the file:
```
    # set environment variables
    export OPENAI_API_KEY=<OPENAI_API_KEY>

    # if Azure OpenAI, include the following information too:
    export OPENAI_TYPE="Azure OpenAI"
    export AZURE_OPENAI_VERSION=2023-12-01-preview
    export AZURE_OPENAI_ENDPOINT="https://<ENDPOINT>.azure.com/"
```

#### Windows:
Open venv/Scripts/Activate.ps1, add the following lines after line 167:
```
    $env:OPENAI_API_KEY="<OPENAI_API_KEY>"

    # if Azure OpenAI, include the following information too:

    $env:OPENAI_TYPE="Azure OpenAI"
    $env:AZURE_OPENAI_VERSION="2023-12-01-preview"
    $env:AZURE_OPENAI_ENDPOINT="https://<ENDPOINT>.openai.azure.com/"
``` 

## Running 

### Running via shell

1. Run the activate script: 

    `source venv/bin/activate`  (Linux)

    `.\venv\Scripts\Activate` (Windows with Powershell)

2. Install all the dependencies with pip:

    `pip install -r requirements.txt`

3. Run the project using streamlit: 

    `streamlit run app/Home.py`

### Running with docker

Download and install docker: https://www.docker.com/products/docker-desktop/

Then, in the root folder, run:

`docker build . -t intel-toolkit`

After building, run the docker container with:

`docker run -d -p 8501:8501 intel-toolkit`

Open [localhost:8501](http://localhost:8501)

## Building a Windows executable

**Note: can only build on Windows**

We use [Pynsist](https://pynsist.readthedocs.io/en/latest/) together with [NSIS (Nullsoft Scriptable Install System)](https://nsis.sourceforge.io/) to build an executable for Windows. This packages the whole project and its dependencies (including Python) into an .exe, which when installed will run the Intelligence Toolkit on the user's localhost.

To build the .exe locally, you need to install pynsis with `pip install pynsist` and NSIS by [downloading it here](https://nsis.sourceforge.io/Main_Page).

Next, run `.\installer_script.ps1` in the root of the app to perform the following steps:
- download wkhtmltox from the source (needed to generate PDF reports). 
- download python-louvain wheel (which is not available on PyPI).
- build an .exe into build\nsis.

Once finished building, you can install the application by running the .exe and open the shortcut to launch intelligence-toolkit at http://localhost:8503 in your web browser.

## Deploying with Azure

In [this tutorial](https://dev.to/keneojiteli/deploy-a-docker-app-to-app-services-on-azure-5d3h), you can learn how to create the necessary services in azure.

From there, you can deploy it manually as described, or use [our YAML file](/.vsts-ci.yml) to automatically deploy to your environment. 
