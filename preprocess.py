import os
import cv2
import argparse

def preprocess_images(input_dir, output_dir, size=(640, 640)):
    os.makedirs(output_dir, exist_ok=True)

    for img_name in os.listdir(input_dir):
        img_path = os.path.join(input_dir, img_name)
        img = cv2.imread(img_path)

        if img is None:
            continue

        img = cv2.resize(img, size)
        cv2.imwrite(os.path.join(output_dir, img_name), img)

    print("✅ Preprocessing completed")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    preprocess_images(args.input, args.output)
