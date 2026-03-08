"""
Module for Medical Technology subcategory.
Part of HYBRID category - Combined/Multi-domain tasks
"""

class MedicalTech:
    """Category: MEDICAL TECHNOLOGY"""

    name = "Медицина + Технологии"
    description = "Медицинская диагностика, персонализированная медицина, drug discovery, хирургические роботы"

    subcategories = [
        {
            "name": "Медицинская диагностика (Imaging + EHR)",
            "description": "Medical diagnostics - combining medical imaging with electronic health records"
        },
        {
            "name": "Персонализированная медицина",
            "description": "Personalized medicine - tailoring treatment to individual patients"
        },
        {
            "name": "Drug Discovery (Chemistry + Biology + ML)",
            "description": "Drug discovery - combining chemistry, biology, and machine learning for drug development"
        },
        {
            "name": "Хирургические роботы (Vision + Control)",
            "description": "Surgical robots - combining computer vision with robotic control"
        },
        {
            "name": "Telemedicine",
            "description": "Telemedicine - remote healthcare delivery using technology"
        }
    ]

__all__ = ["MedicalTech"]
