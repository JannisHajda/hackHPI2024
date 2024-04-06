#include <fstream>
#include <iostream>
#include "json.hpp"

using json = nlohmann::json;

json read_json(std::string json_path){
    std::ifstream file(json_path);

    // Check if the file is opened successfully
    if (!file.is_open()) {
        std::cout << "Error opening file.\n";
        return 1;
    }

    // Parse the JSON content from the file
    json j;
    file >> j;
    return j;
}

int main() {
    json j = read_json("example_json_data.json");
    // ihr könnt euch die Struktur dazu in example_json_data.json anschauen, zugriffe sind wie in python entweder by key oder index
    std::cout << j["members"][1]["powers"];
    return 0;
}