
# Harry's Cloak Effect with OpenCV

This project recreates the "invisibility cloak" effect from Harry Potter using OpenCV in Python. The program captures the background, then uses HSV masking to hide a specific color (usually the color of a cloak or cloth), creating the illusion of invisibility.

## Features

- **Dynamic HSV Range Adjustment**: Allows real-time fine-tuning of the HSV range using trackbars.
- **Improved Mask Quality**: Uses median blur and dilation to enhance mask quality and reduce noise.

## Requirements

- **Python 3.x**
- **OpenCV**
- **Numpy**

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/invisibility-cloak.git
   cd invisibility-cloak
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the code**:
   ```bash
   python invisibility_cloak.py
   ```

## Usage

1. **Initialize the Camera**  
   The script will start the camera and display a window with trackbars to adjust HSV values.

2. **Adjust the Trackbars**  
   - Use the `upper_hue`, `upper_saturation`, and `upper_value` trackbars to set the upper range of the HSV mask.
   - Use the `lower_hue`, `lower_saturation`, and `lower_value` trackbars to set the lower range of the HSV mask.
   - Adjust these values until the cloak or cloth you want to disappear is completely masked.

3. **Press 'q' to Quit**  
   Press the `q` key to close the application.

## Code Explanation

1. **Initialize Camera**: Captures frames from the default camera and sets up a window with trackbars for adjusting HSV values.
2. **Capture Initial Background Frame**: Captures a frame to use as the background, which will appear behind the masked area.
3. **Define the HSV Range for Masking**: Adjust HSV values to accurately mask the cloak color.
4. **Apply Mask and Create Cloak Effect**:
   - Apply the mask to the live frame to remove the specified color.
   - Overlay the background onto the masked area to create the "invisibility" effect.

## Example

Running the program should display a live video feed with the selected color appearing transparent, making it look like you're wearing an invisibility cloak!

## License

This project is licensed under the MIT License.
