# comparator.py

import cv2
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import os

def load_and_preprocess(image_path, target_size=None):
    image = cv2.imread(image_path)

    if target_size:
        image = cv2.resize(image, target_size)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image, gray

def calculate_pixel_differences(gray_ref, gray_test):
    diff = cv2.absdiff(gray_ref, gray_test)
    changed_pixels = np.count_nonzero(diff)
    total_pixels = gray_ref.size
    percentage_changed = (changed_pixels / total_pixels) * 100
    return changed_pixels, total_pixels, percentage_changed

def highlight_differences(reference_img, test_img, gray_ref, gray_test, highlight_color='yellow'):
    score, diff = compare_ssim(gray_ref, gray_test, full=True)
    diff = (diff * 255).astype("uint8")

    thresh = cv2.threshold(diff, 200, 255, cv2.THRESH_BINARY_INV)[1]
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    color_map = {
        "green": (0, 255, 0),
        "yellow": (0, 255, 255),
        "red": (0, 0, 255),
        "blue": (255, 0, 0),
        "gray": (128, 128, 128)
    }
    color = color_map.get(highlight_color.lower(), (0, 255, 255))

    highlighted_img = test_img.copy()
    alpha = 0.15

    change_regions = []

    for i, contour in enumerate(contours, 1):
        x, y, w, h = cv2.boundingRect(contour)
        change_regions.append((i, x, y, w, h))
        roi = highlighted_img[y:y+h, x:x+w]
        overlay = roi.copy()
        overlay[:] = color
        blended = cv2.addWeighted(overlay, alpha, roi, 1 - alpha, 0)
        highlighted_img[y:y+h, x:x+w] = blended
        cv2.rectangle(highlighted_img, (x, y), (x + w, y + h), color, 2)

    abs_diff_gray = cv2.absdiff(gray_ref, gray_test)
    abs_diff_color = cv2.absdiff(reference_img, test_img)

    return highlighted_img, score, change_regions, diff, abs_diff_gray, abs_diff_color

def save_comparison_figure(ref_img, test_img, highlighted_img, ssim_diff, abs_diff_color,
                            ssim_score, changed_pixels, total_pixels, percentage_changed,
                            highlight_color='yellow', save_path='output/output_figure.png'):
    
    ref_img_rgb = cv2.cvtColor(ref_img, cv2.COLOR_BGR2RGB)
    test_img_rgb = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)
    highlighted_img_rgb = cv2.cvtColor(highlighted_img, cv2.COLOR_BGR2RGB)
    abs_diff_rgb = cv2.cvtColor(abs_diff_color, cv2.COLOR_BGR2RGB)

    if highlight_color == "green":
        abs_diff_rgb[:, :, 1] = np.maximum(abs_diff_rgb[:, :, 1], abs_diff_rgb[:, :, 0])
    elif highlight_color == "yellow":
        abs_diff_rgb[:, :, 0] = abs_diff_rgb[:, :, 1] = np.maximum(abs_diff_rgb[:, :, 0], abs_diff_rgb[:, :, 1])
    elif highlight_color == "red":
        abs_diff_rgb[:, :, 0] = np.maximum(abs_diff_rgb[:, :, 0], abs_diff_rgb[:, :, 1])
    elif highlight_color == "blue":
        abs_diff_rgb[:, :, 2] = np.maximum(abs_diff_rgb[:, :, 2], abs_diff_rgb[:, :, 1])

    plt.figure(figsize=(36, 12)) 

    plt.subplot(1, 3, 1)
    plt.imshow(ref_img_rgb)
    plt.title("Reference UI", fontsize=16)
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(test_img_rgb)
    plt.title("Test UI", fontsize=16)
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(highlighted_img_rgb)
    plt.title("Highlighted Changes", fontsize=16)
    plt.axis('off')

    # plt.subplot(1, 5, 4)
    # plt.imshow(ssim_diff, cmap='gray')
    # plt.title("SSIM Difference")
    # plt.axis('off')

    # plt.subplot(1, 5, 5)
    # plt.imshow(abs_diff_rgb)
    # plt.title("Pixel Difference")
    # plt.axis('off')

    metrics_text = f"SSIM: {ssim_score:.4f}\nChanged: {changed_pixels:,}/{total_pixels:,}\n({percentage_changed:.2f}%)"
    plt.gcf().text(0.5, 0.05, metrics_text, ha='center', fontsize=12,
                   bbox=dict(facecolor='white', alpha=0.7))

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()
    return save_path
