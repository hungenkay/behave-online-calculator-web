from selenium import webdriver
from requests.structures import CaseInsensitiveDict
from base64 import b64encode
import os, json, requests


BS_CONFIG_FILE = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' \
    in os.environ else 'config/browserstack_config.json'
TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

with open(BS_CONFIG_FILE) as data_file:
    BS_CONFIG = json.load(data_file)

bs_local = None

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] \
    if 'BROWSERSTACK_USERNAME' in os.environ else BS_CONFIG['user']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] \
    if 'BROWSERSTACK_ACCESS_KEY' in os.environ else BS_CONFIG['key']

def start_local() -> None:
    """Start browserstack local before starting of test."""
    global bs_local
    bs_local = Local()
    bs_local_args = { "key": BROWSERSTACK_ACCESS_KEY, "forcelocal": "true" }
    bs_local.start(**bs_local_args)

def stop_local() -> None:
    """Stop browserstack local after executing of test."""
    global bs_local
    if bs_local is not None:
        bs_local.stop()

def get_browser_name(session_id) -> str:
    """Get the browser name of the current session"""
    url = "https://api-cloud.browserstack.com/automate/sessions/{0}.json"\
        .format(session_id)
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    authentication = b64encode('{0}:{1}'.format(
        BS_CONFIG['user'], BS_CONFIG['key']).encode())
    headers["Authorization"] = "Basic " + str(authentication).\
        replace('b\'','').replace('\'','')
    resp = requests.get(url, headers=headers)
    return str(resp.json()['automation_session']['browser'])

def update_session_name(session_id, new_session_name) -> str:
    """Get the current session name"""
    url = "https://api-cloud.browserstack.com/automate/sessions/{0}.json"\
        .format(session_id)
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    authentication = b64encode('{0}:{1}'.format(
        BS_CONFIG['user'], BS_CONFIG['key']).encode())
    headers["Authorization"] = "Basic " + str(authentication).\
        replace('b\'','').replace('\'','')
    data = '{"name": "' + str(new_session_name) + '"}'
    resp = requests.put(url, headers=headers, data=data)
    return str(resp.status_code)

def before_scenario(context, scenario) -> None:
    """Configure before starting each scenario"""
    desired_capabilities = BS_CONFIG['environments'][TASK_ID]
    for key in BS_CONFIG["capabilities"]:
        if key not in desired_capabilities:
            desired_capabilities[key] = BS_CONFIG["capabilities"][key]
    if "browserstack.local" in desired_capabilities \
            and desired_capabilities["browserstack.local"]:
        start_local()
    context.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://%s:%s@hub.browserstack.com/wd/hub" % \
            (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY)
    )
    scenario.name = "{0} on {1} browser".format(scenario.name, \
        str(get_browser_name(context.browser.session_id)).upper())

def after_scenario(context, scenario) -> None:
    """Configure after executing each scenario"""
    if(context.browser != None):
        update_session_name(context.browser.session_id, scenario.name)
    if context.failed is True:
        context.browser.execute_script('browserstack_executor: \
            {"action": "setSessionStatus", "arguments": \
                {"status":"failed", "reason": "At least 1 assertion failed"}}')
    if context.failed is not True:
        context.browser.execute_script('browserstack_executor: \
            {"action": "setSessionStatus", "arguments": \
                {"status":"passed", "reason": "All assertions passed"}}')
    context.browser.quit()
    stop_local()