# Teknofest İnsansız Kara Aracı (İKA) - ROS2 Workspace

> ⚠️ **Durum: Aktif Geliştirme Aşamasında (In Development)**
> *Bu proje üzerindeki çalışmalarımız devam etmektedir. Kod tabanı, haritalama ve otonom sürüş özellikleri sürekli güncellenmektedir.*

Bu depo, Teknofest İnsansız Kara Aracı (İKA) yarışması için "Yavuz Ekibi" bünyesinde geliştirilen otonom araç yazılımlarını içermektedir. Proje, ROS2 mimarisi üzerine kurulmuş olup, otonom haritalama, navigasyon ve simülasyon ortamı (Gazebo/RViz) testlerini barındırmaktadır.

## 🚀 Proje İçeriği ve Görevler
- **Simülasyon Ortamı:** Gazebo üzerinde yarışma parkurunun (kukalar, engeller) modellenmesi ve otonom testlerin gerçekleştirilmesi.
- **Haritalama ve Navigasyon:** SLAM algoritmaları ile ortam haritasının çıkarılması ve Nav2 kullanılarak otonom rota planlaması.
- **Sensör Entegrasyonu:** Lidar ve derinlik kamerası verilerinin ROS2 ortamına aktarılması.

## 🛠️ Kullanılan Teknolojiler
- **İşletim Sistemi:** Ubuntu 22.04
- **ROS Sürümü:** ROS2 Humble / Iron
- **Diller:** C++, Python
- **Araçlar:** Gazebo, RViz2, Nav2, SLAM Toolbox

## ⚙️ Kurulum ve Derleme
Çalışma alanını klonlamak ve derlemek için:

```bash
mkdir -p ~/ika_ws/src
cd ~/ika_ws/src
git clone [https://github.com/imre-robotics/ika_ws.git](https://github.com/imre-robotics/ika_ws.git) .
cd ~/ika_ws
colcon build --symlink-install
source install/setup.bash
