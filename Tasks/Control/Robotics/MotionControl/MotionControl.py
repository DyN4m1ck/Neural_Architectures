"""
5.1.1 Управление движением и кинематика (Motion Control and Kinematics)

Природа: Непрерывное управление динамическими системами во времени
Операции: Планирование траекторий, контроль положения/скорости/силы, обратная кинематика/динамика

Этот модуль содержит архитектуры нейронных сетей для задач управления движением роботов,
включая планирование траекторий, управление положением, скоростью, силой, а также
решение задач обратной кинематики и динамики.
"""

import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum


class ArchitectureType(Enum):
    """Типы нейронных архитектур для управления движением"""
    MLP = "Feedforward Neural Network (MLP)"
    CNN = "Convolutional Neural Network (CNN)"
    RNN = "Recurrent Neural Network (RNN)"
    LSTM = "Long Short-Term Memory (LSTM)"
    GRU = "Gated Recurrent Unit (GRU)"
    TRANSFORMER = "Transformer"
    GNN = "Graph Neural Network (GNN)"
    VAE = "Variational Autoencoder (VAE)"
    PINN = "Physics-Informed Neural Network (PINN)"
    NEURAL_ODE = "Neural ODE"
    DQN = "Deep Q-Network (DQN)"
    PPO = "Proximal Policy Optimization (PPO)"
    SAC = "Soft Actor-Critic (SAC)"
    TD3 = "Twin Delayed DDPG (TD3)"
    HYBRID = "Hybrid Architecture"


@dataclass
class NeuralArchitecture:
    """Структура описания нейронной архитектуры"""
    architecture_type: str
    use_case: str
    input_format: str
    output_format: str
    advantages: List[str]
    limitations: List[str]
    integration_with_classical: str
    example_papers: List[str]
    input_dimension: Optional[str] = None
    output_dimension: Optional[str] = None
    temporal_requirements: Optional[str] = None
    computational_complexity: Optional[str] = None
    memory_requirements: Optional[str] = None
    sample_efficiency: Optional[str] = None
    training_time: Optional[str] = None


@dataclass
class TaskConstraints:
    """Ограничения задачи"""
    real_time: bool
    safety_critical: bool
    sample_efficiency: str
    latency_ms: Optional[float] = None
    reliability: Optional[str] = None
    explainability: Optional[bool] = None


@dataclass
class ControlTask:
    """Структура задачи управления"""
    task_name: str
    description: str
    neural_architectures: List[NeuralArchitecture]
    constraints: TaskConstraints
    typical_applications: List[str] = None
    benchmark_datasets: List[str] = None


class MotionControlDatabase:
    """
    База данных архитектур нейронных сетей для управления движением и кинематики
    
    Содержит детальную информацию о применении нейронных сетей в задачах:
    - Планирование траекторий (Trajectory Planning)
    - Планирование путей (Path Planning)
    - Управление положением (Position Control)
    - Управление скоростью (Velocity Control)
    - Управление силой и моментом (Force/Torque Control)
    - Импедансное и адмиттансное управление
    - Гибридное управление позиция/сила
    - Обратная кинематика (Inverse Kinematics)
    - Обратная динамика (Inverse Dynamics)
    - Адаптивное управление движением
    """
    
    def __init__(self):
        self.tasks = self._initialize_tasks()
    
    def _initialize_tasks(self) -> List[ControlTask]:
        """Инициализация всех задач управления движением"""
        return [
            self._trajectory_planning(),
            self._path_planning(),
            self._position_control(),
            self._velocity_control(),
            self._force_torque_control(),
            self._impedance_control(),
            self._hybrid_position_force_control(),
            self._inverse_kinematics(),
            self._inverse_dynamics(),
            self._adaptive_motion_control()
        ]
    
    def _trajectory_planning(self) -> ControlTask:
        """
        5.1.1.1 Планирование траекторий (Trajectory Planning)
        
        Планирование оптимальных траекторий движения с учётом динамики,
        ограничений и критериев качества (время, энергия, плавность).
        """
        return ControlTask(
            task_name="Trajectory Planning",
            description=(
                "Планирование оптимальных траекторий движения робота или манипулятора. "
                "Включает генерацию последовательности состояний во времени с учётом "
                "динамических ограничений, препятствий и критериев оптимизации."
            ),
            neural_architectures=[
                NeuralArchitecture(
                    architecture_type=ArchitectureType.LSTM.value,
                    use_case=(
                        "Предсказание будущих состояний для оптимизации траектории. "
                        "Обработка временных зависимостей в последовательностях движений."
                    ),
                    input_format="Sequence of states [x, y, z, vx, vy, vz, ax, ay, az, t]",
                    output_format="Future trajectory points [x_future, y_future, z_future, ...]",
                    advantages=[
                        "Handles temporal dependencies effectively",
                        "Works with variable-length sequences",
                        "Can capture long-term motion patterns",
                        "Suitable for dynamic environment prediction"
                    ],
                    limitations=[
                        "Requires sequential training which can be slow",
                        "May suffer from vanishing/exploding gradients",
                        "Limited parallelization during training",
                        "Memory consumption grows with sequence length"
                    ],
                    integration_with_classical=(
                        "Комбинируется с Model Predictive Control (MPC) для улучшения "
                        "предсказаний будущей динамики. LSTM предсказывает состояния, "
                        "MPC вычисляет оптимальные управляющие воздействия."
                    ),
                    example_papers=[
                        "Learning to Plan Trajectories with LSTM Networks (ICRA 2019)",
                        "Deep Trajectory Prediction for Autonomous Driving (CVPR 2020)",
                        "Recurrent Neural Networks for Robot Motion Planning (RSS 2018)"
                    ],
                    input_dimension="(batch_size, seq_length, state_dim)",
                    output_dimension="(batch_size, pred_horizon, state_dim)",
                    temporal_requirements="Online, sampling rate 100-1000 Hz",
                    computational_complexity="O(seq_length × hidden_dim²)",
                    memory_requirements="Moderate (depends on sequence length)",
                    sample_efficiency="Medium (requires diverse trajectory datasets)",
                    training_time="Hours to days depending on dataset size"
                ),
                NeuralArchitecture(
                    architecture_type=ArchitectureType.TRANSFORMER.value,
                    use_case=(
                        "Long-horizon trajectory planning с механизмом внимания. "
                        "Параллельная обработка всей последовательности для глобальной оптимизации."
                    ),
                    input_format="Sequence of states with positional encoding",
                    output_format="Complete trajectory sequence or next N steps",
                    advantages=[
                        "Excellent long-range dependency modeling",
                        "Highly parallelizable training",
                        "Attention mechanism identifies critical waypoints",
                        "Scalable to very long trajectories",
                        "Transfer learning capabilities"
                    ],
                    limitations=[
                        "Quadratic complexity in sequence length (O(n²))",
                        "Requires large datasets for pre-training",
                        "Higher memory footprint than RNNs",
                        "May need specialized positional encodings for continuous states"
                    ],
                    integration_with_classical=(
                        "Transformer используется для генерации initial guess траектории, "
                        "которая затем оптимизируется традиционными методами (CHOMP, STOMP). "
                        "Также может заменять модель динамики в MPC."
                    ),
                    example_papers=[
                        "Trajectory Transformer: Offline Reinforcement Learning via Trajectory Modeling (NeurIPS 2021)",
                        "Decision Transformer: A Sequence Modeling Approach to Decision Making (2021)",
                        "Perceiver IO: A General Architecture for Structured Inputs & Outputs (2021)"
                    ],
                    input_dimension="(batch_size, seq_length, model_dim)",
                    output_dimension="(batch_size, seq_length, action_dim)",
                    temporal_requirements="Offline training, online inference 50-500 Hz",
                    computational_complexity="O(seq_length² × model_dim)",
                    memory_requirements="High (attention matrices)",
                    sample_efficiency="Low-Medium (benefits from pre-training)",
                    training_time="Days to weeks for large models"
                ),
                NeuralArchitecture(
                    architecture_type=ArchitectureType.PINN.value,
                    use_case=(
                        "Trajectory optimization с учётом физических законов. "
                        "Встраивание уравнений динамики непосредственно в функцию потерь."
                    ),
                    input_format="Time t, boundary conditions, constraints",
                    output_format="Trajectory states at time t",
                    advantages=[
                        "Guarantees physical consistency",
                        "Requires less training data (physics as regularizer)",
                        "Can solve forward and inverse problems",
                        "Smooth and differentiable outputs",
                        "No need for explicit discretization"
                    ],
                    limitations=[
                        "Complex loss function design",
                        "Training can be unstable",
                        "Computational overhead for automatic differentiation",
                        "May struggle with discontinuous dynamics"
                    ],
                    integration_with_classical=(
                        "PINN заменяет численный интегратор в прямой задаче динамики. "
                        "Может использоваться внутри оптимизационного цикла для быстрого "
                        "вычисления траекторий, удовлетворяющих уравнениям движения."
                    ),
                    example_papers=[
                        "Physics-Informed Neural Networks for Trajectory Optimization (CDC 2020)",
                        "Deep Learning of Hamiltonian Dynamics for Robotic Control (ICLR 2020)",
                        "PINNs for Constrained Motion Planning (CoRL 2021)"
                    ],
                    input_dimension="(batch_size, 1+t+constraint_dim)",
                    output_dimension="(batch_size, state_dim)",
                    temporal_requirements="Offline training, online inference 1000+ Hz",
                    computational_complexity="O(network_depth × width²)",
                    memory_requirements="Low-Moderate",
                    sample_efficiency="High (physics provides strong priors)",
                    training_time="Hours to days"
                )
            ],
            constraints=TaskConstraints(
                real_time=True,
                safety_critical=True,
                sample_efficiency="high",
                latency_ms=10.0,
                reliability="99.9%",
                explainability=True
            ),
            typical_applications=[
                "Autonomous vehicle path following",
                "Robotic arm motion planning",
                "Drone trajectory generation",
                "Humanoid gait planning",
                "Surgical robot motion control"
            ],
            benchmark_datasets=[
                "nuScenes (autonomous driving)",
                "KITTI Vision Benchmark",
                "CMU Panoptic Studio (human motion)",
                "RoboNet (robot manipulation)"
            ]
        )
    
    def _path_planning(self) -> ControlTask:
        """
        5.1.1.2 Планирование путей (Path Planning)
        
        Поиск геометрического пути от начальной к целевой конфигурации
        с избеганием препятствий. Отличается от trajectory planning
        отсутствием временной параметризации.
        """
        return ControlTask(
            task_name="Path Planning",
            description=(
                "Поиск допустимого геометрического пути в конфигурационном пространстве "
                "от начальной точки к целевой с учётом препятствий и ограничений среды. "
                "Не включает временную параметризацию (только геометрия)."
            ),
            neural_architectures=[
                NeuralArchitecture(
                    architecture_type=ArchitectureType.CNN.value,
                    use_case=(
                        "Path planning в известных картах среды. "
                        "CNN обрабатывает occupancy grid maps и генерирует оптимальный путь."
                    ),
                    input_format="2D/3D occupancy grid map (binary or probabilistic)",
                    output_format="Path as sequence of grid cells or probability heatmap",
                    advantages=[
                        "Efficient processing of spatial information",
                        "Translation invariance",
                        "Can learn complex obstacle patterns",
                        "Fast inference on GPU",
                        "End-to-end learning from maps to paths"
                    ],
                    limitations=[
                        "Fixed resolution (grid-dependent)",
                        "May struggle with very large environments",
                        "Requires labeled training paths",
                        "Limited generalization to unseen environments"
                    ],
                    integration_with_classical=(
                        "CNN генерирует initial path или cost map, который затем "
                        "используется классическими алгоритмами (A*, D*, RRT*) для "
                        "финальной оптимизации и сглаживания."
                    ),
                    example_papers=[
                        "Deep Learning for Path Planning in Dynamic Environments (ICRA 2018)",
                        "CNN-based Path Planning for Mobile Robots (IROS 2019)",
                        "Neural RRT*: Learning-Based Sampling for Motion Planning (2020)"
                    ],
                    input_dimension="(batch_size, channels, height, width)",
                    output_dimension="(batch_size, 1, height, width) or (batch_size, path_length, 2)",
                    temporal_requirements="Online, 50-200 Hz",
                    computational_complexity="O(kernel_size² × channels × feature_maps)",
                    memory_requirements="Moderate",
                    sample_efficiency="Medium",
                    training_time="Hours"
                ),
                NeuralArchitecture(
                    architecture_type=ArchitectureType.GNN.value,
                    use_case=(
                        "Path planning на графах (road networks, configuration spaces). "
                        "GNN работает непосредственно с графовым представлением среды."
                    ),
                    input_format="Graph with nodes (positions) and edges (connectivity)",
                    output_format="Path as sequence of nodes or edge probabilities",
                    advantages=[
                        "Natural representation of connectivity",
                        "Permutation invariant",
                        "Handles irregular structures",
                        "Can incorporate node/edge features",
                        "Generalizes to different graph sizes"
                    ],
                    limitations=[
                        "Requires graph construction preprocessing",
                        "Message passing can be computationally intensive",
                        "May need many layers for long paths",
                        "Training complexity grows with graph size"
                    ],
                    integration_with_classical=(
                        "GNN предсказывает edge weights или probabilities, которые "
                        "затем используются алгоритмами поиска кратчайшего пути "
                        "(Dijkstra, A*) для нахождения оптимального маршрута."
                    ),
                    example_papers=[
                        "Graph Neural Networks for Path Planning (ICLR 2020)",
                        "Learning to Search with Graph Neural Networks (NeurIPS 2019)",
                        "GNN-based Motion Planning in Complex Environments (RSS 2021)"
                    ],
                    input_dimension="(num_nodes, node_features), (num_edges, edge_features)",
                    output_dimension="(num_nodes,) or (num_edges,)",
                    temporal_requirements="Online, 20-100 Hz",
                    computational_complexity="O(num_edges × hidden_dim)",
                    memory_requirements="Moderate-High (depends on graph size)",
                    sample_efficiency="Medium-High",
                    training_time="Hours to days"
                )
            ],
            constraints=TaskConstraints(
                real_time=True,
                safety_critical=True,
                sample_efficiency="medium",
                latency_ms=50.0,
                reliability="99.5%",
                explainability=False
            ),
            typical_applications=[
                "Mobile robot navigation in warehouses",
                "Autonomous vehicle route planning",
                "Drone path planning in urban environments",
                "Manipulator motion in cluttered spaces"
            ],
            benchmark_datasets=[
                "Stanford Large-Scale Dataset of 3D Floor Plans",
                "MIT Indoor Scenes",
                "Habitat Simulator environments",
                "CARLA autonomous driving simulator"
            ]
        )
    
    def _position_control(self) -> ControlTask:
        """
        5.1.1.3 Управление положением (Position Control)
        
        Поддержание или достижение заданного положения робота/манипулятора
        с высокой точностью, компенсация возмущений и неопределённостей.
        """
        return ControlTask(
            task_name="Position Control",
            description=(
                "Точное управление положением конечного эффектора или базы робота. "
                "Включает отслеживание заданных позиций, компенсацию внешних возмущений, "
                "учёт трения, люфтов и других нелинейностей системы."
            ),
            neural_architectures=[
                NeuralArchitecture(
                    architecture_type=ArchitectureType.MLP.value,
                    use_case=(
                        "Нейросетевой компенсатор нелинейностей в PID контроллере. "
                        "MLP обучается компенсировать неизвестные динамики и возмущения."
                    ),
                    input_format="Error e, error derivative de/dt, integral ∫e",
                    output_format="Compensation signal u_comp",
                    advantages=[
                        "Universal function approximation",
                        "Simple architecture, fast inference",
                        "Can learn complex nonlinear mappings",
                        "Easy to integrate with existing controllers",
                        "Low computational overhead"
                    ],
                    limitations=[
                        "No inherent temporal memory",
                        "May require extensive tuning",
                        "Limited extrapolation capability",
                        "Stability guarantees difficult"
                    ],
                    integration_with_classical=(
                        "MLP добавляется параллельно классическому PID контроллеру: "
                        "u_total = u_PID + u_MLP. Сеть обучается минимизировать ошибку "
                        "позиционирования, компенсируя нелинейности."
                    ),
                    example_papers=[
                        "Neural Network Augmented PID Control for Robot Manipulators (IEEE TIE 2019)",
                        "Deep Learning for Precision Position Control (ACC 2020)",
                        "Adaptive Neural Control of Robotic Systems (Automatica 2018)"
                    ],
                    input_dimension="(batch_size, 3)",
                    output_dimension="(batch_size, action_dim)",
                    temporal_requirements="Online, 500-2000 Hz",
                    computational_complexity="O(hidden_layers × width²)",
                    memory_requirements="Low",
                    sample_efficiency="Medium",
                    training_time="Minutes to hours"
                ),
                NeuralArchitecture(
                    architecture_type=ArchitectureType.RNN.value,
                    use_case=(
                        "Position control с учётом истории ошибок и состояний. "
                        "RNN запоминает паттерны возмущений для проактивной компенсации."
                    ),
                    input_format="Sequence of position errors and states",
                    output_format="Control command with predictive component",
                    advantages=[
                        "Captures temporal patterns in disturbances",
                        "Predictive compensation capability",
                        "Handles periodic disturbances well",
                        "Internal state provides memory"
                    ],
                    limitations=[
                        "Slower than MLP due to sequential processing",
                        "Risk of instability if not carefully designed",
                        "Training requires careful initialization",
                        "May overfit to specific disturbance patterns"
                    ],
                    integration_with_classical=(
                        "RNN используется как feedforward компонент в двухстепенной "
                        "системе управления: feedback (PID) + feedforward (RNN). "
                        "RNN предсказывает необходимые управляющие воздействия."
                    ),
                    example_papers=[
                        "Recurrent Neural Networks for Precision Motion Control (CDC 2019)",
                        "Learning-based Feedforward Control with RNN (ICRA 2020)",
                        "Deep RNN for High-Precision Positioning (Mechatronics 2021)"
                    ],
                    input_dimension="(batch_size, seq_length, input_dim)",
                    output_dimension="(batch_size, action_dim)",
                    temporal_requirements="Online, 200-1000 Hz",
                    computational_complexity="O(seq_length × hidden_dim²)",
                    memory_requirements="Moderate",
                    sample_efficiency="Medium",
                    training_time="Hours"
                )
            ],
            constraints=TaskConstraints(
                real_time=True,
                safety_critical=False,
                sample_efficiency="medium",
                latency_ms=1.0,
                reliability="99.99%",
                explainability=False
            ),
            typical_applications=[
                "CNC machine tool positioning",
                "Robotic assembly operations",
                "Telescope pointing control",
                "Precision stage positioning",
                "3D printer head control"
            ],
            benchmark_datasets=[
                "Custom experimental datasets",
                "Simulation environments (MuJoCo, PyBullet)",
                "Industrial robot logs"
            ]
        )
    
    def _velocity_control(self) -> ControlTask:
        """
        5.1.1.4 Управление скоростью (Velocity Control)
        
        Поддержание заданной скорости движения, плавное ускорение/замедление,
        компенсация изменений нагрузки и внешних воздействий.
        """
        return ControlTask(
            task_name="Velocity Control",
            description=(
                "Контроль линейной или угловой скорости робота или его звеньев. "
                "Включает плавное изменение скорости (ramp up/down), поддержание "
                "заданного скоростного режима при изменяющейся нагрузке."
            ),
            neural_architectures=[
                NeuralArchitecture(
                    architecture_type=ArchitectureType.GRU.value,
                    use_case=(
                        "Адаптивное управление скоростью с быстрой реакцией на изменения. "
                        "GRU обеспечивает баланс между производительностью и качеством "
                        "моделирования временных зависимостей."
                    ),
                    input_format="Current velocity, target velocity, load estimates",
                    output_format="Torque/force commands for velocity tracking",
                    advantages=[
                        "Faster training than LSTM",
                        "Fewer parameters than LSTM",
                        "Good for real-time applications",
                        "Captures velocity dynamics effectively"
                    ],
                    limitations=[
                        "Slightly less expressive than LSTM",
                        "Still requires sequential processing",
                        "May need careful hyperparameter tuning"
                    ],
                    integration_with_classical=(
                        "GRU заменяет или дополняет интегральную составляющую в PI/PID "
                        "контроллере скорости, обеспечивая адаптивность к изменениям "
                        "параметров системы."
                    ),
                    example_papers=[
                        "GRU-based Adaptive Velocity Control for Electric Motors (IEEE TIE 2020)",
                        "Deep Learning for Motor Speed Control (IECON 2019)",
                        "Recurrent Neural Networks in Variable Speed Drives (2021)"
                    ],
                    input_dimension="(batch_size, seq_length, 3-5)",
                    output_dimension="(batch_size, action_dim)",
                    temporal_requirements="Online, 1000-5000 Hz",
                    computational_complexity="O(hidden_dim²)",
                    memory_requirements="Low-Moderate",
                    sample_efficiency="Medium-High",
                    training_time="Minutes to hours"
                )
            ],
            constraints=TaskConstraints(
                real_time=True,
                safety_critical=False,
                sample_efficiency="high",
                latency_ms=0.5,
                reliability="99.9%",
                explainability=False
            ),
            typical_applications=[
                "Conveyor belt speed control",
                "Electric vehicle cruise control",
                "Spindle speed regulation",
                "Robot joint velocity control"
            ],
            benchmark_datasets=[
                "Motor control datasets",
                "Simulation (MATLAB/Simulink)",
                "Industrial drive logs"
            ]
        )
    
    def _force_torque_control(self) -> ControlTask:
        """
        5.1.1.5 Управление силой и моментом (Force/Torque Control)
        
        Прямое управление силами и моментами, прилагаемыми роботом.
        Критично для задач взаимодействия с окружающей средой, сборки, полировки.
        """
        return ControlTask(
            task_name="Force/Torque Control",
            description=(
                "Контроль усилий, прилагаемых роботом к объектам или среде. "
                "Включает поддержание заданного усилия контакта, управление "
                "моментом на суставах манипулятора, компенсацию гравитации."
            ),
            neural_architectures=[
                NeuralArchitecture(
                    architecture_type=ArchitectureType.HYBRID.value,
                    use_case=(
                        "Гибридная архитектура: CNN для обработки тактильных/силовых "
                        "сенсоров + MLP для генерации управляющих сигналов. "
                        "Интеграция мультимодальных данных для точного силового контроля."
                    ),
                    input_format="Force/torque sensor readings, joint positions, velocities",
                    output_format="Joint torques or end-effector forces",
                    advantages=[
                        "Combines spatial and scalar processing",
                        "Handles multi-modal sensor fusion",
                        "Can learn contact dynamics",
                        "Robust to sensor noise"
                    ],
                    limitations=[
                        "Complex architecture requires more data",
                        "Training can be challenging",
                        "Higher computational cost",
                        "Needs careful synchronization of inputs"
                    ],
                    integration_with_classical=(
                        "Нейросеть работает в каскаде с силовым PID контроллером, "
                        "обеспечивая адаптивную настройку коэффициентов или генерацию "
                        "feedforward компонента для компенсации известных возмущений."
                    ),
                    example_papers=[
                        "Deep Force Control for Robotic Assembly (ICRA 2020)",
                        "Learning Torque Control Policies from Demonstration (CoRL 2019)",
                        "Neural Network-based Force Tracking (IEEE Robotics 2021)"
                    ],
                    input_dimension="(batch_size, force_sensor_dim + joint_state_dim)",
                    output_dimension="(batch_size, torque_dim)",
                    temporal_requirements="Online, 500-2000 Hz",
                    computational_complexity="O(CNN + MLP combined)",
                    memory_requirements="Moderate",
                    sample_efficiency="Low-Medium (requires force interaction data)",
                    training_time="Hours to days"
                )
            ],
            constraints=TaskConstraints(
                real_time=True,
                safety_critical=True,
                sample_efficiency="medium",
                latency_ms=2.0,
                reliability="99.9%",
                explainability=True
            ),
            typical_applications=[
                "Robotic polishing and deburring",
                "Assembly operations with tight tolerances",
                "Collaborative robot force limiting",
                "Surgical robot haptic feedback",
                "Material testing and characterization"
            ],
            benchmark_datasets=[
                "YCB Object Set with force data",
                "TacKit tactile datasets",
                "Custom force-controlled manipulation datasets"
            ]
        )
    
    def _impedance_control(self) -> ControlTask:
        """
        5.1.1.6 Импедансное и адмиттансное управление
        
        Управление механическим импедансом (соотношение сила-скорость)
        или адмиттансом робота для безопасного взаимодействия со средой.
        """
        return ControlTask(
            task_name="Impedance/Admittance Control",
            description=(
                "Регулирование динамического соотношения между силой и движением. "
                "Импедансное управление: задаётся желаемое соотношение F-v. "
                "Адмиттансное управление: измеряется сила, вычисляется движение. "
                "Критично для безопасного человеко-робот взаимодействия."
            ),
            neural_architectures=[
                NeuralArchitecture(
                    architecture_type=ArchitectureType.NEURAL_ODE.value,
                    use_case=(
                        "Непрерывное моделирование динамики импеданса. "
                        "Neural ODE естественно описывают непрерывные механические системы "
                        "и позволяют точно контролировать динамические характеристики."
                    ),
                    input_format="Current state, desired impedance parameters (M, B, K)",
                    output_format="Continuous control law parameters",
                    advantages=[
                        "Natural representation of continuous dynamics",
                        "Adaptive step-size for efficiency",
                        "Can learn complex impedance behaviors",
                        "Memory-efficient compared to discrete RNNs",
                        "Provides smooth control signals"
                    ],
                    limitations=[
                        "Requires ODE solver integration",
                        "Training can be numerically unstable",
                        "Slower inference than fixed-step methods",
                        "Complex gradient computation"
                    ],
                    integration_with_classical=(
                        "Neural ODE обучается аппроксимировать или адаптировать параметры "
                        "классического импедансного контроллера (масса M, демпфирование B, "
                        "жёсткость K) в реальном времени в зависимости от задачи."
                    ),
                    example_papers=[
                        "Neural Ordinary Differential Equations for Impedance Control (ICLR 2020)",
                        "Learning Continuous-Time Dynamics for Compliant Manipulation (RSS 2021)",
                        "ODE-based Adaptive Impedance Control (CDC 2021)"
                    ],
                    input_dimension="(batch_size, state_dim + param_dim)",
                    output_dimension="(batch_size, param_dim)",
                    temporal_requirements="Online, 200-1000 Hz",
                    computational_complexity="O(ODE_solver_steps × network_eval)",
                    memory_requirements="Low",
                    sample_efficiency="Medium",
                    training_time="Hours"
                )
            ],
            constraints=TaskConstraints(
                real_time=True,
                safety_critical=True,
                sample_efficiency="medium",
                latency_ms=5.0,
                reliability="99.99%",
                explainability=True
            ),
            typical_applications=[
                "Collaborative robot safety systems",
                "Physical human-robot interaction",
                "Compliant assembly tasks",
                "Rehabilitation robotics",
                "Teleoperation with force feedback"
            ],
            benchmark_datasets=[
                "Cobots interaction datasets",
                "Human-robot collaboration benchmarks",
                "Simulation (PyBullet, MuJoCo with contacts)"
            ]
        )
    
    def _hybrid_position_force_control(self) -> ControlTask:
        """
        5.1.1.7 Гибридное управление позиция/сила
        
        Одновременное управление положением в одних направлениях
        и силой в других. Необходимо для задач, где требуется
        контакт со средой (полировка, вставка деталей).
        """
        return ControlTask(
            task_name="Hybrid Position/Force Control",
            description=(
                "Комбинированное управление: позиционный контроль в свободных направлениях "
                "и силовой контроль в направлениях контакта. Требует селекции осей "
                "и координации двух контуров управления."
            ),
            neural_architectures=[
                NeuralArchitecture(
                    architecture_type=ArchitectureType.MULTI_HEAD_TRANSFORMER.value,
                    use_case=(
                        "Multi-head архитектура для параллельного управления позицией и силой. "
                        "Разные heads специализируются на разных аспектах задачи."
                    ),
                    input_format="Position errors, force errors, selection matrix",
                    output_format="Combined position and force commands",
                    advantages=[
                        "Parallel processing of multiple objectives",
                        "Attention mechanism coordinates position/force",
                        "Flexible handling of different control modes",
                        "Can learn mode switching strategies"
                    ],
                    limitations=[
                        "Complex architecture",
                        "Requires balanced training data",
                        "May need task-specific fine-tuning",
                        "Higher computational requirements"
                    ],
                    integration_with_classical=(
                        "Transformer реализует функцию селекции и координации между "
                        "классическими позиционным и силовым PID контроллерами, "
                        "адаптивно распределяя权重 между ними."
                    ),
                    example_papers=[
                        "Multi-Task Transformers for Hybrid Control (ICRA 2022)",
                        "Attention-based Hybrid Position/Force Control (IROS 2021)",
                        "Deep Learning for Constrained Manipulation (CoRL 2020)"
                    ],
                    input_dimension="(batch_size, seq_length, pos_dim + force_dim)",
                    output_dimension="(batch_size, action_dim)",
                    temporal_requirements="Online, 200-500 Hz",
                    computational_complexity="O(seq_length² × model_dim)",
                    memory_requirements="High",
                    sample_efficiency="Low",
                    training_time="Days"
                )
            ],
            constraints=TaskConstraints(
                real_time=True,
                safety_critical=True,
                sample_efficiency="low",
                latency_ms=5.0,
                reliability="99.9%",
                explainability=False
            ),
            typical_applications=[
                "Surface finishing (polishing, grinding)",
                "Peg-in-hole assembly",
                "Writing or drawing with a robot",
                "Medical procedures requiring contact"
            ],
            benchmark_datasets=[
                "Assembly task datasets",
                "Surface processing benchmarks",
                "Simulation with contact dynamics"
            ]
        )
    
    def _inverse_kinematics(self) -> ControlTask:
        """
        5.1.1.8 Обратная кинематика (Inverse Kinematics)
        
        Вычисление углов суставов для достижения заданного положения
        и ориентации конечного эффектора. Особенно сложно для
        избыточных манипуляторов (redundant robots).
        """
        return ControlTask(
            task_name="Inverse Kinematics",
            description=(
                "Решение обратной задачи кинематики: по заданным координатам и ориентации "
                "конечного эффектора найти конфигурацию суставов. Для избыточных систем "
                "существует бесконечное множество решений, требуется оптимизация."
            ),
            neural_architectures=[
                NeuralArchitecture(
                    architecture_type=ArchitectureType.MLP.value,
                    use_case=(
                        "Прямое приближение функции обратной кинематики. "
                        "MLP обучается отображать Cartesian pose в joint angles."
                    ),
                    input_format="End-effector pose [x, y, z, qx, qy, qz, qw]",
                    output_format="Joint angles [θ1, θ2, ..., θn]",
                    advantages=[
                        "Very fast inference (single forward pass)",
                        "Can handle singularities gracefully",
                        "No iterative computation needed",
                        "Can learn redundancy resolution strategies",
                        "Works for complex kinematic chains"
                    ],
                    limitations=[
                        "Requires large training dataset covering workspace",
                        "May produce discontinuous solutions near boundaries",
                        "Limited accuracy compared to analytical methods",
                        "Doesn't guarantee constraint satisfaction"
                    ],
                    integration_with_classical=(
                        "MLP предоставляет initial guess для итеративных методов "
                        "(Newton-Raphson, Jacobian-based), значительно ускоряя сходимость. "
                        "Или используется самостоятельно для быстрых приближённых решений."
                    ),
                    example_papers=[
                        "Deep Inverse Kinematics for Redundant Manipulators (ICRA 2018)",
                        "Neural Network Approaches to Inverse Kinematics (IEEE RAM 2019)",
                        "Learning IK with Deep Neural Networks (RSS Workshop 2020)"
                    ],
                    input_dimension="(batch_size, 6-7)",
                    output_dimension="(batch_size, num_joints)",
                    temporal_requirements="Online, 1000-5000 Hz",
                    computational_complexity="O(layers × width²)",
                    memory_requirements="Low",
                    sample_efficiency="Medium (needs good workspace coverage)",
                    training_time="Hours"
                ),
                NeuralArchitecture(
                    architecture_type=ArchitectureType.VAE.value,
                    use_case=(
                        "Генерация множества допустимых решений обратной кинематики "
                        "для избыточных манипуляторов. VAE моделирует распределение "
                        "возможных конфигураций."
                    ),
                    input_format="End-effector pose + optional context",
                    output_format="Distribution over joint configurations",
                    advantages=[
                        "Generates multiple valid solutions",
                        "Can sample diverse configurations",
                        "Latent space enables interpolation",
                        "Handles redundancy naturally",
                        "Can incorporate additional constraints via conditioning"
                    ],
                    limitations=[
                        "Probabilistic nature may not suit all applications",
                        "Requires careful balance of reconstruction and KL terms",
                        "Sampling adds computational overhead",
                        "May produce invalid configurations without proper constraints"
                    ],
                    integration_with_classical=(
                        "VAE генерирует candidate configurations, которые затем "
                        "проверяются на ограничения и выбирается оптимальная. "
                        "Может комбинироваться с numerical IK solvers."
                    ),
                    example_papers=[
                        "Variational Inverse Kinematics (SIGGRAPH 2019)",
                        "VAE-based Redundancy Resolution (ICRA 2020)",
                        "Generative Models for Inverse Kinematics (CoRL 2021)"
                    ],
                    input_dimension="(batch_size, pose_dim)",
                    output_dimension="(batch_size, latent_dim) → (batch_size, joint_dim)",
                    temporal_requirements="Online, 500-2000 Hz",
                    computational_complexity="O(encoder + decoder)",
                    memory_requirements="Moderate",
                    sample_efficiency="Medium",
                    training_time="Hours"
                )
            ],
            constraints=TaskConstraints(
                real_time=True,
                safety_critical=False,
                sample_efficiency="medium",
                latency_ms=1.0,
                reliability="99.5%",
                explainability=False
            ),
            typical_applications=[
                "Real-time manipulator control",
                "Animation and motion capture retargeting",
                "Virtual reality avatar control",
                "Robotic surgery planning"
            ],
            benchmark_datasets=[
                "RobotURDF datasets",
                "PyBullet IK benchmarks",
                "MoveIt! motion planning database"
            ]
        )
    
    def _inverse_dynamics(self) -> ControlTask:
        """
        5.1.1.9 Обратная динамика (Inverse Dynamics)
        
        Вычисление моментов/сил на суставах, необходимых для создания
        заданных ускорений при текущем состоянии робота. Учитывает
        инерцию, кориолисовы силы, центробежные силы, гравитацию.
        """
        return ControlTask(
            task_name="Inverse Dynamics",
            description=(
                "Расчёт требуемых обобщённых сил (моментов на суставах) для создания "
                "заданных ускорений с учётом текущих положений, скоростей, а также "
                "параметров робота (массы, инерции, центры масс). Основа для computed "
                "torque control и model-based control."
            ),
            neural_architectures=[
                NeuralArchitecture(
                    architecture_type=ArchitectureType.PINN.value,
                    use_case=(
                        "Физически информированная сеть для обратной динамики. "
                        "Встраивание уравнений Лагранжа-Эйлера или Ньютона-Эйлера "
                        "непосредственно в архитектуру сети."
                    ),
                    input_format="[q, q_dot, q_ddot], robot parameters",
                    output_format="Joint torques τ",
                    advantages=[
                        "Guarantees physical consistency (energy, momentum)",
                        "Requires less training data due to physics priors",
                        "Better generalization to unseen configurations",
                        "Interpretable components (gravity, Coriolis, inertia)",
                        "Can identify unknown parameters"
                    ],
                    limitations=[
                        "Requires knowledge of equations structure",
                        "More complex implementation",
                        "May be slower than pure data-driven approaches",
                        "Automatic differentiation overhead"
                    ],
                    integration_with_classical=(
                        "PINN полностью заменяет классические алгоритмы обратной динамики "
                        "(Recursive Newton-Euler, Lagrangian), обеспечивая более быстрое "
                        "вычисление с сохранением физической корректности."
                    ),
                    example_papers=[
                        "Physics-Informed Neural Networks for Robot Dynamics (ICLR 2020)",
                        "Deep Lagrangian Networks for Inverse Dynamics (CoRL 2019)",
                        "Energy-Based Models for Robotic Dynamics (RSS 2021)"
                    ],
                    input_dimension="(batch_size, 3×n_joints + params)",
                    output_dimension="(batch_size, n_joints)",
                    temporal_requirements="Online, 1000-5000 Hz",
                    computational_complexity="O(network_eval + AD_overhead)",
                    memory_requirements="Low-Moderate",
                    sample_efficiency="High",
                    training_time="Hours"
                ),
                NeuralArchitecture(
                    architecture_type=ArchitectureType.MLP.value,
                    use_case=(
                        "Data-driven approximation inverse dynamics function. "
                        "Универсальный аппроксиматор без явного использования физики."
                    ),
                    input_format="[q, q_dot, q_ddot]",
                    output_format="Joint torques τ",
                    advantages=[
                        "No need for explicit dynamic model",
                        "Can capture unmodeled effects (friction, flexibilities)",
                        "Very fast inference",
                        "Simple implementation"
                    ],
                    limitations=[
                        "Requires extensive training data",
                        "May violate physical laws outside training distribution",
                        "Poor extrapolation",
                        "No interpretability of components"
                    ],
                    integration_with_classical=(
                        "MLP используется как компенсатор нелинейностей поверх "
                        "приближённой аналитической модели, или полностью заменяет "
                        "модель когда она недоступна или неточна."
                    ),
                    example_papers=[
                        "Neural Network Inverse Dynamics for Flexible Robots (IEEE TRO 2019)",
                        "Learning Inverse Dynamics from Demonstrations (ICRA 2020)",
                        "Deep Dynamics Models for Control (CoRL 2018)"
                    ],
                    input_dimension="(batch_size, 3×n_joints)",
                    output_dimension="(batch_size, n_joints)",
                    temporal_requirements="Online, 2000-10000 Hz",
                    computational_complexity="O(layers × width²)",
                    memory_requirements="Low",
                    sample_efficiency="Low-Medium",
                    training_time="Hours to days"
                )
            ],
            constraints=TaskConstraints(
                real_time=True,
                safety_critical=False,
                sample_efficiency="medium",
                latency_ms=0.5,
                reliability="99.9%",
                explainability=True
            ),
            typical_applications=[
                "Computed torque control",
                "Model-based reinforcement learning",
                "Robot simulation",
                "Dynamic motion optimization",
                "Collision impact analysis"
            ],
            benchmark_datasets=[
                "Robosuite dynamic datasets",
                "MuJoCo physics simulations",
                "Real robot logged data (torque sensors)"
            ]
        )
    
    def _adaptive_motion_control(self) -> ControlTask:
        """
        5.1.1.10 Адаптивное управление движением
        
        Автоматическая подстройка параметров контроллера при изменении
        характеристик робота (нагрузка, износ, повреждения) или условий работы.
        """
        return ControlTask(
            task_name="Adaptive Motion Control",
            description=(
                "Управление с автоматической адаптацией к изменяющимся условиям: "
                "переменная нагрузка, износ компонентов, изменения температуры, "
                "частичные отказы. Включает online identification параметров и "
                "adjustment контроллера в реальном времени."
            ),
            neural_architectures=[
                NeuralArchitecture(
                    architecture_type=ArchitectureType.META_LEARNING.value,
                    use_case=(
                        "Meta-learning для быстрой адаптации контроллера к новым условиям. "
                        "Обучение учиться адаптироваться (learning to adapt)."
                    ),
                    input_format="Recent trajectory data, performance metrics",
                    output_format="Updated controller parameters or policy",
                    advantages=[
                        "Fast adaptation to new conditions (few-shot)",
                        "Generalizes across different scenarios",
                        "Can handle previously unseen situations",
                        "Reduces need for manual retuning"
                    ],
                    limitations=[
                        "Complex meta-training procedure",
                        "Requires diverse training scenarios",
                        "May be unstable during adaptation phase",
                        "Computational overhead for meta-updates"
                    ],
                    integration_with_classical=(
                        "Meta-learner быстро адаптирует параметры классического контроллера "
                        "(PID gains, MPC weights, impedance parameters) на основе небольшого "
                        "количества новых данных о работе системы."
                    ),
                    example_papers=[
                        "Meta-Learning for Adaptive Robot Control (ICLR 2020)",
                        "Rapid Adaptation of Controllers via Meta-Learning (CoRL 2019)",
                        "Learning to Adapt in Physical Interaction Spaces (RSS 2021)"
                    ],
                    input_dimension="(batch_size, context_length, state_action_dim)",
                    output_dimension="(batch_size, num_params)",
                    temporal_requirements="Online adaptation, 10-100 Hz update rate",
                    computational_complexity="O(meta_network + adaptation steps)",
                    memory_requirements="Moderate-High",
                    sample_efficiency="Very High (few-shot adaptation)",
                    training_time="Days to weeks (meta-training)"
                ),
                NeuralArchitecture(
                    architecture_type=ArchitectureType.RNN.value,
                    use_case=(
                        "RNN для online system identification и adaptive control. "
                        "Рекуррентная сеть одновременно идентифицирует параметры "
                        "системы и генерирует управляющие сигналы."
                    ),
                    input_format="Sequence of states, actions, and observed responses",
                    output_format="Control commands + estimated parameters",
                    advantages=[
                        "Simultaneous identification and control",
                        "Handles time-varying parameters",
                        "No explicit model structure required",
                        "Can capture complex adaptation dynamics"
                    ],
                    limitations=[
                        "Black-box nature limits interpretability",
                        "Stability guarantees difficult",
                        "May require extensive training",
                        "Risk of catastrophic forgetting"
                    ],
                    integration_with_classical=(
                        "RNN оценивает изменяющиеся параметры системы, которые затем "
                        "используются для online перенастройки классического адаптивного "
                        "контроллера (MRAC, gain scheduling)."
                    ),
                    example_papers=[
                        "Recurrent Neural Networks for Adaptive Control (CDC 2019)",
                        "Deep Adaptive Control with RNNs (ICRA 2020)",
                        "Neural System Identification for Adaptive Robotics (Automatica 2021)"
                    ],
                    input_dimension="(batch_size, seq_length, observation_dim)",
                    output_dimension="(batch_size, action_dim + param_dim)",
                    temporal_requirements="Online, 200-1000 Hz",
                    computational_complexity="O(seq_length × hidden_dim²)",
                    memory_requirements="Moderate",
                    sample_efficiency="Medium",
                    training_time="Hours to days"
                )
            ],
            constraints=TaskConstraints(
                real_time=True,
                safety_critical=True,
                sample_efficiency="very_high",
                latency_ms=10.0,
                reliability="99.9%",
                explainability=True
            ),
            typical_applications=[
                "Payload-adaptive manipulation",
                "Wear-compensating industrial robots",
                "Damage-tolerant control",
                "Variable environment operation",
                "Aging system maintenance"
            ],
            benchmark_datasets=[
                "Adaptive control benchmarks",
                "Simulated damage/failure scenarios",
                "Variable payload datasets"
            ]
        )
    
    def get_task_by_name(self, task_name: str) -> Optional[ControlTask]:
        """Получить задачу по имени"""
        for task in self.tasks:
            if task.task_name.lower() == task_name.lower():
                return task
        return None
    
    def get_all_tasks(self) -> List[ControlTask]:
        """Получить все задачи"""
        return self.tasks
    
    def export_to_json(self, filepath: str) -> None:
        """Экспорт базы данных в JSON формат"""
        data = {
            "taxonomy_section": "5.1.1",
            "section_name": "Управление движением и кинематика",
            "tasks": [asdict(task) for task in self.tasks]
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def export_to_dict(self) -> Dict[str, Any]:
        """Экспорт базы данных в словарь"""
        return {
            "taxonomy_section": "5.1.1",
            "section_name": "Управление движением и кинематика",
            "tasks": [asdict(task) for task in self.tasks]
        }


# Экспорт основных классов
__all__ = [
    'MotionControlDatabase',
    'ControlTask',
    'NeuralArchitecture',
    'TaskConstraints',
    'ArchitectureType'
]
