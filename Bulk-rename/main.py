import os

def arrange_files(files,ext):
    file_with_ext = [file for file in files if file.endswith(ext)]
    print(file_with_ext)
    name = input(f"Enter the common name for {ext} files ")
    
    for i , file in enumerate(file_with_ext):
     
        os.rename(file,f"{name}-{i+1}{ext}")
    # print(files)
    

if __name__ == "__main__":
    files = os.listdir()
    ext = input("Enter the extension like (.txt) :")
    arrange_files(files,ext)


