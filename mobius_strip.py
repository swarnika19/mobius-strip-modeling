import numpy as np
import matplotlib.pyplot as plt


class MobiusStrip:
    def __init__(self, loop_radius, strip_width, mesh_points):
        self.loop_radius = loop_radius
        self.strip_width = strip_width
        self.mesh_points = mesh_points
        
        self.angle_grid = np.linspace(0, 2 * np.pi, mesh_points)
        self.width_shift = np.linspace(-strip_width / 2, strip_width / 2, mesh_points)
        self.ANGLES, self.SHIFTS = np.meshgrid(self.angle_grid, self.width_shift)
        
        self.X, self.Y, self.Z = self._generate_coordinates()
        
    def _generate_coordinates(self):
        u = self.ANGLES
        v = self.SHIFTS
        R = self.loop_radius
        X_vals = (R + v * np.cos(u / 2)) * np.cos(u)
        Y_vals = (R + v * np.cos(u / 2)) * np.sin(u)
        Z_vals = v * np.sin(u / 2)
        return X_vals, Y_vals, Z_vals

    def estimate_area(self):
        dX_u = np.gradient(self.X, axis=1)
        dX_v = np.gradient(self.X, axis=0)
        dY_u = np.gradient(self.Y, axis=1)
        dY_v = np.gradient(self.Y, axis=0)
        dZ_u = np.gradient(self.Z, axis=1)
        dZ_v = np.gradient(self.Z, axis=0)

        norm_x = dY_u * dZ_v - dZ_u * dY_v
        norm_y = dZ_u * dX_v - dX_u * dZ_v
        norm_z = dX_u * dY_v - dY_u * dX_v

        magnitudes = np.sqrt(norm_x**2 + norm_y**2 + norm_z**2)
        area = np.trapz(np.trapz(magnitudes, self.width_shift), self.angle_grid)
        return area

    def boundary_length(self):
        edge_shift = self.strip_width / 2
        u_vals = np.linspace(0, 2 * np.pi, self.mesh_points)
        X_edge = (self.loop_radius + edge_shift * np.cos(u_vals / 2)) * np.cos(u_vals)
        Y_edge = (self.loop_radius + edge_shift * np.cos(u_vals / 2)) * np.sin(u_vals)
        Z_edge = edge_shift * np.sin(u_vals / 2)

        diff_x = np.gradient(X_edge)
        diff_y = np.gradient(Y_edge)
        diff_z = np.gradient(Z_edge)

        one_edge_length = np.trapz(np.sqrt(diff_x**2 + diff_y**2 + diff_z**2), u_vals)
        return 2 * one_edge_length

    def show_surface(self):
        fig = plt.figure(figsize=(9, 7))
        axis = fig.add_subplot(111, projection='3d')
        axis.plot_surface(self.X, self.Y, self.Z, color='lightblue', edgecolor='grey', linewidth=0.2)
        axis.set_title("Möbius Strip Visualization")
        plt.show()


mobius = MobiusStrip(loop_radius=5, strip_width=1, mesh_points=250)

print("Estimated Surface Area:", mobius.estimate_area())
print("Boundary Length:", mobius.boundary_length())

mobius.show_surface()
