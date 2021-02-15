# lcovkv
Simple flask app with a REST API to store lcov values for a commit hash.

Uses [simplekv](https://simplekv.readthedocs.io/en/latest/) as db.
### API

- GET get/
  - 201 = found. 
  - 400 = invalid key
  - 404 = key not found
  - 422 = file could not be read

- PUT set/key
  - 201 = written, anything else not.
  - 400 = invalid key
  - 422 = file could not be read

### Usage

```
# put "95.0" in key "a39lk20"
curl "localhost:5000/set/a39lk20" -d "value=95.0" -X PUT -v 

# get coverage value for commit hash "h"
curl http://localhost:5000/get/ -d "commit_hash=h" -X GET

```
### Run tests
``tox``
