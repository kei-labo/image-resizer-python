import os
from PIL import Image

input_folder="input_images"
output_folder="output_images"
os.makedirs(output_folder,exist_ok=True)

#リサイズ後のサイズ
new_width= 800
new_height= 600

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg",".jpeg",".png")):
        img_path= os.path.join(input_folder,filename)
        img= Image.open(img_path)
        #リサイズ
        resized_img= img.resize((new_width,new_height))
        #保存
        save_path= os.path.join(output_folder,filename)
        resized_img.save(save_path)

        print(f"{filename}をリサイズしました")
print("画像処理が完了しました")