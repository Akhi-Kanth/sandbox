import importlib.machinery, importlib.util

loader = importlib.machinery.SourceFileLoader("tb", "tb")
spec = importlib.util.spec_from_loader("tb", loader)
tb = importlib.util.module_from_spec(spec)
loader.exec_module(tb)

iso = tb.ts("1700000000")
assert tb.ts(iso) == "1700000000"
assert tb.ts("1700000000000") == iso  # ms input
assert tb.ts().isdigit()
assert tb.b64(tb.b64("hello"), decode=True) == "hello"
print("ok")
