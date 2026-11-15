-- RAN Air Wing anonymous counters. One row per day / event kind / aircraft / mission. No IPs, names or accounts are stored.
CREATE TABLE IF NOT EXISTS counts (
  d    TEXT NOT NULL,              -- UTC day, YYYY-MM-DD
  k    TEXT NOT NULL,              -- event kind (see KINDS in worker.js)
  ac   TEXT NOT NULL DEFAULT '',   -- a4 | s2
  ms   TEXT NOT NULL DEFAULT '',   -- mission id such as T7 or S1, or empty
  n    INTEGER NOT NULL DEFAULT 0, -- number of events
  secs INTEGER NOT NULL DEFAULT 0, -- airborne seconds (flight_secs only)
  PRIMARY KEY (d, k, ac, ms)
);
