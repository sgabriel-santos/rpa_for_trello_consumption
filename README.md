The main objective of this project is to generate a document containing information about the trello cards of a given board. This system can be used by institutes as an aid for the development of RD.

## 1. Project Configuration

<details>
  <summary><strong>Project Dependencies</strong></summary>

 it's necessary install dependencies below:

- [Python](https://www.python.org/downloads/)
- [Chrome](https://www.google.com/chrome/)

</details>

<details>
  <summary><strong>Configure credentials</strong></summary>

Update file `config\credentials.py`. Replace informations with your credentials to do login in Trello and get information of Board

 ```sh
LOGIN='your_login'
PASSWORD='your_password'
 ```

</details>

<details>
  <summary><strong>Configure project information</strong></summary>

Update file `config\app_config.json` to application access the desired project. Each field of json is explained below

| Field | Values | Description |
| ----- | ------ | ----------- |
| check_trello | Y/N | If Y, the application will open webdriver and get project information in Trello. For this, the credentials must be configured|
| use_config_project_and_tag | Y | For now, this field should remain at Y |
| project | Any string | Project name that desire get information. The application will use this value to know which project must get information in Trello |
| tag | Array of String | The application will use these Tags to filter the information obtained. Only cards with these tags will be added to the generated document |
| lists_to_get | Array of String | The application will use these Tags to filter the information obtained. Only cards from the list informed will be added to the generated document |

</details>

## 2. Starting application
<details>
<summary><strong>Start Application</strong></summary>

- Open cmd in the `\rpa_for_trello_consumption` directory
- Create a python virtual enviroment with: `py -m venv venv`
- Open the virtual enviroment with: `venv\Scripts\activate` (on Windows)
- Install the project dependencies with: `pip install -r requirements.txt`

```sh
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
- To start application performing the command
```sh
py .\trello_documentation.py
```
- A webdriver will open and access trello with credentials configured in `config\credentials.py`

</details>