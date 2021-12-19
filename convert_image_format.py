from PIL import Image
import os

src_path = './data/vision'
target_path = './data/plant_dataset'

for split_type in os.listdir(src_path):
    if not os.path.exists(os.path.join(target_path, split_type)):
        os.mkdir(os.path.join(target_path, split_type))

for split_type in os.listdir(src_path):
    for disease_name in os.listdir(os.path.join(src_path, split_type)):
        disease_path = os.path.join(src_path, split_type, disease_name)
        if not os.path.exists(disease_path):
            os.mkdir(disease_path)
        target_split_disease_path = os.path.join(target_path, split_type, disease_name)
        if not os.path.exists(target_split_disease_path):
            os.mkdir(target_split_disease_path)

        for image_name in os.listdir(disease_path):
            src_image_path = os.path.join(src_path, split_type, disease_name, image_name)
            target_image_path = os.path.join(target_split_disease_path, ''.join(image_name.split('.')[:-1]) + '.jpeg')
            print(src_image_path)
            print(target_image_path)

            im = Image.open(src_image_path)
            im = im.convert('RGB')
            im.save(target_image_path)
