"""
Module containing architecture categories data as general parameters.
"""

# Architecture categories data
ARCHITECTURE_CATEGORIES = [
    {
        "name": "Convolutional Architectures (CNN)",
        "description": "Neural network architectures primarily based on convolutional layers, commonly used for image processing and computer vision tasks."
    },
    {
        "name": "Transformers & Attention",
        "description": "Architectures utilizing attention mechanisms, particularly transformers, widely used in NLP and other domains requiring sequence modeling."
    },
    {
        "name": "Feedforward Architectures",
        "description": "Traditional neural networks with connections that flow only in one direction, from input to output, without cycles."
    },
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
        "name": "Самоорганизующаяся карта Кохонена (SOM, Self-Organizing Map)",
        "description": "Тип нейронной сети, используемый для кластеризации и визуализации многомерных данных."
    },
    {
        "name": "Обучение векторному квантованию (LVQ, Learning Vector Quantization)",
        "description": "Метод машинного обучения для задач классификации, основанный на сопоставлении с образцами."
    },
    {
        "name": "Экстремальная машина обучения (ELM, Extreme Learning Machine)",
        "description": "Метод обучения однослойных нейронных сетей с быстрым обучением и хорошей обобщающей способностью."
    },
    {
        "name": "Нейронная сеть с радиальными базисными функциями (RBF Network)",
        "description": "Сеть с радиальными базисными функциями, используемая для аппроксимации функций и классификации."
    },
    {
        "name": "Вероятностная нейронная сеть (PNN, Probabilistic Neural Network)",
        "description": "Статистическая нейронная сеть, основанная на байесовской теории вероятностей."
    },
    {
        "name": "Глубокие порождающие модели (DBN, Deep Belief Network)",
        "description": "Глубокая нейронная сеть, состоящая из нескольких слоев стохастических скрытых переменных."
    },
    {
        "name": "Автоэнкодер (Autoencoder)",
        "description": "Нейронная сеть, обучаемая восстанавливать входные данные на выходе, обычно используется для снижения размерности."
    },
    {
        "name": "Деноизинговый автоэнкодер (DAE, Denoising Autoencoder)",
        "description": "Автоэнкодер, обучаемый восстанавливать чистые данные из зашумленных входов."
    },
    {
        "name": "Контрактивный автоэнкодер (CAE, Contractive Autoencoder)",
        "description": "Автоэнкодер, использующий контрактивный штраф для получения инвариантных представлений."
    },
    {
        "name": "Разреженный автоэнкодер (Sparse Autoencoder)",
        "description": "Автоэнкодер, использующий разреженность для ограничения активации нейронов в скрытом слое."
    },
    {
        "name": "Вариационный автоэнкодер (VAE, Variational Autoencoder)",
        "description": "Генеративная модель, объединяющая автоэнкодеры и вариационный вывод для генерации новых данных."
    },
    {
        "name": "Адверсариальный автоэнкодер (AAE, Adversarial Autoencoder)",
        "description": "Автоэнкодер, использующий состязательное обучение для формирования латентного пространства."
    },
    {
        "name": "Глубокая складывающаяся сеть (DSN, Deep Stacking Network)",
        "description": "Архитектура глубокого обучения, использующая модульную структуру с последовательным обучением слоев."
    },
    {
        "name": "Сети Колмогорова-Арнольда (KAN, Kolmogorov-Arnold Networks)",
        "description": "Нейронные сети, основанные на теореме Колмогорова-Арнольда о представлении непрерывных функций."
    },
    {
        "name": "Оптимизированные локальные KAN (X-KAN)",
        "description": "Модифицированная версия KAN с улучшенной локальной аппроксимацией функций."
    },
    {
        "name": "KAGNN (KAN for Graph Neural Networks)",
        "description": "Адаптация сетей Колмогорова-Арнольда для работы с графовыми структурами данных."
    },
    {
        "name": "Generative Models",
        "description": "Models designed to generate new data samples, including GANs, VAEs, and diffusion models."
    },
    {
        "name": "State Space Models and Post-Transformer Architectures",
        "description": "Modern architectures including state space models and other approaches that emerged after transformer dominance."
    },
    {
        "name": "Recurrent and Sequential Architectures (RNN)",
        "description": "Architectures designed for sequential data processing, including RNNs, LSTMs, and GRUs."
    },
    {
        "name": "Graph Neural Networks (GNN)",
        "description": "Neural networks specifically designed to operate on graph-structured data, processing relationships between entities."
    },
    {
        "name": "Нейронные ОДУ и непрерывные модели",
        "description": "Архитектуры, основанные на обыкновенных дифференциальных уравнениях и непрерывных во времени моделях."
    },
    {
        "name": "Спайковые и нейроморфные архитектуры",
        "description": "Архитектуры, имитирующие биологические нейронные сети с использованием спайковых сигналов и нейроморфных принципов."
    },
    {
        "name": "Нейросимволические и гибридные архитектуры",
        "description": "Архитектуры, сочетающие нейронные и символические методы обработки информации."
    },
    {
        "name": "Архитектуры для обучения с усилением (RL)",
        "description": "Архитектуры, разработанные специально для задач обучения с подкреплением."
    },
    {
        "name": "Эффективные и мобильные архитектуры",
        "description": "Архитектуры, оптимизированные для работы на ограниченных вычислительных ресурсах."
    },
    {
        "name": "Архитектуры для малых данных и few-shot learning",
        "description": "Архитектуры, способные эффективно обучаться на ограниченных объемах данных."
    },
    {
        "name": "Архитектуры для поиска архитектур (NAS)",
        "description": "Архитектуры, используемые для автоматического поиска оптимальных архитектур нейронных сетей."
    },
    {
        "name": "Мультимодальные архитектуры",
        "description": "Архитектуры, способные обрабатывать несколько различных типов данных одновременно."
    },
    {
        "name": "Энергетические и равновесные модели",
        "description": "Модели, основанные на энергетических функциях и принципах термодинамического равновесия."
    },
    {
        "name": "Специализированные архитектуры",
        "description": "Архитектуры, разработанные для конкретных задач или областей применения."
    }
]

# Additional general parameters
DEFAULT_CATEGORY_NAMES = [category["name"] for category in ARCHITECTURE_CATEGORIES]
CATEGORY_COUNT = len(ARCHITECTURE_CATEGORIES)