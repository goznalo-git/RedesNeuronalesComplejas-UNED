'''
Title: Functions used in LeakyIntegrate-and-Fire.py
Author: Gonzalo Contreras Aso
'''

def equation(u, t, I, params):
    """Evaluation of du/dt = f(u,t)."""
    
    f = 1/params['tau'] * (-u + params['uR'] + params['R'] * I(t))
    
    return f


def RK4(h, u, t, I, params, equation):
    """Calculation of one Runge-Kutta of order 4 step"""
    
    F1 = equation(u, t, I, params=params) 
    
    F2 = equation(u + h/2, t + F1/2, I, params=params) 
    
    F3 = equation(u + h/2, t + F2/2, I, params=params) 
    
    F4 = equation(u + h, t + F3, I, params=params) 
    
    return u + (h/6) * (F1 + 2*F2 + 2*F3 + F4), t + h


def solve_system(h, I, params, equation=equation, t0=0, tmax=100):
    """Iterate the method from t0 to tmax, spiking if u above threshold"""
    
    u = params['u0']
    t = t0
    
    u_vals = [u]
    t_vals = [t]
    
    while round(t,1) < round(tmax,1):
        
        u, t = RK4(h, u, t, I=I, params=params, equation=equation)
        
        u_vals.append(u)
        t_vals.append(t)
        
        if u > params['theta']:
            print(f'u={u} spike at t={t}')
            u = params['uR']      
                  
    return u_vals, t_vals


def short_pulse(t, dt, I0, init=10):
    '''Short pulse of intensity I0'''
        
    I_pulse = 0
    
    if t > init and t < init + dt:
        I_pulse = I0
        
    return I_pulse
