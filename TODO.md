# TODO

## Features

make sure -version works

## Bugs

- **Windows: path handling breaks `freeze`, `auto_group`, `add_repos`.**
  gitchk builds and compares repo paths assuming POSIX-style `/` separators
  (`utils.py`: `auto_group`, path prefix/common-path logic used by `freeze`
  and `add_repos`). On Windows, `os.path`/`pathlib` operations return
  backslash paths, so grouping and freezing produce wrong output and the
  config CSVs may not round-trip correctly across platforms. Needs an audit
  of path handling in `utils.py` to normalize consistently (e.g. store/compare
  as POSIX paths, or use `pathlib.PurePath` throughout) rather than raw string
  ops. Failing tests on Windows: `test_main.py::test_freeze`,
  `test_utils.py::test_auto_group`, `test_utils.py::test_add_repos`.
