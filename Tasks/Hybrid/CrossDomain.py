"""
Module for Cross-Domain subcategory.
Part of HYBRID category - Combined/Multi-domain tasks
"""

class CrossDomain:
    """Category: CROSS-DOMAIN"""

    name = "Кросс-доменные"
    description = "Физика+Биология, Химия+Математика, Нейробиология+ML, Геология+ML, Экономика+Климат"

    subcategories = [
        {
            "name": "Физика + Биология (BioPhysics)",
            "description": "Biophysics - applying physics principles to biological systems"
        },
        {
            "name": "Химия + Математика (ChemInformatics)",
            "description": "Chemoinformatics - mathematical modeling of chemical data"
        },
        {
            "name": "Нейробиология + ML (NeuroAI)",
            "description": "NeuroAI - combining neuroscience insights with machine learning"
        },
        {
            "name": "Геология + ML (GeoAI)",
            "description": "GeoAI - machine learning applications in geosciences"
        },
        {
            "name": "Экономика + Климат (Climate Economics)",
            "description": "Climate economics - modeling economic impacts of climate change"
        },
        {
            "name": "Any cross-domain",
            "description": "Arbitrary cross-domain combinations - flexible interdisciplinary integration"
        }
    ]

__all__ = ["CrossDomain"]
