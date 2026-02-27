-- Two-level hierarchy: Categories -> Architectures

CREATE INDEX ON :Category(name);
CREATE INDEX ON :Architecture(name);

        CREATE (c:Category {
            name: 'FeedForward',
            type: 'category_group',
            architecture_count: 129
        });
        

        CREATE (c:Category {
            name: 'CNN',
            type: 'category_group',
            architecture_count: 47
        });
        

        CREATE (c:Category {
            name: 'GNN',
            type: 'category_group',
            architecture_count: 50
        });
        

        CREATE (c:Category {
            name: 'TransformersAndAttention',
            type: 'category_group',
            architecture_count: 151
        });
        

        CREATE (c:Category {
            name: 'Generative',
            type: 'category_group',
            architecture_count: 62
        });
        

        CREATE (c:Category {
            name: 'NAS',
            type: 'category_group',
            architecture_count: 50
        });
        

        CREATE (c:Category {
            name: 'Multimodal',
            type: 'category_group',
            architecture_count: 70
        });
        

        CREATE (c:Category {
            name: 'EnergyAndEquilibriaum',
            type: 'category_group',
            architecture_count: 51
        });
        

        CREATE (c:Category {
            name: 'EfficientAndMobile',
            type: 'category_group',
            architecture_count: 58
        });
        

        CREATE (c:Category {
            name: 'RecAndSeq',
            type: 'category_group',
            architecture_count: 51
        });
        

        CREATE (c:Category {
            name: 'RL',
            type: 'category_group',
            architecture_count: 50
        });
        

        CREATE (c:Category {
            name: 'StateSpace',
            type: 'category_group',
            architecture_count: 69
        });
        

        CREATE (c:Category {
            name: 'SmallDataAndFewShot',
            type: 'category_group',
            architecture_count: 70
        });
        

        CREATE (c:Category {
            name: 'Specialized',
            type: 'category_group',
            architecture_count: 72
        });
        

        CREATE (c:Category {
            name: 'SpikeAndNeuromorph',
            type: 'category_group',
            architecture_count: 73
        });
        

        CREATE (c:Category {
            name: 'NeuroSymbolicAndHybrid',
            type: 'category_group',
            architecture_count: 70
        });
        

        CREATE (c:Category {
            name: 'NeuralODEsAndContin',
            type: 'category_group',
            architecture_count: 72
        });
        

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'FeedForward Architectures',
                description: 'artificial neural networks in which the signal propagates strictly from the input layer to the output',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Перцептрон (Perceptron)',
                description: 'Простейшая модель искусственного нейрона, используемая для бинарной классификации.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Adaline / Madaline',
                description: 'Адаптивный линейный элемент и его многослойное расширение, используемые для классификации и регрессии.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Многослойный перцептрон (MLP, Multilayer Perceptron)',
                description: 'Нейронная сеть с прямой связью, состоящая из одного или нескольких скрытых слоев.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Однослойный перцептрон (SLP)',
                description: 'Простейшая нейронная сеть без скрытых слоев для линейной классификации.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Глубокий MLP (Deep MLP)',
                description: 'Многослойный перцептрон с множеством скрытых слоев для сложных задач.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Широкий MLP (Wide MLP)',
                description: 'MLP с большим количеством нейронов в каждом слое.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'MLP с Dropout',
                description: 'MLP с регуляризацией dropout для предотвращения переобучения.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'MLP с Batch Normalization',
                description: 'MLP с пакетной нормализацией для ускорения обучения.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'MLP с Layer Normalization',
                description: 'MLP с нормализацией по слоям.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Residual MLP',
                description: 'MLP с остаточными соединениями для улучшения градиентного потока.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Dense MLP',
                description: 'Плотно связанный MLP с соединениями между всеми слоями.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Самоорганизующаяся карта Кохонена (SOM, Self-Organizing Map)',
                description: 'Тип нейронной сети, используемый для кластеризации и визуализации многомерных данных.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Growing SOM (GSOM)',
                description: 'Расширяемая самоорганизующаяся карта с динамическим ростом.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Hierarchical SOM',
                description: 'Иерархическая SOM для многоуровневой кластеризации.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Fuzzy SOM',
                description: 'Нечеткая самоорганизующаяся карта.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Обучение векторному квантованию (LVQ, Learning Vector Quantization)',
                description: 'Метод машинного обучения для задач классификации, основанный на сопоставлении с образцами.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'LVQ1',
                description: 'Базовая версия обучения векторному квантованию.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'LVQ2.1',
                description: 'Улучшенная версия LVQ с коррекцией границ.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'LVQ3',
                description: 'Расширенная LVQ с дополнительной коррекцией.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'OLVQ (Optimized LVQ)',
                description: 'Оптимизированная LVQ с адаптивными скоростями обучения.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'GRLVQ (Generalized Relevance LVQ)',
                description: 'Обобщенная релевантная LVQ с взвешиванием признаков.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Экстремальная машина обучения (ELM, Extreme Learning Machine)',
                description: 'Метод обучения однослойных нейронных сетей с быстрым обучением и хорошей обобщающей способностью.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Online-ELM',
                description: 'Онлайн версия ELM для потоковых данных.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Incremental-ELM',
                description: 'Инкрементальная ELM с постепенным добавлением нейронов.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Pruned-ELM',
                description: 'Прореженная ELM для уменьшения размера модели.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Ensemble-ELM',
                description: 'Ансамбль ELM для повышения точности.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Deep-ELM',
                description: 'Глубокая ELM с несколькими скрытыми слоями.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Conv-ELM',
                description: 'Сверточная ELM для обработки изображений.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Нейронная сеть с радиальными базисными функциями (RBF Network)',
                description: 'Сеть с радиальными базисными функциями, используемая для аппроксимации функций и классификации.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'RBF с гауссовыми функциями',
                description: 'RBF сеть с гауссовыми радиальными функциями.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'RBF с мультиквадриками',
                description: 'RBF сеть с мультиквадричными функциями.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Orthogonal RBF',
                description: 'Ортогональная RBF сеть для лучшей сходимости.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Normalized RBF',
                description: 'Нормализованная RBF сеть.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Local RBF',
                description: 'Локальная RBF сеть с ограниченной областью влияния.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Вероятностная нейронная сеть (PNN, Probabilistic Neural Network)',
                description: 'Статистическая нейронная сеть, основанная на байесовской теории вероятностей.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'PNN с гауссовым ядром',
                description: 'PNN с гауссовой функцией ядра.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Enhanced PNN',
                description: 'Улучшенная PNN с оптимизированными параметрами.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Reduced PNN',
                description: 'Сокращенная PNN для уменьшения вычислений.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Fuzzy PNN',
                description: 'Нечеткая вероятностная нейронная сеть.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Глубокие порождающие модели (DBN, Deep Belief Network)',
                description: 'Глубокая нейронная сеть, состоящая из нескольких слоев стохастических скрытых переменных.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'DBN с RBM',
                description: 'DBN построенная из ограниченных машин Больцмана.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Convolutional DBN',
                description: 'Сверточная DBN для обработки изображений.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Discriminative DBN',
                description: 'Дискриминативная DBN для классификации.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Глубокая складывающаяся сеть (DSN, Deep Stacking Network)',
                description: 'Архитектура глубокого обучения, использующая модульную структуру с последовательным обучением слоев.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Convolutional DSN',
                description: 'Сверточная DSN для визуальных задач.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Modular DSN',
                description: 'Модульная DSN с независимыми блоками.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Автоэнкодер (Autoencoder)',
                description: 'Нейронная сеть, обучаемая восстанавливать входные данные на выходе, обычно используется для снижения размерности.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Undercomplete Autoencoder',
                description: 'Автоэнкодер с меньшим скрытым слоем для сжатия данных.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Overcomplete Autoencoder',
                description: 'Автоэнкодер с большим скрытым слоем.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Shallow Autoencoder',
                description: 'Поверхностный автоэнкодер с одним скрытым слоем.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Deep Autoencoder',
                description: 'Глубокий автоэнкодер с множеством скрытых слоев.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Stacked Autoencoder',
                description: 'Стекированный автоэнкодер с послойным обучением.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Convolutional Autoencoder',
                description: 'Сверточный автоэнкодер для изображений.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Recurrent Autoencoder',
                description: 'Рекуррентный автоэнкодер для последовательностей.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'LSTM Autoencoder',
                description: 'Автоэнкодер на основе LSTM.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Деноизинговый автоэнкодер (DAE, Denoising Autoencoder)',
                description: 'Автоэнкодер, обучаемый восстанавливать чистые данные из зашумленных входов.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Gaussian DAE',
                description: 'DAE с гауссовым шумом.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Salt-and-Pepper DAE',
                description: 'DAE с импульсным шумом.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Masking DAE',
                description: 'DAE с маскированием входов.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Контрактивный автоэнкодер (CAE, Contractive Autoencoder)',
                description: 'Автоэнкодер, использующий контрактивный штраф для получения инвариантных представлений.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Robust CAE',
                description: 'Робастный контрактивный автоэнкодер.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Higher-order CAE',
                description: 'CAE с производными высшего порядка.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Разреженный автоэнкодер (Sparse Autoencoder)',
                description: 'Автоэнкодер, использующий разреженность для ограничения активации нейронов в скрытом слое.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'L1 Sparse Autoencoder',
                description: 'Разреженный автоэнкодер с L1 регуляризацией.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'KL Sparse Autoencoder',
                description: 'Разреженный автоэнкодер с KL-дивергенцией.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Topographic Sparse AE',
                description: 'Топографический разреженный автоэнкодер.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Вариационный автоэнкодер (VAE, Variational Autoencoder)',
                description: 'Генеративная модель, объединяющая автоэнкодеры и вариационный вывод для генерации новых данных.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Beta-VAE',
                description: 'VAE с параметром бета для разделения представлений.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Conditional VAE (CVAE)',
                description: 'Условный VAE для контролируемой генерации.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'InfoVAE',
                description: 'VAE с максимизацией взаимной информации.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Wasserstein VAE',
                description: 'VAE с метрикой Вассерштейна.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Adversarial VAE',
                description: 'Состязательный вариационный автоэнкодер.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Hierarchical VAE',
                description: 'Иерархический VAE с многоуровневым латентным пространством.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Vector Quantized VAE (VQ-VAE)',
                description: 'VAE с векторным квантованием латентного пространства.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'VQ-VAE-2',
                description: 'Улучшенный VQ-VAE с иерархическим квантованием.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Normalizing Flow VAE',
                description: 'VAE с нормализующими потоками.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Annealed VAE',
                description: 'VAE с аннилингом для лучшего обучения.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Disentangled VAE',
                description: 'VAE с разделенными факторами вариации.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'FactorVAE',
                description: 'VAE с факторизованным латентным пространством.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'DIP-VAE',
                description: 'VAE с disentangled inference prior.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'β-TCVAE',
                description: 'Total Correlation VAE с параметром бета.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'RF-VAE',
                description: 'Relevance Factorized VAE.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Адверсариальный автоэнкодер (AAE, Adversarial Autoencoder)',
                description: 'Автоэнкодер, использующий состязательное обучение для формирования латентного пространства.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'InfoAAE',
                description: 'AAE с максимизацией взаимной информации.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Semi-supervised AAE',
                description: 'Полуавтоматический адверсариальный автоэнкодер.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'CatAAE',
                description: 'Категориальный AAE для дискретных данных.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Continuous AAE',
                description: 'Непрерывный AAE для непрерывных представлений.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Wasserstein AAE',
                description: 'AAE с метрикой Вассерштейна.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Сети Колмогорова-Арнольда (KAN, Kolmogorov-Arnold Networks)',
                description: 'Нейронные сети, основанные на теореме Колмогорова-Арнольда о представлении непрерывных функций.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'FastKAN',
                description: 'Быстрая версия KAN с оптимизированными вычислениями.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'EfficientKAN',
                description: 'Эффективная KAN с уменьшенной сложностью.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'SplineKAN',
                description: 'KAN с сплайн-функциями активации.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'ChebyKAN',
                description: 'KAN с полиномами Чебышева.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'FourierKAN',
                description: 'KAN с функциями Фурье.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'RadialKAN',
                description: 'KAN с радиальными базисными функциями.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'WaveletKAN',
                description: 'KAN с вейвлет-функциями.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Оптимизированные локальные KAN (X-KAN)',
                description: 'Модифицированная версия KAN с улучшенной локальной аппроксимацией функций.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Adaptive X-KAN',
                description: 'Адаптивная X-KAN с динамической настройкой.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Multi-scale X-KAN',
                description: 'Мультимасштабная X-KAN.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'KAGNN (KAN for Graph Neural Networks)',
                description: 'Адаптация сетей Колмогорова-Арнольда для работы с графовыми структурами данных.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'GraphKAN',
                description: 'Графовая версия KAN.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Spectral KAN',
                description: 'Спектральная KAN для графов.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'KAN-Transformer',
                description: 'Гибрид KAN и трансформера.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'KAN-CNN',
                description: 'Гибрид KAN и сверточной сети.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'KAN-ResNet',
                description: 'KAN с остаточными соединениями.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'KAN-U-Net',
                description: 'KAN для сегментации изображений.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'KAN-LSTM',
                description: 'KAN для обработки последовательностей.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'KAN-Attention',
                description: 'KAN с механизмом внимания.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'KAN-RNN',
                description: 'Рекуррентная KAN.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'KAN-GRU',
                description: 'KAN на основе GRU.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'KAN-ODE',
                description: 'KAN с непрерывной глубиной.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Fractional KAN',
                description: 'Дробная KAN для сложных функций.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Quantum KAN',
                description: 'Квантовая версия KAN.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Neurosymbolic KAN',
                description: 'Нейро-символическая KAN.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Interpretable KAN',
                description: 'Интерпретируемая KAN.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Sparse KAN',
                description: 'Разреженная KAN для эффективности.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Pruned KAN',
                description: 'Прореженная KAN.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Quantized KAN',
                description: 'Квантизованная KAN для deployment.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Distilled KAN',
                description: 'Дистиллированная KAN.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Ensemble KAN',
                description: 'Ансамбль KAN моделей.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Multi-task KAN',
                description: 'KAN для многозадачного обучения.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Continual KAN',
                description: 'KAN для непрерывного обучения.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Meta KAN',
                description: 'Мета-обучающаяся KAN.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Federated KAN',
                description: 'Федеративная KAN для распределенного обучения.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Edge KAN',
                description: 'KAN для граничных устройств.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Mobile KAN',
                description: 'Мобильная версия KAN.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Tiny KAN',
                description: 'Крошечная KAN для микроконтроллеров.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'FeedForward'})
            CREATE (a:Architecture:`FeedForward` {
                name: 'Nano KAN',
                description: 'Нано KAN для ultra-low power.',
                category: 'FeedForward'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'LeNet-5',
                description: 'Pioneering CNN architecture for handwritten digit recognition, introduced by Yann LeCun in 1998',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'AlexNet',
                description: 'Breakthrough deep CNN that won ImageNet 2012, featuring ReLU activations and dropout',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'VGG-11',
                description: 'Simple CNN architecture with 11 layers using small 3x3 convolution filters',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'VGG-13',
                description: '13-layer VGG variant with increased depth for better feature extraction',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'VGG-16',
                description: 'Popular 16-layer VGG architecture widely used for transfer learning',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'VGG-19',
                description: '19-layer VGG variant providing deeper hierarchical feature representations',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'GoogLeNet/Inception-v1',
                description: '22-layer CNN with inception modules for efficient computation and accuracy',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'Inception-v2',
                description: 'Improved inception architecture with batch normalization and factorized convolutions',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'Inception-v3',
                description: 'Further optimized inception with label smoothing and advanced factorization',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'Inception-v4',
                description: 'Advanced inception architecture with improved training stability',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'Inception-ResNet-v1',
                description: 'Hybrid architecture combining inception modules with residual connections',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'Inception-ResNet-v2',
                description: 'Deeper hybrid model with enhanced inception-residual blocks',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'ResNet-18',
                description: '18-layer residual network with skip connections for easier training',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'ResNet-34',
                description: '34-layer residual network balancing depth and computational efficiency',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'ResNet-50',
                description: '50-layer residual network with bottleneck architecture for deep learning',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'ResNet-101',
                description: '101-layer deep residual network for high-accuracy image recognition',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'ResNet-152',
                description: '152-layer extremely deep residual network achieving state-of-the-art results',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'ResNeXt-50',
                description: '50-layer network using cardinality (split-transform-merge) strategy',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'ResNeXt-101',
                description: '101-layer ResNeXt with grouped convolutions for improved performance',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'DenseNet-121',
                description: '121-layer densely connected network with feature reuse across layers',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'DenseNet-169',
                description: '169-layer DenseNet with enhanced gradient flow and parameter efficiency',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'DenseNet-201',
                description: '201-layer DenseNet providing maximum feature reuse and connectivity',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'SE-ResNet-50',
                description: 'ResNet-50 with Squeeze-and-Excitation blocks for channel attention',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'SE-ResNet-101',
                description: 'ResNet-101 enhanced with channel-wise attention mechanisms',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'SE-ResNet-152',
                description: 'ResNet-152 with squeeze-and-excitation for improved feature calibration',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'Xception',
                description: 'Extreme inception architecture using depthwise separable convolutions',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'MobileNet-v1',
                description: 'Lightweight CNN using depthwise separable convolutions for mobile devices',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'MobileNet-v2',
                description: 'Improved MobileNet with inverted residuals and linear bottlenecks',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'MobileNet-v3',
                description: 'Neural architecture search optimized MobileNet with attention mechanisms',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'ShuffleNet-v1',
                description: 'Efficient CNN with channel shuffling for mobile applications',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'ShuffleNet-v2',
                description: 'Improved ShuffleNet with better speed-accuracy tradeoff',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'SqueezeNet',
                description: 'Compact CNN achieving AlexNet accuracy with 50x fewer parameters',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'EfficientNet-B0',
                description: 'Baseline efficient CNN with compound scaling of depth, width, and resolution',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'EfficientNet-B7',
                description: 'Largest EfficientNet variant with state-of-the-art accuracy and efficiency',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'NASNet-A',
                description: 'Neural Architecture Search discovered CNN with optimal cell structure',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'NASNet-Large',
                description: 'Large-scale NAS-discovered architecture for high-performance tasks',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'Darknet-53',
                description: '53-layer backbone network for YOLO object detection',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'CSPDarknet53',
                description: 'Cross Stage Partial Darknet for improved gradient flow in YOLOv4',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'ConvNeXt-Tiny',
                description: 'Modernized CNN architecture matching Transformer performance',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'ConvNeXt-Base',
                description: 'Base ConvNeXt model with pure CNN design and Transformer-like accuracy',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'RegNetX-400MF',
                description: '400MF parameter network from design space exploration',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'RegNetY-800MF',
                description: '800MF RegNet with optimized design principles',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'GhostNet',
                description: 'Efficient network generating ghost feature maps for mobile deployment',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'MixNet-S',
                description: 'Small MixNet using mixed depthwise convolutions for efficiency',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'MixNet-M',
                description: 'Medium MixNet balancing accuracy and computational cost',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'MixNet-L',
                description: 'Large MixNet achieving high accuracy with mixed convolution kernels',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'CNN'})
            CREATE (a:Architecture:`CNN` {
                name: 'Convolutional Architectures (CNN)',
                description: 'Neural network architectures primarily based on convolutional layers, commonly used for image processing and computer vision tasks.',
                category: 'CNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'GCN',
                description: 'Graph Convolutional Network using spectral graph convolutions',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'ChebNet',
                description: 'Chebyshev spectral CNN for efficient graph convolutions',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'CayleyNet',
                description: 'Spectral GNN using Cayley polynomials for graph filtering',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'GAT',
                description: 'Graph Attention Network using attention for neighbor aggregation',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'GATv2',
                description: 'Improved GAT with dynamic attention mechanism',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'Multi-Head-GAT',
                description: 'GAT with multiple attention heads for diverse features',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'GraphSAGE',
                description: 'Inductive GNN sampling and aggregating neighbor features',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'Mean-GraphSAGE',
                description: 'GraphSAGE using mean aggregator for neighbors',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'LSTM-GraphSAGE',
                description: 'GraphSAGE with LSTM aggregator for sequential neighbors',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'Pooling-GraphSAGE',
                description: 'GraphSAGE using pooling aggregator for neighbor features',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'GIN',
                description: 'Graph Isomorphism Network with injective aggregation',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'GIN-0',
                description: 'GIN variant with epsilon=0 for maximum expressiveness',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'GraphCNN',
                description: 'Graph CNN with hierarchical pooling for graph classification',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'DGCNN',
                description: 'Deep Graph CNN with SortPooling for graph classification',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'DiffPool',
                description: 'Differentiable pooling for hierarchical GNN',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'MinCutPool',
                description: 'GNN with min-cut pooling for graph coarsening',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'SAGPool',
                description: 'Self-attention graph pooling for hierarchical representation',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'EdgeConv',
                description: 'Dynamic graph CNN operating on edge features',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'PointNet',
                description: 'Deep learning on point sets for 3D classification',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'PointNet++',
                description: 'Hierarchical PointNet for local feature learning',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'DGCNN-Point',
                description: 'Dynamic Graph CNN for point cloud processing',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'PCT',
                description: 'Point Cloud Transformer using self-attention on points',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'Graph-Transformer',
                description: 'Transformer architecture adapted for graph data',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'Graphormer',
                description: 'Transformer with centrality encoding for graphs',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'SAN',
                description: 'Spectral Attention Network for graph representation',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'GPS',
                description: 'Graph Product of Sum combining local and global attention',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'MoNet',
                description: 'Geometric deep learning with mixture models on graphs',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'SplineCNN',
                description: 'Continuous kernel convolution on irregular domains',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'FeaStNet',
                description: 'Feature Steerable CNN for graph-structured data',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'GatedGCN',
                description: 'Gated Graph Convolutional Network with edge features',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'ResGatedGCN',
                description: 'Residual Gated GCN for deep graph learning',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'TAGCN',
                description: 'Topology Adaptive Graph CNN with learnable filters',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'ARMA',
                description: 'Auto-Regressive Moving Average graph filter',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'APPNP',
                description: 'Approximate Personalized Propagation of Neural Predictions',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'SGC',
                description: 'Simplified Graph Convolution removing non-linearities',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'SIGN',
                description: 'Scalable Inception Graph Network with precomputed features',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'Cluster-GCN',
                description: 'GCN using graph clustering for efficient training',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'GraphSAINT',
                description: 'Graph sampling and aggregation for scalable GNN',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'FastGCN',
                description: 'Fast GCN using importance sampling for efficiency',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'LADIES',
                description: 'Layer-wise sampling for deep GCN training',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'VRGCN',
                description: 'Variance Reduced GCN for stable training',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'Graph-BERT',
                description: 'BERT-style pre-training for graph representation',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'GraphMAE',
                description: 'Masked AutoEncoder for self-supervised graph learning',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'BGRL',
                description: 'Bootstrapped Graph Representation Learning',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'GRACE',
                description: 'Graph Representation learning via Adaptive Contrastive Enhancement',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'GCA',
                description: 'Graph Contrastive Augmentation for self-supervised learning',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'MVGRL',
                description: 'Multi-View Graph Representation Learning',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'DGI',
                description: 'Deep Graph Infomax for unsupervised representation',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'GMI',
                description: 'Graph Mutual Information maximization for learning',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'GNN'})
            CREATE (a:Architecture:`GNN` {
                name: 'GCL',
                description: 'Graph Contrastive Learning framework',
                category: 'GNN'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Transformers and mechanisms of attention',
                description: 'abandoning sequential data processing in favor of parallelism and the ability of the model to instantly determine the significance of relationships between any data elements, regardless of the distance between them.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Transformer',
                description: 'Оригинальная архитектура \'Attention Is All You Need\' с self-attention. Варианты: Base (65M), Big (213M).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Transformer-Encoder',
                description: 'Только encoder часть трансформера для задач понимания. Варианты: 6-12 слоев.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Transformer-Decoder',
                description: 'Только decoder часть для генерации последовательностей. Варианты: 6-12 слоев.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Transformer-Encoder-Decoder',
                description: 'Полная архитектура encoder-decoder для seq2seq задач. Варианты: 6-24 слоев.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Pre-LN Transformer',
                description: 'Трансформер с пред-нормализацией (LayerNorm перед подслоями). Более стабильное обучение.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Post-LN Transformer',
                description: 'Трансформер с пост-нормализацией (LayerNorm после подслоев). Оригинальная версия.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Deep Transformer',
                description: 'Трансформер с увеличенной глубиной. Варианты: 12-48 слоев.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Wide Transformer',
                description: 'Трансформер с увеличенной шириной. Варианты: 512-4096 hidden dimensions.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'BERT',
                description: 'Bidirectional Encoder Representations from Transformers. Варианты: Base (110M, 12 слоев), Large (340M, 24 слоя). Uncased/Cased версии.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'BERT-Whole-Word-Masking',
                description: 'BERT с маскированием целых слов вместо токенов. Улучшает понимание слов.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'SpanBERT',
                description: 'BERT с предсказанием span\'ов вместо отдельных токенов. Варианты: Base, Large.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'CodeBERT',
                description: 'BERT для программирования и кода. Обучен на Python и документациях. 125M параметров.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'GraphCodeBERT',
                description: 'BERT для кода с графами потока данных. Улучшенное понимание структуры кода.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'SciBERT',
                description: 'BERT для научных текстов. Обучен на научных публикациях. 114M параметров.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'BioBERT',
                description: 'BERT для биомедицинских текстов. Обучен на PubMed. 110M параметров.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'ClinicalBERT',
                description: 'BERT для клинических записей. Специализирован на медицинских данных.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'LegalBERT',
                description: 'BERT для юридических документов. Обучен на юридических текстах.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'FinBERT',
                description: 'BERT для финансовых текстов. Специализирован на финансовой терминологии.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'RoBERTa',
                description: 'Robustly Optimized BERT Pretraining Approach. Улучшенный BERT без NSP. Варианты: Base (125M), Large (355M), XL (900M), XXL (1.8B).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Longformer-RoBERTa',
                description: 'RoBERTa с sparse attention для длинных документов. До 4096 токенов.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'CodeRoBERTa',
                description: 'RoBERTa для программирования. Улучшенная версия CodeBERT.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'ALBERT',
                description: 'A Lite BERT с параметрическим sharing. Меньше параметров при той же производительности. Варианты: Base (12M), Large (18M), XL (58M), XXL (223M).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'DistilBERT',
                description: 'Дистиллированный BERT: 6 слоев, 40% меньше параметров (66M), 60% скорости, 97% качества BERT.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'DistilRoBERTa',
                description: 'Дистиллированный RoBERTa. 8 слоев, 124M параметров.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'TinyBERT',
                description: 'Крошечный BERT для мобильных устройств. Варианты: 4 слоя (14.5M), 6 слоев (67M).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'MiniLM',
                description: 'Miniature Language Model с эффективной дистилляцией. Варианты: L6 (22M), L12 (33M), v2 (улучшенная версия).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'MobileBERT',
                description: 'Mobile-friendly BERT с bottleneck структурой. 25M параметров, оптимизирован для мобильных.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'FastBERT',
                description: 'Быстрый BERT с adaptive inference (ранний выход). Варианты: Base, Large.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'ELECTRA',
                description: 'Efficiently Learning Encoder that Classifies Token Replacements. Более эффективное обучение. Варианты: Small (14M), Base (110M), Large (335M).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'CodeELECTRA',
                description: 'ELECTRA для программирования. Специализирован на коде.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'T5',
                description: 'Text-To-Text Transfer Transformer. Все задачи как text-to-text. Варианты: Small (60M), Base (220M), Large (770M), 3B, 11B, XXL.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'mT5',
                description: 'Multilingual T5 для 101 языка. Варианты: Small (300M), Base (580M), Large (1.2B), XL (3.7B), XXL (13B).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'CodeT5',
                description: 'T5 для программирования. Поддерживает 11 языков программирования. Варианты: Small, Base, Large.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Flan-T5',
                description: 'T5 с instruction tuning для лучших zero-shot результатов. Варианты: Small, Base, Large, XL, XXL.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'ByT5',
                description: 'Byte-level T5 без токенизатора. Работает на уровне байтов. Варианты: Small, Base, Large.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'GPT',
                description: 'Generative Pre-trained Transformer (OpenAI). Оригинальная версия. 117M параметров.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'GPT-2',
                description: 'Второе поколение GPT. Улучшенная архитектура и данные. Варианты: Small (117M), Medium (345M), Large (774M), XL (1.5B).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'GPT-3',
                description: 'GPT-3 с few-shot learning. Варианты: Ada (350M), Babbage (1.3B), Curie (6.7B), Davinci (175B).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'InstructGPT',
                description: 'GPT с instruction tuning и RLHF. Оптимизирован для следования инструкциям.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'ChatGPT',
                description: 'GPT оптимизированный для диалога. На базе GPT-3.5 с RLHF.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'GPT-4',
                description: 'Четвертое поколение GPT. Мультимодальный. Точное количество параметров не раскрыто.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'GPT-Neo',
                description: 'Open-source GPT от EleutherAI. Варианты: 125M, 1.3B, 2.7B.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'GPT-J',
                description: 'GPT-J с параллельными attention слоями. 6B параметров.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'GPT-NeoX',
                description: 'GPT-NeoX для больших моделей. Варианты: 20B. Языковые версии: Japanese, Korean (Polyglot-Ko).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'BLOOM',
                description: 'BigScience Large Open-science Open-access Multilingual. 46 языков. Варианты: 560M, 1.1B, 1.7B, 3B, 7.1B, 176B.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'OPT',
                description: 'Open Pre-trained Transformer от Meta. Полностью открытая модель. Варианты: 125M, 350M, 1.3B, 2.7B, 6.7B, 13B, 30B, 66B.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'LLaMA',
                description: 'Large Language Model Meta AI. Эффективная архитектура. Варианты: 7B, 13B, 33B, 65B.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'LLaMA-2',
                description: 'Второе поколение LLaMA. Улучшенное обучение и данные. Варианты: 7B, 13B, 70B. Есть Chat версия.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'LLaMA-3',
                description: 'Третье поколение LLaMA. Улучшенная архитектура и токенизатор. Варианты: 8B, 70B.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'CodeLLaMA',
                description: 'LLaMA для программирования. Поддерживает multiple языки. Варианты: 7B, 13B, 34B, 70B.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Vicuna',
                description: 'Fine-tuned LLaMA для диалога. Обучен на ChatGPT данных. Варианты: 7B, 13B, 33B.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Alpaca',
                description: 'Instruction-tuned LLaMA. Обучен на Self-Instruct данных. 7B параметров.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'WizardLM',
                description: 'Улучшенный Alpaca с Evol-Instruct для сложных инструкций. Варианты: 7B, 13B, 70B.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Falcon',
                description: 'Falcon LLM от Technology Innovation Institute. Эффективная attention архитектура. Варианты: 7B, 40B, 180B. Есть Chat версия.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Mistral-7B',
                description: 'Mistral AI с sliding window attention. 7B параметров. Высокая эффективность.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Mixtral',
                description: 'Mixture of Experts от Mistral. Sparse MoE архитектура. Варианты: 8x7B (47B total, 13B active), 8x22B.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'PaLM',
                description: 'Pathways Language Model от Google. Эффективное параллельное обучение. Варианты: 8B, 62B, 540B.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'PaLM-2',
                description: 'Второе поколение PaLM. Улучшенная multilingual поддержка. Варианты: Gecko, Otter, Bison, Unicorn.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Gemini',
                description: 'Multimodal model от Google. Нативная мультимодальность. Варианты: Nano, Pro, Ultra.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Claude',
                description: 'Anthropic Claude model с Constitutional AI. Безопасный и полезный ассистент.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Claude-2',
                description: 'Второе поколение Claude. Улучшенная производительность и контекст.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Claude-3',
                description: 'Третье поколение Claude. Варианты: Haiku (быстрый), Sonnet (сбалансированный), Opus (мощный).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Linformer',
                description: 'Linear complexity Transformer. O(n) вместо O(n²). Варианты: Small, Base.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Performer',
                description: 'Transformer с linear attention через kernel methods (FAVOR+). Варианты: Base.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Reformer',
                description: 'Transformer с locality-sensitive hashing для эффективного attention. До 64K токенов.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Longformer',
                description: 'Transformer для длинных документов с sparse attention. Варианты: Base (4096 tokens), Large (8192 tokens).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'BigBird',
                description: 'Sparse attention Transformer. Комбинация local, global и random attention. Варианты: Base, Large.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Sparse Transformer',
                description: 'Transformer с sparse attention patterns. Различные паттерны разреженности.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Axial Transformer',
                description: 'Transformer с axial attention (factorized по осям). Для изображений.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Synthesizer',
                description: 'Transformer с learned attention weights вместо query-key.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'ViT',
                description: 'Vision Transformer. Первый чистый трансформер для изображений. Варианты: Tiny (5M), Small (22M), Base (86M), Large (307M), Huge (632M), Giant (1B).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'DeiT',
                description: 'Data-efficient Image Transformer. Обучен через distillation. Варианты: Tiny, Small, Base.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Swin Transformer',
                description: 'Hierarchical Vision Transformer с shifted windows. Варианты: Tiny, Small, Base, Large. Версия v2 с улучшенной стабильностью.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'PVT',
                description: 'Pyramid Vision Transformer. Иерархическая структура как у CNN. Варианты: Tiny, Small, Medium, Large. Версия v2 улучшена.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'CvT',
                description: 'Convolutional Vision Transformer. Комбинация convolution и attention. Варианты: 13, 21, W (wide).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'TNT',
                description: 'Transformer in Transformer. Вложенная attention структура. Варианты: Small, Base.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'CrossViT',
                description: 'Cross-attention Vision Transformer. Dual-branch архитектура. Варианты: Small, Base, Large.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'CaiT',
                description: 'Going deeper with Image Transformers. Class attention в последних слоях. Варианты: Small, Medium, Large.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'BoT',
                description: 'Bottleneck Transformer. Attention в bottleneck слоях ResNet. Варианты: 50, 101.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'CoAtNet',
                description: 'Combining Convolution and Attention. Гибрид convolution и attention. Варианты: 0-7 (25M до 3.9B).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'MaxViT',
                description: 'Multi-Axis Vision Transformer. Local и global attention. Варианты: Tiny, Small, Base, Large.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'MobileViT',
                description: 'Mobile Vision Transformer. Легковесный для мобильных. Варианты: XS, S, M, L. Версия v2 улучшена.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'EfficientFormer',
                description: 'Efficient Vision Transformer. Оптимизирован для latency. Варианты: L1, L3, L7.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'EdgeNeXt',
                description: 'Edge-friendly Vision Transformer. Для граничных устройств. Варианты: XXSmall, XSmall, Small, Medium, Large.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'TinyViT',
                description: 'Tiny Vision Transformer. Для мобильных и edge. Варианты: 5M, 11M, 21M параметров.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'LeViT',
                description: 'LeViT: Vision Transformer in ConvNet\'s Clothing. Гибрид архитектура. Варианты: 128, 192, 256, 384 (M operations).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'ViViT',
                description: 'Video Vision Transformer. Для видео классификации. Варианты: Factorised encoder, Decoder.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'TimeSformer',
                description: 'Space-Time Vision Transformer. Раздельное space и time attention. Варианты: Large.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'MViT',
                description: 'Multiscale Vision Transformer. Для видео и изображений. Версии: v1, v2 (улучшенная).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'VideoMAE',
                description: 'Masked Autoencoder для видео. Self-supervised обучение. Версия v2 улучшена.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'UniFormer',
                description: 'Unified Transformer для видео. Единая архитектура для space-time. Варианты: Small, Base.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Video-Swin',
                description: 'Swin Transformer для видео. 3D shifted windows. Варианты: Tiny, Small, Base.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'LayoutLM',
                description: 'Transformer для документов с layout информацией. Версии: v1, v2, v3 (улучшенные).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'StructuralLM',
                description: 'Transformer для структурированных документов. Учитывает структуру документа.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Table Transformer',
                description: 'Transformer для таблиц. Распознавание структуры таблиц.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Donut',
                description: 'Document understanding Transformer. OCR-free document understanding.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Pix2Struct',
                description: 'Pixel-to-Structure Transformer. Скриншот-to-структура.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Nougat',
                description: 'Neural Optical Understanding for Academic Texts. Научные документы в Markdown.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'ChartFormer',
                description: 'Transformer для графиков и диаграмм. Извлечение данных из chart.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Wav2Vec 2.0',
                description: 'Self-supervised learning для speech. Варианты: Base (95M), Large (317M), XL, XXL.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'HuBERT',
                description: 'Hidden Unit BERT для speech. Улучшенная версия Wav2Vec. Варианты: Base, Large.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'WavLM',
                description: 'Unified speech model. Для speech recognition и downstream задач. Варианты: Base, Large.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Data2Vec',
                description: 'General framework для speech, vision, NLP. Универсальная self-supervised модель.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'AST',
                description: 'Audio Spectrogram Transformer. Для классификации аудио. Варианты: Base.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Music Transformer',
                description: 'Transformer для генерации музыки. Relative attention для long-term структуры.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Jukebox',
                description: 'Music generation с lyrics. VQ-VAE + Transformer.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'MusicGen',
                description: 'Music generation model от Meta. Text-to-music.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'MusicLM',
                description: 'High-fidelity music generation от Google. Hierarchical sequence-to-sequence.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Graph Transformer',
                description: 'Transformer для графов. General architecture для graph data.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Graphormer',
                description: 'Transformer с centrality encoding для графов. Варианты: Base, Large.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'SAN',
                description: 'Spectral Attention Network. Spectral encoding для графов.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'GPS',
                description: 'Graph Product of Sum. Комбинация local и global attention.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Graph-BERT',
                description: 'BERT для графов. Pre-training на графах.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'GraphMAE',
                description: 'Masked Autoencoder для графов. Self-supervised на графах. Версия v2 улучшена.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'VisualBERT',
                description: 'BERT для vision-language. Простая архитектура для VQA.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'VL-BERT',
                description: 'Vision-Language BERT. General vision-language representation.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'LXMERT',
                description: 'Learning Cross-Modality Encoder. Cross-modal attention.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'UNITER',
                description: 'UNiversal Image-TExt Representation. Large-scale pretraining.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Oscar',
                description: 'Object-Semantics Aligned Pretraining. Object tags как anchor points.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'VinVL',
                description: 'Vision representations in Vision-Language. Улучшенные visual features.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'ViLT',
                description: 'Vision-and-Language Transformer без convolution. Pure Transformer.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'ALBEF',
                description: 'Align before Fuse. Contrastive learning для vision-language.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'BLIP',
                description: 'Bootstrapping Language-Image Pretraining. Self-training с noisy data. Версия v2 улучшена.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Flamingo',
                description: 'Visual language model для few-shot learning. Interleaved image-text.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'PaLI',
                description: 'Language-Image model. Scaling vision-language. Версии: v1, v2, v3.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'BEiT-3',
                description: 'Image as foreign language. Unified vision-language model.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'KOSMOS',
                description: 'Multimodal large language model. Grounding capabilities. Версии: 1, 2.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Scaled Dot-Product Attention',
                description: 'Оригинальный механизм внимания из Transformer. Scaled для стабильности.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Multi-Head Attention',
                description: 'Multi-head self-attention. Параллельные attention heads.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Additive Attention',
                description: 'Bahdanau attention (additive). Для seq2seq с alignment.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Multiplicative Attention',
                description: 'Luong attention (multiplicative). Варианты: dot, general, concat.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Global Attention',
                description: 'Global attention (все позиции). Для full context.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Local Attention',
                description: 'Local attention (window-based). Для long sequences.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Self-Attention',
                description: 'Self-attention (intra-attention). Within sequence attention.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Cross-Attention',
                description: 'Cross-attention (inter-attention). Between different sequences/modalities.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Hierarchical Attention',
                description: 'Hierarchical attention network. Multi-level attention.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Co-Attention',
                description: 'Co-attention для multimodal. Parallel attention на разных модальностях.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Gated Attention',
                description: 'Gated attention mechanism. С gating для контроля потока.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Dynamic Attention',
                description: 'Dynamic attention (adaptive). Адаптивные weights.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Sparse Attention',
                description: 'Sparse attention patterns. Различные паттерны разреженности.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Linear Attention',
                description: 'Linear complexity attention. O(n) вместо O(n²).',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Flash Attention',
                description: 'IO-aware exact attention. Быстрее и меньше памяти. Версия v2 улучшена.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Paged Attention',
                description: 'Paged attention (vLLM). Для efficient inference.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Ring Attention',
                description: 'Ring attention для long context. Distributed attention.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Window Attention',
                description: 'Sliding window attention. Local window с global.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Relative Position Attention',
                description: 'Relative position encoding. Учитывает относительные позиции.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'RoPE',
                description: 'Rotary Position Embedding. Rotary encoding для позиций.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'ALiBi',
                description: 'Attention with Linear Biases. Linear bias для extrapolation.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'FNet',
                description: 'Fourier Transform вместо attention. Быстрее attention.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'TransformersAndAttention'})
            CREATE (a:Architecture:`TransformersAndAttention` {
                name: 'Perceiver',
                description: 'Perceiver IO architecture. Unified architecture для разных модальностей. Варианты: AR, IO.',
                category: 'TransformersAndAttention'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'Generative Architectures',
                description: 'A type of machine learning algorithms and neural networks designed to create new, original content (text, images, sound, video, code) that mimics the structure and style of training data',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'Vanilla-GAN',
                description: 'Original Generative Adversarial Network with generator and discriminator',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'DCGAN',
                description: 'Deep Convolutional GAN with architectural constraints for stability',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'WGAN',
                description: 'Wasserstein GAN using Earth Mover distance for better training',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'WGAN-GP',
                description: 'WGAN with gradient penalty for improved stability',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'WGAN-LP',
                description: 'WGAN with Lipschitz penalty for stable training',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'LSGAN',
                description: 'Least Squares GAN using least squares loss function',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'HingeGAN',
                description: 'GAN trained with hinge loss for discriminator',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'Relativistic-GAN',
                description: 'GAN with relativistic discriminator comparing real and fake',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'SAGAN',
                description: 'Self-Attention GAN with attention mechanisms for global consistency',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'BigGAN',
                description: 'Large-scale GAN with high-resolution image generation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'StyleGAN',
                description: 'Style-based generator for controllable high-quality synthesis',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'StyleGAN2',
                description: 'Improved StyleGAN with better image quality and training',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'StyleGAN3',
                description: 'StyleGAN with alias-free generation for better quality',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'StyleGAN-XL',
                description: 'Extended StyleGAN for higher resolution and diversity',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'Progressive-GAN',
                description: 'Progressively growing GAN for high-resolution synthesis',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'CycleGAN',
                description: 'Unpaired image-to-image translation with cycle consistency',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'Pix2Pix',
                description: 'Paired image-to-image translation with conditional GAN',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'Pix2PixHD',
                description: 'High-definition Pix2Pix for semantic image synthesis',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'SPADE',
                description: 'Spatially-Adaptive Denormalization for semantic synthesis',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'StarGAN',
                description: 'Unified GAN for multi-domain image-to-image translation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'StarGAN-v2',
                description: 'Improved StarGAN with diverse image synthesis',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'MUNIT',
                description: 'Multimodal Unsupervised Image-to-Image Translation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'DRIT',
                description: 'Diverse Image-to-Image Translation via disentangled representations',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'UNIT',
                description: 'Unsupervised Image-to-Image Translation with shared latent space',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'FUNIT',
                description: 'Few-shot Unsupervised Image-to-Image Translation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'VAE',
                description: 'Variational Autoencoder for probabilistic latent representation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'Beta-VAE',
                description: 'VAE with disentangled latent representation learning',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'CVAE',
                description: 'Conditional VAE for controlled generation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'AAE',
                description: 'Adversarial Autoencoder combining VAE and GAN',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'WAE',
                description: 'Wasserstein Autoencoder with optimal transport',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'InfoVAE',
                description: 'VAE maximizing mutual information in latent space',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'VQ-VAE',
                description: 'Vector Quantized VAE with discrete latent representation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'VQ-VAE-2',
                description: 'Hierarchical VQ-VAE for high-fidelity generation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'NVAE',
                description: 'Normalizing Flow VAE with hierarchical latent variables',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'FlowVAE',
                description: 'VAE with normalizing flow for flexible posterior',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'Flow',
                description: 'Normalizing Flow for exact likelihood modeling',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'RealNVP',
                description: 'Real Non-Volume Preserving flow for density estimation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'Glow',
                description: 'Generative flow with invertible 1x1 convolutions',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'FFJORD',
                description: 'Free-form continuous normalizing flow',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'PixelCNN',
                description: 'Autoregressive pixel-level image generation model',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'PixelCNN++',
                description: 'Improved PixelCNN with better distribution modeling',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'PixelRNN',
                description: 'Recurrent neural network for pixel-level generation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'WaveNet',
                description: 'Autoregressive model for raw audio generation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'Parallel-WaveNet',
                description: 'Fast WaveNet using parallel generation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'WaveGlow',
                description: 'Flow-based model for high-quality audio synthesis',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'EBM',
                description: 'Energy-Based Model for implicit density estimation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'JEM',
                description: 'Joint Energy-based Model for classification and generation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'Diffusion-Model',
                description: 'Denoising diffusion probabilistic model for generation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'DDPM',
                description: 'Denoising Diffusion Probabilistic Model',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'DDIM',
                description: 'Denoising Diffusion Implicit Model for faster sampling',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'Score-SDE',
                description: 'Score-based generative model with stochastic differential equations',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'NCSN',
                description: 'Noise Conditional Score Network for score matching',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'NCSNv2',
                description: 'Improved NCSN with better score estimation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'ADM',
                description: 'Improved Denoising Diffusion Probabilistic Model',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'Guided-Diffusion',
                description: 'Diffusion model with classifier guidance',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'GLIDE',
                description: 'Text-guided diffusion model for image generation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'DALL-E',
                description: 'Autoregressive transformer for text-to-image generation',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'DALL-E-2',
                description: 'Improved DALL-E with diffusion model for higher quality',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'Stable-Diffusion',
                description: 'Latent diffusion model for efficient text-to-image synthesis',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'Midjourney',
                description: 'Text-to-image diffusion model with artistic capabilities',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Generative'})
            CREATE (a:Architecture:`Generative` {
                name: 'Imagen',
                description: 'Text-to-image diffusion with cascaded architecture',
                category: 'Generative'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'NASNet-A',
                description: 'Neural Architecture Search discovered normal and reduction cells',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'NASNet-B',
                description: 'Alternative NASNet variant with different cell structure',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'NASNet-C',
                description: 'Third NASNet variant optimized for mobile devices',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'ENAS',
                description: 'Efficient Neural Architecture Search with parameter sharing',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'DARTS',
                description: 'Differentiable Architecture Search using gradient-based optimization',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'DARTS-v2',
                description: 'Improved DARTS with second-order approximation',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'PDARTS',
                description: 'Progressive DARTS with increasing depth during search',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'SDARTS',
                description: 'Stabilized DARTS with adversarial training',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'PC-DARTS',
                description: 'Partial Channel DARTS for reduced memory consumption',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'DARTS+',
                description: 'Improved DARTS with early stopping and zero-cost proxies',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'AmoebaNet-A',
                description: 'Evolutionary NAS with regularized evolution algorithm',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'AmoebaNet-B',
                description: 'Improved AmoebaNet with better cell structure',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'AmoebaNet-C',
                description: 'Third generation AmoebaNet with enhanced performance',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'PNAS',
                description: 'Progressive Neural Architecture Search',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'PNAS-LS',
                description: 'PNAS with layer-wise search strategy',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'MNASNet',
                description: 'Platform-aware NAS optimizing for mobile latency',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'MNASNet-A1',
                description: 'MNASNet variant A1 balancing accuracy and latency',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'MNASNet-A2',
                description: 'MNASNet variant A2 with different trade-offs',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'MNASNet-B1',
                description: 'MNASNet variant B1 optimized for speed',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'FBNet-A',
                description: 'Facebook NAS variant A for specific hardware',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'FBNet-B',
                description: 'Facebook NAS variant B with different constraints',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'FBNet-C',
                description: 'Facebook NAS variant C optimized for accuracy',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'FBNet-v2',
                description: 'Second generation FBNet with improved search',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'FBNet-v3',
                description: 'Third generation FBNet with multi-objective optimization',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'ProxylessNAS',
                description: 'Direct architecture search on target task without proxy',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'ProxylessNAS-Mobile',
                description: 'ProxylessNAS optimized for mobile devices',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'ProxylessNAS-GPU',
                description: 'ProxylessNAS optimized for GPU inference',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'ProxylessNAS-FPGA',
                description: 'ProxylessNAS optimized for FPGA deployment',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'Once-for-All',
                description: 'OFA network supporting multiple architectures from one model',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'OFA-ResNet-50',
                description: 'Once-for-All ResNet-50 with elastic depth and width',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'OFA-MobileNet-v3',
                description: 'OFA variant of MobileNet-v3 with flexible kernels',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'AutoML-MobileNet',
                description: 'AutoML discovered MobileNet architecture',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'MNasNet-1.3',
                description: 'MNASNet with 1.3x depth multiplier',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'EfficientNet-NAS',
                description: 'NAS-discovered EfficientNet architecture',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'TinyNAS',
                description: 'NAS for extreme resource constraints',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'MicroNet',
                description: 'Ultra-efficient NAS for micro-controllers',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'MCUNet',
                description: 'NAS for micro-controllers with tiny memory',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'AutoKeras-CNN',
                description: 'AutoKeras discovered CNN architecture',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'AutoKeras-ResNet',
                description: 'AutoKeras discovered ResNet variant',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'AutoML-Zero',
                description: 'NAS discovering algorithms from scratch',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'Evolving-Transformer',
                description: 'Evolutionary search for optimal Transformer',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'Evolved-Transformer',
                description: 'NAS-discovered Transformer for sequence modeling',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'NAS-Bench-101',
                description: 'Tabular NAS benchmark with 423K architectures',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'NAS-Bench-201',
                description: 'Extended NAS benchmark with 15K architectures',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'NAS-Bench-301',
                description: 'Surrogate-based NAS benchmark',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'TransNAS-Bench',
                description: 'NAS benchmark for transfer learning',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'HW-NAS-Bench',
                description: 'Hardware-aware NAS benchmark',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'NAS-FPN',
                description: 'NAS-discovered Feature Pyramid Network',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'NAS-FCOS',
                description: 'NAS-discovered FCOS for object detection',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NAS'})
            CREATE (a:Architecture:`NAS` {
                name: 'DetNAS',
                description: 'NAS for object detection backbones',
                category: 'NAS'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Мультимодальные архитектуры',
                description: 'Архитектуры, способные обрабатывать несколько различных типов данных одновременно.',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'CLIP-Text-Encoder',
                description: 'CLIP text encoder component',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'CLIP-Image-Encoder',
                description: 'CLIP image encoder component',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'OpenCLIP',
                description: 'Open-source CLIP implementation',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'OpenCLIP-ViT-H',
                description: 'OpenCLIP with ViT-Huge',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'OpenCLIP-ViT-G',
                description: 'OpenCLIP with ViT-Giant',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'SigLIP',
                description: 'Sigmoid Loss for Language-Image Pre-training',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'LiT-Base',
                description: 'Locked-image text tuning Base model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'LiT-Large',
                description: 'Locked-image text tuning Large model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'ALIGN-Base',
                description: 'ALIGN Base model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'ALIGN-Large',
                description: 'ALIGN Large model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'BasicVSR',
                description: 'Basic Video Super-Resolution',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'BasicVSR++',
                description: 'Improved Basic Video Super-Resolution',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'EDVR',
                description: 'Enhanced Deep Video Restoration',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'TTVSR',
                description: 'Temporal Transformer Video Super-Resolution',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'VSR-Transformer',
                description: 'Transformer for Video Super-Resolution',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Video-CLIP',
                description: 'CLIP for video understanding',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'CLIP4Clip',
                description: 'CLIP for video retrieval',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'X-CLIP',
                description: 'Cross-modal CLIP for video',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'ViViT',
                description: 'Video Vision Transformer',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'ViViT-Factorised',
                description: 'ViViT with factorised encoder',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'ViViT-Decoder',
                description: 'ViViT with decoder',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'TimeSformer',
                description: 'Space-Time Vision Transformer',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'VideoMAE',
                description: 'Masked Autoencoder for Video',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'VideoMAE-v2',
                description: 'Improved VideoMAE',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'SlowFast',
                description: 'SlowFast networks for video recognition',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'I3D',
                description: 'Inflated 3D ConvNet',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'R(2+1)D',
                description: 'Residual 2+1D ConvNet',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'S3D',
                description: 'Separated 3D ConvNet',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'CSN',
                description: 'Channel-Separated ConvNet',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'X3D',
                description: 'Expanded 3D ConvNet',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'MViT',
                description: 'Multiscale Vision Transformer',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'MViT-v2',
                description: 'Improved Multiscale Vision Transformer',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'UniFormer',
                description: 'Unified Transformer for video',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Video-Swin',
                description: 'Swin Transformer for video',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Video-Swin-Tiny',
                description: 'Tiny Video Swin Transformer',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Video-Swin-Small',
                description: 'Small Video Swin Transformer',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Video-Swin-Base',
                description: 'Base Video Swin Transformer',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Video-MAE-Pretrain',
                description: 'Video MAE pre-trained model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Audio-Visual',
                description: 'Audio-Visual learning network',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'AV-HuBERT',
                description: 'Audio-Visual HuBERT',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'AV-Speech',
                description: 'Audio-Visual speech recognition',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Lip-Reading',
                description: 'Lip reading network',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'TalkNet',
                description: 'TalkNet for audio-visual',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'SyncNet',
                description: 'Synchronization network',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Wav2Lip',
                description: 'Accurate lip-sync network',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'MakeItTalk',
                description: 'Audio-driven talking head',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'ATVG',
                description: 'Audio-Visual Talking Face',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Speech2Face',
                description: 'Speech to face reconstruction',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Voice2Face',
                description: 'Voice to face generation',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Multimodal-Fusion',
                description: 'General multimodal fusion network',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Early-Fusion',
                description: 'Early fusion multimodal network',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Late-Fusion',
                description: 'Late fusion multimodal network',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Hybrid-Fusion',
                description: 'Hybrid fusion multimodal network',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Cross-Modal-Attention',
                description: 'Cross-modal attention network',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Multimodal-Transformer',
                description: 'Transformer for multimodal data',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Multimodal-BERT',
                description: 'BERT for multimodal understanding',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Oscar-Base',
                description: 'Oscar Base model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Oscar-Large',
                description: 'Oscar Large model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'VinVL-Base',
                description: 'VinVL Base model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'VinVL-Large',
                description: 'VinVL Large model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'UniVL',
                description: 'Unified Video-Language model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Hero-Base',
                description: 'Hero Base model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'Hero-Large',
                description: 'Hero Large model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'VIOLET-Base',
                description: 'VIOLET Base model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'VIOLET-Large',
                description: 'VIOLET Large model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'All-in-One',
                description: 'All-in-One multimodal model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'UniPT',
                description: 'Universal Pre-trained Transformer',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'OFA-Base',
                description: 'OFA Base model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Multimodal'})
            CREATE (a:Architecture:`Multimodal` {
                name: 'OFA-Large',
                description: 'OFA Large model',
                category: 'Multimodal'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Energy & Equilibrium Architectures',
                description: 'analytical tools used to predict the state of complex systems (economic or physico-chemical) based on the balance of supply and demand, minimizing costs and optimizing the use of resources. They find the optimal balance by ensuring consistency between production capacity, commodity/energy flows, and consumption.',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Hopfield-Network',
                description: 'Classic recurrent network with energy function for associative memory',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Modern-Hopfield-Network',
                description: 'Dense associative memory with continuous states and higher capacity',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Boltzmann-Machine',
                description: 'Stochastic recurrent network using energy-based learning',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Restricted-Boltzmann-Machine',
                description: 'Two-layer undirected graphical model for unsupervised learning',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Deep-Belief-Network',
                description: 'Stack of RBMs trained greedily for deep representation learning',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Deep-Boltzmann-Machine',
                description: 'Deep undirected network with hidden layers for complex modeling',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Contrastive-Divergence-RBM',
                description: 'RBM trained with contrastive divergence for efficient learning',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Persistent-Contrastive-Divergence',
                description: 'Improved RBM training with persistent Markov chains',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Energy-Based-Model',
                description: 'General framework learning energy functions for data modeling',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Joint-Energy-Based-Model',
                description: 'EBM modeling joint distribution of inputs and labels',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Implicit-Energy-Model',
                description: 'Energy-based model with implicit density estimation',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Deep-Equilibrium-Model',
                description: 'Network finding fixed point instead of finite layers',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Monotone-Deep-Equilibrium',
                description: 'DEQ with monotone operator for guaranteed convergence',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Multiscale-Deep-Equilibrium',
                description: 'MDEQ with multiple equilibrium points for different scales',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Optimization-Equilibrium',
                description: 'Network interpreting layers as optimization steps',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Neural-ODE',
                description: 'Continuous-depth model using ordinary differential equations',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Augmented-Neural-ODE',
                description: 'Neural ODE with augmented state space for expressiveness',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'FFJORD',
                description: 'Free-form continuous normalizing flow for density estimation',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'ANODE-v2',
                description: 'Improved augmented Neural ODE with better stability',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Latent-ODE',
                description: 'ODE modeling latent dynamics for irregular time series',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'ODE-RNN',
                description: 'RNN with ODE-based hidden state evolution',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'GRU-ODE',
                description: 'Gated recurrent unit with continuous-time dynamics',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Continuous-RNN',
                description: 'RNN operating in continuous time domain',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Neural-CDE',
                description: 'Neural controlled differential equation for time series',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Neural-SDE',
                description: 'Neural stochastic differential equation for uncertainty',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Hamiltonian-Neural-Network',
                description: 'Network learning Hamiltonian dynamics for physical systems',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Lagrangian-Neural-Network',
                description: 'Network learning Lagrangian mechanics from data',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Symplectic-ODE-Net',
                description: 'Energy-conserving network for physical system modeling',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Deep-Hamiltonian',
                description: 'Deep network learning Hamiltonian from observations',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Implicit-Layer-Network',
                description: 'Network with layers defined implicitly by fixed point',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Deep-Implicit-Layer',
                description: 'Multi-layer implicit network for complex functions',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Equilibrium-RNN',
                description: 'RNN reaching equilibrium state for sequence processing',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Convergent-RNN',
                description: 'RNN with guaranteed convergence to fixed point',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Stable-Equilibrium-Net',
                description: 'Network with provably stable equilibrium points',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Monotone-Operator-Network',
                description: 'Network using monotone operators for implicit depth',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Proximal-Recurrence-Network',
                description: 'Network with proximal operator for stable recurrence',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Deep-Equilibrium-Transformer',
                description: 'Transformer with implicit depth through equilibrium',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Energy-Transformer',
                description: 'Transformer using energy-based attention mechanisms',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Implicit-Transformer',
                description: 'Transformer with implicit layer computation',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Score-Based-Model',
                description: 'Model learning score function for density estimation',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Denoising-Score-Matching',
                description: 'Score-based model trained with denoising objective',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Noise-Conditional-Score-Network',
                description: 'Score network conditioned on noise level',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Score-SDE',
                description: 'Score-based model with stochastic differential equations',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Consistency-Model',
                description: 'Model learning consistent mappings for fast generation',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Equilibrium-Consistency-Model',
                description: 'Consistency model with equilibrium constraints',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Energy-Based-GAN',
                description: 'GAN using energy-based discriminator',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Wasserstein-Energy-Model',
                description: 'Energy model with Wasserstein distance training',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Contrastive-Energy-Model',
                description: 'Energy model trained with contrastive learning',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Deep-Energy-Model',
                description: 'Deep network parameterizing energy function',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EnergyAndEquilibriaum'})
            CREATE (a:Architecture:`EnergyAndEquilibriaum` {
                name: 'Compositional-Energy-Model',
                description: 'Energy model with compositional structure',
                category: 'EnergyAndEquilibriaum'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'Efficient & Mobile Architectures',
                description: 'structured software design patterns (MVC, MVP, MVVM, MVI) that ensure high performance, ease of support, and scalability of applications.',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MobileNet-v1-0.25',
                description: 'Ultra-lightweight MobileNet with 0.25 width multiplier for extreme efficiency',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MobileNet-v1-0.5',
                description: 'MobileNet with 0.5 width multiplier balancing speed and accuracy',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MobileNet-v1-0.75',
                description: 'MobileNet with 0.75 width multiplier for mobile applications',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MobileNet-v2-0.35',
                description: 'Lightweight MobileNet-v2 with inverted residuals and reduced width',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MobileNet-v2-1.4',
                description: 'Wider MobileNet-v2 for improved accuracy on mobile devices',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MobileNet-v3-Small',
                description: 'Small variant optimized for latency using neural architecture search',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MobileNet-v3-Large',
                description: 'Large MobileNet-v3 with advanced squeeze-and-excitation blocks',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MobileNetV4-Conv-Small',
                description: 'Latest MobileNetV4 optimized for mobile convolution operations',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MobileNetV4-Hybrid',
                description: 'Hybrid MobileNetV4 combining convolution and attention mechanisms',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'ShuffleNet-v1-0.5x',
                description: 'ShuffleNet with 0.5x channels for ultra-fast mobile inference',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'ShuffleNet-v1-1x',
                description: 'Standard ShuffleNet with channel shuffle for efficient computation',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'ShuffleNet-v1-2x',
                description: 'Wider ShuffleNet for better accuracy on mobile platforms',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'ShuffleNet-v2-0.5x',
                description: 'Improved ShuffleNet-v2 with optimized memory access patterns',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'ShuffleNet-v2-1x',
                description: 'Standard ShuffleNet-v2 balancing speed and accuracy',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'ShuffleNet-v2-1.5x',
                description: 'Wider ShuffleNet-v2 for enhanced mobile performance',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'ShuffleNet-v2-2x',
                description: 'Maximum width ShuffleNet-v2 for mobile applications',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'SqueezeNet-1.0',
                description: 'Original SqueezeNet with fire modules achieving AlexNet accuracy',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'SqueezeNet-1.1',
                description: 'Improved SqueezeNet with 2.4x fewer parameters than v1.0',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'EfficientNet-Lite0',
                description: 'Mobile-friendly EfficientNet without squeeze-and-excitation',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'EfficientNet-Lite1',
                description: 'Scaled EfficientNet-Lite for mobile and edge devices',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'EfficientNet-Lite2',
                description: 'Medium EfficientNet-Lite variant for mobile deployment',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'EfficientNet-Lite3',
                description: 'Larger EfficientNet-Lite with improved mobile accuracy',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'EfficientNet-Lite4',
                description: 'Largest EfficientNet-Lite for high-performance mobile inference',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'EfficientNet-EdgeTPU-S',
                description: 'Small EfficientNet optimized for Google Edge TPU accelerators',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'EfficientNet-EdgeTPU-M',
                description: 'Medium EfficientNet designed for Edge TPU deployment',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'EfficientNet-EdgeTPU-L',
                description: 'Large EfficientNet optimized for Edge TPU performance',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'GhostNet-1.0',
                description: 'GhostNet generating more feature maps from cheap operations',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'GhostNet-1.3',
                description: 'Wider GhostNet for improved accuracy on mobile devices',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MixNet-S',
                description: 'Small MixNet using mixed depthwise convolution kernel sizes',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MixNet-M',
                description: 'Medium MixNet balancing efficiency and accuracy',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MixNet-L',
                description: 'Large MixNet achieving high accuracy with mixed kernels',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MNASNet-0.5',
                description: 'Lightweight MNASNet discovered by platform-aware NAS',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MNASNet-0.75',
                description: 'Medium MNASNet optimized for mobile latency',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MNASNet-1.0',
                description: 'Standard MNASNet balancing accuracy and latency',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MNASNet-1.3',
                description: 'Larger MNASNet for improved mobile performance',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'FBNet-A',
                description: 'Hardware-aware FBNet variant A for specific mobile devices',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'FBNet-B',
                description: 'FBNet variant B optimized for mobile inference speed',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'FBNet-C',
                description: 'FBNet variant C balancing accuracy and latency',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'ProxylessNAS-Mobile',
                description: 'Mobile-optimized architecture from ProxylessNAS search',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'ProxylessNAS-GPU',
                description: 'GPU-optimized architecture from ProxylessNAS',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'TinyNet-A',
                description: 'Ultra-efficient TinyNet variant A for extreme constraints',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'TinyNet-B',
                description: 'TinyNet variant B balancing size and performance',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'FastNet-Small',
                description: 'FastNet optimized for speed on mobile processors',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'FastNet-Medium',
                description: 'Medium FastNet for balanced mobile performance',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'FastNet-Large',
                description: 'Large FastNet for high-accuracy mobile applications',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'LCNet-0.35',
                description: 'Lightweight ConvNet with 0.35 scale for mobile devices',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'LCNet-0.50',
                description: 'LCNet with 0.50 scale balancing efficiency and accuracy',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'LCNet-0.75',
                description: 'LCNet with 0.75 scale for improved mobile performance',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'LCNet-1.0',
                description: 'Full-scale LCNet for mobile and edge deployment',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MobileViT-XS',
                description: 'Extra-small Mobile Vision Transformer for mobile devices',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MobileViT-S',
                description: 'Small MobileViT combining CNN and Transformer benefits',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MobileViT-M',
                description: 'Medium MobileViT for balanced mobile vision tasks',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'MobileViT-L',
                description: 'Large MobileViT for high-accuracy mobile applications',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'EdgeNeXt-XXSmall',
                description: 'Extra-extra-small EdgeNeXt for extreme edge deployment',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'EdgeNeXt-XSmall',
                description: 'Extra-small EdgeNeXt optimized for edge devices',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'EdgeNeXt-Small',
                description: 'Small EdgeNeXt balancing efficiency and accuracy',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'EfficientAndMobile'})
            CREATE (a:Architecture:`EfficientAndMobile` {
                name: 'EdgeNeXt-Medium',
                description: 'Medium EdgeNeXt for edge computing applications',
                category: 'EfficientAndMobile'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Recurant&Sequental Architectures',
                description: 'These are architectures that perceive the world not as a set of frozen frames, but as a continuous stream, where the past determines the understanding of the present',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Vanilla-RNN',
                description: 'Simple recurrent neural network with hidden state',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Elman-RNN',
                description: 'Simple RNN with context units',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Jordan-RNN',
                description: 'RNN with output feedback to input',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'LSTM',
                description: 'Long Short-Term Memory with gates for long-range dependencies',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'LSTM-Forward',
                description: 'Unidirectional LSTM processing sequences forward',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'LSTM-Backward',
                description: 'Unidirectional LSTM processing sequences backward',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'BiLSTM',
                description: 'Bidirectional LSTM with forward and backward passes',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Stacked-LSTM',
                description: 'Multiple LSTM layers for hierarchical representation',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Deep-LSTM',
                description: 'Deep LSTM with multiple hidden layers',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Peephole-LSTM',
                description: 'LSTM with peephole connections from cell state',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'GRU',
                description: 'Gated Recurrent Unit with simplified gates',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'BiGRU',
                description: 'Bidirectional GRU for sequence modeling',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Stacked-GRU',
                description: 'Multiple GRU layers for deep representation',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Deep-GRU',
                description: 'Deep GRU architecture with multiple layers',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'MGU',
                description: 'Minimal Gated Unit with simplified gating',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'UGRNN',
                description: 'Unidirectional Gated Recurrent Neural Network',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'LSTM-Attention',
                description: 'LSTM with attention mechanism for focus',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'BiLSTM-Attention',
                description: 'Bidirectional LSTM with attention',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'GRU-Attention',
                description: 'GRU with attention for sequence tasks',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Seq2Seq',
                description: 'Sequence-to-Sequence model with encoder-decoder',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Seq2Seq-LSTM',
                description: 'Seq2Seq using LSTM encoder and decoder',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Seq2Seq-GRU',
                description: 'Seq2Seq using GRU encoder and decoder',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Seq2Seq-Attention',
                description: 'Seq2Seq with attention mechanism',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Bahdanau-Attention',
                description: 'Additive attention for neural machine translation',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Luong-Attention',
                description: 'Multiplicative attention variants (dot, general, concat)',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Global-Attention',
                description: 'Global attention considering all source positions',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Local-Attention',
                description: 'Local attention focusing on subset of positions',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Self-Attention',
                description: 'Attention mechanism relating different positions',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Multi-Head-Attention',
                description: 'Multiple attention heads for diverse representations',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Transformer-Encoder',
                description: 'Transformer encoder stack for sequence encoding',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Transformer-Decoder',
                description: 'Transformer decoder stack for sequence generation',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'QRNN',
                description: 'Quasi-Recurrent Neural Network for parallelism',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'SRU',
                description: 'Simple Recurrent Unit for faster training',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'SRU++',
                description: 'Improved SRU with layer normalization',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'IndRNN',
                description: 'Independently Recurrent Neural Network',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Dilated-RNN',
                description: 'RNN with dilated connections for long dependencies',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Clockwork-RNN',
                description: 'RNN with partitioned hidden state at different speeds',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Phased-LSTM',
                description: 'LSTM with time gates for irregular sequences',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'NADE',
                description: 'Neural Autoregressive Distribution Estimator',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'RNN-NADE',
                description: 'RNN-based NADE for sequence modeling',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'PixelRNN',
                description: 'Pixel-level RNN for image generation',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'PixelCNN',
                description: 'Pixel-level CNN for autoregressive generation',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Row-LSTM',
                description: 'Row-wise LSTM for 2D sequence processing',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Diagonal-BiLSTM',
                description: 'Diagonal bidirectional LSTM for images',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'ConvLSTM',
                description: 'Convolutional LSTM for spatiotemporal sequences',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'TrajGRU',
                description: 'Trajectory GRU for precipitation nowcasting',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'MDCN',
                description: 'Multi-Depth Convolutional Network for sequences',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'Temporal-ConvNet',
                description: 'Temporal Convolutional Network for sequences',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'WaveNet',
                description: 'Dilated causal CNN for audio generation',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RecAndSeq'})
            CREATE (a:Architecture:`RecAndSeq` {
                name: 'ByteNet',
                description: 'Fast density estimator with dilated convolutions',
                category: 'RecAndSeq'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'DQN',
                description: 'Deep Q-Network for value-based reinforcement learning',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'Double-DQN',
                description: 'DQN with double Q-learning to reduce overestimation',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'Dueling-DQN',
                description: 'DQN with separate value and advantage streams',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'Prioritized-DQN',
                description: 'DQN with prioritized experience replay',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'Rainbow-DQN',
                description: 'Combining improvements to DQN',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'C51',
                description: 'Categorical DQN for distributional RL',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'QR-DQN',
                description: 'Quantile Regression DQN for distributional RL',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'IQN',
                description: 'Implicit Quantile Networks for distributional RL',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'FQF',
                description: 'Fully Parameterized Quantile Function',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'A3C',
                description: 'Asynchronous Advantage Actor-Critic',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'A2C',
                description: 'Advantage Actor-Critic synchronous variant',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'GA3C',
                description: 'GPU-optimized Asynchronous Advantage Actor-Critic',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'TRPO',
                description: 'Trust Region Policy Optimization',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'PPO',
                description: 'Proximal Policy Optimization with clipped objective',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'PPO-Clip',
                description: 'PPO with clipped surrogate objective',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'PPO-Penalty',
                description: 'PPO with KL penalty constraint',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'ACKTR',
                description: 'Actor-Critic using Kronecker-factored Trust Region',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'DDPG',
                description: 'Deep Deterministic Policy Gradient for continuous actions',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'TD3',
                description: 'Twin Delayed DDPG with improved stability',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'DDPGf',
                description: 'DDPG with further improvements',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'SAC',
                description: 'Soft Actor-Critic with entropy maximization',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'SAC-Alpha',
                description: 'SAC with automatic temperature tuning',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'REDQ',
                description: 'Randomized Ensemble Double Q-learning',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'TD7',
                description: 'TD3 with seven improvements',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'REINFORCE',
                description: 'Monte Carlo policy gradient algorithm',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'Actor-Critic',
                description: 'Basic actor-critic architecture',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'GAE',
                description: 'Generalized Advantage Estimation',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'NPG',
                description: 'Natural Policy Gradient',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'FAC',
                description: 'Feudal Actor-Critic for hierarchical RL',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'HIRO',
                description: 'Hierarchical Reinforcement Learning with Off-policy correction',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'HAC',
                description: 'Hierarchical Actor-Critic',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'Option-Critic',
                description: 'Learning options and policies end-to-end',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'Feudal-Network',
                description: 'Feudal reinforcement learning architecture',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'MAXQ',
                description: 'Hierarchical decomposition of value function',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'DyNA',
                description: 'Dynamic Neural Architecture for RL',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'MB-MPO',
                description: 'Model-Based Meta Policy Optimization',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'MBPO',
                description: 'Model-Based Policy Optimization',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'STEVE',
                description: 'Sample-efficient model-based RL',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'PETS',
                description: 'Probabilistic Ensembles with Trajectory Sampling',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'Dyna',
                description: 'Integrated model-based and model-free RL',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'World-Model',
                description: 'Learning world models for planning',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'Dreamer',
                description: 'Learning long-horizon predictions for RL',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'Dreamer-v2',
                description: 'Improved Dreamer with discrete representations',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'Dreamer-v3',
                description: 'Third generation Dreamer with better scaling',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'PlaNet',
                description: 'Planning with latent dynamics models',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'MuZero',
                description: 'Mastering Atari, Go, chess without rules',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'AlphaZero',
                description: 'General reinforcement learning algorithm',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'AlphaGo',
                description: 'Deep neural networks for Go',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'AlphaGo-Zero',
                description: 'AlphaGo learning from self-play',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'RL'})
            CREATE (a:Architecture:`RL` {
                name: 'AlphaStar',
                description: 'Mastering StarCraft II with deep RL',
                category: 'RL'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'S4',
                description: 'Structured State Space sequence model for long-range dependencies',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'S4D',
                description: 'S4 with diagonal state matrix for efficiency',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'S4-LegS',
                description: 'S4 with Legendre polynomial basis',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'S4-FouT',
                description: 'S4 with Fourier transform basis',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'S5',
                description: 'Simplified S4 with parallel scan for speed',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Mamba',
                description: 'Selective State Space Model with input-dependent parameters',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Mamba-130M',
                description: 'Small Mamba model with 130 million parameters',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Mamba-370M',
                description: 'Medium Mamba model with 370 million parameters',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Mamba-790M',
                description: 'Large Mamba model with 790 million parameters',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Mamba-1.4B',
                description: 'Mamba model with 1.4 billion parameters',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Mamba-2.8B',
                description: 'Mamba model with 2.8 billion parameters',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Jamba',
                description: 'Hybrid Mamba-Transformer architecture',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Jamba-1.5-Mini',
                description: 'Smaller Jamba variant for efficient inference',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Jamba-1.5-Large',
                description: 'Larger Jamba variant for high performance',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'H3',
                description: 'Hungry Hungry Hippo state space model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'H3-125M',
                description: 'Small H3 model with 125M parameters',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'H3-350M',
                description: 'Medium H3 model with 350M parameters',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'H3-1.3B',
                description: 'Large H3 model with 1.3B parameters',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Hyena',
                description: 'Sub-quadratic sequence model with implicit convolutions',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'HyenaDNA',
                description: 'Hyena model for genomic sequence modeling',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Long-Conv',
                description: 'Long convolution sequence model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Griffin',
                description: 'Gated linear attention with convolutions',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Griffin-2B',
                description: 'Griffin model with 2 billion parameters',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Griffin-6B',
                description: 'Griffin model with 6 billion parameters',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'RWKV',
                description: 'Receptance Weighted Key Value for RNN-Transformer hybrid',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'RWKV-4-169M',
                description: 'Small RWKV v4 model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'RWKV-4-430M',
                description: 'Medium RWKV v4 model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'RWKV-4-1.5B',
                description: 'Large RWKV v4 model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'RWKV-4-3B',
                description: 'RWKV v4 with 3 billion parameters',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'RWKV-4-7B',
                description: 'RWKV v4 with 7 billion parameters',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'RWKV-4-14B',
                description: 'RWKV v4 with 14 billion parameters',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'RWKV-5-Eagle',
                description: 'RWKV v5 with improved attention mechanism',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'RWKV-6-Falcon',
                description: 'RWKV v6 with enhanced performance',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'RetNet',
                description: 'Retentive Network for efficient sequence modeling',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'RetNet-Base',
                description: 'Base RetNet model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'RetNet-Large',
                description: 'Large RetNet model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'RetNet-XL',
                description: 'Extra-large RetNet model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'GLA',
                description: 'Gated Linear Attention for efficient transformers',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'DeltaNet',
                description: 'Delta rule based state space model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'VMamba',
                description: 'Visual Mamba for computer vision tasks',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Vim',
                description: 'Vision Mamba for image recognition',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Vim-Tiny',
                description: 'Tiny Vision Mamba variant',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Vim-Small',
                description: 'Small Vision Mamba variant',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Vim-Base',
                description: 'Base Vision Mamba variant',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Vamamba',
                description: 'Video Mamba for video understanding',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'AudioMamba',
                description: 'Mamba for audio processing',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Mamba-2',
                description: 'Second generation Mamba with improved efficiency',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Mamba-2-130M',
                description: 'Small Mamba-2 model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Mamba-2-370M',
                description: 'Medium Mamba-2 model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Mamba-2-780M',
                description: 'Large Mamba-2 model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Mamba-2-1.3B',
                description: 'Mamba-2 with 1.3B parameters',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Mamba-2-2.7B',
                description: 'Mamba-2 with 2.7B parameters',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Zamba',
                description: 'Hybrid SSM-Transformer model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Zamba-1.3B',
                description: 'Small Zamba model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Zamba-7B',
                description: 'Large Zamba model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Minerva',
                description: 'State space model for mathematical reasoning',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'LSSL',
                description: 'Linear State Space Layer for sequences',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'DSS',
                description: 'Diagonal State Space model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'GSS',
                description: 'Gated State Space model',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'SSM-Conv',
                description: 'State Space Model with convolutional layers',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Bi-Mamba',
                description: 'Bidirectional Mamba for context understanding',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Cross-Mamba',
                description: 'Cross-modal Mamba for multimodal tasks',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Mamba-LLaMA',
                description: 'Mamba integrated with LLaMA architecture',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Mambaformer',
                description: 'Hybrid Mamba-Transformer architecture',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Sparse-Mamba',
                description: 'Sparse Mamba for efficient computation',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Quantized-Mamba',
                description: 'Quantized Mamba for edge deployment',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Distilled-Mamba',
                description: 'Distilled Mamba for smaller footprint',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Multi-Scale-Mamba',
                description: 'Mamba with multi-scale processing',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'StateSpace'})
            CREATE (a:Architecture:`StateSpace` {
                name: 'Hierarchical-Mamba',
                description: 'Hierarchical Mamba for complex sequences',
                category: 'StateSpace'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'Архитектуры для малых данных и FEW-SHOT LEARNING',
                description: 'Models are able to draw accurate conclusions based on an extremely limited set of examples (literally 1-5 samples), simulating the human ability to learn quickly.',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'ProtoNet',
                description: 'Prototypical Networks for few-shot classification',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'ProtoNet-ResNet12',
                description: 'ProtoNet with ResNet-12 backbone',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'ProtoNet-Conv4',
                description: 'ProtoNet with simple Conv4 backbone',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'ProtoNet-TiResNet',
                description: 'ProtoNet with Tiny ResNet backbone',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'MatchingNet',
                description: 'Matching Networks for one-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'MatchingNet-Conv',
                description: 'Matching Network with convolutional encoder',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'MatchingNet-LSTM',
                description: 'Matching Network with LSTM encoder',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'RelationNet',
                description: 'Learning to compare for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'RelationNet-ResNet',
                description: 'Relation Network with ResNet backbone',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'MAML',
                description: 'Model-Agnostic Meta-Learning for fast adaptation',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'MAML-ResNet',
                description: 'MAML with ResNet architecture',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'MAML-Conv',
                description: 'MAML with convolutional network',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'Meta-SGD',
                description: 'Meta-learning with learned optimizer',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'Reptile',
                description: 'Simple meta-learning algorithm',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'ANIL',
                description: 'Almost No Inner Loop for efficient meta-learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'BOIL',
                description: 'Body Only Inner Loop meta-learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'MetaOptNet',
                description: 'Meta-learning with differentiable optimization',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'MetaOptNet-ResNet',
                description: 'MetaOptNet with ResNet backbone',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'MetaOptNet-Conv',
                description: 'MetaOptNet with Conv backbone',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'LEO',
                description: 'Latent Embedding Optimization for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'TADAM',
                description: 'Task-dependent adaptive metric for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'SNAIL',
                description: 'Simple Neural Attentive Meta-Learner',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'MTL',
                description: 'Meta Transfer Learning for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'MetaBaseline',
                description: 'Simple baseline for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'SimpleShot',
                description: 'Revisiting nearest neighbor for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'FEAT',
                description: 'Feature Transformation for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'DeepEMD',
                description: 'Deep Earth Mover\'s Distance for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'RENé',
                description: 'Rectified Embeddings for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'FRN',
                description: 'Feature Reweighting Network for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'SIB',
                description: 'Self-Imitation Learning for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'EPNet',
                description: 'Edge Propagation Network for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'AttMAML',
                description: 'Attention-based MAML for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'CAMONet',
                description: 'Context Attention Modulation for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'DCNet',
                description: 'Dense Classification Network for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'FSCE',
                description: 'Few-Shot Contrastive Embedding',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'CovaMNet',
                description: 'Covariance Metric Network for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'DeepBDC',
                description: 'Deep Brownian Distance Covariance',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'K-shot-NN',
                description: 'K-shot Nearest Neighbor classifier',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'Transductive-ProtoNet',
                description: 'ProtoNet with transductive inference',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'LaplacianShot',
                description: 'Laplacian regularization for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'TIM',
                description: 'Transductive Information Maximization',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'Simple-CNAPS',
                description: 'Simple Conditional Neural Adaptive Processes',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'CNAPS',
                description: 'Conditional Neural Adaptive Processes',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'SUR',
                description: 'Self-Supervised Representation for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'SelfSupervised-ProtoNet',
                description: 'ProtoNet with self-supervised pretraining',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'SimCLR-FewShot',
                description: 'SimCLR pretraining for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'MoCo-FewShot',
                description: 'MoCo pretraining for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'BYOL-FewShot',
                description: 'BYOL pretraining for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'SwAV-FewShot',
                description: 'SwAV pretraining for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'DINO-FewShot',
                description: 'DINO pretraining for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'MAE-FewShot',
                description: 'Masked Autoencoder for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'BEiT-FewShot',
                description: 'BEiT pretraining for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'CrossTransformers',
                description: 'Cross-transformers for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'FewShot-ViT',
                description: 'Vision Transformer for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'FewShot-Swin',
                description: 'Swin Transformer for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'Tip-Adapter',
                description: 'Training-free adapter for few-shot CLIP',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'Tip-Adapter-F',
                description: 'Fine-tuned Tip-Adapter for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'LP-CLIP',
                description: 'Linear Probe CLIP for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'CoOp',
                description: 'Context Optimization for CLIP few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'CoCoOp',
                description: 'Conditional Context Optimization',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'MaPLe',
                description: 'Multi-modal Prompt Learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'PromptSRC',
                description: 'Prompt Source for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'AdaPT',
                description: 'Adaptive Prompt Tuning for few-shot',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'MetaPrompt',
                description: 'Meta-learning for prompt optimization',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'ProGrad',
                description: 'Prompt Gradient for few-shot CLIP',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'LoRA-FewShot',
                description: 'Low-Rank Adaptation for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'Adapter-FewShot',
                description: 'Adapter modules for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'Prefix-FewShot',
                description: 'Prefix tuning for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SmallDataAndFewShot'})
            CREATE (a:Architecture:`SmallDataAndFewShot` {
                name: 'IA3-FewShot',
                description: 'Infused Adapter for few-shot learning',
                category: 'SmallDataAndFewShot'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'U-Net',
                description: 'Convolutional network for biomedical image segmentation',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'U-Net-ResNet',
                description: 'U-Net with ResNet encoder backbone',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'U-Net-EfficientNet',
                description: 'U-Net with EfficientNet encoder',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Attention-U-Net',
                description: 'U-Net with attention gates for segmentation',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'U-Net++',
                description: 'Nested U-Net architecture for segmentation',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'U-Net-3+',
                description: 'Full-scale skip connections in U-Net',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'TransU-Net',
                description: 'U-Net with Transformer encoder',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Swin-U-Net',
                description: 'U-Net with Swin Transformer backbone',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'DeepLab-v3',
                description: 'DeepLab semantic segmentation with atrous convolution',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'DeepLab-v3+',
                description: 'Improved DeepLab with encoder-decoder',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'DeepLab-Cityscapes',
                description: 'DeepLab optimized for Cityscapes dataset',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'PSPNet',
                description: 'Pyramid Scene Parsing Network for segmentation',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'FCN-8s',
                description: 'Fully Convolutional Network with 8x upsampling',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'FCN-16s',
                description: 'FCN with 16x upsampling',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'FCN-32s',
                description: 'FCN with 32x upsampling',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Mask-RCNN',
                description: 'Mask Region CNN for instance segmentation',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Mask-RCNN-ResNet50',
                description: 'Mask R-CNN with ResNet-50 backbone',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Mask-RCNN-ResNet101',
                description: 'Mask R-CNN with ResNet-101 backbone',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'YOLO-v3',
                description: 'You Only Look Once v3 for object detection',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'YOLO-v4',
                description: 'YOLO v4 with improved detection',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'YOLO-v5-Small',
                description: 'YOLO v5 small variant',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'YOLO-v5-Medium',
                description: 'YOLO v5 medium variant',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'YOLO-v5-Large',
                description: 'YOLO v5 large variant',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'YOLO-v5-XL',
                description: 'YOLO v5 extra-large variant',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'YOLO-v7',
                description: 'YOLO v7 with extended efficient layer aggregation',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'YOLO-v8-Nano',
                description: 'YOLO v8 nano variant',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'YOLO-v8-Small',
                description: 'YOLO v8 small variant',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'YOLO-v8-Medium',
                description: 'YOLO v8 medium variant',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'YOLO-v8-Large',
                description: 'YOLO v8 large variant',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'YOLO-v8-XL',
                description: 'YOLO v8 extra-large variant',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'YOLOX-Small',
                description: 'YOLOX small variant',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'YOLOX-Medium',
                description: 'YOLOX medium variant',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'YOLOX-Large',
                description: 'YOLOX large variant',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'YOLOX-XL',
                description: 'YOLOX extra-large variant',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Faster-RCNN',
                description: 'Faster R-CNN with region proposal network',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Faster-RCNN-ResNet50',
                description: 'Faster R-CNN with ResNet-50',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Faster-RCNN-ResNet101',
                description: 'Faster R-CNN with ResNet-101',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'RetinaNet',
                description: 'Focal loss for dense object detection',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'RetinaNet-ResNet50',
                description: 'RetinaNet with ResNet-50 backbone',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'FCOS',
                description: 'Fully Convolutional One-Stage detector',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'CenterNet',
                description: 'Objects as points for detection',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'CornerNet',
                description: 'Detecting objects as paired keypoints',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'DETR',
                description: 'Detection Transformer for end-to-end detection',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'DETR-ResNet50',
                description: 'DETR with ResNet-50 backbone',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Deformable-DETR',
                description: 'DETR with deformable attention',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'DINO-DETR',
                description: 'DETR with improved de-noising training',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Sparse-RCNN',
                description: 'Sparse R-CNN for end-to-end detection',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'GFL',
                description: 'Generalized Focal Loss for detection',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'ATSS',
                description: 'Automatic Target Sampling Strategy',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'SRNet',
                description: 'Super-Resolution Network',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'ESPCN',
                description: 'Efficient Sub-Pixel CNN for SR',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'FSRCNN',
                description: 'Fast Super-Resolution CNN',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'VDSR',
                description: 'Very Deep Super-Resolution Network',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'EDSR',
                description: 'Enhanced Deep Residual Networks for SR',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'SRGAN',
                description: 'Super-Resolution GAN',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'ESRGAN',
                description: 'Enhanced SRGAN for realistic images',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Real-ESRGAN',
                description: 'Practical SR for real-world images',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'SwinIR',
                description: 'Swin Transformer for Image Restoration',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'HAT',
                description: 'Hybrid Attention Transformer for SR',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'DAT',
                description: 'Dual Aggregation Transformer for SR',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'NAFNet',
                description: 'Nonlinear Activation Free Network for restoration',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Restormer',
                description: 'Efficient Transformer for image restoration',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'MPRNet',
                description: 'Multi-Stage Progressive Restoration Network',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Uformer',
                description: 'U-Net shaped Transformer for restoration',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'IRNet',
                description: 'Infrared Small Target Detection Network',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'SAR-Net',
                description: 'Synthetic Aperture Radar processing network',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'LiDAR-Net',
                description: 'LiDAR point cloud processing network',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Medical-Net',
                description: '3D medical image analysis network',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Pathology-Net',
                description: 'Computational pathology analysis network',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Genomics-Net',
                description: 'Genomic sequence analysis network',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Protein-Net',
                description: 'Protein structure prediction network',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'Specialized'})
            CREATE (a:Architecture:`Specialized` {
                name: 'Drug-Discovery-Net',
                description: 'Molecular property prediction network',
                category: 'Specialized'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Spike and neuromorphic architectures',
                description: 'simulations of the biological principles of the brain at the hardware and software levels to achieve extreme energy efficiency and real-time operation',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'LIF-Neuron',
                description: 'Leaky Integrate-and-Fire spiking neuron model',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'IF-Neuron',
                description: 'Integrate-and-Fire spiking neuron model',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Hodgkin-Huxley',
                description: 'Biologically realistic neuron model',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Izhikevich',
                description: 'Efficient biologically plausible neuron model',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'AdEx',
                description: 'Adaptive Exponential integrate-and-fire neuron',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'SNN-LIF',
                description: 'Spiking Neural Network with LIF neurons',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'SNN-IF',
                description: 'Spiking Neural Network with IF neurons',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Deep-SNN',
                description: 'Deep Spiking Neural Network architecture',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Conv-SNN',
                description: 'Convolutional Spiking Neural Network',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'ResNet-SNN',
                description: 'Residual Spiking Neural Network',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'VGG-SNN',
                description: 'VGG-style Spiking Neural Network',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Spiking-YOLO',
                description: 'Spiking neural network for object detection',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Spiking-ResNet-18',
                description: '18-layer Spiking ResNet',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Spiking-ResNet-34',
                description: '34-layer Spiking ResNet',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Spiking-ResNet-50',
                description: '50-layer Spiking ResNet',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'SEW-ResNet',
                description: 'Spiking Element-Wise ResNet',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Spikformer',
                description: 'Spiking Transformer architecture',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Spiking-Transformer',
                description: 'Transformer with spiking neurons',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'SpikeGPT',
                description: 'Spiking neural network for language generation',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Spiking-BERT',
                description: 'BERT implemented with spiking neurons',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Event-CNN',
                description: 'CNN for event camera data processing',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Event-ResNet',
                description: 'ResNet for event-based vision',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'EV-Net',
                description: 'Event-based Vision Network',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'EST',
                description: 'Event-based Spiking Transformer',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'V2E',
                description: 'Video to Event conversion network',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'DVS-CNN',
                description: 'CNN for Dynamic Vision Sensor data',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'DVS-ResNet',
                description: 'ResNet for DVS event streams',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Neuromorphic-Vision',
                description: 'Vision processing for neuromorphic sensors',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Loihi-SNN',
                description: 'SNN optimized for Intel Loihi chip',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'TrueNorth-Net',
                description: 'Network for IBM TrueNorth chip',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'SpiNNaker-Net',
                description: 'Network for SpiNNaker neuromorphic system',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'BrainScaleS-Net',
                description: 'Network for BrainScaleS platform',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'ODIN',
                description: 'Online Dynamic Inference for SNNs',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'TSSL-BP',
                description: 'Temporal Spike Sequence Learning via BP',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'STDP-Learning',
                description: 'Spike-Timing-Dependent Plasticity learning',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'R-STDP',
                description: 'Reward-modulated STDP learning',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Surrogate-Gradient',
                description: 'Surrogate gradient learning for SNNs',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Direct-Training-SNN',
                description: 'Direct training method for SNNs',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'ANN2SNN',
                description: 'ANN to SNN conversion method',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Rate-Coding-SNN',
                description: 'Rate-coded Spiking Neural Network',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Temporal-Coding-SNN',
                description: 'Temporally coded Spiking Neural Network',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Population-Coding-SNN',
                description: 'Population-coded Spiking Neural Network',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Hybrid-ANN-SNN',
                description: 'Hybrid ANN-SNN architecture',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Neuromorphic-RL',
                description: 'Reinforcement Learning on neuromorphic hardware',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Spiking-Actor-Critic',
                description: 'Actor-Critic with spiking neurons',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Neuromorphic-ODR',
                description: 'Optical Character Recognition on neuromorphic chips',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Event-Object-Detection',
                description: 'Object detection for event cameras',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Event-Tracking',
                description: 'Visual tracking with event data',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Neuromorphic-Audio',
                description: 'Audio processing on neuromorphic hardware',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Cochlea-Net',
                description: 'Cochlea-inspired spiking audio network',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Neuromorphic-Nav',
                description: 'Navigation on neuromorphic systems',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Event-SLAM',
                description: 'SLAM using event camera data',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Spiking-LSTM',
                description: 'LSTM implemented with spiking neurons',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Spiking-GRU',
                description: 'GRU implemented with spiking neurons',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Neurogrid-Net',
                description: 'Network for Neurogrid neuromorphic system',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Dynap-Net',
                description: 'Network for Dynap-SEL neuromorphic chip',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Speck-Net',
                description: 'Network for Speck neuromorphic sensor',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Prophesee-Net',
                description: 'Network for Prophesee event cameras',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'IniVation-Net',
                description: 'Network for IniVation event sensors',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'CeleX-Net',
                description: 'Network for CeleX neuromorphic sensor',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'SKIM',
                description: 'Sparse Kernel Iterative Machine for SNNs',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'ReSuMe',
                description: 'Remote Supervised Method for SNN training',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Chronotron',
                description: 'Precise spike timing learning algorithm',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'SPAN',
                description: 'Spike Pattern Association Neuron',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Tempotron',
                description: 'Tempotron learning rule for SNNs',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'Multi-Spike-Tempotron',
                description: 'Extended Tempotron for multiple spikes',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'NormAD',
                description: 'Normalized Approximate Descent for SNNs',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'SLAYER',
                description: 'Spike Layer Error Reassignment in Time',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'RMP-Loss',
                description: 'Reset Membrane Potential Loss for SNNs',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'GLIF',
                description: 'Generalized Leaky Integrate-and-Fire neuron',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'ALIF',
                description: 'Adaptive Leaky Integrate-and-Fire neuron',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'SpikeAndNeuromorph'})
            CREATE (a:Architecture:`SpikeAndNeuromorph` {
                name: 'PLIF',
                description: 'Parametric Leaky Integrate-and-Fire neuron',
                category: 'SpikeAndNeuromorph'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Neuro-Symbolic&Hybrid Architectures',
                description: 'architectures where learnability (the ability to extract knowledge from experience) is combined with determinism (the ability to follow strict rules)',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Neural-Theorem-Prover',
                description: 'Neural network for automated theorem proving',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'DeepProbLog',
                description: 'Deep probabilistic logic programming',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Neural-Logic-Network',
                description: 'Neural network implementing logical operations',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'NLN-AND',
                description: 'Neural Logic Network with AND gate',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'NLN-OR',
                description: 'Neural Logic Network with OR gate',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'NLN-NOT',
                description: 'Neural Logic Network with NOT gate',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'TensorLog',
                description: 'Differentiable logic programming framework',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Logic-LM',
                description: 'Logic-enhanced Language Model',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Neural-Symbolic-Learner',
                description: 'Combined neural and symbolic learning',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'NS-CL',
                description: 'Neuro-Symbolic Concept Learner',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'NS-VQA',
                description: 'Neuro-Symbolic Visual Question Answering',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'NS-DR',
                description: 'Neuro-Symbolic Dynamic Reasoning',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'MAC-Network',
                description: 'Memory, Attention, Composition for reasoning',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Graph-Network',
                description: 'Graph Neural Network for relational reasoning',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Relation-Network',
                description: 'Network for learning relationships',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Compositional-NN',
                description: 'Compositional Neural Network',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Module-Network',
                description: 'Modular architecture for reasoning',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Neural-Program-Interpreter',
                description: 'Neural network interpreting programs',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Neural-Programmer',
                description: 'Neural network that writes programs',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Neural-GPU',
                description: 'Neural network with GPU-like memory',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Neural-Turing-Machine',
                description: 'Neural network with external memory',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Differentiable-Neural-Computer',
                description: 'DNC with advanced memory addressing',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Memory-Network',
                description: 'Network with explicit memory component',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'End-to-End-Memory-Network',
                description: 'End-to-end trainable memory network',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Dynamic-Memory-Network',
                description: 'Memory network with dynamic updates',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Key-Value-Memory-Network',
                description: 'Memory network with key-value addressing',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Sparse-Differentiable-Neural-Computer',
                description: 'Sparse DNC for efficiency',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Neural-Stack',
                description: 'Neural network with stack memory',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Neural-Queue',
                description: 'Neural network with queue memory',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Neural-Dictionary',
                description: 'Neural network with dictionary memory',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Neural-Program-Synthesis',
                description: 'Neural network for program synthesis',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'RobustFill',
                description: 'Neural program synthesis for string manipulation',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'DeepCoder',
                description: 'Learning to write programs from examples',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Solar',
                description: 'Synthesis of programs with neural guidance',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Neural-Symbolic-VQA',
                description: 'VQA with neuro-symbolic reasoning',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Neural-Symbolic-RL',
                description: 'Reinforcement Learning with symbolic reasoning',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Symbolic-DQN',
                description: 'DQN with symbolic state representation',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Neural-Logic-RL',
                description: 'RL with neural logic reasoning',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Concept-Bottleneck',
                description: 'Model with interpretable concept layer',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Explainable-NN',
                description: 'Neural network with built-in explanations',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Interpretable-CNN',
                description: 'CNN with interpretable features',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Attention-Explanation',
                description: 'Attention mechanism for explanations',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Rationale-Network',
                description: 'Network generating rationales for predictions',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Self-Explaining-NN',
                description: 'Neural network that explains itself',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Prototype-Network',
                description: 'Network using prototypes for classification',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Case-Based-NN',
                description: 'Neural network with case-based reasoning',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Analogical-NN',
                description: 'Neural network for analogical reasoning',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Causal-NN',
                description: 'Neural network with causal reasoning',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Counterfactual-NN',
                description: 'Neural network for counterfactual reasoning',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Bayesian-NN',
                description: 'Bayesian Neural Network for uncertainty',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Probabilistic-NN',
                description: 'Probabilistic Neural Network',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Fuzzy-NN',
                description: 'Fuzzy Neural Network for uncertain reasoning',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Rough-NN',
                description: 'Rough set-based Neural Network',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Quantum-NN',
                description: 'Quantum Neural Network architecture',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Hybrid-Classical-Quantum',
                description: 'Hybrid classical-quantum neural network',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Analog-NN',
                description: 'Analog Neural Network for continuous processing',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Digital-Analog-Hybrid',
                description: 'Hybrid digital-analog neural network',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Optical-NN',
                description: 'Optical Neural Network for light-based computing',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Photonic-NN',
                description: 'Photonic Neural Network architecture',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Memristor-NN',
                description: 'Memristor-based Neural Network',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Spintronic-NN',
                description: 'Spintronic Neural Network architecture',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'DNA-NN',
                description: 'DNA-based Neural Network',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Molecular-NN',
                description: 'Molecular Neural Network architecture',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Chemical-NN',
                description: 'Chemical reaction-based Neural Network',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Biological-NN',
                description: 'Biological Neural Network using cells',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Organoid-NN',
                description: 'Brain organoid-based computing',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Wetware-NN',
                description: 'Wetware Neural Network architecture',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Biohybrid-NN',
                description: 'Biological-electronic hybrid neural network',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuroSymbolicAndHybrid'})
            CREATE (a:Architecture:`NeuroSymbolicAndHybrid` {
                name: 'Cyborg-NN',
                description: 'Cyborg neural network architecture',
                category: 'NeuroSymbolicAndHybrid'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'NeuralODEs&Continuous',
                description: 'They allow simulating the continuous change of latent states, which opens up new possibilities for time series analysis, signal processing, and dynamic systems',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Neural-ODE',
                description: 'Neural Ordinary Differential Equation',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Neural-ODE-Base',
                description: 'Base Neural ODE architecture',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Neural-ODE-ResNet',
                description: 'Neural ODE with ResNet parameterization',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Neural-ODE-CNN',
                description: 'Convolutional Neural ODE',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Neural-ODE-RNN',
                description: 'Recurrent Neural ODE',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Augmented-Neural-ODE',
                description: 'Augmented Neural ODE with extra dimensions',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'ANODE-v1',
                description: 'First version of Augmented Neural ODE',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'ANODE-v2',
                description: 'Improved Augmented Neural ODE',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'FFJORD',
                description: 'Free-form Continuous Normalizing Flow',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'CNF',
                description: 'Continuous Normalizing Flow',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'OT-CNF',
                description: 'Optimal Transport Continuous Normalizing Flow',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Wasserstein-CNF',
                description: 'Wasserstein Continuous Normalizing Flow',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Latent-ODE',
                description: 'Latent Neural ODE for time series',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'ODE-RNN',
                description: 'ODE-based Recurrent Neural Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'ODE-LSTM',
                description: 'LSTM with ODE dynamics',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'GRU-ODE',
                description: 'GRU with continuous ODE evolution',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'GRU-ODE-Bayes',
                description: 'Bayesian GRU-ODE for uncertainty',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Continuous-RNN',
                description: 'Continuous-time Recurrent Neural Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Neural-CDE',
                description: 'Neural Controlled Differential Equation',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Neural-SDE',
                description: 'Neural Stochastic Differential Equation',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'SDE-Net',
                description: 'Stochastic Differential Equation Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Diffusion-SDE',
                description: 'SDE for diffusion models',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Score-SDE',
                description: 'Score-based SDE for generation',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Hamiltonian-NN',
                description: 'Hamiltonian Neural Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'HNN',
                description: 'Hamiltonian Neural Network for physics',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Lagrangian-NN',
                description: 'Lagrangian Neural Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'LNN',
                description: 'Lagrangian Neural Network for mechanics',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Symplectic-ODENet',
                description: 'Symplectic ODE Network for conservation',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Deep-Hamiltonian',
                description: 'Deep Hamiltonian Neural Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Deep-Lagrangian',
                description: 'Deep Lagrangian Neural Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Physics-Informed-NN',
                description: 'Physics-Informed Neural Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'PINN',
                description: 'PINN for solving differential equations',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'XPINN',
                description: 'Extended PINN with domain decomposition',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'B-PINN',
                description: 'Bayesian Physics-Informed Neural Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'VPINN',
                description: 'Variational Physics-Informed Neural Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'fPINN',
                description: 'Fractional PINN for fractional PDEs',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'DeepONet',
                description: 'Deep Operator Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Fourier-DeepONet',
                description: 'Fourier Neural Operator',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'FNO',
                description: 'Fourier Neural Operator for PDEs',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'FNO-2D',
                description: '2D Fourier Neural Operator',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'FNO-3D',
                description: '3D Fourier Neural Operator',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Geo-FNO',
                description: 'Geometry-aware Fourier Neural Operator',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'U-NO',
                description: 'U-Net shaped Neural Operator',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'WNO',
                description: 'Wavelet Neural Operator',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'LOCA',
                description: 'Learning Operators with Coupled Attention',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'GNO',
                description: 'Graph Neural Operator',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Continuous-Transformer',
                description: 'Transformer in continuous time',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Neural-Flow',
                description: 'Neural Flow model',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Continuous-Flow',
                description: 'Continuous Flow-based model',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Neural-CP-Flow',
                description: 'Neural Continuous Piecewise Flow',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Neural-Transport',
                description: 'Neural Transport model',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Continuous-Depth-ResNet',
                description: 'ResNet with continuous depth',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Infinitesimal-Transformer',
                description: 'Transformer with infinitesimal layers',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Neural-Process',
                description: 'Neural Process for function learning',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'CNP',
                description: 'Conditional Neural Process',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'ANP',
                description: 'Attentive Neural Process',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'TNP',
                description: 'Transformer Neural Process',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'GNP',
                description: 'Gaussian Neural Process',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Continuous-Bayesian-NN',
                description: 'Continuous-time Bayesian Neural Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Neural-SPDE',
                description: 'Neural Stochastic Partial Differential Equation',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Continuous-GNN',
                description: 'Continuous-time Graph Neural Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Graph-ODE',
                description: 'Graph Neural ODE',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Graph-CDE',
                description: 'Graph Controlled Differential Equation',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Neural-Manifold',
                description: 'Neural Network on manifolds',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Riemannian-NN',
                description: 'Riemannian Neural Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Lie-Group-NN',
                description: 'Lie Group Neural Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Equivariant-ODE',
                description: 'Equivariant Neural ODE',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Continuous-Attention',
                description: 'Continuous-time Attention mechanism',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Neural-Integral',
                description: 'Neural Integral Equation solver',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Volterra-NN',
                description: 'Volterra Neural Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            

            MATCH (c:Category {name: 'NeuralODEsAndContin'})
            CREATE (a:Architecture:`NeuralODEsAndContin` {
                name: 'Fredholm-NN',
                description: 'Fredholm Neural Network',
                category: 'NeuralODEsAndContin'
            })
            CREATE (a)-[:BELONGS_TO]->(c);
            
