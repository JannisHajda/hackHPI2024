import json
import statistics

def main():

  seasons = ["summer", "winter"]
  area_types = ["COMMERCIAL", "FARM", "HIGH_DENSITY_RESIDENTIAL", "INDUSTRIAL", "RETAIL", "TRANSPORT"]

  data = []

  for season in seasons:
    path = f"src/data/loadprofiles/{season}"
    for area_type in area_types:
      with open(f'{path}/{area_type}.json', 'r') as f:
        data_area = json.load(f)
        electro_usage = data_area["Electro"]
        electro_averge = statistics.mean(electro_usage)
        try:
          heating_usage = data_area["Heating"]      
          heating_average = statistics.mean(heating_usage)
        except KeyError:
          heating_average = 0
        data.append([season, area_type, electro_averge, heating_average])
      print(season, area_type, "\n", data_area , "\n ------------------------ \n")


  cluster_usage = []
  cluster_usage_electric = 0
  cluster_usage_heat = 0
  all_cluster_usage_electric = 0
  all_cluster_usage_heat = 0

  with open(f'clusters.json', 'r') as f:
    data_clusters = json.load(f)

  with open(f'graph.json', 'r') as f:
    data_graph = json.load(f)

  buildings = data_graph['buildings']
  for i, cluster in enumerate(data_clusters):
    cluster_usage_electric = 0
    cluster_usage_heat = 0
    node_ids = cluster['nodes']
    for node_id in node_ids:
      building_type = buildings[node_id]["type"]
      building_base_area = buildings[node_id]["base_area"]
      for item in data:
        season = item[0]
        area_type = item[1]


        if season == seasons[0] and area_type.lower() == building_type.lower():
          cluster_usage_electric += building_base_area * item[2]
          cluster_usage_heat += building_base_area * item[3]
    print(f"Cluster Usage {i}: \n Electro {cluster_usage_electric} \n Heat {cluster_usage_heat} \n ------------ \n")
    all_cluster_usage_electric += cluster_usage_electric
    all_cluster_usage_heat += cluster_usage_heat
    cluster_usage.append([i, cluster_usage_electric, cluster_usage_heat])
  print(f"All Cluster Usage: \n Electro {all_cluster_usage_electric} \n Heat {all_cluster_usage_heat} \n ------------ \n")

if __name__ == "__main__":
  main()