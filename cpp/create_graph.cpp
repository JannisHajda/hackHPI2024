#include <iostream>
#include "json_import.cpp"
#include "graph.cpp"

Graph create_graph(json j){
    Graph g;
    //read json graph
    return g;
}

int main() {
    json j = read_json("example_json_data.json");
    Graph g = create_graph(j);
    return 0;
}