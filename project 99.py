import os
import shutil
import time
def main():
    deleted_folders_count=0
    deleted_files_count=0

    path="/ path to delete"
    days=30
    seconds=time.time()-(days*24*60*60)
    if  os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds >=get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deleted_folders_count+=1
                break


            else:
                for folder in folders:
                    folder_path=os.path.join(root_folder, folder)
                    if second >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folders_count+=1



        for file in files:
            file_path=os.path.join(root_folder, file)
               if seconds >=get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deleted_folders_count+=1

            else:
                  if second >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folders_count+=1

            else:
                print(F"{path} is not found")
                deleted_files_count+=1

if __name__ == "__main__":
    main()
