# conTest
Consistency testing at the executable level between 2 [usually different] github branches.

### Example Output
```
tests/test_config.py::test_screen_settings PASSED [ 1%]
tests/test_config.py::test_screen_settings_reload PASSED [ 3%]
tests/test_config.py::test_settings_cfg PASSED [ 4%]
tests/test_config.py::test_settings_organism_cfg PASSED [ 6%]
tests/test_config.py::test_settings_world_cfg PASSED [ 8%]
tests/test_config.py::test_settings_reload_cfg PASSED [ 9%]
<redacted for length>
tests/test_poploader.py::test_reload_most_byid_noerror[least-1] FAILED [ 57%]
tests/test_poploader.py::test_reload_most_byid_noerror[least-5] FAILED [ 59%]
tests/test_poploader.py::test_reload_most_byid_noerror[least-50] FAILED [ 60%]
tests/test_poploader.py::test_reload_most_byid_noerror[least-100] FAILED [ 62%]
tests/test_poploader.py::test_reload_most_byid_error[baseline-greatest-(-1)] PASSED [ 63%]
tests/test_poploader.py::test_reload_most_byid_error[baseline-greatest-(0)] PASSED [ 65%]
tests/test_poploader.py::test_reload_most_byid_error[baseline-greatest-(101)] PASSED [ 67%]
<redacted for length>
tests/test_settings_randseed.py::test_screen_randseed_random[baseline] PASSED [ 91%]
tests/test_settings_randseed.py::test_screen_randseed_random[testline] PASSED [ 93%]
tests/test_settings_randseed.py::test_screen_randseed_nonrandom[baseline] PASSED [ 96%]
tests/test_settings_randseed.py::test_screen_randseed_nonrandom[testline] PASSED [ 98%]
tests/test_settings_randseed.py::test_screen_randseed_nonrandom_consistency PASSED [100%]
```

Additionally, each failed test with diff output is stored in a directory `failed/test_name/` so you can inspect why exactly it failed.

### Example
Show help:
```bash
python contest.py -h
```
List all available tests:
```bash
python contest.py -ls
```
Clone a web repo and test two branches, specifying how they're built, and what the executable name is:
```bash
python contest.py git@github.com:joryschossau/build master development "make -j2" build.exe
```
Same as above, but with an older commit (either one optional):
```bash
python contest.py git@github.com:joryschossau/build master:2fabc8 development:88acda "make -j2" build.exe
```
Same as above, but using a local repo:
```bash
python contest.py ../../myrepo master development "make -j2" build.exe
```

### Usage
```
usage: contest.py [-h] [-ls] [-s SUBSET]
                  [repo] [basebranch] [testbranch] [makeCommand] [exeName]

positional arguments:
  repo
  basebranch
  testbranch
  makeCommand
  exeName

optional arguments:
  -h, --help            show this help message and exit
  -ls, --list           list all available tests found
  -s SUBSET, --subset SUBSET
                        test filter expression: "defaults and not settings"
```
