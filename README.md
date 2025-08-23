# WhisperCast

**WhisperCast** is a student-friendly, real-time speech-to-text application built on the powerful Faster-Whisper engine. Designed for accessibility, simplicity, and speed, WhisperCast enables users to transcribe spoken language with optional GPU support, intuitive hotkeys, clean code structure, and easily configurable settings.

***

## Features

- **Real-time Speech-to-Text:** Converts spoken language into text instantly with minimal latency.
- **Faster-Whisper Integration:** Utilizes the efficient Faster-Whisper backend for high-quality transcription.
- **GPU Acceleration:** Optional GPU support for lightning-fast processing on compatible hardware.
- **Hotkey Controls:** Easily start, stop, and manage transcriptions with customizable keyboard shortcuts.
- **Silence Detection (Future/Optional):** Uncomment/add `silence_timeout` in config.toml.
- **Clean Codebase:** Simple architecture facilitates quick understanding and easy contributions.
- **Student-Friendly:** Optimized for use in classrooms, lectures, and personal study.

***


## 📁 Project Structure & Path

WhisperCast/
├── README.md                 # This file
├── LICENSE                   # MIT license
├── requirements.txt          # Python dependencies
├── config.toml              # Configuration settings
├── .gitignore               # Git ignore rules
│
├── whispercast/             # Main package directory
│   ├── __init__.py          # Package initializer
│   ├── main.py              # Application entry point
│   ├── transcription.py     # Speech-to-text engine
│   ├── audio_capture.py     # Microphone audio capture
│   └── utils.py             # Configuration and logging utilities
│
└── .venv/                   # Virtual environment (created during setup)

## Keep in mind the naming of all files and folders.

Key Files:
main.py: Application controller with hotkey handling and audio processing loop
transcription.py: Whisper model interface with GPU auto-detection
audio_capture.py: PyAudio wrapper for microphone input
utils.py: Configuration loader and logging setup
config.toml: User-editable settings file


***

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/aiman-riaz/whisper-cast
    ```
2. Navigate to the project directory:
    ```bash
    cd whisper-cast
    ```
3. Install dependencies (see `requirements.txt`):
    ```bash
    pip install -r requirements.txt
    ```
    **Optional GPU:** Install PyTorch: `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121` (replace `cu121` with your CUDA version from `nvidia-smi`). The app auto-detects and uses it if available.
   
4. Setup any additional configurations as described below.

On first execution, WhisperCast will automatically download the specified Whisper model:
tiny: ~39MB (fastest, basic accuracy)
base: ~74MB (balanced speed/accuracy) - Default
small: ~244MB (better accuracy)
medium: ~769MB (high accuracy)
large-v3: ~1550MB (best accuracy, slowest)

***

## Usage

- Launch the app:
    ```bash
    python whisper_cast.py
    ```
- Use the provided hotkeys to begin and end recording.
- Configure preferences (model settings) in the configuration file or via command-line arguments.
- Transcribed text will appear in real time; you can copy, export, or save it as needed.
- "No module named 'whispercast'":
    Ensure you're running from the project root directory (WhisperCast/)
    Activate your virtual environment: .venv\Scripts\activate

***

## Configuration

Edit `config.toml` (or similar configuration file, see documentation) to customize:

- Hotkeys
- Input device (microphone)
- Transcription language (currently tested in English)
- Whisper model selection (Options: tiny/base/small/medium/large-v3) (bigger = more accurate but slower)
- GPU/CPU usage


***

## Contributing

Contributions welcome! Fork the repo, make changes, and submit a pull request. Focus on features like GUI integration or mobile support.

***

## License

This project is licensed under the MIT License.

***

## Acknowledgments

- Powered by [Faster-Whisper](https://github.com/faster-whisper)
- Inspired by student needs for quick and accurate lecture transcription.

***

*For more information and support, please refer to the project's documentation or open an issue on the GitHub repo.*

[1] https://github.com/aiman-riaz/whisper-cast
