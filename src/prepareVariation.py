#
# prepareVariation.py
#

# import modules
from const_project import FILE_INIT_RVT, FILE_SA_PARAM_LIST, DIRS_DATA_SA, DIRS_DATA_SA_FIG, DIRS_DATA_SA_DUP, FILE_SA_VARY
from const_sensi import K_LEVEL_PARAMETER, N_SMP, SA_CALC_SECOND_ORDER, BOUNDARY_VALUES, SET_SA_DISTRIBUTION, SALTELLI_SKIP

from funct_sensi import *
# from funct_plot import plot_sa_parallel_parameters
# from base_classes import NewDesign

def prepareVariants(set_dup_rvt=False):

    csv_sa_parameter = FILE_SA_PARAM_LIST.replace('tbd', str(K_LEVEL_PARAMETER))
    sa_parameter_data = pd.read_csv(csv_sa_parameter, names=['names', 'values'], header=None)
    sa_parameter_values = sa_parameter_data['values'].tolist()

    sa_parameter_names = sa_parameter_data['names'].tolist()
    sa_parameter_num = len(sa_parameter_names)
    sa_parameter_bounds = np.array([[v-BOUNDARY_VALUES, v+BOUNDARY_VALUES] for v in sa_parameter_values]).reshape((sa_parameter_num,2))

    # values via Saltelli’s extension of the Sobol’ sequence
    sa_problem = {
        'num_vars': sa_parameter_num,
        'names': sa_parameter_names,
        'bounds': sa_parameter_bounds,
        # 'bounds': np.array(list([-BOUNDARY_VALUES, BOUNDARY_VALUES] * sa_parameter_num)),
        'dists': np.array([SET_SA_DISTRIBUTION] * sa_parameter_num),
        }

    sa_values = saltelli.sample(sa_problem, N_SMP, calc_second_order=SA_CALC_SECOND_ORDER, skip_values=SALTELLI_SKIP)
    save_ndarray_2txt(sa_values, DIRS_DATA_SA+"/sa_values.txt")
    save_dict(sa_problem, DIRS_DATA_SA+"/sa_problem.pickle")

    df_sa_variation = pd.DataFrame(sa_values, columns=sa_parameter_names).T
    df_sa_variation.to_csv(FILE_SA_VARY, header=False)

    if set_dup_rvt:
        duplicateRVT(FILE_INIT_RVT, DIRS_DATA_SA_DUP, amount=sa_values.shape[0], clear_destination=True)
    
    # initial_design = NewDesign(0)
    # initial_design.add_codecompliance(BUILDING_RULES, init_output)

    # sa_samples, sa_samples_df = build_samples(initial_design, sa_values, sa_problem)
    # plot_sa_parallel_parameters(DIRS_DATA_SA_FIG, sa_samples_df)
