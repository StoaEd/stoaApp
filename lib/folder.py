import os

def create_folder_structure(base_path):
    structure = {
        "core": ["constants", "errors", "utils", "networking", "usecases", "themes"],
        "features": {
            "feature_1": [
                "data/datasources",
                "data/models",
                "data/repositories",
                "domain/entities",
                "domain/usecases",
                "domain/repositories",
                "presentation/blocs",
                "presentation/blocs/events",
                "presentation/blocs/states",
                "presentation/pages",
                "presentation/widgets",
                "presentation/mappers",
            ],
            "feature_2": [
                "data/datasources",
                "data/models",
                "data/repositories",
                "domain/entities",
                "domain/usecases",
                "domain/repositories",
                "presentation/blocs",
                "presentation/blocs/events",
                "presentation/blocs/states",
                "presentation/pages",
                "presentation/widgets",
                "presentation/mappers",
            ],
        },
        "shared": ["widgets", "extensions", "services"],
        "injection": [],
        "localization": [],
        "app": ["env"],
    }


    def create_dirs(base, dirs):
        for d in dirs:
            path = os.path.join(base, d)
            os.makedirs(path, exist_ok=True)

    # Create core folders
    create_dirs(base_path, structure["core"])

    # Create feature folders
    features_path = os.path.join(base_path, "features")
    for feature, subdirs in structure["features"].items():
        for subdir in subdirs:
            os.makedirs(os.path.join(features_path, feature, subdir), exist_ok=True)

    # Create shared folders
    create_dirs(base_path, structure["shared"])

    # Create injection, localization, and app folders
    for key in ["injection", "localization", "app"]:
        create_dirs(base_path, structure[key])

    # Create main.dart placeholder
    with open(os.path.join(base_path, "main.dart"), "w") as f:
        f.write("// Main entry point of the Flutter application\n")

if __name__ == "__main__":
    project_path = input("Enter the base path for your Flutter project: ")
    create_folder_structure(project_path)
    print(f"Folder structure created at {project_path}")