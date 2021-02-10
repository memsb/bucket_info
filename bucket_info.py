import os
from collections import Counter
import boto3
import humanize as humanize
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MaxNLocator
import sys


def clear():
    os.system('clear')


def get_all_keys():
    client = boto3.client('s3')

    paginator = client.get_paginator("list_objects")
    page_iterator = paginator.paginate(Bucket=bucket)

    bucket_object_list = []
    for page in page_iterator:
        if "Contents" in page:
            for key in page["Contents"]:
                bucket_object_list.append(key["Key"])

    return bucket_object_list


if len(sys.argv) < 2:
    print("Please specify a bucket")
    quit()
bucket = sys.argv[1]
prefix = sys.argv[2] if len(sys.argv) == 3 else ""

s3 = boto3.resource('s3')
keys = get_all_keys()
keys = [x for x in keys if x.startswith(prefix)]

extensions = [os.path.splitext(x)[1] for x in keys]
mime_types = []
sizes = []
total_bytes = 0

for i, key in enumerate(keys):
    progress = round((i / len(keys)) * 100)
    clear()
    print(f"Loading object metadata: {progress}%")
    obj = s3.Object(bucket, key)
    sizes.append(obj.content_length)
    mime_types.append(obj.content_type)

plt.figure(1, figsize=(14, 4))
plt.subplot(121)
mime_type_labels = Counter(mime_types).keys()
mime_type_counts = Counter(mime_types).values()
total_size = humanize.naturalsize(sum(sizes))
wedges, texts, auto_texts = plt.pie(
    mime_type_counts,
    autopct=lambda pct: int(pct / 100. * len(keys)),
    textprops=dict(color="w"),
    startangle=90
)
plt.title("File types")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
fontP = FontProperties()
fontP.set_size('xx-small')
plt.legend(
    wedges,
    mime_type_labels,
    title="MIME type",
    loc="best",
    prop=fontP
)
plt.setp(auto_texts, size=8, weight="bold")

plt.subplot(122)
plt.hist(sizes, facecolor='g', bins=20)
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
plt.gca().xaxis.set_major_formatter(lambda x, p: humanize.naturalsize(x))
plt.title(f"Total Files: {total_size}")
plt.xlabel('File Size')
plt.ylabel('File Count')

plt.savefig(f"output/{bucket}.png", bbox_inches='tight', orientation='landscape')
plt.show()
