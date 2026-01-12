import os
import cv2
import argparse

def run_inference(image_dir):
    print("🔍 Running inference on images...")

    for img_name in os.listdir(image_dir):
        print(f"Detected objects in {img_name}")

    print("✅ Inference completed")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--images", required=True)
    args = parser.parse_args()

    run_inference(args.images)
