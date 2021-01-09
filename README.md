# Python_selenium_StackOverflow

Requirements:
1. have python installed `brew install python`
2. Install `pyenv` to use different python versions
3. Make sure ChromeDriver and GekoDriver aer in executable path
`brew install chromedriver` and `brew install geckodriver` 
```
 pyenv local 3.6.8
 pyenv virtualenvwrapper_lazy
 mkvirtualenv venv
 pip install -r requirements.txt
```
## Optionally you can also run 
```python setup.py install``` to install requirements at /usr/local/bin

### Selecting the base url

You can set the base url with `--baseUrl` cli argument (if running your app against different ENV):

```
py.test --base-url "https://any_test_env_url_to_override"
```
