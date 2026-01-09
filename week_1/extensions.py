f_name = input("File name: ").strip().lower()

if f_name.endswith(".gif"):
    print("image/gif")
elif f_name.endswith("jpg") or f_name.endswith("jpeg"):
    print("image/jpeg")
elif f_name.endswith("pdf"):
    print("application/pdf")
elif f_name.endswith("png"):
    print("image/png")
elif f_name.endswith("txt"):
    print("text/plain")
elif f_name.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream")