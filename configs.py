import getpass

USER = getpass.getuser()

"""
Standard Flink config

"""
flink_config = {
    'path' : "/home/%s/flink" % USER,
    'git_repository' : "https://github.com/apache/incubator-flink",
    'git_commit' : "master",
    'num_task_slots' : 8,
    'parallelization' : 1,
    'taskmanager_heap' : 512,
    'jobmanager_heap' : 256,
    'taskmanager_num_buffers' : 2048,
    'jvm_opts' : "",
    'extra_config_entries' : [
        { 'entry' : "#this: wontdoanything" },
        { 'entry' : "#another: entry" },
    ]
}

"""
Standard Hadoop config

"""
hadoop_config = {
    'source' : "http://mirror.arcor-online.net/www.apache.org/hadoop/common/hadoop-2.5.2/hadoop-2.5.2.tar.gz",
    'path' : "/home/%s/hadoop" % USER,
    'data_path' : "/home/%s/mnt" % USER,
    'replication_factor' : 3,
}

"""
Standard Google Compute Engine config

"""
compute_engine_config = {
    'num_workers' : 2,
    'project_name' : "braided-keel-768",
    'zone' : "europe-west1-c",
    'machine_type' : "n1-standard-2",
    'disk_image' : "https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/backports-debian-7-wheezy-v20141108",
    'prefix' : "benchmark-",
    'disk_space_gb' : 50,
    'disk_type' : 'pd-standard', # change to pd-ssd for ssd
}

"""
Standard Tez config

"""
tez_config = {
        'git_repository' : 'https://github.com/apache/tez.git',
        'git_commit' : 'master',
        'path' : "/home/%s/tez" % USER,
        'path_client' : "/home/%s/tez_client/" % USER,
    }