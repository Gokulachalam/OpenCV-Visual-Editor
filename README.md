# OpenCV-Visual-Editor


This Flask application allows users to upload an image and apply various image processing operations. It uses OpenCV for image manipulation and PIL for handling image data.


## Demo 

![opencv_visual_editor](https://github.com/Gokulachalam/OpenCV-Visual-Editor/assets/89055461/7e3b56c8-0bfd-4df8-ab68-44ecd8c14f4a)


## Development Environment

This project is developed and tested on a Debian 12 Linux paltform





## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/Gokulachalam/OpenCV-Visual-Editor.git
    cd image_pro
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask app:

    ```bash
    python app.py
    ```

4. Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

1. On the home page, upload an image file.

2. Choose an image processing operation from the dropdown menu.

3. Click the "Process" button to apply the selected operation.

4. The processed image will be displayed on the page.



## Features

### Image Processing Operations

1. **Background Removal:**
   - Description: Removes the background of an image based on color thresholding.
   - Usage: Select "bg_removal" as the operation.

2. **Clarity Enhancement:**
   - Description: Enhances the clarity of an image using Laplacian filtering.
   - Usage: Select "clarity_enhancement" as the operation.

3. **Color Enhancement:**
   - Description: Enhances the color saturation of an image in the HSV color space.
   - Usage: Select "color_enhancement" as the operation.

4. **Object Removal:**
   - Description: Removes specified objects from an image based on contour area.
   - Usage: Select "object_removal" as the operation.

5. **Black and White Conversion:**
   - Description: Converts the image to black and white.
   - Usage: Select "black_and_white" as the operation.

6. **Invert Colors:**
   - Description: Inverts the colors of the image.
   - Usage: Select "invert_colors" as the operation.

7. **Oil Painting Effect:**
   - Description: Applies an oil painting effect to the image.
   - Usage: Select "oil_painting_effect" as the operation.

8. **Blur Background:**
   - Description: Blurs the background of an image.
   - Usage: Select "blur_background" as the operation.

### File Upload and Processing

- **File Upload:**
  - Description: Users can upload an image file for processing.

- **Result Download:**
  - Description: Processed images can be downloaded by users.

### Web Interface

- **Interactive Web Interface:**
  - Description: Users can interact with the application through a web interface.

---

Feel free to customize the descriptions and details based on the specific behavior and usage of your application. This section gives users a clear understanding of what features are available and how to use them.


## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add a new feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License 
