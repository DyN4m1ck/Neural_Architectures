"""
Module for Транформеры и механизмы внимания
"""
from dataclasses import dataclass
from typing import Optional

# Specialized Architectures data
SPECIALIZED_ARCHITECTURES = [
    {
        "name": "Transformers and mechanisms of attention",
        "description": "abandoning sequential data processing in favor of parallelism and the ability of the model to instantly determine the significance of relationships between any data elements, regardless of the distance between them."
    }
]

@dataclass
class TransformersAndAttention:
    """
    Represents a State Space Model Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
Transformer and Attention-Based Architectures
Self-attention mechanisms and variants
"""

TRANSFORMER_ATTENTION_ARCHITECTURES = [
    # ========== Original Transformer Variants ==========
    {
        "name": "Transformer",
        "description": "Оригинальная архитектура 'Attention Is All You Need' с self-attention. Варианты: Base (65M), Big (213M)."
    },
    {
        "name": "Transformer-Encoder",
        "description": "Только encoder часть трансформера для задач понимания. Варианты: 6-12 слоев."
    },
    {
        "name": "Transformer-Decoder",
        "description": "Только decoder часть для генерации последовательностей. Варианты: 6-12 слоев."
    },
    {
        "name": "Transformer-Encoder-Decoder",
        "description": "Полная архитектура encoder-decoder для seq2seq задач. Варианты: 6-24 слоев."
    },
    {
        "name": "Pre-LN Transformer",
        "description": "Трансформер с пред-нормализацией (LayerNorm перед подслоями). Более стабильное обучение."
    },
    {
        "name": "Post-LN Transformer",
        "description": "Трансформер с пост-нормализацией (LayerNorm после подслоев). Оригинальная версия."
    },
    {
        "name": "Deep Transformer",
        "description": "Трансформер с увеличенной глубиной. Варианты: 12-48 слоев."
    },
    {
        "name": "Wide Transformer",
        "description": "Трансформер с увеличенной шириной. Варианты: 512-4096 hidden dimensions."
    },
    
    # ========== BERT Family (Google) ==========
    {
        "name": "BERT",
        "description": "Bidirectional Encoder Representations from Transformers. Варианты: Base (110M, 12 слоев), Large (340M, 24 слоя). Uncased/Cased версии."
    },
    {
        "name": "BERT-Whole-Word-Masking",
        "description": "BERT с маскированием целых слов вместо токенов. Улучшает понимание слов."
    },
    {
        "name": "SpanBERT",
        "description": "BERT с предсказанием span'ов вместо отдельных токенов. Варианты: Base, Large."
    },
    {
        "name": "CodeBERT",
        "description": "BERT для программирования и кода. Обучен на Python и документациях. 125M параметров."
    },
    {
        "name": "GraphCodeBERT",
        "description": "BERT для кода с графами потока данных. Улучшенное понимание структуры кода."
    },
    {
        "name": "SciBERT",
        "description": "BERT для научных текстов. Обучен на научных публикациях. 114M параметров."
    },
    {
        "name": "BioBERT",
        "description": "BERT для биомедицинских текстов. Обучен на PubMed. 110M параметров."
    },
    {
        "name": "ClinicalBERT",
        "description": "BERT для клинических записей. Специализирован на медицинских данных."
    },
    {
        "name": "LegalBERT",
        "description": "BERT для юридических документов. Обучен на юридических текстах."
    },
    {
        "name": "FinBERT",
        "description": "BERT для финансовых текстов. Специализирован на финансовой терминологии."
    },
    
    # ========== RoBERTa Family (Meta) ==========
    {
        "name": "RoBERTa",
        "description": "Robustly Optimized BERT Pretraining Approach. Улучшенный BERT без NSP. Варианты: Base (125M), Large (355M), XL (900M), XXL (1.8B)."
    },
    {
        "name": "Longformer-RoBERTa",
        "description": "RoBERTa с sparse attention для длинных документов. До 4096 токенов."
    },
    {
        "name": "CodeRoBERTa",
        "description": "RoBERTa для программирования. Улучшенная версия CodeBERT."
    },
    
    # ========== ALBERT Family (Google) ==========
    {
        "name": "ALBERT",
        "description": "A Lite BERT с параметрическим sharing. Меньше параметров при той же производительности. Варианты: Base (12M), Large (18M), XL (58M), XXL (223M)."
    },
    
    # ========== Distilled Models ==========
    {
        "name": "DistilBERT",
        "description": "Дистиллированный BERT: 6 слоев, 40% меньше параметров (66M), 60% скорости, 97% качества BERT."
    },
    {
        "name": "DistilRoBERTa",
        "description": "Дистиллированный RoBERTa. 8 слоев, 124M параметров."
    },
    {
        "name": "TinyBERT",
        "description": "Крошечный BERT для мобильных устройств. Варианты: 4 слоя (14.5M), 6 слоев (67M)."
    },
    {
        "name": "MiniLM",
        "description": "Miniature Language Model с эффективной дистилляцией. Варианты: L6 (22M), L12 (33M), v2 (улучшенная версия)."
    },
    {
        "name": "MobileBERT",
        "description": "Mobile-friendly BERT с bottleneck структурой. 25M параметров, оптимизирован для мобильных."
    },
    {
        "name": "FastBERT",
        "description": "Быстрый BERT с adaptive inference (ранний выход). Варианты: Base, Large."
    },
    
    # ========== ELECTRA Family (Google) ==========
    {
        "name": "ELECTRA",
        "description": "Efficiently Learning Encoder that Classifies Token Replacements. Более эффективное обучение. Варианты: Small (14M), Base (110M), Large (335M)."
    },
    {
        "name": "CodeELECTRA",
        "description": "ELECTRA для программирования. Специализирован на коде."
    },
    
    # ========== T5 Family (Google) ==========
    {
        "name": "T5",
        "description": "Text-To-Text Transfer Transformer. Все задачи как text-to-text. Варианты: Small (60M), Base (220M), Large (770M), 3B, 11B, XXL."
    },
    {
        "name": "mT5",
        "description": "Multilingual T5 для 101 языка. Варианты: Small (300M), Base (580M), Large (1.2B), XL (3.7B), XXL (13B)."
    },
    {
        "name": "CodeT5",
        "description": "T5 для программирования. Поддерживает 11 языков программирования. Варианты: Small, Base, Large."
    },
    {
        "name": "Flan-T5",
        "description": "T5 с instruction tuning для лучших zero-shot результатов. Варианты: Small, Base, Large, XL, XXL."
    },
    {
        "name": "ByT5",
        "description": "Byte-level T5 без токенизатора. Работает на уровне байтов. Варианты: Small, Base, Large."
    },
    
    # ========== GPT Family (OpenAI) ==========
    {
        "name": "GPT",
        "description": "Generative Pre-trained Transformer (OpenAI). Оригинальная версия. 117M параметров."
    },
    {
        "name": "GPT-2",
        "description": "Второе поколение GPT. Улучшенная архитектура и данные. Варианты: Small (117M), Medium (345M), Large (774M), XL (1.5B)."
    },
    {
        "name": "GPT-3",
        "description": "GPT-3 с few-shot learning. Варианты: Ada (350M), Babbage (1.3B), Curie (6.7B), Davinci (175B)."
    },
    {
        "name": "InstructGPT",
        "description": "GPT с instruction tuning и RLHF. Оптимизирован для следования инструкциям."
    },
    {
        "name": "ChatGPT",
        "description": "GPT оптимизированный для диалога. На базе GPT-3.5 с RLHF."
    },
    {
        "name": "GPT-4",
        "description": "Четвертое поколение GPT. Мультимодальный. Точное количество параметров не раскрыто."
    },
    
    # ========== Open Source GPT Variants ==========
    {
        "name": "GPT-Neo",
        "description": "Open-source GPT от EleutherAI. Варианты: 125M, 1.3B, 2.7B."
    },
    {
        "name": "GPT-J",
        "description": "GPT-J с параллельными attention слоями. 6B параметров."
    },
    {
        "name": "GPT-NeoX",
        "description": "GPT-NeoX для больших моделей. Варианты: 20B. Языковые версии: Japanese, Korean (Polyglot-Ko)."
    },
    
    # ========== BLOOM (BigScience) ==========
    {
        "name": "BLOOM",
        "description": "BigScience Large Open-science Open-access Multilingual. 46 языков. Варианты: 560M, 1.1B, 1.7B, 3B, 7.1B, 176B."
    },
    
    # ========== OPT (Meta) ==========
    {
        "name": "OPT",
        "description": "Open Pre-trained Transformer от Meta. Полностью открытая модель. Варианты: 125M, 350M, 1.3B, 2.7B, 6.7B, 13B, 30B, 66B."
    },
    
    # ========== LLaMA Family (Meta) ==========
    {
        "name": "LLaMA",
        "description": "Large Language Model Meta AI. Эффективная архитектура. Варианты: 7B, 13B, 33B, 65B."
    },
    {
        "name": "LLaMA-2",
        "description": "Второе поколение LLaMA. Улучшенное обучение и данные. Варианты: 7B, 13B, 70B. Есть Chat версия."
    },
    {
        "name": "LLaMA-3",
        "description": "Третье поколение LLaMA. Улучшенная архитектура и токенизатор. Варианты: 8B, 70B."
    },
    {
        "name": "CodeLLaMA",
        "description": "LLaMA для программирования. Поддерживает multiple языки. Варианты: 7B, 13B, 34B, 70B."
    },
    {
        "name": "Vicuna",
        "description": "Fine-tuned LLaMA для диалога. Обучен на ChatGPT данных. Варианты: 7B, 13B, 33B."
    },
    {
        "name": "Alpaca",
        "description": "Instruction-tuned LLaMA. Обучен на Self-Instruct данных. 7B параметров."
    },
    {
        "name": "WizardLM",
        "description": "Улучшенный Alpaca с Evol-Instruct для сложных инструкций. Варианты: 7B, 13B, 70B."
    },
    
    # ========== Falcon (TII) ==========
    {
        "name": "Falcon",
        "description": "Falcon LLM от Technology Innovation Institute. Эффективная attention архитектура. Варианты: 7B, 40B, 180B. Есть Chat версия."
    },
    
    # ========== Mistral Family ==========
    {
        "name": "Mistral-7B",
        "description": "Mistral AI с sliding window attention. 7B параметров. Высокая эффективность."
    },
    {
        "name": "Mixtral",
        "description": "Mixture of Experts от Mistral. Sparse MoE архитектура. Варианты: 8x7B (47B total, 13B active), 8x22B."
    },
    
    # ========== Google Large Models ==========
    {
        "name": "PaLM",
        "description": "Pathways Language Model от Google. Эффективное параллельное обучение. Варианты: 8B, 62B, 540B."
    },
    {
        "name": "PaLM-2",
        "description": "Второе поколение PaLM. Улучшенная multilingual поддержка. Варианты: Gecko, Otter, Bison, Unicorn."
    },
    {
        "name": "Gemini",
        "description": "Multimodal model от Google. Нативная мультимодальность. Варианты: Nano, Pro, Ultra."
    },
    
    # ========== Anthropic Models ==========
    {
        "name": "Claude",
        "description": "Anthropic Claude model с Constitutional AI. Безопасный и полезный ассистент."
    },
    {
        "name": "Claude-2",
        "description": "Второе поколение Claude. Улучшенная производительность и контекст."
    },
    {
        "name": "Claude-3",
        "description": "Третье поколение Claude. Варианты: Haiku (быстрый), Sonnet (сбалансированный), Opus (мощный)."
    },
    
    # ========== Efficient Transformers ==========
    {
        "name": "Linformer",
        "description": "Linear complexity Transformer. O(n) вместо O(n²). Варианты: Small, Base."
    },
    {
        "name": "Performer",
        "description": "Transformer с linear attention через kernel methods (FAVOR+). Варианты: Base."
    },
    {
        "name": "Reformer",
        "description": "Transformer с locality-sensitive hashing для эффективного attention. До 64K токенов."
    },
    {
        "name": "Longformer",
        "description": "Transformer для длинных документов с sparse attention. Варианты: Base (4096 tokens), Large (8192 tokens)."
    },
    {
        "name": "BigBird",
        "description": "Sparse attention Transformer. Комбинация local, global и random attention. Варианты: Base, Large."
    },
    {
        "name": "Sparse Transformer",
        "description": "Transformer с sparse attention patterns. Различные паттерны разреженности."
    },
    {
        "name": "Axial Transformer",
        "description": "Transformer с axial attention (factorized по осям). Для изображений."
    },
    {
        "name": "Synthesizer",
        "description": "Transformer с learned attention weights вместо query-key."
    },
    
    # ========== Vision Transformers ==========
    {
        "name": "ViT",
        "description": "Vision Transformer. Первый чистый трансформер для изображений. Варианты: Tiny (5M), Small (22M), Base (86M), Large (307M), Huge (632M), Giant (1B)."
    },
    {
        "name": "DeiT",
        "description": "Data-efficient Image Transformer. Обучен через distillation. Варианты: Tiny, Small, Base."
    },
    {
        "name": "Swin Transformer",
        "description": "Hierarchical Vision Transformer с shifted windows. Варианты: Tiny, Small, Base, Large. Версия v2 с улучшенной стабильностью."
    },
    {
        "name": "PVT",
        "description": "Pyramid Vision Transformer. Иерархическая структура как у CNN. Варианты: Tiny, Small, Medium, Large. Версия v2 улучшена."
    },
    {
        "name": "CvT",
        "description": "Convolutional Vision Transformer. Комбинация convolution и attention. Варианты: 13, 21, W (wide)."
    },
    {
        "name": "TNT",
        "description": "Transformer in Transformer. Вложенная attention структура. Варианты: Small, Base."
    },
    {
        "name": "CrossViT",
        "description": "Cross-attention Vision Transformer. Dual-branch архитектура. Варианты: Small, Base, Large."
    },
    {
        "name": "CaiT",
        "description": "Going deeper with Image Transformers. Class attention в последних слоях. Варианты: Small, Medium, Large."
    },
    {
        "name": "BoT",
        "description": "Bottleneck Transformer. Attention в bottleneck слоях ResNet. Варианты: 50, 101."
    },
    {
        "name": "CoAtNet",
        "description": "Combining Convolution and Attention. Гибрид convolution и attention. Варианты: 0-7 (25M до 3.9B)."
    },
    {
        "name": "MaxViT",
        "description": "Multi-Axis Vision Transformer. Local и global attention. Варианты: Tiny, Small, Base, Large."
    },
    
    # ========== Efficient ViT Variants ==========
    {
        "name": "MobileViT",
        "description": "Mobile Vision Transformer. Легковесный для мобильных. Варианты: XS, S, M, L. Версия v2 улучшена."
    },
    {
        "name": "EfficientFormer",
        "description": "Efficient Vision Transformer. Оптимизирован для latency. Варианты: L1, L3, L7."
    },
    {
        "name": "EdgeNeXt",
        "description": "Edge-friendly Vision Transformer. Для граничных устройств. Варианты: XXSmall, XSmall, Small, Medium, Large."
    },
    {
        "name": "TinyViT",
        "description": "Tiny Vision Transformer. Для мобильных и edge. Варианты: 5M, 11M, 21M параметров."
    },
    {
        "name": "LeViT",
        "description": "LeViT: Vision Transformer in ConvNet's Clothing. Гибрид архитектура. Варианты: 128, 192, 256, 384 (M operations)."
    },
    
    # ========== Video Transformers ==========
    {
        "name": "ViViT",
        "description": "Video Vision Transformer. Для видео классификации. Варианты: Factorised encoder, Decoder."
    },
    {
        "name": "TimeSformer",
        "description": "Space-Time Vision Transformer. Раздельное space и time attention. Варианты: Large."
    },
    {
        "name": "MViT",
        "description": "Multiscale Vision Transformer. Для видео и изображений. Версии: v1, v2 (улучшенная)."
    },
    {
        "name": "VideoMAE",
        "description": "Masked Autoencoder для видео. Self-supervised обучение. Версия v2 улучшена."
    },
    {
        "name": "UniFormer",
        "description": "Unified Transformer для видео. Единая архитектура для space-time. Варианты: Small, Base."
    },
    {
        "name": "Video-Swin",
        "description": "Swin Transformer для видео. 3D shifted windows. Варианты: Tiny, Small, Base."
    },
    
    # ========== Specialized Transformers ==========
    {
        "name": "LayoutLM",
        "description": "Transformer для документов с layout информацией. Версии: v1, v2, v3 (улучшенные)."
    },
    {
        "name": "StructuralLM",
        "description": "Transformer для структурированных документов. Учитывает структуру документа."
    },
    {
        "name": "Table Transformer",
        "description": "Transformer для таблиц. Распознавание структуры таблиц."
    },
    {
        "name": "Donut",
        "description": "Document understanding Transformer. OCR-free document understanding."
    },
    {
        "name": "Pix2Struct",
        "description": "Pixel-to-Structure Transformer. Скриншот-to-структура."
    },
    {
        "name": "Nougat",
        "description": "Neural Optical Understanding for Academic Texts. Научные документы в Markdown."
    },
    {
        "name": "ChartFormer",
        "description": "Transformer для графиков и диаграмм. Извлечение данных из chart."
    },
    
    # ========== Audio Transformers ==========
    {
        "name": "Wav2Vec 2.0",
        "description": "Self-supervised learning для speech. Варианты: Base (95M), Large (317M), XL, XXL."
    },
    {
        "name": "HuBERT",
        "description": "Hidden Unit BERT для speech. Улучшенная версия Wav2Vec. Варианты: Base, Large."
    },
    {
        "name": "WavLM",
        "description": "Unified speech model. Для speech recognition и downstream задач. Варианты: Base, Large."
    },
    {
        "name": "Data2Vec",
        "description": "General framework для speech, vision, NLP. Универсальная self-supervised модель."
    },
    {
        "name": "AST",
        "description": "Audio Spectrogram Transformer. Для классификации аудио. Варианты: Base."
    },
    {
        "name": "Music Transformer",
        "description": "Transformer для генерации музыки. Relative attention для long-term структуры."
    },
    {
        "name": "Jukebox",
        "description": "Music generation с lyrics. VQ-VAE + Transformer."
    },
    {
        "name": "MusicGen",
        "description": "Music generation model от Meta. Text-to-music."
    },
    {
        "name": "MusicLM",
        "description": "High-fidelity music generation от Google. Hierarchical sequence-to-sequence."
    },
    
    # ========== Graph Transformers ==========
    {
        "name": "Graph Transformer",
        "description": "Transformer для графов. General architecture для graph data."
    },
    {
        "name": "Graphormer",
        "description": "Transformer с centrality encoding для графов. Варианты: Base, Large."
    },
    {
        "name": "SAN",
        "description": "Spectral Attention Network. Spectral encoding для графов."
    },
    {
        "name": "GPS",
        "description": "Graph Product of Sum. Комбинация local и global attention."
    },
    {
        "name": "Graph-BERT",
        "description": "BERT для графов. Pre-training на графах."
    },
    {
        "name": "GraphMAE",
        "description": "Masked Autoencoder для графов. Self-supervised на графах. Версия v2 улучшена."
    },
    
    # ========== Multimodal Transformers ==========
    {
        "name": "VisualBERT",
        "description": "BERT для vision-language. Простая архитектура для VQA."
    },
    {
        "name": "VL-BERT",
        "description": "Vision-Language BERT. General vision-language representation."
    },
    {
        "name": "LXMERT",
        "description": "Learning Cross-Modality Encoder. Cross-modal attention."
    },
    {
        "name": "UNITER",
        "description": "UNiversal Image-TExt Representation. Large-scale pretraining."
    },
    {
        "name": "Oscar",
        "description": "Object-Semantics Aligned Pretraining. Object tags как anchor points."
    },
    {
        "name": "VinVL",
        "description": "Vision representations in Vision-Language. Улучшенные visual features."
    },
    {
        "name": "ViLT",
        "description": "Vision-and-Language Transformer без convolution. Pure Transformer."
    },
    {
        "name": "ALBEF",
        "description": "Align before Fuse. Contrastive learning для vision-language."
    },
    {
        "name": "BLIP",
        "description": "Bootstrapping Language-Image Pretraining. Self-training с noisy data. Версия v2 улучшена."
    },
    {
        "name": "Flamingo",
        "description": "Visual language model для few-shot learning. Interleaved image-text."
    },
    {
        "name": "PaLI",
        "description": "Language-Image model. Scaling vision-language. Версии: v1, v2, v3."
    },
    {
        "name": "BEiT-3",
        "description": "Image as foreign language. Unified vision-language model."
    },
    {
        "name": "KOSMOS",
        "description": "Multimodal large language model. Grounding capabilities. Версии: 1, 2."
    },
    
    # ========== Attention Mechanisms ==========
    {
        "name": "Scaled Dot-Product Attention",
        "description": "Оригинальный механизм внимания из Transformer. Scaled для стабильности."
    },
    {
        "name": "Multi-Head Attention",
        "description": "Multi-head self-attention. Параллельные attention heads."
    },
    {
        "name": "Additive Attention",
        "description": "Bahdanau attention (additive). Для seq2seq с alignment."
    },
    {
        "name": "Multiplicative Attention",
        "description": "Luong attention (multiplicative). Варианты: dot, general, concat."
    },
    {
        "name": "Global Attention",
        "description": "Global attention (все позиции). Для full context."
    },
    {
        "name": "Local Attention",
        "description": "Local attention (window-based). Для long sequences."
    },
    {
        "name": "Self-Attention",
        "description": "Self-attention (intra-attention). Within sequence attention."
    },
    {
        "name": "Cross-Attention",
        "description": "Cross-attention (inter-attention). Between different sequences/modalities."
    },
    {
        "name": "Hierarchical Attention",
        "description": "Hierarchical attention network. Multi-level attention."
    },
    {
        "name": "Co-Attention",
        "description": "Co-attention для multimodal. Parallel attention на разных модальностях."
    },
    {
        "name": "Gated Attention",
        "description": "Gated attention mechanism. С gating для контроля потока."
    },
    {
        "name": "Dynamic Attention",
        "description": "Dynamic attention (adaptive). Адаптивные weights."
    },
    {
        "name": "Sparse Attention",
        "description": "Sparse attention patterns. Различные паттерны разреженности."
    },
    {
        "name": "Linear Attention",
        "description": "Linear complexity attention. O(n) вместо O(n²)."
    },
    {
        "name": "Flash Attention",
        "description": "IO-aware exact attention. Быстрее и меньше памяти. Версия v2 улучшена."
    },
    {
        "name": "Paged Attention",
        "description": "Paged attention (vLLM). Для efficient inference."
    },
    {
        "name": "Ring Attention",
        "description": "Ring attention для long context. Distributed attention."
    },
    {
        "name": "Window Attention",
        "description": "Sliding window attention. Local window с global."
    },
    {
        "name": "Relative Position Attention",
        "description": "Relative position encoding. Учитывает относительные позиции."
    },
    {
        "name": "RoPE",
        "description": "Rotary Position Embedding. Rotary encoding для позиций."
    },
    {
        "name": "ALiBi",
        "description": "Attention with Linear Biases. Linear bias для extrapolation."
    },
    {
        "name": "FNet",
        "description": "Fourier Transform вместо attention. Быстрее attention."
    },
    {
        "name": "Perceiver",
        "description": "Perceiver IO architecture. Unified architecture для разных модальностей. Варианты: AR, IO."
    },
]