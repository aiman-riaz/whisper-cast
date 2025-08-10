# WhisperCast

**WhisperCast** is a student-friendly, real-time speech-to-text application built on the powerful Faster-Whisper engine. Designed for accessibility, simplicity, and speed, WhisperCast enables users to transcribe spoken language with optional GPU support, intuitive hotkeys, clean code structure, and easily configurable settings.[1]

***

## Features

- **Real-time Speech-to-Text:** Converts spoken language into text instantly with minimal latency.
- **Faster-Whisper Integration:** Utilizes the efficient Faster-Whisper backend for high-quality transcription.
- **GPU Acceleration:** Optional GPU support for lightning-fast processing on compatible hardware.
- **Hotkey Controls:** Easily start, stop, and manage transcriptions with customizable keyboard shortcuts.
- **Configurable Settings:** User-friendly configuration options for adapting to different environments and needs.
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
4. Setup any additional configurations as described below.

***

## Usage

- Launch the app:
    ```bash
    python whisper_cast.py
    ```
- Use the provided hotkeys to begin and end recording.
- Configure preferences (API, device, language, and model settings) in the configuration file or via command-line arguments.
- Transcribed text will appear in real time; you can copy, export, or save it as needed.

***

## Configuration

Edit `config.json` (or similar configuration file, see documentation) to customize:

- Hotkeys
- Input device (microphone)
- Transcription language
- Whisper model selection
- GPU/CPU usage

***

## Contributing

Pull requests and suggestions are welcome! Please keep your code clean and follow the repo's contribution guidelines.

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
