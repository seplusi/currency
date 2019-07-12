The ui test script is: test_currency_converter.py
It's placed in src/test

BEFORE:
Set the chromedriver path in test_currency_converter.py (chromedriver_path)
using selenium==3.141.0
using ddt==1.2.1
using python3.5
using chromedriver  75.0.3770.90
using geckodriver 0.24.0 ( 2019-01-28)

    Pull the master branch

Go to project base directory

    cd ~/currency

Set python path env variable

    PYTHONPATH='pwd'
    export PYTHONPATH

Go to test scritp folder and run it

    cd src/test
    python3.5 ./master_test_survey.py

Expected output

    /home/luis/Programs/pycharm/pycharm-community-2019.1.3/virtualEnv/bin/python3.5 /home/luis/Programs/pycharm/pycharm-community-2019.1.3/helpers/pydev/pydevd.py --multiproc --qt-support=auto --client 127.0.0.1 --port 42093 --file /home/luis/Programs/pycharm/pycharm-community-2019.1.3/PycharmProjects/git/currency/src/test/test_currency_converter.py -v
    pydev debugger: process 3919 is connecting

    Connected to pydev debugger (build 191.7479.30)
    test_convert_euro_2_pounds_01_11111 (__main__.TestCurrencyConverter) ... ok
    test_convert_euro_2_pounds_02_1 (__main__.TestCurrencyConverter) ... No cookie. No need to accept
    ok
    test_convert_euro_2_pounds_03_2 (__main__.TestCurrencyConverter) ... No cookie. No need to accept
    ok
    test_convert_euro_2_pounds_04_333 (__main__.TestCurrencyConverter) ... No cookie. No need to accept
    ok
    test_convert_euro_2_pounds_05_234 (__main__.TestCurrencyConverter) ... No cookie. No need to accept
    ok
    test_convert_euro_2_pounds_06_543 (__main__.TestCurrencyConverter) ... No cookie. No need to accept
    ok
    test_convert_euro_2_pounds_07_9 (__main__.TestCurrencyConverter) ... No cookie. No need to accept
    ok
    test_convert_euro_2_pounds_08_10345 (__main__.TestCurrencyConverter) ... No cookie. No need to accept
    ok
    test_convert_euro_2_pounds_09_2345 (__main__.TestCurrencyConverter) ... No cookie. No need to accept
    ok
    test_convert_euro_2_pounds_10_9876 (__main__.TestCurrencyConverter) ... No cookie. No need to accept
    ok
    test_convert_euro_cents_2_pounds (__main__.TestCurrencyConverter) ... No cookie. No need to accept
    ok
    test_convert_euro_cents_2_pounds1 (__main__.TestCurrencyConverter) ... No cookie. No need to accept
    ok

    ----------------------------------------------------------------------
    Ran 12 tests in 202.371s

    OK

    Process finished with exit code 0
