import os
import cv2
import numpy as np
import albumentations as A
import tqdm


def augment_background_image(image, augmentation_for_background: A.Compose):
    out = augmentation_for_background(image=image)
    return out['image']


def augment_normal_image(image, augmentation_normal: A.Compose, boxes, cls):
    out = augmentation_normal(image=image, bboxes=boxes, class_labels=cls)
    return out['image'], out['bboxes'], out['class_labels']


def save_txt_and_image_to_path(path, i, new_image, new_boxes=None, new_classes=None, k=None):
    if k is None:
        suffix = f'_{i}'
    else:
        suffix = f'_{i}_{k}'
    name_for_copy = file.split('.')[0] + suffix + '.jpg'
    out = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)

    cv2.imwrite(path + f'/{name_for_copy}', out)

    if new_boxes is None or new_classes is None:

        with open(path + f'/{file[:-4]}{suffix}.txt', 'w') as t:
            t.writelines([])
            t.close()

    else:

        new_data = []

        for bbox, cls in zip(new_boxes, new_classes):
            list_for_str = [str(cls)] + list(map(str, bbox)) + ['\n']
            out_str = ' '.join(list_for_str)
            new_data.append(out_str)

        with open(path + f'/{file[:-4]}{suffix}.txt', 'w') as t:
            t.writelines(new_data)
            t.close()


a_list = [
    A.HorizontalFlip(p=0.7),
    A.VerticalFlip(p=0.7),
    A.Rotate(limit=(-45, 45),
             p=0.5),
    A.CLAHE(2, p=0.5),
    A.RandomBrightnessContrast(brightness_limit=(-0.15, 0.15),
                               contrast_limit=0.25,
                               p=0.6),

    A.OneOf([A.GaussianBlur((3, 3), p=0.7),
             A.MedianBlur(5, p=0.3)], p=0.3),

    A.Sharpen(lightness=(0, 0.5), p=0.34),
    A.Perspective(scale=(0.05, 0.11),
                  p=0.45),

    A.OneOf([A.GaussNoise(p=0.5),
             A.ISONoise((0, 0.075), p=0.5)], p=0.4),
]

augmentation_list = A.Compose(a_list,
                              bbox_params=A.BboxParams(format='yolo',
                                                       min_visibility=0.7,
                                                       label_fields=['class_labels'])
                              )

augmentation_list_for_back = A.Compose(a_list)

path = ''

txts_files = sorted(os.listdir(path))[1::2]

big_cls = [0, 2]
small_cls = [1, 3, 4]

i = 0
count_of_augmented_background = 0

for file in tqdm.tqdm(txts_files):

    with open(path + f'/{file}', 'r') as txt:
        data = txt.readlines()
        txt.close()

    cls_list = [int(line.strip()[0]) for line in data]

    image = cv2.imread(path + file.split('.')[0] + '.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    try:
        if not data and count_of_augmented_background < 75:

            augmented_background_image = augment_background_image(image=image,
                                                                  augmentation_for_background=augmentation_list_for_back)

            save_txt_and_image_to_path(path=path,
                                       i=i,
                                       new_image=augmented_background_image)

            count_of_augmented_background += 1

        else:
            cls_list = np.array(cls_list)

            boxes = [list(map(float, line.split()[1:])) for line in data]

            if np.isin(cls_list, small_cls).sum():

                for k in range(2):

                    a_image, a_bboxes, a_cls = augment_normal_image(image=image,
                                                                    augmentation_normal=augmentation_list,
                                                                    boxes=boxes,
                                                                    cls=cls_list)

                    save_txt_and_image_to_path(path=path,
                                               i=i,
                                               k=k,
                                               new_image=a_image,
                                               new_boxes=a_bboxes,
                                               new_classes=a_cls)
            else:

                a_image, a_bboxes, a_cls = augment_normal_image(image=image,
                                                                augmentation_normal=augmentation_list,
                                                                boxes=boxes,
                                                                cls=cls_list)

                save_txt_and_image_to_path(path=path,
                                           i=i,
                                           new_image=a_image,
                                           new_boxes=a_bboxes,
                                           new_classes=a_cls)
    except:
        print(file)

    i += 1




