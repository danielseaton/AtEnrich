from GAFER import analyse_clustering,ClusterObj
import os
import inspect

main_dir = os.path.dirname(inspect.getfile(analyse_clustering))
data_dir = os.path.join(main_dir,'tests','test_data_files')
clustering_file_location = os.path.join(data_dir,'diurnal_clustering_300916.json')
cData = ClusterObj.from_json(clustering_file_location)
db_id = 'GeneListDB'
cluster_indices = [85]
feature_list = ['chen2014_phyA_induced']

method = 'pval'
FR_df = analyse_clustering(cData,db_id,method=method,feature_list=feature_list,excluded_features=None,cluster_indices=cluster_indices)
FR_df.loc['chen2014_phyA_induced',85]

method = 'FE'
FR_df = analyse_clustering(cData,db_id,method=method,feature_list=feature_list,excluded_features=None,cluster_indices=cluster_indices)
FR_df.loc['chen2014_phyA_induced',85]