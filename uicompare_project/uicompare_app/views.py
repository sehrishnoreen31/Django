from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .utils.comparator import load_and_preprocess, highlight_differences, calculate_pixel_differences, save_comparison_figure
from django.core.files.storage import FileSystemStorage

def compare_images_view(request):
    if request.method == "POST":
        ref_img_file = request.FILES.get('ref_image')
        test_img_file = request.FILES.get('test_image')
        highlight_color = request.POST.get('color', 'yellow')

        # Validate uploaded files presence
        if not ref_img_file or not test_img_file:
            return HttpResponseBadRequest("Both reference and test images must be uploaded.")

        fs = FileSystemStorage()

        # Save uploaded images to media folder
        ref_path = fs.save(ref_img_file.name, ref_img_file)
        test_path = fs.save(test_img_file.name, test_img_file)

        # Load and preprocess images
        ref_img, gray_ref = load_and_preprocess(fs.path(ref_path))
        test_img, gray_test = load_and_preprocess(fs.path(test_path), target_size=(ref_img.shape[1], ref_img.shape[0]))


        # Calculate pixel differences
        changed_pixels, total_pixels, percent_changed = calculate_pixel_differences(gray_ref, gray_test)

        # Highlight differences and generate comparison images
        highlighted_img, ssim_score, regions, ssim_diff, abs_diff_gray, abs_diff_color = highlight_differences(
            ref_img.copy(), test_img.copy(), gray_ref, gray_test, highlight_color
        )

        # Save output comparison figure
        output_path = save_comparison_figure(
            ref_img, test_img, highlighted_img, ssim_diff, abs_diff_color,
            ssim_score, changed_pixels, total_pixels, percent_changed,
            highlight_color, save_path='media/output/output_figure.png'
        )

        # Render results page with context
        return render(request, 'results.html', {
            'output_image': fs.url('output/output_figure.png'),
            'ssim_score': round(ssim_score, 4),
            'changed_pixels': changed_pixels,
            'total_pixels': total_pixels,
            'percent_changed': round(percent_changed, 2),
            'regions': regions
        })

    # GET or other methods render upload form
    return render(request, 'upload.html')
