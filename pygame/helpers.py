"""
Helper functions and utilities for OOZORA SKY DEFENDER
"""

import math
import random

def clamp(value, min_val, max_val):
    """Clamp a value between min and max."""
    return max(min_val, min(max_val, value))

def distance(x1, y1, x2, y2):
    """Calculate Euclidean distance between two points."""
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx * dx + dy * dy)

def vec_from_angle(angle_deg, magnitude=1.0):
    """
    Convert angle (degrees) and magnitude to velocity vector.
    0° = right, 90° = down, 180° = left, 270° = up (pygame coords)
    """
    rad = math.radians(angle_deg)
    return (magnitude * math.cos(rad), magnitude * math.sin(rad))

def angle_from_vec(vx, vy):
    """Convert velocity vector to angle in degrees."""
    return math.degrees(math.atan2(vy, vx))

def lerp(a, b, t):
    """Linear interpolation."""
    return a + (b - a) * t

def ease_in_out_quad(t):
    """Smooth ease-in-out (0 to 1 progress)."""
    if t < 0.5:
        return 2 * t * t
    return -1 + (4 - 2 * t) * t

def normalize_vector(vx, vy):
    """Normalize a vector to unit length."""
    length = math.sqrt(vx * vx + vy * vy)
    if length == 0:
        return (0, 0)
    return (vx / length, vy / length)

def rotate_point(x, y, cx, cy, angle_deg):
    """Rotate point (x,y) around center (cx,cy) by angle_deg."""
    rad = math.radians(angle_deg)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)
    
    # Translate to origin
    x -= cx
    y -= cy
    
    # Rotate
    new_x = x * cos_a - y * sin_a
    new_y = x * sin_a + y * cos_a
    
    # Translate back
    return (new_x + cx, new_y + cy)

def random_in_range(min_val, max_val):
    """Random float between min and max."""
    return random.uniform(min_val, max_val)

def weighted_choice(choices, weights):
    """
    Weighted random choice.
    choices: list of items
    weights: list of weights (don't need to sum to 1)
    """
    total = sum(weights)
    pick = random.uniform(0, total)
    current = 0
    for choice, weight in zip(choices, weights):
        current += weight
        if pick <= current:
            return choice
    return choices[-1]

def color_lerp(c1, c2, t):
    """Lerp between two RGB colors."""
    r = int(c1[0] + (c2[0] - c1[0]) * t)
    g = int(c1[1] + (c2[1] - c1[1]) * t)
    b = int(c1[2] + (c2[2] - c1[2]) * t)
    return (r, g, b)

def rgba_to_rgb(rgba, bg_color):
    """Blend RGBA color with background (for alpha blending in pygame)."""
    r = int(rgba[0] * rgba[3] / 255 + bg_color[0] * (1 - rgba[3] / 255))
    g = int(rgba[1] * rgba[3] / 255 + bg_color[1] * (1 - rgba[3] / 255))
    b = int(rgba[2] * rgba[3] / 255 + bg_color[2] * (1 - rgba[3] / 255))
    return (r, g, b)
