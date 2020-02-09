""""

    Design an efficient key value store which supports the following requirements:
    The requirements can change
    in future so your design needs to be flexible.

1. Efficient write and read of the data provided as a input
2. The data will be stored in the disk in the form of SST sorted segment tables.
   These tables will have a size limit and a new file will be created once the size limit is reached.
3. There will be a background process that keeps on checking the status of the segment files.
   This process will do the compaction of the segment files.
   The compaction will remove the duplicates keys and will keep only the latest keys in the
   system.
4. The inmemory cache table will also be persisted in the disk in case of failures so
   that the system can resume the
  state.


"""


