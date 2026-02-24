import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    pkg_name = 'ika_bot_description'
    
    # 1. URDF İşleme
    xacro_file = os.path.join(get_package_share_directory(pkg_name), 'urdf', 'ika_bot.xacro')
    robot_description_config = xacro.process_file(xacro_file)
    robot_desc = robot_description_config.toxml()

    # --- DÜZELTME BAŞLANGICI ---
    # Dünya dosyasının yolunu buluyoruz
    world_file_name = 'teknofest.world'
    world_path = os.path.join(get_package_share_directory(pkg_name), 'worlds', world_file_name)

    # 2. Gazebo Başlat (GÜNCELLENDİ)
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
        # İşte burası eksikti! Gazebo'ya senin dünyanı açmasını söylüyoruz:
        launch_arguments={'world': world_path}.items()
    )
    # --- DÜZELTME BİTİŞİ ---

    # 3. Robot State Publisher
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc, 'use_sim_time': True}]
    )

    # 4. Spawn Entity
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'ika_bot', '-z', '0.2', '-Y', '3.14'],
        output='screen'
    )

    # 5. Kontrolcüler
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
    )

    gimbal_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["gimbal_controller", "--controller-manager", "/controller_manager"],
    )

    # 7. DEPTH TO LASERSCAN
    depth_to_laser = Node(
        package='depthimage_to_laserscan',
        executable='depthimage_to_laserscan_node',
        name='depthimage_to_laserscan',
        output='screen',
        parameters=[{
            'output_frame': 'camera_link',
            'range_min': 0.1,
            'range_max': 10.0,
            'scan_height': 10
        }],
        remappings=[
            ('depth', '/camera_sensor/depth/image_raw'),
            ('depth_camera_info', '/camera_sensor/depth/camera_info'),
            ('scan', '/scan')
        ]
    )

    # 8. RViz
    node_rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
    )

    return LaunchDescription([
        gazebo,
        node_robot_state_publisher,
        spawn_entity,
        joint_state_broadcaster_spawner,
        gimbal_controller_spawner,
        depth_to_laser,
        node_rviz
    ])