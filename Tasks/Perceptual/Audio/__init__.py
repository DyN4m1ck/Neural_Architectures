"""
Audio and Sound Processing Tasks
=================================
Природа: Непрерывные аудиосигналы
Операции: Распознавание, синтез, классификация звуков

Subcategories:
- Speech Recognition (ASR)
- Speech Synthesis (TTS)
- Sound Classification
- Music Generation & Analysis
- Ultrasound Processing
- Infrasound Monitoring
- Acoustic Monitoring
"""

from .SpeechRecognition import SpeechRecognition
from .SpeechSynthesis import SpeechSynthesis
from .SoundClassification import SoundClassification
from .MusicProcessing import MusicProcessing
from .Ultrasound import Ultrasound
from .Infrasound import Infrasound
from .AcousticMonitoring import AcousticMonitoring

__all__ = [
    "SpeechRecognition",
    "SpeechSynthesis", 
    "SoundClassification",
    "MusicProcessing",
    "Ultrasound",
    "Infrasound",
    "AcousticMonitoring",
]