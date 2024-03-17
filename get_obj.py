import open3d as o3d
import numpy as np
import trimesh

def gen_obj(dataset):
    pcd = o3d.io.read_point_cloud(f"output/{dataset}.ply")
    pcd.estimate_normals()

    # estimate radius for rolling ball
    distances = pcd.compute_nearest_neighbor_distance()
    avg_dist = np.mean(distances)
    radius = 1.5 * avg_dist   

    mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
            pcd,
            o3d.utility.DoubleVector([radius, radius * 2]))

    # create the triangular mesh with the vertices and faces from open3d
    tri_mesh = trimesh.Trimesh(np.asarray(mesh.vertices), np.asarray(mesh.triangles),
                            vertex_normals=np.asarray(mesh.vertex_normals))

    trimesh.convex.is_convex(tri_mesh)

    trimesh.exchange.export.export_mesh(tri_mesh, 'out.obj')