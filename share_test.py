from kiwoom.data import Share

share = Share()

print("args", share.args)
print("single", share.single)
print("multi", share.multi)
print("history", share.history)

print("single", dict(share.single))
print("multi", {k: dict(v) for k, v in share.multi.items()})
print("history", {k: dict(v) for k,v in share.history.items()})


share.update_args("함수1", {"key1": "value1", "key2":"value2"})
print("args", share.args)

share.update_single("함수1","key1", "value1")
print("single", dict(share.single))




