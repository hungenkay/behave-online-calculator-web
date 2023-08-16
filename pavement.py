from paver.easy import *
from paver.setuputils import setup
import sys, os, threading, platform, json
sys.path.append(os.getcwd())
from utilities.json_utilities import *


CONFIG = get_object_from_file(os.path.join(\
    os.path.dirname(__file__), "config/browserstack_config.json"))

setup(
    name = "behave-browserstack",
    version = "0.1.0",
    author = "BrowserStack",
    author_email = "hung.nguyenkim.1983@gmail.com",
    description = ("Behave Integration with BrowserStack"),
    packages=['features']
)

def run_behave_browserstack_test(task_id=0) -> None:
    """Run the browserstack test based on the tag name"""
    if platform.system() == 'Windows':
        sh("SET TASK_ID={0} & behave --tags={1} --no-capture --no-skipped --format plain".\
            format(task_id, CONFIG['tags']))
    else:
        sh("export TASK_ID={0} && behave --tags={1} --no-capture --no-skipped --format plain".\
            format(task_id, CONFIG['tags']))

@task
@consume_nargs(1)
def run(args) -> None:
    if (args[0] == 'e2e'):
        number_of_browser = len(CONFIG['environments'])
        jobs = []
        for index in range(number_of_browser):
            thread = threading.Thread(target=run_behave_browserstack_test,args=(index,))
            jobs.append(thread)
            thread.start()

        for thread in jobs:
            thread.join()
    else:
        print("Wrong paver task given")
