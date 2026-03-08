"""
Motion Control and Kinematics - 5.1.1

This module contains neural network architectures for motion control and kinematics tasks
in robotics, including trajectory planning, path planning, position/velocity control,
force/torque control, impedance control, inverse kinematics/dynamics, and adaptive control.

Taxonomy Section: 5.1.1
Section Name: Motion Control and Kinematics
"""

from . import (
    01_Trajectory_Planning,
    02_Path_Planning,
    03_Position_Control,
    04_Velocity_Control,
    05_Force_Torque_Control,
    06_Impedance_Admittance_Control,
    07_Hybrid_Position_Force_Control,
    08_Inverse_Kinematics,
    09_Inverse_Dynamics,
    10_Adaptive_Motion_Control
)

TAXONOMY_SECTION = "5.1.1"
SECTION_NAME = "Motion Control and Kinematics"

SUBSECTIONS = [
    "01_Trajectory_Planning",
    "02_Path_Planning",
    "03_Position_Control",
    "04_Velocity_Control",
    "05_Force_Torque_Control",
    "06_Impedance_Admittance_Control",
    "07_Hybrid_Position_Force_Control",
    "08_Inverse_Kinematics",
    "09_Inverse_Dynamics",
    "10_Adaptive_Motion_Control"
]

__all__ = [
    'TAXONOMY_SECTION',
    'SECTION_NAME',
    'SUBSECTIONS',
    '01_Trajectory_Planning',
    '02_Path_Planning',
    '03_Position_Control',
    '04_Velocity_Control',
    '05_Force_Torque_Control',
    '06_Impedance_Admittance_Control',
    '07_Hybrid_Position_Force_Control',
    '08_Inverse_Kinematics',
    '09_Inverse_Dynamics',
    '10_Adaptive_Motion_Control'
]
