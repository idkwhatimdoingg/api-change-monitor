def compare(old, new):

    old_ids = set(old.keys())
    new_ids = set(new.keys())

    return {
        "added": new_ids - old_ids,
        "removed": old_ids - new_ids
    }