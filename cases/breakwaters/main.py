import timeit
import pickle
import argparse

from gefest.core.opt.gen_design import design
from cases.breakwaters.configuration_de import bw_domain, bw_sampler
from cases.breakwaters.configuration_surrogate import bw_estimator
from cases.breakwaters.configuration_spea2 import bw_optimizer

parser = argparse.ArgumentParser()
parser.add_argument("--pop_size", type=int, default=3, help='number of individs in population')
parser.add_argument("--n_steps", type=int, default=80, help='number of generative design steps')
parser.add_argument('--n_polys', type=int, default=5, help='maximum number of polygons in structure')
parser.add_argument('--n_points', type=int, default=15, help='maximum number of points in polygon')
parser.add_argument('--c_rate', type=float, default=0.6, help='crossover rate')
parser.add_argument('--m_rate', type=float, default=0.6, help='mutation rate')
parser.add_argument('--is_closed', type=bool, default=False, help='type of polygon')
opt = parser.parse_args()

# ------------
# GEFEST tools configuration
# ------------
domain, task_setup = bw_domain.configurate_domain(poly_num=opt.n_polys,
                                                  points_num=opt.n_points,
                                                  is_closed=opt.is_closed)

estimator = bw_estimator.configurate_estimator(domain=domain)
sampler = bw_sampler.configurate_sampler(domain=domain)
optimizer = bw_optimizer.configurate_optimizer(pop_size=opt.pop_size,
                                               crossover_rate=opt.c_rate,
                                               mutation_rate=opt.m_rate,
                                               task_setup=task_setup)

# ------------
# Generative design stage
# ------------

start = timeit.default_timer()
optimized_pop = design(n_steps=opt.n_steps,
                       pop_size=opt.pop_size,
                       estimator=estimator,
                       sampler=sampler,
                       optimizer=optimizer,
                       extra=True)
spend_time = timeit.default_timer() - start
print(f'spent time {spend_time} sec')
