#
# tempoCheck.py
#

# import modules

# https://www.analyticsvidhya.com/blog/2021/03/beginners-guide-to-support-vector-machine-svm/
# https://towardsdatascience.com/support-vector-machines-svm-clearly-explained-a-python-tutorial-for-classification-problems-29c539f3ad8
# https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC
# http://www.cs.cornell.edu/courses/cs4780/2018fa/lectures/lecturenote09.html

from base_external_packages import *
from funct_data import *
from funct_svm import executeLinearSVC, evaluateLinearSVC, displaySVCinPC
from Space import SolutionSpace
from const_project import DIRS_DATA

from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt
from sklearn import svm, metrics, tree
from sklearn.svm import LinearSVC
from sklearn.datasets import make_blobs
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.model_selection import train_test_split

# -Import the dataset
# -Explore the data to figure out what they look like
# -Pre-process the data
# -Split the data into attributes and labels
# -Divide the data into training and testing sets
# -Train the SVM algorithm
# -Make some predictions 
# -Evaluate the results of the algorithm

dataset = [
    '\sa-14-0.3',
    '\sa-19-0.3',
    ]

pathIni = DIRS_DATA + dataset[0] + r'\DesignIni.pickle'
pathRes = DIRS_DATA + dataset[0] + r'\res'
problems =  get_problems_from_paths(pathRes)

designIni = load_dict(pathIni)
# del designIni.parameters["U1_OK_d_wl_sn25"]

pathsNew = [DIRS_DATA + set + r'\DesignsNew.pickle' for set in dataset]
designsNew = flatten([load_dict(path) for path in pathsNew])

firstSpace = SolutionSpace(problems)

firstSpace.set_center(designIni)

firstSpace.form_space(designsNew)

firstSpace.subdivide_space()
print(firstSpace)

X = firstSpace.data_X
y = firstSpace.data_Y
svc_class_weight = 4
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2023)

clf = executeLinearSVC(X, y, C=1.0, y_train_weight=svc_class_weight)
y_pred_error_index, y_pred_val_index = evaluateLinearSVC(clf, X, y)
displaySVCinPC(X, y, svckernel="linear")

# y = clf.decision_function(X)
# w_norm = np.linalg.norm(clf.coef_)
# dist = y / w_norm
# print("Distance to the boundary: ", dist)

# calculate the distance from samples to the hyperplane
# here the y value converges with y_pred, but not alwadys with y_test



# w = clf.coef_[0]
# a = -w[0] / w[1]
# xx = np.linspace(-5, 5)
# yy = a * xx - (clf.intercept_[0]) / w[1]
# margin = 1 / np.sqrt(np.sum(clf.coef_ ** 2))
# yy_down = yy - np.sqrt(1 + a ** 2) * margin
# yy_up = yy + np.sqrt(1 + a ** 2) * margin
# plt.figure(1, figsize=(4, 3))
# plt.clf()
# plt.plot(xx, yy, "k-")
# plt.plot(xx, yy_down, "k-")
# plt.plot(xx, yy_up, "k-")
# plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80,
#  facecolors="none", zorder=10, edgecolors="k")
# plt.scatter(X[:, 0], X[:, 1], c=y, zorder=10, cmap=plt.cm.Paired,
#  edgecolors="k")
# plt.xlabel("x1")
# plt.ylabel("x2")
# plt.show()

# displaySVC(clf, X, y)

# fig, ax = plt.subplots()
# plot_decision_regions(X[:,:2], y, clf=clf, legend=2)
# plt.show()

# # title for the plots
# title = ('Decision surface of linear SVC ')
# # Set-up grid for plotting.
# X0, X1 = X[:, 0], X[:, 1]
# xx, yy = make_meshgrid(X0, X1)

# plot_contours(ax, clf, xx, yy, cmap=plt.cm.coolwarm, alpha=0.8)
# ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
# ax.set_ylabel('y label here')
# ax.set_xlabel('x label here')
# ax.set_xticks(())
# ax.set_yticks(())
# ax.set_title(title)
# ax.legend()
# plt.show()

# clf, y_pred, dist, y_pred_error_index, y_pred_val_index = executeLinearSVC(X, y, svc_class_weight)
# y_pred = clf.predict(X)

# displaySVC(clf, X, y)

# model = svm.SVC(kernel="linear", C=1.0, probability=True, class_weight={1: int(svc_class_weight)})
# clf = model.fit(X, y)

# X0, X1 = X[:, 0], X[:, 1]
# https://datascience.stackexchange.com/questions/33910/number-of-features-of-the-model-must-match-the-input-model-n-features-is-n-an
# https://stackoverflow.com/questions/72252887/valueerror-x-has-1-features-but-svc-is-expecting-3-features-as-input
# https://www.analyticsvidhya.com/blog/2021/10/support-vector-machinessvm-a-complete-guide-for-beginners/

# fig, ax = plt.subplots(figsize=(10, 6))
# disp = DecisionBoundaryDisplay.from_estimator(
#     clf,
#     X,
#     response_method="predict",
#     cmap=plt.cm.coolwarm,
#     alpha=0.8,
#     ax=ax,
#     xlabel='1',
#     ylabel='2',)

# ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors="k")
# ax.set_xticks(())
# ax.set_yticks(())
# ax.set_title('t')
# plt.savefig('test.png', dpi=200)

# Von Stavros.

# # Run SVM and fit data
# svc = svm.SVC(kernel='linear')
# X_train = df2.to_numpy()
# svc.fit(X_train, y_train)


# # Outcomes
# y_pred = svc.predict(X_train)
# supp=svc.support_vectors_


# # Find distance to boundary
# x1=X_train[0,:]
# x1=np.expand_dims(x1, axis=0)
# y = svc.decision_function(x1)
# w_norm = np.linalg.norm(svc.coef_)
# dist = y / w_norm



# y_pred_error_dist = [item for item in dist[y_pred_error_index]]
# y_pred_val_dist = [item for item in dist[y_pred_val_index]]



# nu_list = [0.01, 0.02, 0.05, 0.1, 0.125]
# for nu_v in nu_list:
#     display_svc_pc(X, y, svckernel="nu", nu_nu=nu_v)

# # fit the model and get the separating hyperplane
# clf = svm.SVC(kernel="linear", C=1.0)
# clf.fit(X, y)
# # fit the model and get the separating hyperplane using weighted classes
# wclf = svm.SVC(kernel="linear", class_weight={1: 10})
# wclf.fit(X, y)
# # plot the samples
# plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, edgecolors="k")
# # plot the decision functions for both classifiers
# ax = plt.gca()
# disp = DecisionBoundaryDisplay.from_estimator(
#     clf,
#     X,
#     plot_method="contour",
#     colors="k",
#     levels=[0],
#     alpha=0.5,
#     linestyles=["-"],
#     ax=ax,
# )
# # plot decision boundary and margins for weighted classes
# wdisp = DecisionBoundaryDisplay.from_estimator(
#     wclf,
#     X,
#     plot_method="contour",
#     colors="r",
#     levels=[0],
#     alpha=0.5,
#     linestyles=["-"],
#     ax=ax,
# )
# plt.legend(
#     [disp.surface_.collections[0], wdisp.surface_.collections[0]],
#     ["non weighted", "weighted"],
#     loc="upper right",
# )
# plt.show()

# # Read the initial data
# df_init = pd.read_csv(r'data/0_initial_parameters.csv',
#                       index_col=0, header=None).T

# # Read the sampling data
# df_raw = pd.read_csv(r'data/samples.csv')

# # drop list
# # drop empty columns that concerns zone4 and other unassociated columns
# drop_list = ['room_zone4_x', 'room_zone4_y', 'zone4_sep_x1']
# add_drop_list = ['room_zone1_x', 'room_zone1_y', 'zone1_sep_x1',
#                  'zone3_sep_x1', 'zone3_sep_x2', 'zone3_sep_x3']
# drop_list = drop_list + add_drop_list
# df_raw.drop(columns=drop_list, inplace=True)
# df = df_raw.iloc[:, 5:12].copy()

# rules_list = ['comp_IBC1020_2', 'comp_IBC1207_1', 'comp_IBC1207_2', 'comp_IBC1207_3']
# y_train_byrule = dict.fromkeys(rules_list)
# y_train_weight_byrule = dict.fromkeys(rules_list)

# g_all_rl = []
# for rl in rules_list:
#     g_rl = df_raw[rl].to_numpy()
#     g_all_rl.append(g_rl)
#     y_train_byrule[rl] = [g_rl[i] for i in range(np.shape(g_rl)[0])]
#     y_train_weight_byrule[rl] = [4.0 if item else 1.0 for item in y_train_byrule[rl]]
    
# y_train_allrules = [g_all_rl[0][i] and g_all_rl[1][i] and g_all_rl[2][i] and g_all_rl[3][i] for i in range(np.shape(g_all_rl[0])[0])]
# y_train_weight_allrules = [4.0 if item else 1.0 for item in y_train_allrules]

# test_rule = 'all'

# if test_rule == 'all':
#     y_train = y_train_allrules
#     y_train_weight = y_train_weight_allrules
# else:
#     for rl in list(y_train_byrule.keys()):
#         if test_rule in rl:
#             y_train = y_train_byrule[rl]
#             y_train_weight = y_train_weight_byrule[rl]

# svc, y_pred, dist, y_pred_error_index, y_pred_val_index = execute_linearsvc(test_rule, X_train, y_train, y_train_weight)
# y_pred_error_dist = [item for item in dist[y_pred_error_index]]
# y_pred_val_dist = [item for item in dist[y_pred_val_index]]

# # initial parameter values
# sample_ini = [12., 7.5, 5., 6., 3., 6., 10.]

# # calculate the dissimilarity
# y_pred_val_dissimilarity = []
# for i in y_pred_val_index:
#     sp = list(df.iloc[i])
#     for ii in range(len(sample_ini)):
#         sp[ii] = abs((sp[ii] - sample_ini[ii]) / sample_ini[ii])
#         sp[ii] = sp[ii] * sp[ii]
#     y_pred_val_dissimilarity.append(sum(sp))

# # normalization of the dissimilarity of the parameter value (percent) to [0,1]
# α_norm, β_norm = get_α_β(y_pred_val_dissimilarity, norm=True, norm_01=True)
# norm_y_pred_val_dissimilarity = out_stnd_nrml(y_pred_val_dissimilarity, α_norm, β_norm)

# # normalization of the distance from valid design options to the predicted hyperplane to [0,1]
# α_norm, β_norm = get_α_β(y_pred_val_dist, norm=True, norm_01=True)
# norm_y_pred_val_dist = out_stnd_nrml(y_pred_val_dist, α_norm, β_norm)


# fig, ax = plt.subplots(figsize=(30, 8))
# ax.scatter(y_pred_val_index, norm_y_pred_val_dissimilarity, s=100, marker="o", label = 'via parameter square difference')
# ax.plot(y_pred_val_index, norm_y_pred_val_dissimilarity, linewidth=4)

# ax.scatter(y_pred_val_index, norm_y_pred_val_dist, s=100, marker="^", label = 'via the predicted distance to hyperplane')
# ax.plot(y_pred_val_index, norm_y_pred_val_dist, linewidth=4)

# ax.scatter(y_pred_error_index,[0]*len(y_pred_error_index), s=150, marker="X", color = "maroon", label = 'wrong classification prediction')

# ax.set_xticks(y_pred_val_index)
# ax.tick_params(axis='x', which='major', direction='out', length=5, width=2, color='grey',
#                     pad=5, labelsize=8, labelcolor='black', labelrotation=90)
# ax.tick_params(axis='y', labelsize=15, labelcolor='black')
# ax.legend(loc="best", fontsize=15)
# ax.set_title("Dissimilarity / Distance", size=25)
# # ax.set_title("Dissimilarity from predicted valid design options to the initial design", size=18)

# """
# Plot second sensitivity indices
# """


# def convert2Matrix(second):
#     param_names = []
#     for m in range(second.shape[0]):
#         for n in range(second.shape[1]):
#             if second.index[m][n] not in param_names:
#                 param_names.append(second.index[m][n])
#             else:
#                 continue

#     matrix = np.zeros((len(param_names), len(param_names)), float)
#     for k in range(second['S2'].shape[0]):
#         j = param_names.index(second['S2'].index[k][0])
#         i = param_names.index(second['S2'].index[k][1])
#         matrix[j][i] = second['S2'].iloc[k]
#     return param_names, matrix