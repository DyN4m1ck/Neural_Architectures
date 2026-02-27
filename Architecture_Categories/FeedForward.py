"""
Module for FeedForward Architectures
"""
from dataclasses import dataclass
from typing import Optional

# Convolutional Architectures data
CONVOLUTIONAL_ARCHITECTURES = [
    {
        "name": "FeedForward Architectures",
        "description": "artificial neural networks in which the signal propagates strictly from the input layer to the output"
    }
]

@dataclass
class FeedForward:
    """
    Represents a FeedForward Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
FeedForward Model Architectures
Networks for generating new data samples
"""

# Before ARCHITECTURE_CATEGORIES
FEEDFORWARD_ARCHITECTURES = [
    {
        "name": "Перцептрон (Perceptron)",
        "description": "Простейшая модель искусственного нейрона, используемая для бинарной классификации."
    },
    {
        "name": "Adaline / Madaline",
        "description": "Адаптивный линейный элемент и его многослойное расширение, используемые для классификации и регрессии."
    },
    {
        "name": "Многослойный перцептрон (MLP, Multilayer Perceptron)",
        "description": "Нейронная сеть с прямой связью, состоящая из одного или нескольких скрытых слоев."
    },
    {
        "name": "Однослойный перцептрон (SLP)",
        "description": "Простейшая нейронная сеть без скрытых слоев для линейной классификации."
    },
    {
        "name": "Глубокий MLP (Deep MLP)",
        "description": "Многослойный перцептрон с множеством скрытых слоев для сложных задач."
    },
    {
        "name": "Широкий MLP (Wide MLP)",
        "description": "MLP с большим количеством нейронов в каждом слое."
    },
    {
        "name": "MLP с Dropout",
        "description": "MLP с регуляризацией dropout для предотвращения переобучения."
    },
    {
        "name": "MLP с Batch Normalization",
        "description": "MLP с пакетной нормализацией для ускорения обучения."
    },
    {
        "name": "MLP с Layer Normalization",
        "description": "MLP с нормализацией по слоям."
    },
    {
        "name": "Residual MLP",
        "description": "MLP с остаточными соединениями для улучшения градиентного потока."
    },
    {
        "name": "Dense MLP",
        "description": "Плотно связанный MLP с соединениями между всеми слоями."
    },
    {
        "name": "Самоорганизующаяся карта Кохонена (SOM, Self-Organizing Map)",
        "description": "Тип нейронной сети, используемый для кластеризации и визуализации многомерных данных."
    },
    {
        "name": "Growing SOM (GSOM)",
        "description": "Расширяемая самоорганизующаяся карта с динамическим ростом."
    },
    {
        "name": "Hierarchical SOM",
        "description": "Иерархическая SOM для многоуровневой кластеризации."
    },
    {
        "name": "Fuzzy SOM",
        "description": "Нечеткая самоорганизующаяся карта."
    },
    {
        "name": "Обучение векторному квантованию (LVQ, Learning Vector Quantization)",
        "description": "Метод машинного обучения для задач классификации, основанный на сопоставлении с образцами."
    },
    {
        "name": "LVQ1",
        "description": "Базовая версия обучения векторному квантованию."
    },
    {
        "name": "LVQ2.1",
        "description": "Улучшенная версия LVQ с коррекцией границ."
    },
    {
        "name": "LVQ3",
        "description": "Расширенная LVQ с дополнительной коррекцией."
    },
    {
        "name": "OLVQ (Optimized LVQ)",
        "description": "Оптимизированная LVQ с адаптивными скоростями обучения."
    },
    {
        "name": "GRLVQ (Generalized Relevance LVQ)",
        "description": "Обобщенная релевантная LVQ с взвешиванием признаков."
    },
    {
        "name": "Экстремальная машина обучения (ELM, Extreme Learning Machine)",
        "description": "Метод обучения однослойных нейронных сетей с быстрым обучением и хорошей обобщающей способностью."
    },
    {
        "name": "Online-ELM",
        "description": "Онлайн версия ELM для потоковых данных."
    },
    {
        "name": "Incremental-ELM",
        "description": "Инкрементальная ELM с постепенным добавлением нейронов."
    },
    {
        "name": "Pruned-ELM",
        "description": "Прореженная ELM для уменьшения размера модели."
    },
    {
        "name": "Ensemble-ELM",
        "description": "Ансамбль ELM для повышения точности."
    },
    {
        "name": "Deep-ELM",
        "description": "Глубокая ELM с несколькими скрытыми слоями."
    },
    {
        "name": "Conv-ELM",
        "description": "Сверточная ELM для обработки изображений."
    },
    {
        "name": "Нейронная сеть с радиальными базисными функциями (RBF Network)",
        "description": "Сеть с радиальными базисными функциями, используемая для аппроксимации функций и классификации."
    },
    {
        "name": "RBF с гауссовыми функциями",
        "description": "RBF сеть с гауссовыми радиальными функциями."
    },
    {
        "name": "RBF с мультиквадриками",
        "description": "RBF сеть с мультиквадричными функциями."
    },
    {
        "name": "Orthogonal RBF",
        "description": "Ортогональная RBF сеть для лучшей сходимости."
    },
    {
        "name": "Normalized RBF",
        "description": "Нормализованная RBF сеть."
    },
    {
        "name": "Local RBF",
        "description": "Локальная RBF сеть с ограниченной областью влияния."
    },
    {
        "name": "Вероятностная нейронная сеть (PNN, Probabilistic Neural Network)",
        "description": "Статистическая нейронная сеть, основанная на байесовской теории вероятностей."
    },
    {
        "name": "PNN с гауссовым ядром",
        "description": "PNN с гауссовой функцией ядра."
    },
    {
        "name": "Enhanced PNN",
        "description": "Улучшенная PNN с оптимизированными параметрами."
    },
    {
        "name": "Reduced PNN",
        "description": "Сокращенная PNN для уменьшения вычислений."
    },
    {
        "name": "Fuzzy PNN",
        "description": "Нечеткая вероятностная нейронная сеть."
    },
    {
        "name": "Глубокие порождающие модели (DBN, Deep Belief Network)",
        "description": "Глубокая нейронная сеть, состоящая из нескольких слоев стохастических скрытых переменных."
    },
    {
        "name": "DBN с RBM",
        "description": "DBN построенная из ограниченных машин Больцмана."
    },
    {
        "name": "Convolutional DBN",
        "description": "Сверточная DBN для обработки изображений."
    },
    {
        "name": "Discriminative DBN",
        "description": "Дискриминативная DBN для классификации."
    },
    {
        "name": "Глубокая складывающаяся сеть (DSN, Deep Stacking Network)",
        "description": "Архитектура глубокого обучения, использующая модульную структуру с последовательным обучением слоев."
    },
    {
        "name": "Convolutional DSN",
        "description": "Сверточная DSN для визуальных задач."
    },
    {
        "name": "Modular DSN",
        "description": "Модульная DSN с независимыми блоками."
    },
    {
        "name": "Автоэнкодер (Autoencoder)",
        "description": "Нейронная сеть, обучаемая восстанавливать входные данные на выходе, обычно используется для снижения размерности."
    },
    {
        "name": "Undercomplete Autoencoder",
        "description": "Автоэнкодер с меньшим скрытым слоем для сжатия данных."
    },
    {
        "name": "Overcomplete Autoencoder",
        "description": "Автоэнкодер с большим скрытым слоем."
    },
    {
        "name": "Shallow Autoencoder",
        "description": "Поверхностный автоэнкодер с одним скрытым слоем."
    },
    {
        "name": "Deep Autoencoder",
        "description": "Глубокий автоэнкодер с множеством скрытых слоев."
    },
    {
        "name": "Stacked Autoencoder",
        "description": "Стекированный автоэнкодер с послойным обучением."
    },
    {
        "name": "Convolutional Autoencoder",
        "description": "Сверточный автоэнкодер для изображений."
    },
    {
        "name": "Recurrent Autoencoder",
        "description": "Рекуррентный автоэнкодер для последовательностей."
    },
    {
        "name": "LSTM Autoencoder",
        "description": "Автоэнкодер на основе LSTM."
    },
    {
        "name": "Деноизинговый автоэнкодер (DAE, Denoising Autoencoder)",
        "description": "Автоэнкодер, обучаемый восстанавливать чистые данные из зашумленных входов."
    },
    {
        "name": "Gaussian DAE",
        "description": "DAE с гауссовым шумом."
    },
    {
        "name": "Salt-and-Pepper DAE",
        "description": "DAE с импульсным шумом."
    },
    {
        "name": "Masking DAE",
        "description": "DAE с маскированием входов."
    },
    {
        "name": "Контрактивный автоэнкодер (CAE, Contractive Autoencoder)",
        "description": "Автоэнкодер, использующий контрактивный штраф для получения инвариантных представлений."
    },
    {
        "name": "Robust CAE",
        "description": "Робастный контрактивный автоэнкодер."
    },
    {
        "name": "Higher-order CAE",
        "description": "CAE с производными высшего порядка."
    },
    {
        "name": "Разреженный автоэнкодер (Sparse Autoencoder)",
        "description": "Автоэнкодер, использующий разреженность для ограничения активации нейронов в скрытом слое."
    },
    {
        "name": "L1 Sparse Autoencoder",
        "description": "Разреженный автоэнкодер с L1 регуляризацией."
    },
    {
        "name": "KL Sparse Autoencoder",
        "description": "Разреженный автоэнкодер с KL-дивергенцией."
    },
    {
        "name": "Topographic Sparse AE",
        "description": "Топографический разреженный автоэнкодер."
    },
    {
        "name": "Вариационный автоэнкодер (VAE, Variational Autoencoder)",
        "description": "Генеративная модель, объединяющая автоэнкодеры и вариационный вывод для генерации новых данных."
    },
    {
        "name": "Beta-VAE",
        "description": "VAE с параметром бета для разделения представлений."
    },
    {
        "name": "Conditional VAE (CVAE)",
        "description": "Условный VAE для контролируемой генерации."
    },
    {
        "name": "InfoVAE",
        "description": "VAE с максимизацией взаимной информации."
    },
    {
        "name": "Wasserstein VAE",
        "description": "VAE с метрикой Вассерштейна."
    },
    {
        "name": "Adversarial VAE",
        "description": "Состязательный вариационный автоэнкодер."
    },
    {
        "name": "Hierarchical VAE",
        "description": "Иерархический VAE с многоуровневым латентным пространством."
    },
    {
        "name": "Vector Quantized VAE (VQ-VAE)",
        "description": "VAE с векторным квантованием латентного пространства."
    },
    {
        "name": "VQ-VAE-2",
        "description": "Улучшенный VQ-VAE с иерархическим квантованием."
    },
    {
        "name": "Normalizing Flow VAE",
        "description": "VAE с нормализующими потоками."
    },
    {
        "name": "Annealed VAE",
        "description": "VAE с аннилингом для лучшего обучения."
    },
    {
        "name": "Disentangled VAE",
        "description": "VAE с разделенными факторами вариации."
    },
    {
        "name": "FactorVAE",
        "description": "VAE с факторизованным латентным пространством."
    },
    {
        "name": "DIP-VAE",
        "description": "VAE с disentangled inference prior."
    },
    {
        "name": "β-TCVAE",
        "description": "Total Correlation VAE с параметром бета."
    },
    {
        "name": "RF-VAE",
        "description": "Relevance Factorized VAE."
    },
    {
        "name": "Адверсариальный автоэнкодер (AAE, Adversarial Autoencoder)",
        "description": "Автоэнкодер, использующий состязательное обучение для формирования латентного пространства."
    },
    {
        "name": "InfoAAE",
        "description": "AAE с максимизацией взаимной информации."
    },
    {
        "name": "Semi-supervised AAE",
        "description": "Полуавтоматический адверсариальный автоэнкодер."
    },
    {
        "name": "CatAAE",
        "description": "Категориальный AAE для дискретных данных."
    },
    {
        "name": "Continuous AAE",
        "description": "Непрерывный AAE для непрерывных представлений."
    },
    {
        "name": "Wasserstein AAE",
        "description": "AAE с метрикой Вассерштейна."
    },
    {
        "name": "Сети Колмогорова-Арнольда (KAN, Kolmogorov-Arnold Networks)",
        "description": "Нейронные сети, основанные на теореме Колмогорова-Арнольда о представлении непрерывных функций."
    },
    {
        "name": "FastKAN",
        "description": "Быстрая версия KAN с оптимизированными вычислениями."
    },
    {
        "name": "EfficientKAN",
        "description": "Эффективная KAN с уменьшенной сложностью."
    },
    {
        "name": "SplineKAN",
        "description": "KAN с сплайн-функциями активации."
    },
    {
        "name": "ChebyKAN",
        "description": "KAN с полиномами Чебышева."
    },
    {
        "name": "FourierKAN",
        "description": "KAN с функциями Фурье."
    },
    {
        "name": "RadialKAN",
        "description": "KAN с радиальными базисными функциями."
    },
    {
        "name": "WaveletKAN",
        "description": "KAN с вейвлет-функциями."
    },
    {
        "name": "Оптимизированные локальные KAN (X-KAN)",
        "description": "Модифицированная версия KAN с улучшенной локальной аппроксимацией функций."
    },
    {
        "name": "Adaptive X-KAN",
        "description": "Адаптивная X-KAN с динамической настройкой."
    },
    {
        "name": "Multi-scale X-KAN",
        "description": "Мультимасштабная X-KAN."
    },
    {
        "name": "KAGNN (KAN for Graph Neural Networks)",
        "description": "Адаптация сетей Колмогорова-Арнольда для работы с графовыми структурами данных."
    },
    {
        "name": "GraphKAN",
        "description": "Графовая версия KAN."
    },
    {
        "name": "Spectral KAN",
        "description": "Спектральная KAN для графов."
    },
    {
        "name": "KAN-Transformer",
        "description": "Гибрид KAN и трансформера."
    },
    {
        "name": "KAN-CNN",
        "description": "Гибрид KAN и сверточной сети."
    },
    {
        "name": "KAN-ResNet",
        "description": "KAN с остаточными соединениями."
    },
    {
        "name": "KAN-U-Net",
        "description": "KAN для сегментации изображений."
    },
    {
        "name": "KAN-LSTM",
        "description": "KAN для обработки последовательностей."
    },
    {
        "name": "KAN-Attention",
        "description": "KAN с механизмом внимания."
    },
    {
        "name": "KAN-RNN",
        "description": "Рекуррентная KAN."
    },
    {
        "name": "KAN-GRU",
        "description": "KAN на основе GRU."
    },
    {
        "name": "KAN-ODE",
        "description": "KAN с непрерывной глубиной."
    },
    {
        "name": "Fractional KAN",
        "description": "Дробная KAN для сложных функций."
    },
    {
        "name": "Quantum KAN",
        "description": "Квантовая версия KAN."
    },
    {
        "name": "Neurosymbolic KAN",
        "description": "Нейро-символическая KAN."
    },
    {
        "name": "Interpretable KAN",
        "description": "Интерпретируемая KAN."
    },
    {
        "name": "Sparse KAN",
        "description": "Разреженная KAN для эффективности."
    },
    {
        "name": "Pruned KAN",
        "description": "Прореженная KAN."
    },
    {
        "name": "Quantized KAN",
        "description": "Квантизованная KAN для deployment."
    },
    {
        "name": "Distilled KAN",
        "description": "Дистиллированная KAN."
    },
    {
        "name": "Ensemble KAN",
        "description": "Ансамбль KAN моделей."
    },
    {
        "name": "Multi-task KAN",
        "description": "KAN для многозадачного обучения."
    },
    {
        "name": "Continual KAN",
        "description": "KAN для непрерывного обучения."
    },
    {
        "name": "Meta KAN",
        "description": "Мета-обучающаяся KAN."
    },
    {
        "name": "Federated KAN",
        "description": "Федеративная KAN для распределенного обучения."
    },
    {
        "name": "Edge KAN",
        "description": "KAN для граничных устройств."
    },
    {
        "name": "Mobile KAN",
        "description": "Мобильная версия KAN."
    },
    {
        "name": "Tiny KAN",
        "description": "Крошечная KAN для микроконтроллеров."
    },
    {
        "name": "Nano KAN",
        "description": "Нано KAN для ultra-low power."
    },
]