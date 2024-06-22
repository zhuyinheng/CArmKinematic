import os
import trimesh
import numpy as np

# Get the directory path of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get a list of all STL files in the directory
stl_files = [f for f in os.listdir(current_dir) if f.endswith('.stl')]

# Process each STL file
for stl_file in stl_files:
    # Load the STL file
    mesh = trimesh.load_mesh(os.path.join(current_dir, stl_file))

    # Check if the mesh is watertight
    print(mesh.is_watertight)
    # Fix the normals to ensure the mesh is watertight
    mesh.fix_normals()

    # Adjust the order of vertices in each face to be consistent with the normals
    # mesh.align_normals()
    # # Function to arrange vertex indices in each face to be consistent with face normals
    # def arrange_vertex_indices(mesh):
    #     # Get the face normals
    #     face_normals = mesh.face_normals

    #     # Get the vertex indices of each face
    #     face_vertex_indices = mesh.faces

    #     # Iterate over each face
    #     for i in range(len(face_vertex_indices)):
    #         # Get the vertex indices of the current face
    #         vertex_indices = face_vertex_indices[i]

    #         # Get the normal of the current face
    #         normal = face_normals[i]

    #         # Calculate the centroid of the face
    #         centroid = np.mean(mesh.vertices[vertex_indices], axis=0)

    #         # Calculate the vector from the centroid to each vertex
    #         vectors = mesh.vertices[vertex_indices] - centroid

    #         # Calculate the dot product between each vector and the face normal
    #         dot_products = np.dot(vectors, normal)

    #         # Sort the vertex indices based on the dot product
    #         sorted_indices = vertex_indices[np.argsort(dot_products)]

    #         # Update the vertex indices of the current face
    #         face_vertex_indices[i] = sorted_indices

    #     # Update the mesh with the arranged vertex indices
    #     mesh.faces = face_vertex_indices

    # # Call the function to arrange the vertex indices in each face
    # arrange_vertex_indices(mesh)

    # Export the mesh to an OBJ file with the same name as the STL file
    obj_file = os.path.splitext(stl_file)[0] + '.obj'
    mesh.export(os.path.join(current_dir, obj_file), file_type='obj')