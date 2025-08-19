import numpy as np 
from faster_whisper import WhisperModel  
from .utils import load_config, logger  
class TranscriptionEngine:
    def __init__(self):
        cfg = load_config()["transcription"]
        device = cfg["device"]
        compute_type = cfg["compute_type"]
        if device == "auto":
            try:
                import torch
                if torch.cuda.is_available():
                    device = "cuda"
                    compute_type = "float16"
                    logger.info("GPU detected - Using CUDA")
                else:
                    device = "cpu"
                    logger.info("No GPU detected - Falling back to CPU")
            except:
                device = "cpu"
                logger.warning("Torch check failed - Using CPU")
        self.model = WhisperModel(cfg["model_size"], device=device, compute_type=compute_type)
        self.rate = load_config()["audio"]["sample_rate"]
    def transcribe(self, pcm_bytes: bytes) -> str:
        audio = np.frombuffer(pcm_bytes, np.int16).astype(np.float32) / 32768.0
        segments, _ = self.model.transcribe(audio, beam_size=1, language="en")
        text = " ".join([s.text.strip() for s in list(segments)])
        return text
