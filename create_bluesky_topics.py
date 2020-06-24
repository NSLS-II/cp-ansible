from confluent_kafka.admin import AdminClient, NewTopic


admin_client = AdminClient({"bootstrap.servers": "nslskafka01:9092, nslskafka02:9092, nslskafka03:9092"})

beamlines = ['amx', 'bmm', 'chx', 'cms', 'csx', 'esm', 'fmx',
             'fxi', 'hxn', 'ios', 'isr', 'iss', 'ixs', 'jpls',
             'lix', 'pdf', 'qas', 'rsoxs', 'six', 'smi', 'srx',
             'tes', 'xfm', 'xfp', 'xpd', 'xpdd']

topic_list = [NewTopic(f"{beamline}.test.bluesky.documents", 3, 3) for beamline in beamlines]

# Topic for bluesky-kafka tests.
topic_list.append(NewTopic("bluesky-kafka-test", 3, 3))

print(topic_list)

admin_client.create_topics(topic_list)
