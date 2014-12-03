from lib import Experiment, Benchmark, ClusterSuite

# import cluster and systems classes
from clusters import ComputeEngine
from systems import Hadoop, Flink

# import standard configs
from configs import compute_engine_config, hadoop_config, flink_config

# import experiment's main class
from experiments.wordcount import WordCount

from results import Results

cluster = ComputeEngine(compute_engine_config)
hadoop = Hadoop(hadoop_config)
flink = Flink(flink_config)

systems = [hadoop, flink]

custom_flink_conf = flink_config.copy()
custom_flink_conf['git_commit'] = "858d1bccf957bf36c04ab011ec9a26933109086c"
custom_flink_conf['taskmanager_num_buffers'] = 1024

custom_flink = Flink(custom_flink_conf)

benchmarks = [
    Benchmark("WordCount1000",
        [hadoop, flink],
        WordCount({
            'id' : 1,
            'num_lines' : 1000
        })
    ),

    Benchmark("WordCount1000-custom",
        [hadoop, custom_flink],
        WordCount({
            'id' : 3,
            'num_lines' : 1000
        })
    )
]

suite = ClusterSuite("DefaultSuite", cluster, systems, benchmarks)

suite.setup()
suite.run()
suite.shutdown()

results = Results(suite)
results.save_results()