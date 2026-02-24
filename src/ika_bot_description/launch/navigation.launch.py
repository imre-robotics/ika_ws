import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    # 1. Paket Yollarını Bul
    pkg_ika_bot = get_package_share_directory('ika_bot_description')
    pkg_nav2 = get_package_share_directory('nav2_bringup')

    # 2. Harita Dosyası (Senin kaydettiğin yeni harita)
    map_file_path = os.path.join(pkg_ika_bot, 'maps', 'teknofest_harita.yaml')

    # 3. Nav2 Parametreleri (Varsayılan)
    params_file_path = os.path.join(pkg_nav2, 'params', 'nav2_params.yaml')

    # 4. Navigasyon Başlatma
    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_nav2, 'launch', 'bringup_launch.py')
        ),
        launch_arguments={
            'map': map_file_path,
            'use_sim_time': 'true',
            'params_file': params_file_path,
            'autostart': 'true'
        }.items()
    )

    return LaunchDescription([
        nav2_launch
    ])