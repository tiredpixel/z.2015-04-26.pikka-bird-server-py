# Pikka Bird Server Changelog

This changelog documents the main changes between released versions.
For a full list of changes, consult the commit history.


## 0.1.0

- first release! :D
- `pikka-bird-server` providing commands: `server`, `database-migrate`
- database schema principal tables: `machines`, `services`, `collections`,
  `reports`
- `GET /` providing greeting
- `POST /collections` for collecting reports, supporting JSON and binary
  payloads
