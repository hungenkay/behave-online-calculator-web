# behave-online-calculator-web

This repository demonstrates how to execute cross browser test of the calculation web-app on BrowserStack.


## Requirements

1. Python 3.7.5

    - If Python is not installed, follow these instructions:
        - For Windows, download latest python version from [here](https://www.python.org/downloads/windows/) and run the installer executable
        - For Mac and Linux, run `python --version` to see what python version is pre-installed. If you want a different version download from [here](https://www.python.org/downloads/)

2. Package Manager `pip`

    Note : `pip` comes installed with Python 2.7.9+ and python 3.4+

    - If `pip` is not installed, follow these instructions:
        - Securely download get-pip.py by following this link: [get-pip.py](https://bootstrap.pypa.io/get-pip.py) or use following cURL command to download it:

        ```sh
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        ```

        - After dowloading, run the file :

            - For Python 3

                ```sh
                python3 get-pip.py
                ```

            - For Python 2

                ```sh
                python2 get-pip.py
                ```



### Install the dependencies

To install the dependencies for Android tests, run :

- For Python 3

    ```sh
    pip3 install -r android/requirements.txt
    ```

- For Python 2

    ```sh
    pip2 install -r android/requirements.txt
    ```



## Getting Started

Refer to "config" folder, start executing cross browser test on BrowserStack by using the following steps:

- Configure value in "config/browserstack_config.json" file
- Run the following command to execute test on BrowserStack:
    ```sh
    paver run e2e
    ```