# if something could regularly fail in one or more specific ways, it is often best to use a try...except statement to handle those situations.

datafile_index = {
    # Omitted for brevity.
    # Just assume there's a lot of data in here.
}


def get_datafile_id(subject):
    identi = datafile_index[subject]
    print(f"See datafile {identi}.")

datafile_index["Clara Oswald"] = 2342342
get_datafile_id("Clara Oswald")
get_datafile_id("Ashildir")

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
#   File "c:\Users\webnl\Documents\_workspace\loggar-py\py-refs\py-errors\ex.3.exceptions.py", line 14, in <module>
#     get_datafile_id("Clara Oswald")
#   File "c:\Users\webnl\Documents\_workspace\loggar-py\py-refs\py-errors\ex.3.exceptions.py", line 10, in get_datafile_id
#     identi = datafile_index[subject]
# KeyError: 'Clara Oswald'
