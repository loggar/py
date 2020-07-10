if "var_name" in globals():
    print("var_name exists!")
elif "var_name" in locals():
    print("var_name exists locally!")
else:
    print("var_name does not exist.")
