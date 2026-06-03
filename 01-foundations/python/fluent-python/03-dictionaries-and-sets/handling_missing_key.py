import collections
import re

WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)

text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Quisque ut quam at velit iaculis maximus.
Suspendisse a ipsum ac magna cursus dignissim imperdiet sit amet diam.
Cras scelerisque lacus vitae orci dictum interdum.
Suspendisse vitae lacus sit amet neque varius pulvinar.
Fusce a nulla ac orci dictum feugiat in quis ex.
In vitae risus eu dui blandit iaculis sed et est.
Sed a sem vel ipsum sagittis bibendum quis ac est.
Aliquam sit amet mauris in est lobortis varius dapibus eu mi.
Sed vulputate urna vitae magna lobortis volutpat.
Aenean ac metus at ligula placerat ultrices.
Sed placerat eros a odio pulvinar, eu tincidunt libero efficitur.
Mauris sed orci facilisis lacus iaculis tristique et nec nulla.
""".split('\n')

for line_no, line in enumerate(text, 1):
    for match in WORD_RE.finditer(line):
        word = match.group()
        column_no = match.start() + 1
        location = (line_no, column_no)
        index[word].append(location)

for word in sorted(index, key=str.upper):
    print( word, index[word] )
