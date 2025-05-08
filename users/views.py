from django.shortcuts import render
from accounts.models import RegisterTable

#------------------------------------------------------------------------------------------
def UserHomePage(request):
    user = request.session['username']
    return render(request, 'users/home.html',{'user':user})

#-------------------------------------------------------------------------------------------

def MachineLearningPage(request):
    user = request.session['username']
    return render(request,'users/ml.html',{'user':user})

#-------------------------------------------------------------------------------------------
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from ultralytics import YOLO
from django.conf import settings
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import shutil

# Define a directory to store final prediction results
FINAL_DIR = os.path.join(settings.MEDIA_ROOT, 'predicted')

def clear_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

def PredictPage(request):
    user = request.session.get('username')

    if request.method == 'POST' and request.FILES.get('image'):
        # Handle uploaded image
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_path = fs.path(filename)
        uploaded_file_url = fs.url(filename)

        # Path to the YOLO model
        model_path = os.path.join(settings.MEDIA_ROOT, 'model', 'best.pt')
        model = YOLO(model_path )

        # Clear the final directory before prediction
        clear_directory(FINAL_DIR)

        # Perform prediction
        results = model.predict(source=uploaded_file_path, task='segment', save=False)
        print('Predicted results of the image uploaded:', results)

        # Assuming results[0] contains the predicted image as a numpy array
        predicted_image = results[0].plot()  # or any appropriate method to get the image

        # Save the predicted image with the same name 'predicted.jpg'
        predicted_filename = 'predicted.jpg'
        predicted_filepath = os.path.join(FINAL_DIR, predicted_filename)
        plt.imsave(predicted_filepath, predicted_image)

        # Load the uploaded image for display
        uploaded_img = mpimg.imread(uploaded_file_path)

        # Plotting both images on a single canvas
        fig, ax = plt.subplots(1, 2, figsize=(10, 5))
        ax[0].imshow(uploaded_img)
        ax[0].axis('off')
        ax[0].set_title('Uploaded Image')

        ax[1].imshow(predicted_image)
        ax[1].axis('off')
        ax[1].set_title('Predicted Image')

        plt.tight_layout()
        plt.show()

        # Get the URL for displaying in the template
        final_file_url = os.path.join(settings.MEDIA_URL, 'predicted', predicted_filename)

        return render(request, 'users/predict.html', {
            'uploaded_file_url': uploaded_file_url,
            'result_image_url': final_file_url,
            'user': user
        })

    return render(request, 'users/predict.html', {'user': user})




#-------------------------------------------------------------------------------------------

def DatasetView(request):
    user = request.session['username']
     
    return render(request, 'users/dataset.html',{'user':user})

#--------------------------------------------------------------------------------------------
