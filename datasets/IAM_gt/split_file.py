lines_per_file = int(44412/4)
smallfile = None
with open('gan.iam.tr_va.gt.filter27') as bigfile:
    file_id = 0
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'batch_{}.filter27'.format(file_id)
            file_id += 1
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()


