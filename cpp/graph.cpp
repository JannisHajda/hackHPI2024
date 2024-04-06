#include <iostream>
#include <vector>
#include <map>
#include <tuple>

//feel free to edit

class Graph {
    private:
        std::map<int, std::tuple<int, float>> adj_list;
    public:
        void add_connection(int id, int id2, float weight);
        void remove_connection(int id, int id2);
        std::vector<int> get_connections(int id);
        float get_weight(int id, int id2);
};

struct Building {
    int id;
    std::tuple<float, float> position; // long, lat center
    std::string type;
};

struct Area {
    int id;
    std::tuple<float, float> position; // long, lat center
    float area;
};

struct Cluster {
    std::tuple<float, float> position; // long, lat center
    std::vector<int> nodeIDs; // IDs of buildings in graph
};






//Graph implementation von copilot (und Joscha)

void Graph::add_connection(int id, int id2, float weight) {
    adj_list[id] = std::make_tuple(id2, weight);
}
void Graph::remove_connection(int id, int id2) {
    adj_list.erase(id);
}
std::vector<int> Graph::get_connections(int id) {
    std::vector<int> connections;
    for (auto const& x : adj_list) {
        if (std::get<0>(x.second) == id) {
            connections.push_back(x.first);
        }
    }
    return connections;
}
float Graph::get_weight(int id, int id2) {
    return std::get<1>(adj_list[id]);
}