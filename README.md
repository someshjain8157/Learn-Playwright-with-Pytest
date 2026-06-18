Example1: test_POM_example.py: Demonstrates the Page Object Model (POM) pattern with a Playwright test. Pages: BasePage.py, ABTestPage.py

Example2: test_mouse_action1.py: Mouse actions, Click on hidden link.Hover Mouse pointer on a hidden item to make that appear and click on that.

Example3: test_testbox_locator.py: Login form submission, fill the form using fill and type functions.

Exmaple4: test_expand_tree_locator.py: Expand tree and check the checkbox nodes.

Example5: test_api_get_apikey.py, Calling get API using requests Python lib.

Example6: test_api_post.py, Post API using requests Python lib.

Example7: test_api_put_apikey.py, PUt API using requests Python lib.

Example8: test_Checkbox_selector.py, Check and uncheck checkboxes in a form.

Example9: test_dowload_file.py, download a file.

Example10: test_upload_file.py, upload a file.

Example11: test_list_webtable_column_values.py

Example12: test_generate_encription_key.py, test_encript_password.py, test_login.py, Add User and encripted Password to .env file, and use that for login, Generate the encription key, encode and decode the password using the key and save incripted password in .env file and key in a secure vault.

Example13: test_Login2.py, Providing credentials as browser context for the login without entering user and password.

Example14: test_fixture_example.py, Use pytest fixtures, Fixtures help with setup and cleanup that multiple tests need. fixtures can be defined in conftest.py in tests folder.
- function fixture	Once per test function
- class fixture	Once per test class
- module fixture	Once per Python test file
- session fixture	Once per entire pytest run
- autouse fixture	Automatically runs according to its scope

Example15: test_marker.py, Configure pytest.ini, Using markers to execute specific set of tests like Sanity, Regression, Smoke. Define them in pytest.ini at root directory. generates report.html in root with test result.
pytest.ini
[pytest]
addopts = --headed -s --html=report.html --self-contained-html

markers =
    smoke: Smoke tests
    regression: Regression tests
    sanity: Sanity tests

testpaths = tests
Command: pytest -m regression .\tests\marker_test.py

Example16: test_storage_state_save.py, test_storage_state_reuse.py: Storage State in Playwright is used to save a logged-in session (cookies, localStorage, session data) and reuse it in other tests so you don't have to log in every time. Storage state allows to save user login session to auth.json file, later, use auth.json for login to the website without credentials.

Example17:test_wait_until.py, In Playwright, wait_until is mainly used with page.goto() to tell Playwright when navigation should be considered complete.
1. wait_until="commit"
Waits only until the browser receives the first response and starts loading the page.
2. wait_until="domcontentloaded"
Waits until HTML is parsed.
3. wait_until="load" (default)
Waits for the page load event.

Example18: test_wait_after_click_button.py: Submit a login page and wait until next page is loaded.

Example18: test_slow_mo.py: Playwright waits 2 second after each action using slow_mo.

Example19: test_custom_wait.py: Explicit wait for element using WAIT_FOR and WAIT_FOR_SELECTOR.

Example20: event listener: Keep listening for an event and execute a function whenever that event occurs.
test_event_listener_response.py, test_event_lisener_dialog.py, test_event_listener_popup.py
page.on("event_name", callback_function)
page.on() = register an event listener
"event_name" = request, response, dialog, console, etc.
callback_function = code to run when the event occurs

Example21: test_screenshot.py take Screenshot after clicking a link. 

Example22: test_record_video.py, Record browser test execution.

Example23: test_trace_gen_viewer.py, Trace generator and viewer
Command: playwright show-trace trace.zip

Example24: Assertions expect(): 
expect(locator).to_be_visible()
expect(locator).to_be_hidden()
expect(locator).to_be_enabled()
expect(locator).to_be_disabled()
expect(locator).to_be_editable()
expect(locator).to_be_checked()
expect(locator).not_to_be_checked()
expect(locator).to_have_text()
expect(locator).to_contain_text()
expect(locator).to_have_value()
expect(locator).to_have_attribute()
expect(locator).to_have_class()
expect(locator).to_have_count()
expect(locator).to_be_focused()
expect(page).to_have_title()
expect(page).to_have_url()

Example 25: Distributed Parallel Execution: Run Tests in parellel using pytest-xdist. run test_parallel_run_google.py, test_t_parallel_run_github.py, test_t_parallel_run_bootswatch.py in parallel in different browser instances.

Command: pytest .\tests\test_parallel_run_bootswatch.py .\tests\test_parallel_run_google.py .\tests\test_parallel_rungithub.py -n 4

Example 26: Rerun failed testcases: 1 failed out of 3 testcases. currect the input url and rerun only the failed testcases.
pytest .\tests\test_async_parallel_para_execution.py 
Command: pytest tests/test_async_parallel_para_execution.py --lf
Command: pytest tests/test_async_parallel_para_execution.py --last-failed
Command pytest--last-failedtest_async

Example 27: test_api_post_get_json.py, Reading data from a users.json file and load in database using post api, and displaying data using get api.

Example 28: Running get and post apis from excel and compare expected output with actual json output. mismatched data to be written in root/logs folder in mismatched.txt

project_root/
│
├── api_testdata.xlsx
│
├── expected_resp/
│   ├── TC001_resp_expected.json
│   ├── TC002_resp_expected.json
│
├── actual_resp/
│   ├── TC001_resp_actual.json
│   ├── TC002_resp_actual.json
├── utils/
│   ├── excel_reader.py
│   └── json_utils.py
│
└── tests/
    └── test_api_validation.py

Expample 29: Configure allure Report:
Download allure and specify the path in env path: C:\allure-2.42.1\bin
pytest.ini:
[pytest]
addopts = --alluredir=allure-results --video retain-on-failure --screenshot on

tests/conftest.py:
import subprocess
import os


def pytest_sessionfinish(session, exitstatus):
    try:
        subprocess.run(
            [
                "allure.bat",
                "generate",
                "allure-results",
                "-o",
                "allure-report",
                "--clean"
            ],
            shell=True,
            check=True
        )

        print("\n✅ Allure HTML generated: allure-report/index.html")

    except Exception as e:
        print(f"\n❌ Allure generation failed: {e}")

Command: allure open allure-report    
Starting web server...
Server started at <http://127.0.0.1:64584>. Press <Ctrl+C> to exit    


