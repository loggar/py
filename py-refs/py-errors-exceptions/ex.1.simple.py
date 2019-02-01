def initiate_security_protocol(c):
    if c == 1:
        print("Returning onboard companion to home location...")
    if c == 712:
        print("Dematerializing to preset location...")


code = int(input("Enter security protocol code: "))
initiate_security_protocol(code)

# Enter security protocol code: dd
# Traceback (most recent call last):
#   File "c:\Users\webnl\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\ptvsd_launcher.py", line 45, in <module>
#     main(ptvsdArgs)
#   File "c:\Users\webnl\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\lib\python\ptvsd\__main__.py", line 348, in main
#     run()
#   File "c:\Users\webnl\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\lib\python\ptvsd\__main__.py", line 253, in run_file
#     runpy.run_path(target, run_name='__main__')
#   File "c:\_dev\python\python37-32\Lib\runpy.py", line 263, in run_path
#     pkg_name=pkg_name, script_name=fname)
#   File "c:\_dev\python\python37-32\Lib\runpy.py", line 96, in _run_module_code
#     mod_name, mod_spec, pkg_name, script_name)
#   File "c:\_dev\python\python37-32\Lib\runpy.py", line 85, in _run_code
#     exec(code, run_globals)
#   File "c:\Users\webnl\Documents\_workspace\loggar-py\py-refs\py-errors\ex.1.simple.py", line 8, in <module>
#     code = int(input("Enter security protocol code: "))
# ValueError: invalid literal for int() with base 10: 'dd'
