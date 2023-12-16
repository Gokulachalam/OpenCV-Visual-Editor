# OpenCV-Visual-Editor


This Flask application allows users to upload an image and apply various image processing operations. It uses OpenCV for image manipulation and PIL for handling image data.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/image-processing-flask-app.git
    cd image-processing-flask-app
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

## Supported Operations

- **Background Removal**: Remove the background from the image.
- **Clarity Enhancement**: Enhance the clarity of the image.
- **Color Enhancement**: Enhance the color saturation of the image.
- **Object Removal**: Remove specified objects based on contour area.
- **Black and White**: Convert the image to black and white.
- **Invert Colors**: Invert the colors of the image.
- **Oil Painting Effect**: Apply an oil painting effect to the image.
- **Blur Background**: Blur the background of the image.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add a new feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
