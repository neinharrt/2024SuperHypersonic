import math

def shock_init(**kwargs):

    # IDEAL GAS
    g = 1.4
    R = 1

    # UPSTREAM CONDITIONS
    rho_u = 1.0
    u_u = 1.5 * math.sqrt(1.4) #changed!!
    v_u = 0.0
    w_u = 0.0
    p_u = 1.0
    t_u = p_u / (rho_u * R)

    # SHOCK CONDITIONS
    M_s = 1.5

    # DOWNSTREAM CONDITIONS
    rho_d = rho_u * (g + 1.0) * M_s * M_s / (2.0 + (g - 1.0) * M_s * M_s)
    u_d = u_u * (2.0 + (g - 1.0) * M_s * M_s) / ((g + 1.0) * M_s * M_s)
    v_d = v_u
    w_d = w_u
    p_d = p_u * (1.0 + (2.0 * g / (g + 1.0)) * (M_s * M_s - 1.0))

    # SOLUTION DATA
    location = kwargs['location']
    pressure = p_u
    temperature = t_u
    velocity = [0.0,0.0,0.0]

    # SHOCK CONDITIONS
    if location[0] <= 0.5:
        pressure = p_u
        temperature = t_u
        velocity[0] = u_u
        velocity[1] = v_u
        velocity[2] = w_u
    else:
        pressure = p_d
        temperature = p_d / (rho_d * R)
        velocity[0] = u_d
        velocity[1] = v_d
        velocity[2] = w_d

    # VORTEX LOCATION
    x_c = 0.25
    y_c = 0.5

    # VORTEX SIZES
    a = 0.075
    b = 0.175

    # VORTEX STRENGTH
    M_v = 0.9
    v_m = M_v * math.sqrt(g)

    # DISTANCE FROM VORTEX
    dx = (location[0] - x_c)
    dy = (location[1] - y_c)
    r = math.sqrt(dx * dx + dy * dy)

    # SUPERIMPOSE VORTEX
    if r <= b:

        if r > 0:
            sin_theta = dy / r
            cos_theta = dx / r
        else:
            sin_theta = 0.0
            cos_theta = 0.0

        if r <= a:
            mag = v_m * r / a
            velocity[0] = velocity[0] - mag * sin_theta
            velocity[1] = velocity[1] + mag * cos_theta

            # TEMPERATURE AT a, from below
            radial_term = -2.0 * b * b * math.log(b) - (0.5 * a * a) + (2.0 * b * b * math.log(a)) + (0.5 * b * b * b * b / (a * a))
            t_a = t_u - (g - 1.0) * math.pow(v_m * a / (a * a - b * b),2) * radial_term / (R * g)
            radial_term = 0.5 * (1.0 - r * r / (a * a))
            temperature = t_a - (g - 1.0) * v_m * v_m * radial_term / (R * g)

        else:
            mag = v_m * a * (r - b * b / r) / (a * a - b * b)
            velocity[0] = velocity[0] - mag * sin_theta
            velocity[1] = velocity[1] + mag * cos_theta

            # TEMPERATURE RADIAL TERM
            radial_term = -2.0 * b * b * math.log(b) - (0.5 * r * r) + (2.0 * b * b * math.log(r)) + (0.5 * b * b * b * b / (r * r))
            temperature = t_u - (g - 1.0) * math.pow(v_m * a / (a * a - b * b),2) * radial_term / (R * g)

        pressure = p_u * math.pow(temperature / t_u, g / (g - 1.0))

    return {'pressure': pressure,'temperature':temperature, 'velocity': tuple(velocity)}