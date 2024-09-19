# Video Steganography Project

This project implements video steganography, allowing you to hide secret messages within video files. It consists of two main components: an encoder to hide messages and a decoder to extract them.

## Features

- Hide text messages within video files
- Extract hidden messages from steganographic videos
- Minimal impact on video quality
- Works with MP4 video format

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy

## Installation

1. Clone this repository or download the source code.
2. Install the required dependencies:
     -- pip install opencv-python numpy

## Usage

### Encoding a Message

To hide a message in a video:

1. Open the `encoder.py` file.
2. Modify the following variables at the bottom of the file:
   - `input_video`: Path to your input video file
   - `output_video`: Path where the steganographic video will be saved
   - `secret_message`: The message you want to hide
3. Run the script:


### Decoding a Message

To extract a hidden message from a video:

1. Run the `decoder.py` script:


2. When prompted, enter the binary message extracted from the video.

## How It Works

### Encoding

The encoder hides the message by modifying the least significant bit of each color channel in the video frames. It adds a 32-bit zero sequence as an end marker.

### Decoding

The decoder extracts the least significant bits from the video frames and reconstructs the hidden message. It stops when it encounters the 32-bit zero sequence end marker.

## Limitations

- The current implementation works with MP4 videos.
- The message length is limited by the video size and duration.
- Excessive compression or modification of the steganographic video may corrupt the hidden message.

## Future Improvements

- Add error handling and input validation
- Implement a graphical user interface
- Support for other video formats
- Enhance security with encryption
- audio steganography
- image steganography
- video to image steganography

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## Author

- PappuWalker

## Acknowledgments

- OpenCV library
- NumPy library
