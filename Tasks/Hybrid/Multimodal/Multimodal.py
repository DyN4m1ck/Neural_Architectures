"""
Module for Multimodal subcategory.
Part of HYBRID category - Combined/Multi-domain tasks
"""

class Multimodal:
    """Category: MULTIMODAL"""

    name = "Мультимодальные"
    description = "Комбинации текст+изображение, аудио+видео, сенсор+зрение+контроль"

    subcategories = [
        {
            "name": "Text + Image (CLIP, DALL-E)",
            "description": "Text-image models - connecting language and visual representations"
        },
        {
            "name": "Text + Audio + Video",
            "description": "Multimodal fusion - combining text, audio, and video modalities"
        },
        {
            "name": "Vision + Language (VQA, Captioning)",
            "description": "Vision-language tasks - visual question answering and image captioning"
        },
        {
            "name": "Sensor + Vision + Control",
            "description": "Sensor-vision-control integration - robotics and autonomous systems"
        },
        {
            "name": "Any combination",
            "description": "Arbitrary multimodal combinations - flexible cross-modal integration"
        }
    ]

__all__ = ["Multimodal"]
