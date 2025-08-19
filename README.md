# WhisperCast

**WhisperCast** is a student-friendly, real-time speech-to-text application built on the powerful Faster-Whisper engine. Designed for accessibility, simplicity, and speed, WhisperCast enables users to transcribe spoken language with optional GPU support, intuitive hotkeys, clean code structure, and easily configurable settings.[1]

***

## Features

- **Real-time Speech-to-Text:** Converts spoken language into text instantly with minimal latency.
- **Faster-Whisper Integration:** Utilizes the efficient Faster-Whisper backend for high-quality transcription.
- **GPU Acceleration:** Optional GPU support for lightning-fast processing on compatible hardware.
- **Hotkey Controls:** Easily start, stop, and manage transcriptions with customizable keyboard shortcuts.
- **Clean Codebase:** Simple architecture facilitates quick understanding and easy contributions.
- **Student-Friendly:** Optimized for use in classrooms, lectures, and personal study.

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

***

## Usage

- Launch the app:
    ```bash
    python whisper_cast.py
    ```
- Use the provided hotkeys to begin and end recording.
- Configure preferences (model settings) in the configuration file or via command-line arguments.
- Transcribed text will appear in real time; you can copy, export, or save it as needed.

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
