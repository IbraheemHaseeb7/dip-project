# import os
# import papermill as pm

# folder_path = './brain_tumor_dataset/no'

# file_names = os.listdir(folder_path)

# for file_name in file_names:
#     pm.execute_notebook("./preprocessing.ipynb", "./preprocessing.ipynb", parameters={"input_filename": f"./brain_tumor_dataset/no/{file_name}", "output_filename": f"./results/no/{file_name}"})

import sklearn
print(sklearn.__version__)