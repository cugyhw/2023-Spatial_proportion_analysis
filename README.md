# Spatial-proportion-analysis
Spatial proportion analysis(空间比例分析)

Project description: Calculate the spatial proportion of an event based on geospatial coordinates.  
Advantages: the code runs fast (several times faster than Arcgis' neighborhood analysis), the results are accurate, millions of points can be analyzed, and the memory footprint is relatively small.  
Project details: This project is based on the KDTree algorithm, which is used to calculate the spatial proportion of shp data (or panel data), for example: this project takes urban renewal field as an example, in urban renewal research (need to study whether the building has been renewed or not), calculates the proportion of the number of neighboring buildings that have been renewed to the total number of neighboring buildings within the radius of 500 meters of a certain building.  
Prerequisites for code use:
1.Provide your own data, which should be in csv(UTF-8) format;  
2.If your data is not csv (UTF-8) format, you can convert your data to that format, for example: shp data lead to csv format data, and use notepad software to convert it to csv (UTF-8) format;  
3.In your data, the coordinate system must be a projected coordinate system, because in this project, the analysis radius is in meters.

项目介绍：根据地理空间坐标计算某个事件的空间比例
项目优点：代码运行速度迅速（相比Arcgis的邻域分析速度提高数倍），结果准确，可以分析数以百万计的点数据，内存占用相对小得多  
项目详情：本项目基于KDTree算法，用于计算shp数据（或面板数据）的空间比例，例如：本项目以城市更新领域为例，在城市更新研究中（需要研究建筑物是否发生更新），计算某一建筑物在半径为500米的范围内，发生更新的邻域建筑物数目占总邻域建筑物的比例
代码使用前提：
1.自备数据，数据需为csv(UTF-8)格式；
2.倘若你的数据不是csv(UTF-8)格式的，可以将你的数据转换为该格式，例如：将shp数据导为csv格式的数据，并使用记事本软件将其转换为csv(UTF-8)格式；  
3.你的数据中，坐标系必须是投影坐标系，因为在本项目中，分析半径是以米为单位的。
